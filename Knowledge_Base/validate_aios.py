#!/usr/bin/env python3
"""
AI-OS Documentation Compliance Validator
Scans every .md file, extracts metadata, and reports defects against the
project's own governance rules (SSOT, DRY, Consistency, Traceability).
Reusable: run `python3 validate_aios.py <repo_root>`.
"""
import os, re, sys, json
from datetime import datetime

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
VALID_STATUS = {"Draft", "Review", "Active", "Deprecated", "Archived", "Stable", "Approved"}
CANON_STATUS = {"Draft", "Review", "Active", "Deprecated", "Archived"}  # per Document Registry

def rel(p): return os.path.relpath(p, ROOT)

md_files = []
for dp, dn, fn in os.walk(ROOT):
    if "/." in dp: continue
    for f in fn:
        if f.lower().endswith(".md"):
            md_files.append(os.path.join(dp, f))
md_files.sort()

def get_field(text, name):
    # matches "Field: value" or table row "| Field | value |"
    m = re.search(rf"^\s*{re.escape(name)}\s*:\s*(.+)$", text, re.M | re.I)
    if m: return m.group(1).strip()
    m = re.search(rf"\|\s*{re.escape(name)}\s*\|\s*([^|]*)\|", text, re.I)
    if m: return m.group(1).strip()
    return None

docs = []
for p in md_files:
    with open(p, encoding="utf-8", errors="replace") as fh:
        t = fh.read()
    docs.append({
        "path": rel(p),
        "name": os.path.basename(p),
        "lines": t.count("\n") + 1,
        "chars": len(t),
        "text": t,
        "doc_id": get_field(t, "Document ID"),
        "version": get_field(t, "Version"),
        "status": get_field(t, "Status"),
        "owner": get_field(t, "Owner"),
        "dtype": get_field(t, "Document Type"),
        "layer": get_field(t, "Layer"),
    })

findings = {}  # code -> list of messages
def add(code, msg): findings.setdefault(code, []).append(msg)

# Registry doc IDs (parse the Document Registry table)
registry = next((d for d in docs if "Document_Registry" in d["path"]), None)
registered_ids, registered_titles = set(), set()
if registry:
    for row in re.findall(r"\|\s*(DOC-[A-Z]+-\d+)\s*\|\s*([^|]+)\|", registry["text"]):
        registered_ids.add(row[0].strip())
        registered_titles.add(row[1].strip().lower())

for d in docs:
    P = d["path"]
    # C1 missing Document ID
    if not d["doc_id"]:
        add("C1_MISSING_DOC_ID", P)
    # C2 empty/blank version info fields
    if d["version"] is None or d["version"] == "":
        add("C2_EMPTY_VERSION", P)
    if d["status"] is None or d["status"] == "":
        add("C3_EMPTY_STATUS", P)
    # C4 invalid status token
    if d["status"] and d["status"] not in VALID_STATUS:
        add("C4_INVALID_STATUS", f"{P}  -> '{d['status']}'")
    elif d["status"] and d["status"] not in CANON_STATUS:
        add("C4b_NONCANON_STATUS", f"{P} -> '{d['status']}' (not in Registry's 5-state model)")
    # C5 typos in Document Type
    if d["dtype"] and re.search(r"standart", d["dtype"], re.I):
        add("C5_TYPO_STANDART", f"{P} -> Document Type '{d['dtype']}'")
    # C6 owner inconsistency
    if d["owner"] and "viktor" in d["owner"].lower():
        add("C6_OWNER_INCONSISTENT", f"{P} -> Owner '{d['owner']}'")
    # C7 doc id present but not in registry
    if d["doc_id"] and registered_ids and d["doc_id"] not in registered_ids:
        add("C7_ID_NOT_IN_REGISTRY", f"{P} -> {d['doc_id']}")
    # C8 stub files
    if d["lines"] <= 5 and "template" not in d["name"].lower():
        add("C8_STUB", f"{P} ({d['lines']} lines)")
    # C9 filename convention (spaces in name)
    if " " in d["name"]:
        add("C9_FILENAME_SPACES", P)
    # C10 terminology conflict Execution vs Workflow inside Execution layer
    if "03_Execution_Layer" in P and re.search(r"\bWorkflow\b", d["text"]):
        n = len(re.findall(r"\bWorkflow\b", d["text"]))
        add("C10_TERM_WORKFLOW_IN_EXEC", f"{P} ('Workflow' x{n})")

# C11 broken Related Documents references (title not matching any doc h1/name)
doc_titles = set()
for d in docs:
    m = re.search(r"^#\s+(.+)$", d["text"], re.M)
    if m: doc_titles.add(m.group(1).strip().lower())
    doc_titles.add(os.path.splitext(d["name"])[0].lower())

# C12 registry completeness: layers whose files are absent from registry
gov_docs = [d for d in docs if ("Governance" in d["path"] or "02_Analysis" in d["path"]
            or "03_Generation" in d["path"] or d["path"].startswith("03_Execution_Layer"))]
unregistered_gov = [d["path"] for d in gov_docs
                    if not d["doc_id"] or (registered_ids and d["doc_id"] not in registered_ids)]

# empty dirs
empty_dirs = []
for dp, dn, fn in os.walk(ROOT):
    if "/." in dp: continue
    if not dn and not fn: empty_dirs.append(rel(dp))

# summary
print("="*70)
print(f"AI-OS COMPLIANCE VALIDATOR — {datetime.now():%Y-%m-%d %H:%M}")
print(f"Scanned {len(docs)} markdown files under {os.path.abspath(ROOT)}")
print("="*70)
order = ["C1_MISSING_DOC_ID","C2_EMPTY_VERSION","C3_EMPTY_STATUS","C4_INVALID_STATUS",
         "C4b_NONCANON_STATUS","C5_TYPO_STANDART","C6_OWNER_INCONSISTENT",
         "C7_ID_NOT_IN_REGISTRY","C8_STUB","C9_FILENAME_SPACES","C10_TERM_WORKFLOW_IN_EXEC"]
total = 0
for code in order:
    items = findings.get(code, [])
    total += len(items)
    print(f"\n### {code}  ({len(items)})")
    for it in items: print("   -", it)
print(f"\n### REGISTERED IDS IN DOCUMENT REGISTRY ({len(registered_ids)})")
print("   ", sorted(registered_ids))
print(f"\n### EMPTY DIRECTORIES ({len(empty_dirs)})")
for e in empty_dirs: print("   -", e)
print(f"\nTOTAL FLAGGED ITEMS: {total}")

# machine-readable dump
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"aios_findings.json"),"w") as jf:
    json.dump({k:v for k,v in findings.items()}, jf, indent=2)
