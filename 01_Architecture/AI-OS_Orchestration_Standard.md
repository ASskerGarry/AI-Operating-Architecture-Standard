# AI-OS Orchestration Standard

Version: 1.1.0
Status: Active
Layer: Architecture
Document Type: Standard
Document ID: DOC-ARCH-009
Owner: AI-OS Architecture

---

## Purpose

This standard defines how AI-OS scales from a single assistant to a **multi-agent system (MAS)**: an Orchestrator coordinating Specialist agents, each built from existing AI-OS building blocks. It is the Single Source of Truth (SSOT) for the orchestration model.

The central design decision: **AI-OS already contains the agent contracts.** A Capability Module defines what a Specialist knows; an Execution Module defines the protocol a task follows; the Capability Registry defines routing. Orchestration adds coordination rules on top — it does not introduce a parallel architecture (DP-003, DP-010).

**Validation status:** promoted to **Active** on 2026-07-19 after the first orchestrated deployment passed the Quality Validation criteria of DOC-CORE-002 (DP-015). Evidence: the MAS pilot run (`Knowledge_Base/mas_pilot/run_2026-07-19.md`) — a sequential Analyze → Generate → Validate pipeline with three Specialist subagents on Claude Code that produced, reviewed (two iterations, independent Reviewer), and promoted the Power Query Capability Module (DOC-CAPA-022). The run exercised task/response packets, context isolation, escalations, iteration budgets, and all three quality-gate layers as specified.

---

## Scope

**Included:** the platform-agnostic orchestration model — roles, routing, handoff contracts, context isolation, quality gates, and orchestration patterns.

**Excluded:** platform mechanics for spawning and running agents (Claude subagents, API-level agent frameworks — owned by Platform Adapters, DP-009); domain expertise (Capability Layer); memory internals (DOC-MEM-002).

---

## When to Use MAS — and When Not To

Orchestration is a cost. Apply it only when a single agent demonstrably cannot deliver (DP-013).

| Criterion | Single agent | MAS justified |
| --------- | ------------ | ------------- |
| Domains involved | One or two related | Several deep, distinct specializations |
| Context pressure | Fits comfortably in one window | Task context would crowd out instructions (attention drift) |
| Parallelism | Sequential work | Independent subtasks that can run concurrently |
| Failure isolation | Errors are cheap to correct inline | One subtask's failure must not poison the rest |
| Verification | Self-check suffices (RP-008) | Independent review adds real assurance (RP-009) |

If none of the right-hand column applies, use a single agent with the relevant Capability Modules activated. A MAS with one meaningful agent is over-engineering.

---

## Role Model

| Role | Built from | Responsibility |
| ---- | ---------- | -------------- |
| **Orchestrator** | Core Identity + Core Execution Engine | Decomposes the objective, routes subtasks, owns the merged result and final quality gate. Does not perform specialist work itself. |
| **Specialist agent** | One Capability Module (Primary) + the Execution Module matching its subtask | Executes exactly one subtask per handoff, within its declared expertise. |
| **Reviewer agent** (optional) | Capability Module relevant to the artifact + Validate (DOC-EXEC-015) | Independent check against acceptance criteria; used when the cost of an undetected error is high. |

Rules:

- Each Specialist SHALL have exactly one Primary capability per subtask (SoC, DP-002). Partner capabilities follow the Recommended Partners field of the module.
- The Orchestrator SHALL NOT restate specialist knowledge in its own instructions — it references the module (DP-001).
- Agent identity is assembled per the target platform's Adapter Assembly Rule (e.g. DOC-PLAT-002 for Claude).

---

## Routing

The **Capability Registry** (DOC-CAPA-002) is the routing table: the Orchestrator matches each subtask's domain to a module's Capability Domain and Role Eligibility. The **Execution Registry** (DOC-EXEC-005) selects the process (Analyze / Generate / Validate / Optimize / …).

Routing decisions SHALL be explicit in the task packet (below) so every delegation is traceable (DP-008).

---

## Handoff Contract

Delegation and return are structured packets — never free-form chat.

