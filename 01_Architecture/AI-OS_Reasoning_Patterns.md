# AI-OS Reasoning Patterns

Version: 1.0.1
Status: Active
Layer: Architecture
Document Type: Reference
Document ID: DOC-ARCH-008
Owner: AI-OS Architecture

---

## Purpose

This document is the Single Source of Truth (SSOT) for reusable reasoning and prompting patterns used across AI-OS. Each pattern has a stable ID (`RP-NNN`) so that Capability Modules, Execution Modules, and Platform assets can **reference** a pattern instead of re-describing it (DP-001, DP-003, DP-010).

A pattern entry answers four questions: what it does, when to use it, when **not** to use it, and what its structure looks like. Selecting the right pattern — and declining unnecessary ones — is part of the pattern discipline: over-engineering is an error (DP-013).

---

## Scope

**Included:** platform-agnostic reasoning and prompt-structure patterns.

**Excluded:** platform-specific syntax (XML tags, section markers — owned by Platform Adapters, DP-009); domain expertise (Capability Layer); execution sequencing (Execution Layer). Pattern IDs are immutable; superseded patterns are marked Deprecated, never deleted.

---

## Pattern Index

| ID | Pattern | Class | One-line purpose |
| -- | ------- | ----- | ---------------- |
| RP-001 | Chain-of-Thought | Reasoning | Force explicit intermediate steps for multi-step problems |
| RP-002 | Tree-of-Thoughts | Reasoning | Explore several solution paths before committing |
| RP-003 | Self-Consistency | Validation | Filter stochastic errors by majority over repeated runs |
| RP-004 | ReAct with Error Fallback | Agentic | Tool loop: thought → action → observation, with failure handling |
| RP-005 | Context Stack | Structure | Layer instructions by authority so critical rules cannot be diluted |
| RP-006 | Batch Processing | Scale | Process large data sets in uniform, mergeable chunks |
| RP-007 | Inverted Context Positioning | Structure | Place directives after large data to counter attention drift |
| RP-008 | Meta-prompting Self-Check | Validation | Audit a generated prompt against a checklist before delivery |
| RP-009 | Constitutional Self-Critique | Validation | Draft → critique against principles → revise before delivery |
| RP-010 | Recursive Prompting | Reasoning | Chain outputs as inputs for staged transformation |

---

## RP-001 — Chain-of-Thought (CoT)

**Purpose:** improve accuracy on multi-step tasks by requiring explicit intermediate reasoning instead of a direct answer.

**Use when:** the task has verifiable intermediate steps — calculations, audits, multi-criteria evaluation (e.g. a staged SQL review: returned data → join efficiency → predicate/index use → row estimate → I/O cost).

**Do not use when:** the task is trivial (adds noise), or the target is a dedicated reasoning model whose provider advises against explicit "think step by step" triggers — redundant CoT can degrade such models.

**Structure:** enumerate the required stages explicitly; require the answer only after the stages. A fixed stage list beats a generic "think step by step."

---

## RP-002 — Tree-of-Thoughts (ToT)

**Purpose:** avoid premature commitment by generating and comparing several candidate approaches before selecting one.

**Use when:** design and architecture decisions with real trade-offs (cost vs. complexity vs. scalability) where the first idea is often not the best.

**Do not use when:** one correct procedure exists (use RP-001) or the decision is cheap to reverse.

**Structure:** generate N distinct approaches → evaluate each against named criteria → select with justification → discard the rest explicitly.

---

## RP-003 — Self-Consistency

**Purpose:** filter stochastic errors by running the same task several times (at higher temperature where controllable) and taking the modal answer.

**Use when:** answers are short and comparable (classification, extraction, numeric results) and single-run reliability is insufficient.

**Do not use when:** outputs are long-form and non-comparable, or the run budget does not allow repeats.

**Structure:** K independent runs → normalize answers → majority vote; report disagreement rate as an uncertainty signal.

---

## RP-004 — ReAct with Error Fallback

**Purpose:** structure tool-using (agentic) work as an explicit loop so each action is justified by the previous observation, and tool failures degrade gracefully instead of producing fabricated results.

**Use when:** the AI actually has tools in the current run (search, file access, APIs, connectors) and the task needs multiple look-then-act iterations.

**Do not use when:** no tools are available — ReAct without tools is empty reasoning theater.

**Structure:**

```
Loop (max N iterations):
  THOUGHT      what is needed this step and why
  ACTION       tool + parameters
  OBSERVATION  tool result
  ON ERROR     retry with changed parameters → alternative tool →
               STOP and report (never fabricate)
Stop early when the observation already answers; final answer outside the loop.
```

