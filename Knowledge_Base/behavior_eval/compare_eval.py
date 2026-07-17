#!/usr/bin/env python3
"""
AI-OS Behavioral Evaluation Gate — comparator (DOC-EXEC-024)

Enforces the thresholds and regression limits from eval_spec.json:
  - every metric must satisfy its min/max threshold;
  - no metric may regress from the baseline by more than max_absolute_drop
    (critical metrics: critical_max_absolute_drop).

Exit code 0 = gate passed, 1 = gate failed. Stdlib-only.

Usage:
  python3 compare_eval.py --spec eval_spec.json \
      --baseline baseline_results.json --candidate results_candidate.json
"""
import argparse
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--candidate", required=True)
    args = ap.parse_args()

    spec, baseline, candidate = load(args.spec), load(args.baseline), load(args.candidate)
    max_drop = spec["regression"]["max_absolute_drop"]
    crit_drop = spec["regression"]["critical_max_absolute_drop"]

    failures = []
    for m in spec["metrics"]:
        name, critical = m["name"], m.get("critical", False)
        b, c = baseline.get(name), candidate.get(name)
        if b is None or c is None:
            failures.append(f"{name}: missing in baseline or candidate")
            continue
        if "min" in m and c < m["min"]:
            failures.append(f"{name}: {c:.4f} below min {m['min']:.4f}")
        if "max" in m and c > m["max"]:
            failures.append(f"{name}: {c:.4f} above max {m['max']:.4f}")
        # regression: for min-metrics a drop is bad, for max-metrics a rise is bad
        delta = (b - c) if "min" in m else (c - b)
        allowed = crit_drop if critical else max_drop
        if delta > allowed:
            failures.append(f"{name}: regression {delta:+.4f} exceeds allowed {allowed:.4f}"
                            f" ({'critical' if critical else 'normal'})")

    if failures:
        print("BEHAVIORAL GATE: FAIL")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("BEHAVIORAL GATE: PASS — all thresholds met, no regression beyond limits")


if __name__ == "__main__":
    main()
