#!/usr/bin/env python3
"""
AI-OS Working Kit Generator

Rebuilds AI-OS_AI_Working_Kit.md (DOC-CORE-009) from the current official
source documents, so the single-file operational context never drifts from
the SSOT (DP-001, DP-003 — the kit is a *rendered copy*; sources prevail).

Usage:  python3 Knowledge_Base/generate_working_kit.py [repo_root]
"""
import os, re, sys
from datetime import date

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
KIT_VERSION = "2.0.0"
TODAY = date.today().isoformat()

# Full-body sources, in kit order: (section title, path)
FULL_SOURCES = [
    ("Core Identity",          "00_Core/Core_Identity.md"),
    ("Core Execution Engine",  "00_Core/Core_Execution_Engine.md"),
    ("AI-OS Design Principles","01_Architecture/AI-OS_Design_Principles.md"),
    ("AI-OS Reasoning Patterns","01_Architecture/AI-OS_Reasoning_Patterns.md"),
    ("Memory Architecture",    "06_Memory/Memory_Architecture.md"),
    ("AI-OS Glossary",         "01_Architecture/AI-OS_Glossary.md"),
]
CAPA_DIR = "02_Capability_Layer/02_Modules"
EXEC_DIRS = ["02_Analysis","03_Generation","04_Validation","05_Optimization","06_Development","07_Education"]

def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as fh:
        return fh.read()

def field(text, name):
    m = re.search(rf"^{name}\s*:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else "?"

def body(text):
    """Document body: after the header separator, before Version Information."""
    m = re.search(r"\n---\n", text)
    start = m.end() if m else 0
    m = re.search(r"^#{1,2} Version Information\s*$", text, re.M)
    end = m.start() if m else len(text)
    b = text[start:end].strip()
    # drop a trailing separator left before Version Information
    b = re.sub(r"\n---\s*$", "", b).strip()
    # demote top-level section headings so the kit's own H1/H2 hierarchy holds
    b = re.sub(r"^# ", "### ", b, flags=re.M)
    b = re.sub(r"^## ", "### ", b, flags=re.M)
    return b

def purpose_line(text):
    """First paragraph of the Purpose section, single line."""
    m = re.search(r"^#{1,3}\s*(?:\d+\.\s*)?Purpose\s*$(.+?)(?=^#{1,3}\s|\n---)", text, re.M | re.S)
    if not m:
        return "—"
    para = m.group(1).strip().split("\n\n")[0]
    return " ".join(para.split())

parts = []
sources_table = []

# --- assemble full sections
for title, path in FULL_SOURCES:
    t = read(path)
    ver, did = field(t, "Version"), field(t, "Document ID")
    sources_table.append((title, did, ver))
    parts.append(f"## {title}\n\n> Source: `{path}` ({did} v{ver}) — the source document prevails on conflict.\n\n{body(t)}")

# --- capability index
rows = []
for f in sorted(os.listdir(os.path.join(ROOT, CAPA_DIR))):
    if not f.endswith(".md") or f == "README.md":
        continue
    t = read(f"{CAPA_DIR}/{f}")
    rows.append(f"| {field(t,'Document ID')} | {t.splitlines()[0].lstrip('# ').strip()} | {purpose_line(t)} |")
capa = "## Capability Layer — Module Index\n\n> Full modules live in `02_Capability_Layer/02_Modules/`. Activate only the expertise a task needs.\n\n| ID | Module | Purpose |\n| -- | ------ | ------- |\n" + "\n".join(rows)
parts.append(capa)

# --- execution index
rows = []
for d in EXEC_DIRS:
    dirp = os.path.join(ROOT, "03_Execution_Layer", d)
    for f in sorted(os.listdir(dirp)):
        if not f.endswith(".md") or f == "README.md":
            continue
        t = read(f"03_Execution_Layer/{d}/{f}")
        rows.append(f"| {field(t,'Document ID')} | {t.splitlines()[0].lstrip('# ').strip()} | {purpose_line(t)} |")
exe = "## Execution Layer — Module Index\n\n> Full modules live in `03_Execution_Layer/`. Each defines a reusable work process; domain content comes from the active Capability Modules.\n\n| ID | Module | Purpose |\n| -- | ------ | ------- |\n" + "\n".join(rows)
parts.append(exe)

toc = "\n".join(f"{i+1}. {p.splitlines()[0].lstrip('# ')}" for i, p in enumerate(parts))
srcs = "\n".join(f"| {t} | {d} | {v} |" for t, d, v in sources_table)

kit = f"""# AI-OS — AI Working Kit

Document ID: DOC-CORE-009
Version: {KIT_VERSION}
Status: Active
Layer: Core
Document Type: Reference
Owner: AI-OS Architecture
Last Updated: {TODAY}

> **GENERATED FILE — do not edit by hand.** This is a rendered copy assembled
> from the official AI-OS documents (sources prevail on conflict, DP-001).
> Regenerate with: `python3 Knowledge_Base/generate_working_kit.py`
>
> **Purpose:** single-file operational context for any AI model working within
> the AI-OS framework.

## Source Versions

| Section | Document ID | Version |
| ------- | ----------- | ------- |
{srcs}

## Table of Contents

{toc}

---

""" + "\n\n---\n\n".join(parts) + "\n"

out = os.path.join(ROOT, "AI-OS_AI_Working_Kit.md")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(kit)
print(f"Generated {out}: {len(kit.splitlines())} lines, {len(parts)} sections")
