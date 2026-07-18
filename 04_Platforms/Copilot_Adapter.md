# Copilot Adapter

Version: 1.0.0
Status: Draft
Layer: Platform
Document Type: Platform Adapter
Document ID: DOC-PLAT-008
Owner: AI-OS Architecture

---

## Purpose

This document is the **GitHub Copilot Platform Adapter**. It defines how AI-OS governs the AI coding assistants operating **inside this repository** — Copilot Chat, Copilot coding agent, and compatible agents — so their behavior follows AI-OS rules without altering any Core document (DP-009).

Unlike the conversational adapters (Claude/GPT/Gemini), Copilot's unit of deployment is the **repository itself**: instructions ship as files the platform auto-loads.

Status is **Draft by design**: promotion to Active requires observed compliant behavior from Copilot agents on real tasks (DP-015).

---

## Scope

**Included:** mapping of AI-OS concepts to Copilot instruction files, the governed content of `.github/copilot-instructions.md`, interaction rules with the CI gates, constraints.

**Excluded:** conversational deployments (other adapters); IDE-level personal Copilot settings (out of repository governance).

---

## Concept Mapping

| AI-OS Concept | Copilot Primitive | Notes |
| ------------- | ----------------- | ----- |
| Agent ground rules | `.github/copilot-instructions.md` | Auto-loaded into Copilot Chat / coding agent context for this repo; governed by this adapter |
| Cross-agent instructions | `AGENTS.md` (DOC-CORE-008) | Shared standard consumed by multiple agent products; copilot-instructions defers to it |
| Core Identity / Execution Engine | Referenced, not embedded | Copilot context is small — instruct the agent to consult the lean kit instead of embedding it |
| Quality Gates | CI workflows (`validate.yml`, `behavior_eval.yml`) | Agent-produced PRs pass the same gates as human changes — no exceptions |
| Change governance | Log-first rule in the instructions | Agents MUST write the Change_Log_day.md entry as part of every change-set |

---

## Governed Asset: `.github/copilot-instructions.md`

The deployable asset of this adapter. Its content contract:

1. Identify the repository as an AI-OS-governed standard (link the lean kit for orientation).
2. State the two non-negotiable rules: **log first** and **registry before Active**.
3. Require agents to run `validate_aios.py` and the behavioral gate locally before proposing changes.
4. Forbid: editing generated files by hand (Working Kits, archival index, baselines except via their scripts), adding write surfaces to the MCP server, unregistering or renumbering Document IDs.
5. Stay short (< 60 lines) — Copilot context is expensive; depth lives in `AGENTS.md` and the kit.

---

## Platform Constraints

| Constraint | Behavior on Copilot |
| ---------- | ------------------- |
| Small effective context | Instructions must be brief and reference-based, not embedded copies |
| Agent-initiated PRs | Enter the same PR + ruleset + CI path as human changes; the two gates are the enforcement point |
| No tool-calling contract | Copilot cannot call the MCP server; it reads repository files directly — the registry and lean kit are its "tools" |
| Behavioral drift | Not directly testable via DOC-EXEC-024 (no scriptable chat surface); enforcement is CI-side |

---

## Deployment Procedure

1. Keep `.github/copilot-instructions.md` in sync with this adapter's content contract (it is reviewed like any governed change).
2. Observe agent-produced changes: a compliant agent logs first, registers documents, and passes both gates.
3. Promotion to Active requires: at least one nontrivial Copilot-agent change-set that satisfied all governance rules without human correction, recorded in the change log as evidence.

---

# Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.0              |
| Status         | Draft              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-17         |
| Created date   | 2026-07-17         |
| Change Summary | Initial adapter: repository-as-deployment model, copilot-instructions content contract, CI-side enforcement |

---

# Related Documents

- AI-OS Agent Instructions (DOC-CORE-008)
- Claude Adapter (DOC-PLAT-002)
- GPT Adapter (DOC-PLAT-006)
- Gemini Adapter (DOC-PLAT-007)
- Behavioral Evaluation (DOC-EXEC-024)
- Platform Layer README (DOC-PLAT-001)
