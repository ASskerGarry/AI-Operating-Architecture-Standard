#!/usr/bin/env python3
"""
AI-OS FinOps size gate.

Fails (exit 1) if either Working Kit grew more than the allowed ratio over
the recorded baseline — protecting the model-facing context (and its token
cost) from silent bloat. Growth is legitimate only as an explicit decision:
update the baseline in the same change-set with --update and justify it in
the change log.

Usage:
  python3 Knowledge_Base/check_kit_size.py            # gate (CI)
  python3 Knowledge_Base/check_kit_size.py --update   # record new baseline
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE = os.path.join(ROOT, "Knowledge_Base", "kit_size_baseline.json")
KITS = ["AI-OS_AI_Working_Kit.md", "AI-OS_AI_Working_Kit_lean.md"]
MAX_GROWTH = 0.15  # +15% over baseline fails the gate


def sizes():
    return {k: os.path.getsize(os.path.join(ROOT, k)) for k in KITS}


def main():
    current = sizes()
    if "--update" in sys.argv:
        with open(BASELINE, "w", encoding="utf-8") as fh:
            json.dump(current, fh, indent=2)
        print(f"Baseline updated: {current}")
        return

    with open(BASELINE, encoding="utf-8") as fh:
        base = json.load(fh)

    failed = False
    for kit, cur in current.items():
        b = base.get(kit)
        if b is None:
            print(f"FINOPS GATE: {kit} missing from baseline — run --update")
            failed = True
            continue
        growth = (cur - b) / b
        mark = "FAIL" if growth > MAX_GROWTH else "ok"
        print(f"  {kit}: {b} -> {cur} bytes ({growth:+.1%}, limit +{MAX_GROWTH:.0%}) [{mark}]")
        if growth > MAX_GROWTH:
            failed = True

    if failed:
        print("FINOPS GATE: FAIL — kit growth exceeds the limit; either trim the "
              "content or update the baseline deliberately (--update + change-log entry)")
        sys.exit(1)
    print("FINOPS GATE: PASS")


if __name__ == "__main__":
    main()
