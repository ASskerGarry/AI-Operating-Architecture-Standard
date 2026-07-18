#!/usr/bin/env python3
"""
AI-OS Behavioral Evaluation Runner (DOC-EXEC-024)

Scores a set of behavioral cases (cases.jsonl) deterministically and writes a
metrics JSON. By default each case's curated golden response is scored — that
produces the baseline. To evaluate a real model or a changed instruction set,
record its answers into a responses file {case_id: response_text} and pass
--responses; the same checks then measure the candidate behavior.

Metrics (see eval_spec.json):
  task_success_rate        pass rate of group "task"
  policy_compliance_rate   pass rate of group "policy"
  refusal_correctness_rate pass rate of group "refusal"
  format_adherence_rate    pass rate of group "format"
  hallucination_flag_rate  FAIL rate of group "hallucination" (lower is better)

Usage:
  python3 run_behavior_eval.py --cases cases.jsonl --output results.json
  python3 run_behavior_eval.py --cases cases.jsonl --responses model_answers.json --output results.json

Stdlib-only by design (no supply-chain surface), same as the other AI-OS tools.
"""
import argparse
import json
import re
import sys

GROUP_METRIC = {
    "task": "task_success_rate",
    "policy": "policy_compliance_rate",
    "refusal": "refusal_correctness_rate",
    "format": "format_adherence_rate",
    "hallucination": "hallucination_flag_rate",
    "injection": "injection_resistance_rate",
}


def check_case(response, checks):
    """True if the response passes every declared check."""
    for needle in checks.get("must_contain", []):
        if needle.lower() not in response.lower():
            return False
    for needle in checks.get("must_not_contain", []):
        if needle.lower() in response.lower():
            return False
    pattern = checks.get("regex")
    if pattern and not re.fullmatch(pattern, response.strip(), re.S):
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True)
    ap.add_argument("--responses", help="JSON file {case_id: response}; defaults to golden answers")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    responses = {}
    if args.responses:
        with open(args.responses, encoding="utf-8") as fh:
            responses = json.load(fh)

    totals, passed, failures = {}, {}, []
    with open(args.cases, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            case = json.loads(line)
            group = case["group"]
            if group not in GROUP_METRIC:
                sys.exit(f"unknown group '{group}' in case {case['id']}")
            response = responses.get(case["id"], case["golden"])
            ok = check_case(response, case["checks"])
            totals[group] = totals.get(group, 0) + 1
            passed[group] = passed.get(group, 0) + (1 if ok else 0)
            if not ok:
                failures.append(case["id"])

    results = {}
    for group, metric in GROUP_METRIC.items():
        if group not in totals:
            continue
        rate = passed[group] / totals[group]
        # hallucination metric counts flagged (failed) cases: lower is better
        results[metric] = round(1 - rate, 4) if group == "hallucination" else round(rate, 4)

    results["_cases_total"] = sum(totals.values())
    results["_cases_failed"] = failures

    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    print(f"Scored {results['_cases_total']} cases -> {args.output}")
    for metric in sorted(k for k in results if not k.startswith("_")):
        print(f"  {metric}: {results[metric]}")
    if failures:
        print(f"  failed cases: {', '.join(failures)}")


if __name__ == "__main__":
    main()
