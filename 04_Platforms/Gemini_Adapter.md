# Gemini Adapter

Version: 1.0.0
Status: Draft
Layer: Platform
Document Type: Platform Adapter
Document ID: DOC-PLAT-007
Owner: AI-OS Architecture

---

## Purpose

This document is the **Gemini Platform Adapter**. It defines how the platform-agnostic AI-OS content is assembled, mapped, and constrained for Google's Gemini platforms (Google AI Studio, Vertex AI, Gems), so AI-OS can be deployed on Gemini without altering any Core, Capability, or Execution document (DP-009).

Status is **Draft by design**: promotion to Active requires a validated live-platform deployment (DP-015).

---

## Scope

**Included:** concept mapping to Gemini primitives, the assembly rule for system instructions, the large-context strategy, function declarations, platform constraints, deployment procedure.

**Excluded:** content of Core/Capability/Execution documents; other platforms (Claude — DOC-PLAT-002, GPT — DOC-PLAT-006, Copilot — DOC-PLAT-008).

---

## Concept Mapping

| AI-OS Concept | Gemini Primitive | Notes |
| ------------- | ---------------- | ----- |
| Core Identity + Core Execution Engine | `system_instruction` (AI Studio / Vertex AI) or Gem instructions | Assembled verbatim; stable across the session |
| Capability Module | Inline context section or file via the Files API | Large context (up to 2M tokens on 1.5/2.x Pro) permits full-kit deployments — but lean-first remains the default (cost) |
| Execution Module | Structured section of system instruction | One process active per request |
| Tool access to AI-OS documents | Function declarations (`tools: function_declarations`) | Translate `Knowledge_Base/openai_tools.json` schemas 1:1 — parameter schemas are compatible JSON Schema subsets |
| Structured output contract | `response_mime_type: application/json` + `response_schema` | Use for task/response packets (DOC-ARCH-009) |
| Long-term memory | Context caching + `MEMORY.md` in system instruction | Context caching prices repeated large payloads down — cache Core + kit, vary only the task |

---

## Assembly Rule

Assemble `system_instruction` in this order (identity first, task last):

1. **Core Identity** (DOC-CORE-001)
2. **Core Execution Engine** (DOC-CORE-002)
3. **Active Capability Modules**
4. **Active Execution Module**
5. **User prompt** (as the user turn, not inside system instruction)

Use Markdown headings as delimiters (same convention as the GPT Adapter). Gemini honors system instructions well but weights recent tokens strongly on very long contexts — restate the active Execution Module's Quality Gates at the end of the system instruction when the assembled payload exceeds ~100K tokens (RP-007 inverted positioning).

**Large-context strategy:** the 2M-token window makes a full-corpus deployment (all 80 documents) technically possible; do it only for research/audit sessions. Production deployments use the lean kit plus function calls — attention dilution and cost grow with context regardless of the window limit.

---

## Platform Constraints

| Constraint | Value / Behavior on Gemini |
| ---------- | -------------------------- |
| Context window | Up to 2M tokens (Pro tiers); flash tiers smaller — verify per model |
| Context caching | Available — cache the assembled Core + kit; pay per-token once |
| Function calling | Function declarations; parallel calls supported |
| Safety filters | Platform-level filters may pre-empt AI-OS refusal behavior — test the refusal and injection case groups explicitly |
| Behavioral drift | Run the DOC-EXEC-024 gate after each model version change |

---

## Deployment Procedure

1. Create the system instruction per the Assembly Rule (AI Studio for prototyping, Vertex AI for production).
2. Register function declarations translated from `openai_tools.json`; back them with an implementation enforcing the MCP-server rules (read-only, sandboxed).
3. Record answers to all 35 behavioral cases; run the DOC-EXEC-024 gate — pay special attention to `injection_resistance_rate` and refusal cases (platform safety filters interact here).
4. Promotion to Active requires gate PASS on the live platform + a logged evidence entry.

---

# Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.0              |
| Status         | Draft              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-17         |
| Created date   | 2026-07-17         |
| Change Summary | Initial adapter: concept mapping, assembly rule, 2M-context strategy, context caching, function declarations |

---

# Related Documents

- Claude Adapter (DOC-PLAT-002)
- GPT Adapter (DOC-PLAT-006)
- Copilot Adapter (DOC-PLAT-008)
- AI-OS MCP Server (DOC-PLAT-005)
- Behavioral Evaluation (DOC-EXEC-024)
- Platform Layer README (DOC-PLAT-001)
