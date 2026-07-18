# GPT Adapter

Version: 1.0.0
Status: Draft
Layer: Platform
Document Type: Platform Adapter
Document ID: DOC-PLAT-006
Owner: AI-OS Architecture

---

## Purpose

This document is the **GPT Platform Adapter**. It defines how the platform-agnostic AI-OS Core, Capability, and Execution content is assembled, mapped, and constrained for OpenAI's platforms (ChatGPT Projects/Custom GPTs, the Responses/Assistants API), so AI-OS can be deployed on GPT models without altering any Core, Capability, or Execution document (DP-009).

Status is **Draft by design**: the mapping is complete, but promotion to Active requires a validated deployment on the live platform (DP-015 Evidence-Based Decision Making).

---

## Scope

**Included:** concept mapping to OpenAI primitives, the assembly rule for system input, JSON-schema tool calling for the AI-OS document tools, platform constraints, deployment procedure.

**Excluded:** content of Core/Capability/Execution documents (owned by their layers); other platforms (Claude — DOC-PLAT-002, Gemini — DOC-PLAT-007, Copilot — DOC-PLAT-008).

---

## Concept Mapping

| AI-OS Concept | OpenAI Primitive | Notes |
| ------------- | ---------------- | ----- |
| Core Identity + Core Execution Engine | `instructions` (Responses API) / GPT "Instructions" field | Assembled verbatim; stable across sessions |
| Capability Module | Retrieval file / knowledge upload, or fetched via tool call | Load on demand — do not paste all modules statically |
| Execution Module | Structured section of `instructions`, or a distinct Assistant per process | One Assistant per Execution Module keeps thread state clean |
| Tool access to AI-OS documents | Function calling with `Knowledge_Base/openai_tools.json` | Same three tools as the MCP server (`list_documents`, `get_document`, `search_documents`); backend can be the MCP server behind a thin HTTP shim or a direct filesystem implementation |
| Structured output contract | `response_format: json_schema` (strict mode) | Use for task/response packets per DOC-ARCH-009 |
| Long-term memory | Project files / memory feature, `MEMORY.md` upload | Core Memory tier per DOC-MEM-002 |

---

## Assembly Rule

Assemble the system input in this order (identity first, task last):

1. **Core Identity** (DOC-CORE-001)
2. **Core Execution Engine** (DOC-CORE-002)
3. **Active Capability Modules** — only those the task needs
4. **Active Execution Module**
5. **User prompt**

GPT models have no XML-parsing preference: use **Markdown headings** (`## IDENTITY`, `## EXECUTION ENGINE`, `## CAPABILITY: <name>`, `## PROCESS: <name>`, `## TASK`) as section delimiters instead of the XML tags used on Claude. The assembled artifacts are the source documents unchanged.

For minimal-context deployments use `AI-OS_AI_Working_Kit_lean.md` as a single instructions payload, or rely on tool calling and keep only Core Identity + Core Execution Engine static.

---

## Tool Calling

`Knowledge_Base/openai_tools.json` defines the three AI-OS document tools as OpenAI function schemas. Wire them to any backend that enforces the same rules as the MCP server (DOC-PLAT-005): read-only, path-sandboxed, official-scope `.md` only. This file is the platform-neutral tool contract — the same JSON schemas translate directly to Gemini function declarations.

---

## Platform Constraints

| Constraint | Value / Behavior on GPT |
| ---------- | ----------------------- |
| Context window | 128K–1M tokens depending on model; prefer lean kit + tool calls over full static context |
| Instruction adherence | Strong for system `instructions`; repeat critical gate rules at the end of long payloads (recency effect) |
| Tool calling | JSON-schema functions, strict mode available — use it for packet contracts |
| No MCP-native STDIO in Custom GPTs | Use Actions (OpenAPI) or server-side function execution instead |
| Behavioral drift | Model updates are provider-controlled — run the Behavioral Evaluation gate (DOC-EXEC-024) after each announced model change |

---

## Deployment Procedure

1. Create the Assistant/GPT with the assembled instructions (Assembly Rule above).
2. Attach `openai_tools.json` functions; implement the backend with the MCP-server rules.
3. Record answers to all 35 behavioral cases into a responses file; run the DOC-EXEC-024 gate.
4. Promotion to Active requires: gate PASS on the live platform + a change-log entry with the evidence.

---

# Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.0              |
| Status         | Draft              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-17         |
| Created date   | 2026-07-17         |
| Change Summary | Initial adapter: concept mapping, Markdown assembly rule, JSON-schema tool contract, gate-based promotion criteria |

---

# Related Documents

- Claude Adapter (DOC-PLAT-002)
- Gemini Adapter (DOC-PLAT-007)
- Copilot Adapter (DOC-PLAT-008)
- AI-OS MCP Server (DOC-PLAT-005)
- Behavioral Evaluation (DOC-EXEC-024)
- Platform Layer README (DOC-PLAT-001)
