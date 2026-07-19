#!/usr/bin/env python3
"""
AI-OS Link Integrity gate.

Scans official-scope markdown (same scope rules as validate_aios.py:
Knowledge_Base/, Archive/ and dot-directories excluded) for relative
markdown links and fails (exit 1) if any target does not exist. External
links (http/https/mailto) and pure in-page anchors are skipped — this gate
guards repository-internal integrity, deterministically and offline.

Usage:  python3 Knowledge_Base/check_links.py [repo_root]
"""
import os
import re
import sys
import urllib.parse

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
SKIP_PREFIXES = ("Knowledge_Base", "Archive", "docs")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def in_scope(rel):
    parts = rel.replace("\\", "/").split("/")
    if any(p.startswith(".") for p in parts if p):
        return False
    return parts[0] not in SKIP_PREFIXES


def md_files():
    for dp, dn, fn in os.walk(ROOT):
        rel_dir = os.path.relpath(dp, ROOT)
        if rel_dir != "." and not in_scope(rel_dir):
            dn[:] = []
            continue
        for f in fn:
            if f.lower().endswith(".md"):
                yield os.path.join(dp, f)


def main():
    broken = []
    checked = 0
    for path in md_files():
        rel_file = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            checked += 1
            clean = urllib.parse.unquote(target.split("#", 1)[0])
            if not clean:
                continue
            base = ROOT if clean.startswith("/") else os.path.dirname(path)
            resolved = os.path.normpath(os.path.join(base, clean.lstrip("/")))
            if not os.path.exists(resolved):
                broken.append(f"{rel_file}: ({target}) -> missing {os.path.relpath(resolved, ROOT)}")

    print(f"Checked {checked} relative link(s) across official markdown.")
    if broken:
        print("LINK INTEGRITY GATE: FAIL")
        for b in broken:
            print("  -", b)
        sys.exit(1)
    print("LINK INTEGRITY GATE: PASS")


if __name__ == "__main__":
    main()