**Task packet (Orchestrator → Specialist):**

```
objective:        <one sentence — what done looks like>
capability:       <DOC-CAPA-NNN to act as (Primary)>
execution:        <DOC-EXEC-NNN protocol to follow>
context:          <only the slice this subtask needs — see Context Isolation>
constraints:      <immutable rules for this subtask (RP-005 Level 1)>
output_contract:  <exact format + acceptance criteria>
iteration_budget: <N per RP-004: 5 simple / 10 medium / 20 complex>
```

**Response packet (Specialist → Orchestrator):**

```
result:       <the artifact, in the contracted format>
assumptions:  <what was assumed where information was missing>
confidence:   <high / medium / low, with the weakest point named>
escalations:  <anything outside scope or budget — returned, not guessed>
```

A Specialist that exhausts its iteration budget or hits a hard blocker SHALL escalate rather than fabricate (RP-004 error rule; Core Identity, Factual Integrity).

---

## Context Isolation

Per the Memory Architecture (DOC-MEM-002):

- **Shared Core Memory** — every agent receives the same minimal identity/preferences slice; kept small by design.
- **Scoped task context** — each Specialist gets only its subtask's slice, positioned per RP-007 (data first, directives last). Full-history sharing is prohibited: it recreates the attention-drift problem MAS exists to solve.
- **Recall discipline** — the Orchestrator records decomposition, routing, and merge decisions in the Recall tier (`Change_Log_day.md` for repository work; run log otherwise), so the run is reconstructible (DP-008).

---

## Quality Gates

Validation is embedded at every boundary (DP-014):

1. **Pre-dispatch** — the Orchestrator checks each task packet against the Meta-prompting checklist (RP-008): unambiguous contract, non-conflicting constraints, error fallback present.
2. **On return** — each response packet is checked against its own output contract before merging; failures go back with the specific defect, within the iteration budget.
3. **Post-merge** — the assembled result passes the Quality Validation criteria of DOC-CORE-002; high-stakes results additionally pass an independent Reviewer agent (RP-009).

---

## Orchestration Patterns

| Pattern | Shape | Use when | Built on |
| ------- | ----- | -------- | -------- |
| **Sequential pipeline** | A → B → C, each output is the next input | Staged transformation (analyze → generate → optimize) | RP-010; each stage's summary passes forward, not full history |
| **Parallel fan-out** | Orchestrator → N specialists → merge | Independent subtasks (per-domain analysis, large corpora) | RP-006 semantics: one schema for all branches, or results cannot merge |
| **Review loop** | Producer ⇄ Reviewer until gate passes | High cost of undetected error | RP-009; bounded iterations, then escalate to the user |

Patterns compose (a fan-out branch may itself be a pipeline), but composition depth SHOULD stay ≤ 2 until the model is validated in practice.

---

## Platform Mapping

Platform mechanics belong to adapters (DP-009). For Claude, the natural mapping — to be specified in the Claude Adapter (DOC-PLAT-002) when implementation begins:

| This standard | Claude primitive |
| ------------- | ---------------- |
| Orchestrator | Main session (Claude Code / Projects) |
| Specialist agent | Subagent / Agent tool invocation with scoped prompt |
| Task packet | Subagent prompt assembled per the Adapter's Assembly Rule |
| Shared Core Memory | `CLAUDE.md` (DOC-PLAT-003) |

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.1.0              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-19         |
| Created date   | 2026-07-14         |
| Change Summary | Promoted to Active: first orchestrated deployment (MAS pilot, Power Query module) passed DOC-CORE-002 validation per DP-015 |

---

## Related Documents

- Core Identity (DOC-CORE-001) / Core Execution Engine (DOC-CORE-002)
- Capability Registry (DOC-CAPA-002) / Execution Registry (DOC-EXEC-005)
- Validate (DOC-EXEC-015)
- Memory Architecture (DOC-MEM-002)
- AI-OS Reasoning Patterns (DOC-ARCH-008)
- Claude Adapter (DOC-PLAT-002)
- AI-OS Design Principles (DOC-ARCH-004)
