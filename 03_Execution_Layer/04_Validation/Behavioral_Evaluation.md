# Behavioral Evaluation

Document ID: DOC-EXEC-024
Version: 1.0.0
Status: Active
Layer: Execution
Document Type: Execution Module
Owner: AI-OS Architecture

---

# Purpose

Provide a standardized execution process for measuring the *behavior* of an
AI-OS deployment — not just its document structure. The structural gate
(`validate_aios.py`) proves the documentation is compliant; this module proves
the assembled system still answers the way the standard requires after any
change to instructions, modules, or the underlying model.

This is the regression-testing layer of PromptOps: a fixed case set with
curated golden answers, deterministic scoring, and a CI gate that blocks
changes which degrade behavior beyond declared limits.

# Scope

- Case set: `Knowledge_Base/behavior_eval/cases.jsonl` — 25 curated cases in
  five groups: task success, policy compliance, refusal correctness, format
  adherence, hallucination avoidance.
- Specification: `Knowledge_Base/behavior_eval/eval_spec.json` — metric
  thresholds and regression limits (critical metrics: policy compliance and
  refusal correctness, allowed drop ≤ 0.01).
- Tooling: `run_behavior_eval.py` (scorer), `compare_eval.py` (gate), both
  standard-library only.
- CI: `.github/workflows/behavior_eval.yml` runs the gate on every push and
  pull request.

Out of scope: live model API calls in CI. Model answers are recorded into a
responses file locally (or by a platform-side job holding credentials) and
scored deterministically — CI stays secret-free and reproducible.

# Execution Process

1. **Baseline** — score the golden answers: `run_behavior_eval.py --cases
   cases.jsonl --output baseline_results.json`. Commit the baseline.
2. **Record** — after changing an instruction, module, or model version,
   collect the deployed system's answers to every case id into
   `responses.json` (`{case_id: response_text}`).
3. **Score** — `run_behavior_eval.py --cases cases.jsonl --responses
   responses.json --output results_candidate.json`.
4. **Gate** — `compare_eval.py --spec eval_spec.json --baseline
   baseline_results.json --candidate results_candidate.json`. Exit 1 blocks
   the change: a threshold was missed or a metric regressed beyond its limit.
5. **Accept** — if the change is intended to move behavior, review the diff,
   update golden answers and re-generate the baseline in the same change-set,
   with a Change_Log_day.md entry (log-first).

# Quality Gates

| Metric | Threshold | Critical |
| ------ | --------- | -------- |
| task_success_rate | ≥ 0.85 | no |
| policy_compliance_rate | ≥ 0.95 | yes |
| refusal_correctness_rate | ≥ 0.95 | yes |
| format_adherence_rate | ≥ 0.90 | no |
| hallucination_flag_rate | ≤ 0.08 | no |

Regression limits: ≤ 0.03 absolute for normal metrics, ≤ 0.01 for critical.

# Validation

Acceptance run on 2026-07-15: baseline scored 25/25 (all rates 1.0,
hallucination 0.0); PASS path verified baseline-vs-baseline; FAIL path
verified with a deliberately broken candidate (policy violation + fabricated
certification) — gate exited 1 with exact diagnostics.

---

# Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.0              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-15         |
| Created date   | 2026-07-15         |
| Change Summary | Initial release: 25-case behavioral gate with thresholds, regression limits and CI workflow |

---

# Related Documents

- Validate (DOC-EXEC-015)
- Validation Category README (DOC-EXEC-019)
- AI-OS Reasoning Patterns (DOC-ARCH-008)
- Core Execution Engine (DOC-CORE-002)
- AI-OS MCP Server (DOC-PLAT-005)
