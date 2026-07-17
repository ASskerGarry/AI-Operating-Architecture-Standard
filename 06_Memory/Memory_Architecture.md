# Memory Architecture

Version: 1.1.0
Status: Active
Layer: Memory
Document Type: Standard
Document ID: DOC-MEM-002
Owner: AI-OS Architecture

---

## Purpose

This standard defines how AI-OS manages knowledge **across time** — beyond a single request and beyond a single context window. It establishes a three-tier memory hierarchy, the contract for the persistent `MEMORY.md` artifact, and the consolidation cycle that keeps memory accurate.

It is the Single Source of Truth (SSOT) for AI-OS memory architecture. Other layers reference this standard instead of defining their own memory rules (DP-001, DP-003).

**Position in the architecture:** the Core Layer defines who the AI is; the Capability Layer defines what it knows how to do; this layer defines **what it remembers**. Platform-specific memory mechanisms (e.g. Claude Projects knowledge, `CLAUDE.md` loading) belong to Platform Adapters (DP-009) — this standard defines the platform-agnostic model they implement.

---

## Scope

**Included:** the memory tier model, tier assignment rules, the `MEMORY.md` artifact contract, the consolidation cycle, and the mapping of repository artifacts onto tiers.

**Excluded:** conversation-level context management within one request (Core Execution Engine, DOC-CORE-002); domain knowledge content (Capability Layer); platform storage mechanics (Platform Adapters); external memory runtimes (Letta, Hindsight) — they MAY implement this model but are not required by it.

---

## Memory Tier Model

AI-OS memory is organized in three tiers, ordered by access cost and persistence (modeled on the OS-style hierarchy validated by MemGPT/Letta-class systems):

| Tier | Analogy | Contents | Access | AI-OS Instantiation |
| ---- | ------- | -------- | ------ | ------------------- |
| **Core Memory** | RAM | Identity, stable user profile, active preferences, key entities | Always in context | `MEMORY.md`; assembled system prompt (Core Identity + user preferences per the active Platform Adapter) |
| **Recall Memory** | Disk cache | Recent events, decisions, work-in-progress state | Retrieved on demand (search/reference) | `Change_Log_day.md`; layer Change Logs; session summaries |
| **Archival Memory** | Cold storage | Large reference material, research, media, historical artifacts | Explicitly loaded when needed | `Knowledge_Base/`; `Archive/` |

### Tier Assignment Rules

- Information SHALL live in exactly one authoritative tier (DP-001); other tiers reference it.
- Core Memory SHALL stay small: only what materially changes behavior in most sessions. When in doubt, place content in Recall or Archival and reference it.
- Recall Memory entries SHALL be dated and traceable (DP-008); the log-first policy makes `Change_Log_day.md` the canonical Recall tier for repository work.
- Archival Memory SHALL be indexed or referenced from an official document — unreferenced archival content is invisible and violates DP-007.

---

## The MEMORY.md Contract

`MEMORY.md` is the Core Memory artifact: a single file, always loaded, that turns a general model into a consistent long-term collaborator. It SHALL follow this structure:

```markdown
# MEMORY

## User Profile
<who the user is, role, proficiency level — stable facts only>

## Preferences
<communication, formatting, decision-priority preferences that override defaults>

## Entities
<projects, systems, and terms with agreed definitions (entity resolution)>

## Decisions
<standing decisions that must not be re-litigated, with dates>

## Open Threads
<work in progress that should survive between sessions>
```

Rules:

- Every entry SHALL be a verified fact or an explicit user decision — never an inference presented as fact (Core Identity, Factual Integrity).
- Entries SHOULD be dated where time matters (decisions, open threads).
- `MEMORY.md` SHALL NOT duplicate official documents — it references them (e.g. "prefers output per DOC-CORE-002 Output Policy" rather than restating the policy).
- In this repository, `CLAUDE.md` currently serves the Core Memory role for Claude sessions; a platform-neutral `MEMORY.md` MAY replace or back it, with the Claude Adapter mapping one onto the other.

---

## Consolidation Cycle

Memory is kept accurate through a recurring four-step cycle (the LLM-Wiki pattern):

1. **Orient** — determine what changed since the last consolidation: new sessions, new documents, new decisions. Sources: `Change_Log_day.md`, recent conversation outcomes.
2. **Gather** — extract candidate facts, entities, decisions, and preferences from those sources.
3. **Consolidate** — merge candidates into the correct tier: update `MEMORY.md` sections, add Recall entries, file large material into Archival with a reference. Identical concepts keep identical terminology (DP-006).
4. **Prune** — remove or archive contradictions, superseded decisions, and stale open threads. A contradiction between memory and an official document SHALL be resolved in favor of the official document (registry is authoritative).

Consolidation SHALL be recorded in `Change_Log_day.md` like any other change (log-first policy). Consolidation SHOULD run at natural boundaries: end of a work day, end of a project phase, or when Core Memory grows past roughly one page.

---

### Tooling

The deterministic part of this cycle is automated by
`Knowledge_Base/consolidate_memory.py`: it rotates fully completed day
sections of `Change_Log_day.md` older than 14 days into
`Knowledge_Base/change_log_archive/` (Recall → Archival transition) and
rebuilds `Knowledge_Base/archival_index.md`, the navigable index of the
Archival tier. Dry-run by default; `--apply` writes. Semantic consolidation
(clustering, summarization) remains a manual or model-assisted step.

## Governance

- Memory artifacts follow the same rules as all repository content: log-first change recording, metadata compliance where applicable, and SSOT.
- The Memory Layer owns the **model**; Platform Adapters own the **mechanics** (how a given platform loads Core Memory, e.g. Claude's `CLAUDE.md`/Projects). Adapters SHALL map their mechanism to these tiers explicitly.
- Quality criterion (DP-014): a reader with no session history, given Core + Recall memory, can continue the work without re-asking the user for known facts.

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.1.0              |
| Status         | Active              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-14         |
| Change Summary | Documented the consolidation tooling (consolidate_memory.py, change-log rotation, archival index) |

---

## Related Documents

- Memory Layer README (DOC-MEM-001)
- Core Identity (DOC-CORE-001)
- Core Execution Engine (DOC-CORE-002)
- AI-OS Design Principles (DOC-ARCH-004)
- Claude Adapter (DOC-PLAT-002)
