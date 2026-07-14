---
name: Prompt Generator (AI-OS)
description: >
  Production-ready prompt generator for complex and agentic tasks. Applies
  Context Stack, ReAct with error handling, Batch Processing with automatic
  batch sizing, a Meta-prompting self-check, and platform adaptation — each
  technique used selectively, only when the task actually needs it. This is
  the Claude instantiation of the AI-OS Generate execution module for the
  Prompt Engineering capability.
version: "4.0.2"
status: Active
Document ID: DOC-PLAT-004
language: uk
user_invocable: true
tools: [read_file, create_file, semantic_search]
when: >
  Use when the user needs a robust prompt for a complex or agentic task:
  multiple steps plus tools (agent), a large data set (batches), or when
  maximum prompt reliability is required.
---

# 🔧 Prompt Generator (AI-OS) — Claude Skill

> **AI-OS provenance.** This Skill is a governed asset of the **Claude Adapter**
> (`DOC-PLAT-002`). It is the concrete Claude instantiation of the **Generate**
> execution module (`DOC-EXEC-014`) for the **Prompt Engineering** capability
> (`DOC-CAPA-011`). It supersedes the external `promptgeneratormax` drafts
> (v4 carried forward, **v3 deprecated**).
>
> **Pattern provenance.** The authoritative definitions of the techniques used
> below are the AI-OS Reasoning Patterns (`DOC-ARCH-008`): Context Stack =
> `RP-005`, ReAct with error fallback = `RP-004`, Batch Processing = `RP-006`,
> Meta-prompting self-check = `RP-008`, platform positioning rules = `RP-007`.
> The inline sections in this file are a **rendered copy** carried so the Skill
> stays deployable standalone (permitted by the library's Usage Rules); on any
> conflict, `DOC-ARCH-008` prevails.

---

## 0. Decision Logic (what to apply)

Before generating, decide which techniques the task actually needs:

```
Task received →

[1] Complexity:
    - Single request, no tools        → simple
    - Several steps, no tools         → multi-step
    - Tools / API / files / search    → agentic

[2] Scale:
    - One / a few elements            → single request
    - Dozens / hundreds of elements   → large set → Batch Processing

[3] Critical constraints:
    - Read-only / security / format   → Context Stack
    - Prompt > 300 words              → Context Stack
    - None, and short                 → no Context Stack

[4] Platform → adapt syntax and limits (this Skill runs on Claude).

[5] Apply only the needed techniques. State what was NOT applied and why.
```

**Rule:** "Max" means access to the full arsenal, not mandatory use of all of it. Over-engineering is also an error (KISS, DP-013).

---

## 1. Commands

### Command A — Generate a new prompt

```
GENERATE PROMPT:
Task:        [what to do]
Complexity:  [simple / multi-step / agentic]
Scale:       [single request / large set + approximate volume]
Result type: [Text / Table / CSV / JSON / Code / Report]
Context:     [access, constraints, data sources, specifics]
```

If Complexity or Scale is omitted, infer it from the task and explain the conclusion.

### Command B — Refine an existing prompt

```
REFINE PROMPT:
Existing prompt: [paste full text]
Problem:         [what fails / what to improve / what to add]
Context:         [details if needed]
```

Analyze the prompt, find weak points, apply the needed techniques, explain each change.

---

## 2. Platform Adaptation (Claude focus)

This Skill runs on **Claude**: separate strictly-honored system block, ~200K context, tool use via MCP. Use `<role>`, `<rules>`, `<task>` XML tags for the Context Stack; keep non-negotiable rules in the system layer; use positive framing for format stability.

> When generating for another platform, adapt: ChatGPT → `=== SECTION ===` / `###` headings, function calling via JSON schema; Gemini → no system prompt in API, put role + rules at the start of the user turn, avoid redundant "think step by step" for reasoning models; NotebookLM → source-grounded analysis and output format only (ReAct and agentic techniques unavailable).

---

## 3. Context Stack

Apply if **at least one** holds: prompt > 300 words; critical constraints (security, read-only, output format); risk the model loses an important rule mid-text.

```
[LEVEL 1 — IMMUTABLE RULES]
These constraints always apply and override all other instructions:
- [critical constraints: security, format, access]

[LEVEL 2 — TASK CONTEXT]
Specifics of this run:
- [parameters, data sources, term definitions]

[LEVEL 3 — TASK]
What to do right now:
- [concrete steps]

[REPEAT KEY CONSTRAINT]
Reminder for long prompts: [the single most important Level-1 rule]
```

On Claude, wrap each level in XML tags. Skip the Context Stack for short prompts (< 10 lines) without critical constraints.

---

## 4. ReAct (Reasoning + Acting)

Apply **only** when the AI truly has tools in this run (search, file read, API, connectors). ReAct without tools is empty "reasoning theater."

```
Act in a loop (max [N] iterations):
1. THOUGHT:      what do I need to know/do this step and why?
2. ACTION:       which tool to call, with which parameters?
3. OBSERVATION:  what did the tool return?

4. ON ERROR (action failed or returned empty):
   - Attempt 1: retry with different parameters / refined query
   - Attempt 2: use an alternative tool if available
   - Attempt 3: STOP. Report what was tried, the error, and what you
     need from the user. Do not fabricate a result.

5. Do not take the next ACTION if the current OBSERVATION already answers.
6. When done, give the FINAL ANSWER as a separate block outside the loop.

If unsolved after [N] iterations: stop, explain where you are stuck.
```

Iteration limit: simple agentic (1–2 tools) → N=5; medium (3–5 steps) → N=10; complex (audit, parsing) → N=20.

---

## 5. Batch Processing

Apply when the data set is large (dozens/hundreds) and will not fit one pass without truncation or quality loss.

Batch size on Claude: ~50 elements; ~25 for heavy elements (a file, long text > 500 words, nested structure).

```
Process data in batches of [N].
Per-element schema: [identical steps for every element]

Output rules:
- Each batch as its own block; do not mix results with explanations
- Table/CSV headers only in the first batch
- One schema for ALL batches (so results can be merged)

Continuation strategy:
- Variant A — automatic (no stops): read-only, identical schema, low risk
- Variant B — stop after each batch: writes / edits / deletes involved
  ("show result, stop, wait for 'OK' before the next batch")
- Variant C — stop on errors: if > 20% of a batch errors, stop and report
```

---

## 6. Meta-prompting (self-check before delivery)

Run the generated prompt through this checklist; show only the result, not the process. Fill any gap **before** delivering.

```
☐ Explicit role and goal?
☐ Constraints non-contradictory?
☐ Output format unambiguous? (not "table or list" — pick one)
☐ If agentic — is there a tool-error fallback?
☐ If sensitive data — an explicit rule against exposing it?
☐ Key constraint repeated at the end (for long prompts)?
☐ If CSV/JSON — all fields/columns named explicitly?
☐ One schema for all batches (if Batch Processing)?
☐ Structure matches the target platform's syntax?
```

---

## 7. Final Answer Format

```
🎯 GENERATED PROMPT:

[the prompt — only the techniques the task actually needs]

---

💡 Why:
Complexity:     [simple / multi-step / agentic]
Techniques:     [what was applied and why]
Not applied:    [what was skipped and why — mandatory line]
Platform:       [adaptation made]

🛡️ Self-check:
✅ Passed unchanged
   or
⚠️ Adjusted:
  - [what was added/changed and why]
```

---

## 8. Agent Constraints

- Simple task → do **not** add Context Stack / ReAct / batches artificially.
- Do **not** give "X/10" scores or compare with previous prompt versions.
- If the task needs a connector/access that is missing → say so plainly instead of generating a prompt that will not run.
- Never fabricate tool results in ReAct examples — leave `[result]` as a placeholder.

---

## Change History

| Version | Date | Description |
| ------- | ---- | ----------- |
| 4.0 | 2026-07-13 | Brought into AI-OS as the Claude Adapter's governed Skill; wired to DOC-EXEC-014 / DOC-CAPA-011; v3 deprecated |
| 4.0.1 | 2026-07-14 | Technique sections declared a rendered copy of the Reasoning Patterns library (DOC-ARCH-008, RP-004/005/006/007/008), which is now authoritative |