Iteration budget: ~5 (1–2 tools), ~10 (3–5 steps), ~20 (audits/parsing).

---

## RP-005 — Context Stack

**Purpose:** make the instruction hierarchy explicit so critical rules (security, read-only, output contract) are not diluted by task detail.

**Use when:** the prompt exceeds ~300 words, or contains constraints that must never be overridden, or mixes instructions of different authority.

**Do not use when:** the prompt is short (< 10 lines) with no critical constraints.

**Structure:** `LEVEL 1 — immutable rules` (highest authority, stated as overriding) → `LEVEL 2 — task context` → `LEVEL 3 — the task` → optional key-rule repetition at the end (see RP-007). Platform Adapters define the concrete markup (e.g. XML tags on Claude).

---

## RP-006 — Batch Processing

**Purpose:** process data sets too large for one pass without truncation or quality decay, in chunks that can be merged.

**Use when:** dozens to hundreds of uniform elements (files, rows, documents).

**Do not use when:** the set fits one pass comfortably.

**Structure:** fixed batch size (platform-dependent; halve it for heavy elements) → identical schema for every batch (headers once) → results separated from commentary → continuation strategy: **A** automatic (read-only, low risk), **B** stop for confirmation after each batch (writes/deletes), **C** auto-stop if > 20% of a batch errors.

**Key rule:** one schema for ALL batches — otherwise results cannot be merged.

---

## RP-007 — Inverted Context Positioning

**Purpose:** counter attention drift in large contexts: directives placed before a large data mass lose priority by the time the model acts.

**Use when:** the prompt carries a large reference payload (documents, tables, logs) followed by work to do.

**Do not use when:** the prompt is short — position effects are negligible.

**Structure:** data first, critical instructions last; reactivate attention with a bridging anchor ("Based on all the information provided above, now do the following…"). Combine with RP-005 by repeating the key Level-1 rule at the very end.

---

## RP-008 — Meta-prompting Self-Check

**Purpose:** audit a generated prompt against an explicit checklist before delivering it, and fix gaps before — not after — the user sees it.

**Use when:** producing prompt artifacts for reuse or for agentic execution.

**Do not use when:** the artifact is a throwaway one-liner.

**Structure (minimum checklist):** explicit role and goal · non-contradictory constraints · unambiguous output format · tool-error fallback if agentic (RP-004) · sensitive-data rule if applicable · key constraint repeated at the end for long prompts (RP-007) · all fields named if CSV/JSON · one schema across batches (RP-006) · syntax matches the target platform. Report only the result ("passed" / "adjusted: …").

---

## RP-009 — Constitutional Self-Critique

**Purpose:** improve a draft by critiquing it against a named set of principles before delivery, ending with the explicit question "did I miss anything?"

**Use when:** the deliverable must conform to a known rule set (e.g. AI-OS review checklists, REST principles, style standards).

**Do not use when:** no explicit principle set exists — critique without criteria drifts into rewriting by taste.

**Structure:** draft → critique strictly against the listed principles → revise → answer "what did I miss?" → deliver. In AI-OS, the principle set is typically a Review Standard or the Design Principles (DOC-ARCH-004).

---

## RP-010 — Recursive Prompting

**Purpose:** decompose a large transformation into staged passes where each stage's output is the next stage's input, preserving quality beyond single-pass limits.

**Use when:** staged refactoring (extract → type → test), or documents larger than a comfortable context slice — segment the input, carry a compact structured summary ("context memory") between segments, and keep segments well under half the context window to avoid degradation.

**Do not use when:** a single pass suffices — stages add latency and drift risk.

**Structure:** define stages with explicit output contracts → run sequentially, feeding forward the previous output (or its structured summary) → validate at each boundary (quality gate per DP-014).

---

## Usage Rules

- Documents SHALL reference patterns by ID (`RP-004`) instead of restating them; a one-line gloss is permitted for readability.
- Platform assets that must run standalone (e.g. a deployed Skill) MAY carry a rendered copy of pattern text; the copy SHALL declare this document as its source, and this document prevails on conflict.
- New patterns receive the next `RP-NNN`; changed semantics require a version bump here and a change-log entry (log-first).

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.1              |
| Status         | Active              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-14         |
| Change Summary | Promoted to Active after Quality Gate review |

---

## Related Documents

- AI-OS Design Principles (DOC-ARCH-004)
- Prompt Engineering (DOC-CAPA-011)
- Generate (DOC-EXEC-014)
- Claude Adapter (DOC-PLAT-002)
- AI-OS Glossary (DOC-ARCH-003)
