# AI-OS — AI Operating Architecture Standard

Document ID: DOC-CORE-005
Version: 1.2.0
Status: Active
Layer: Core
Document Type: README
Owner: AI-OS Architecture

**AI-OS** is a layered, platform-agnostic architecture standard for operating an AI assistant as a governed system — not a pile of prompts.

It separates *who the AI is* (stable identity) from *what it knows* (capabilities), *how it works* (execution processes), and *where it runs* (platform adapters), with enterprise-style documentation governance on top: a document registry, immutable IDs, metadata standards, lifecycle states, and a mandatory change log.

---

## Architecture at a Glance

| Layer | Directory | Responsibility | Analogy |
| ----- | --------- | -------------- | ------- |
| **Core** | `00_Core/` | Identity, values, decision priorities, execution engine | Kernel |
| **Architecture** | `01_Architecture/` | Design principles (DP-001…015), registry, metadata & documentation standards, glossary | System policies |
| **Capability** | `02_Capability_Layer/` | Domain expertise modules (Prompt Engineering, SQL, Python, Data Analytics, Power BI, …) | Installed libraries |
| **Execution** | `03_Execution_Layer/` | Reusable work processes (Analyze, Generate, Validate, Optimize, Develop, Teach) | Programs |
| **Platform** | `04_Platforms/` | Platform Adapters that deploy the platform-agnostic core to concrete AI platforms | Device drivers |
| **Templates** | `05_Templates/` | Reusable document structures | Scaffolding |
| **Memory** | `06_Memory/` | Cross-session persistence: Core/Recall/Archival tiers, `MEMORY.md` contract, consolidation cycle | Filesystem & cache |

The design rules are defined in [`01_Architecture/AI-OS_Design_Principles.md`](01_Architecture/AI-OS_Design_Principles.md) — including Single Source of Truth (DP-001), DRY (DP-003), Separation of Concerns (DP-002), and Platform Agnostic Design (DP-009).

---

## How to Deploy

AI-OS content is deployed through **Platform Adapters** — no vendor-specific behavior lives in the Core.

- **Claude** (Projects, Claude Code, MCP): see the [Claude Adapter](04_Platforms/Claude_Adapter.md) (`DOC-PLAT-002`) — assembly rule, concept mapping, constraints, and the governed [Prompt Generator Skill](04_Platforms/Claude/prompt-generator.skill.md).
- **GPT / Generic platforms**: planned — see the [Platform Layer README](04_Platforms/README.md).

Quick start (Claude): assemble `Core_Identity` + `Core_Execution_Engine` + the Capability and Execution modules your task needs, in that order, per the adapter's Assembly Rule — or use the single-file [`AI-OS_AI_Working_Kit.md`](AI-OS_AI_Working_Kit.md).

---

## Governance

Every official document is registered in the [Document Registry](01_Architecture/AI-OS_Document_Registry.md) (SSOT, 68 documents) with an immutable `DOC-<LAYER>-<NNN>` ID, semantic version, lifecycle status, and owner.

Two rules are non-negotiable:

1. **Log first** — every change is recorded in [`Change_Log_day.md`](Change_Log_day.md) *before or as* it is made.
2. **Registry before Active** — no document becomes authoritative until registered and metadata-compliant.

Compliance is checked automatically: [`Knowledge_Base/validate_aios.py`](Knowledge_Base/validate_aios.py) runs in CI on every push (see `.github/workflows/validate.yml`).

---

## Contributing & Security

- Contribution workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Security policy: [`SECURITY.md`](SECURITY.md)
- License: [MIT](LICENSE)

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.2.0              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-14         |
| Change Summary | Registered as DOC-CORE-005 and promoted to Active; registry count → 68 |

---

## Related Documents

- Core Identity (DOC-CORE-001)
- AI-OS Design Principles (DOC-ARCH-004)
- AI-OS Document Registry (DOC-ARCH-001)
- Platform Layer README (DOC-PLAT-001)
