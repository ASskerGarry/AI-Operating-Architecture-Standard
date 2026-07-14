# Memory Layer

Version: 1.0.1
Status: Active
Layer: Memory
Document Type: README
Document ID: DOC-MEM-001
Owner: AI-OS Architecture

---

## Purpose

The Memory Layer defines how AI-OS retains and retrieves knowledge **across sessions** — the persistence dimension the other layers deliberately do not cover. Core defines identity, Capability defines expertise, Execution defines process; Memory defines continuity.

---

## Contents

| Document | ID | Role |
| -------- | -- | ---- |
| [Memory Architecture](Memory_Architecture.md) | DOC-MEM-002 | SSOT: three-tier model (Core / Recall / Archival), `MEMORY.md` contract, consolidation cycle |

---

## Relationship to Other Layers

- **Core Layer** — Core Identity is *part of* Core Memory when assembled into a system prompt, but is owned by `00_Core`; this layer only places it in the tier model.
- **Platform Layer** — adapters implement the memory mechanics for each platform (e.g. the Claude Adapter maps Core Memory onto `CLAUDE.md` / Project instructions).
- **Existing artifacts** — `Change_Log_day.md` (Recall tier) and `Knowledge_Base/` (Archival tier) already play memory roles de facto; the Memory Architecture standard formalizes them.

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

- Memory Architecture (DOC-MEM-002)
- AI-OS Document Registry (DOC-ARCH-001)
- AI-OS Design Principles (DOC-ARCH-004)
