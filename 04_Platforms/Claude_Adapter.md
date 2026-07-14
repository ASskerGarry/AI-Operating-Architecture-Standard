# Claude Adapter

Version: 1.0.2
Status: Active
Layer: Platform
Document Type: Platform Adapter
Document ID: DOC-PLAT-002
Owner: AI-OS Architecture

---

## Purpose

This document is the **Claude Platform Adapter**. It defines how the platform-agnostic AI-OS Core, Capability, and Execution content is assembled, mapped, and constrained for Anthropic's Claude platform (Claude Projects, Claude Code, and MCP), so that AI-OS can be **deployed and run** on Claude without altering any Core, Capability, or Execution document.

It is the Single Source of Truth (SSOT) for Claude-specific deployment of AI-OS. Per DP-009, no Claude-specific behavior belongs in the Core; it lives here. Per DP-001/DP-003, this adapter **references and assembles** source documents — it does not restate their content.

---

## Scope

**Included:** the mapping of AI-OS concepts to Claude primitives, the assembly rule for the Claude system prompt, Claude platform constraints and graceful degradation, the deployment/verification procedure, and the list of Claude assets this adapter governs.

**Excluded:** the content of Core/Capability/Execution documents (owned by their own layers); other platforms (see the GPT Adapter and Generic Adapter, planned in DOC-PLAT-001); model training or fine-tuning.

---

## Concept Mapping

How AI-OS concepts are realized on Claude:

| AI-OS Concept | Claude Primitive | Notes |
| ------------- | ---------------- | ----- |
| Core Identity (DOC-CORE-001) + Core Execution Engine (DOC-CORE-002) | Project instructions / `CLAUDE.md` | Assembled verbatim into the system layer; stable across sessions |
| Capability Module (e.g. Prompt Engineering, DOC-CAPA-011) | Skill or Knowledge document | Loaded on demand; activated by the Capability Registry |
| Execution Module (Analyze / Generate / Validate / Optimize, DOC-EXEC-013…016) | Skill or slash command | Concrete Claude instantiation of the abstract execution process |
| Platform integration / external tools | MCP servers, tools | Enables ReAct-style tool loops (see the Generate Skill) |
| Long-term memory | `CLAUDE.md` / `MEMORY.md` | Core Memory tier per the Memory Architecture standard (DOC-MEM-002); Claude loads it via `CLAUDE.md` / Project instructions |

---

## Assembly Rule

The Claude system configuration SHALL be assembled in this order (identity first, task last — Claude follows the system block strictly and honors XML structure):

1. **Core Identity** (DOC-CORE-001) — who the AI is.
2. **Core Execution Engine** (DOC-CORE-002) — how it works.
3. **Active Capability Modules** — selected by the Capability Registry for the request (e.g. Prompt Engineering for prompt tasks).
4. **Active Execution Module** — the workflow for the request (e.g. Generate).
5. **User prompt** — the immediate instruction.

Wrap each assembled section in XML tags (`<identity>`, `<execution_engine>`, `<capability>`, `<execution>`, `<task>`) — Claude parses XML structure reliably and this preserves the instruction hierarchy. The assembled artifacts are the source documents unchanged; the adapter only combines and tags them.

---

## Platform Constraints

| Constraint | Value / Behavior on Claude |
| ---------- | -------------------------- |
| Context window | ~200K tokens. Batch large data sets (see the Generate Skill's Batch Processing section). |
| System prompt | Separate, strictly honored system block. Place non-negotiable rules there. |
| Structure | Prefer XML tags over heavy Markdown for instruction hierarchy. |
| Tools | Available via MCP / tool use — enables ReAct loops with error handling. |
| Framing | Positive framing is required for format stability (state what to do, not what to avoid). |

**Graceful degradation:** if a required MCP connector/tool is unavailable in a given deployment, the affected Execution artifact SHALL detect and report it rather than fabricate results (agent-level rule enforced in the Generate Skill).

---

## Governed Assets

This adapter governs the following Claude-specific assets:

| Asset | Location | Instantiates | Status |
| ----- | -------- | ------------ | ------ |
| Prompt Generator Skill | `04_Platforms/Claude/prompt-generator.skill.md` | Generate (DOC-EXEC-014) for the Prompt Engineering capability (DOC-CAPA-011) | Draft |

The Prompt Generator Skill is the production-ready Claude instantiation of the Generate execution process for prompt authoring. It supersedes the two external `promptgeneratormax` drafts (v3 and v4); **v4 is carried forward as the reference, v3 is deprecated.** When the Reasoning Patterns library is introduced (project analysis, Idea 3), the Skill's inline technique descriptions (Context Stack, ReAct, Batch Processing) SHALL be replaced by references to that library (DP-001).

---

## Deployment Procedure

1. Assemble the system configuration per the Assembly Rule for the target Claude surface (Project instructions, `CLAUDE.md`, or Skill).
2. Install governed Skills into the Claude environment (e.g. the Claude Code skills directory or a Claude Project).
3. Configure required MCP connectors for any Execution artifact that uses tools.
4. Verify behavior against the Core Execution Engine's Quality Validation criteria (DOC-CORE-002) — the deployment is valid only if those criteria hold.
5. Record the deployment and any version change in `Change_Log_day.md` (log-first policy) and update the Registry if a new asset becomes an official document.

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.2              |
| Status         | Active              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-13         |
| Change Summary | Promoted to Active after Quality Gate review |

---

## Related Documents

- Platform Layer README (DOC-PLAT-001)
- Core Identity (DOC-CORE-001)
- Core Execution Engine (DOC-CORE-002)
- Prompt Engineering (DOC-CAPA-011)
- Generate (DOC-EXEC-014)
- Memory Architecture (DOC-MEM-002)
- AI-OS Design Principles — DP-009 (DOC-ARCH-004)
- AI-OS Document Registry (DOC-ARCH-001)
