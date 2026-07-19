# AI-OS — AI Operating Architecture Standard

Document ID: DOC-CORE-005
Version: 1.3.5
Status: Active
Layer: Core
Document Type: README
Owner: AI-OS Architecture

[![AI-OS Governance Validation](https://github.com/ASskerGarry/AI-Operating-Architecture-Standard/actions/workflows/validate.yml/badge.svg)](https://github.com/ASskerGarry/AI-Operating-Architecture-Standard/actions/workflows/validate.yml)

**Make your AI behave the same way tomorrow as it did today.**

Teams adopting LLMs hit the same three walls: the AI behaves *unpredictably* (the same prompt drifts between sessions and model updates), changes are *untraceable* (nobody knows which instruction edit broke production), and context is *expensive* (monolithic prompts burn tokens on content the task never uses).

**AI-OS** answers all three with one move: it treats AI instructions as a governed software system — not a pile of prompts.

## Why AI-OS

- **Predictability through Quality Gates.** Every artifact passes explicit validation criteria before it ships (`Validate`, DOC-EXEC-015; DP-014 Quality by Design), and a zero-defect CI gate ([`validate.yml`](.github/workflows/validate.yml)) blocks any change that breaks the standard. The AI operates inside hard rails, not vibes.
- **Traceability through governed change control.** Immutable document IDs, semantic versions, lifecycle states, and a mandatory log-first change log mean every behavior change has an author, a reason, and a diff — so regressions are found in minutes, not sprints.
- **Token efficiency through modular context.** The AI loads only the capability and process modules a task needs; a generated, metadata-free [Lean Working Kit](AI-OS_AI_Working_Kit_lean.md) keeps the model's context window on business rules instead of bureaucracy.

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
- **Any MCP client** (Claude Desktop, Claude Code, other MCP hosts): the read-only [AI-OS MCP Server](04_Platforms/AIOS_MCP_Server.md) (`DOC-PLAT-005`) serves the registry and modules as on-demand tools — no static context needed.
- **GPT** ([adapter](04_Platforms/GPT_Adapter.md), `DOC-PLAT-006`), **Gemini** ([adapter](04_Platforms/Gemini_Adapter.md), `DOC-PLAT-007`), **GitHub Copilot** ([adapter](04_Platforms/Copilot_Adapter.md), `DOC-PLAT-008`): Draft adapters — complete mappings pending live-platform validation. Overview: [Platform Layer README](04_Platforms/README.md).

Quick start (Claude): assemble `Core_Identity` + `Core_Execution_Engine` + the Capability and Execution modules your task needs, in that order, per the adapter's Assembly Rule — or use a single generated file: [`AI-OS_AI_Working_Kit.md`](AI-OS_AI_Working_Kit.md) (full, with provenance for audit) or [`AI-OS_AI_Working_Kit_lean.md`](AI-OS_AI_Working_Kit_lean.md) (token-efficient, for the model's context window). Both are rebuilt deterministically by `python3 Knowledge_Base/generate_working_kit.py`.

---

## Governance

Every official document is registered in the [Document Registry](01_Architecture/AI-OS_Document_Registry.md) (SSOT, 81 documents) with an immutable `DOC-<LAYER>-<NNN>` ID, semantic version, lifecycle status, and owner.

Two rules are non-negotiable:

1. **Log first** — every change is recorded in [`Change_Log_day.md`](Change_Log_day.md) *before or as* it is made.
2. **Registry before Active** — no document becomes authoritative until registered and metadata-compliant.

Compliance is checked automatically at two layers: **structural** — [`Knowledge_Base/validate_aios.py`](Knowledge_Base/validate_aios.py) verifies metadata and registry consistency on every push (`validate.yml`); **behavioral** — a 35-case evaluation gate (incl. adversarial injection resistance) ([Behavioral Evaluation](03_Execution_Layer/04_Validation/Behavioral_Evaluation.md), `DOC-EXEC-024`) blocks changes that degrade task success, policy compliance, refusal correctness, format adherence, or hallucination avoidance beyond declared limits (`behavior_eval.yml`).

---

## Contributing & Security

- Contribution workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Security policy: [`SECURITY.md`](SECURITY.md)
- License: [MIT](LICENSE)

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.3.5              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-14         |
| Change Summary | 81 documents; Orchestration Standard now Active (validated by the MAS pilot) |

---

## Related Documents

- Core Identity (DOC-CORE-001)
- AI-OS Design Principles (DOC-ARCH-004)
- AI-OS Document Registry (DOC-ARCH-001)
- Platform Layer README (DOC-PLAT-001)
