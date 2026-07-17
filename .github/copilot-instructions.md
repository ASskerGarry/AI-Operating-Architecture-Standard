# Copilot Instructions — AI-OS Repository

This repository is an AI-OS-governed architecture standard (governed by the
Copilot Adapter, DOC-PLAT-008). For orientation read
`AI-OS_AI_Working_Kit_lean.md`; for agent ground rules see `AGENTS.md`.

## Non-negotiable rules

1. **Log first.** Every change-set starts with an entry in
   `Change_Log_day.md` (time, author, scope, change, reason, files, status)
   — before or as the change is made, never only after.
2. **Registry before Active.** A document may not carry `Status: Active`
   unless it is registered in `01_Architecture/AI-OS_Document_Registry.md`.
   Document IDs are immutable and never reused.

## Before proposing any change

Run both gates locally and include the results in the PR description:

```bash
python3 Knowledge_Base/validate_aios.py .          # expect: TOTAL FLAGGED ITEMS: 0
python3 Knowledge_Base/behavior_eval/run_behavior_eval.py \
  --cases Knowledge_Base/behavior_eval/cases.jsonl \
  --output Knowledge_Base/behavior_eval/results_candidate.json
python3 Knowledge_Base/behavior_eval/compare_eval.py \
  --spec Knowledge_Base/behavior_eval/eval_spec.json \
  --baseline Knowledge_Base/behavior_eval/baseline_results.json \
  --candidate Knowledge_Base/behavior_eval/results_candidate.json
python3 Knowledge_Base/check_kit_size.py           # FinOps size gate
```

## Never do

- Edit generated files by hand: `AI-OS_AI_Working_Kit*.md` (use
  `generate_working_kit.py`), `archival_index.md` (use
  `consolidate_memory.py`), eval baselines (use the eval scripts).
- Add write tools to the AI-OS MCP server (read-only by design,
  DOC-PLAT-005).
- Renumber, reuse, or unregister Document IDs.
- Commit commercial/private content — the public repo carries the open
  core only.
