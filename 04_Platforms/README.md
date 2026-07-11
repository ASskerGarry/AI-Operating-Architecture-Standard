# Platform Layer

Version: 1.1.0
Status: Draft
Layer: Platform
Document Type: README
Document ID: DOC-PLAT-001
Owner: AI-OS Architecture

---

## Purpose

The Platform Layer connects the platform-agnostic AI-OS Core to concrete AI platforms through **Platform Adapters**.

Per DP-009 (Platform Agnostic Design), no vendor-specific behavior may exist in the Core, Capability, or Execution layers. An adapter translates AI-OS documents into the configuration format of a specific platform — without modifying their content.

---

## Adapter Concept

A Platform Adapter defines, for one target platform:

- **Assembly rules** — which AI-OS documents are combined into the platform's system prompt / instructions (typically: Core Identity + Core Execution Engine + selected Capability and Execution Modules).
- **Mapping** — how AI-OS concepts map to platform primitives (see table below).
- **Constraints** — platform limits (context size, formatting, tool availability) and how to degrade gracefully.
- **Deployment procedure** — how to install, update, and verify the configuration.

| AI-OS Concept | Claude | OpenAI GPT | Other platforms |
| ------------- | ------ | ---------- | --------------- |
| Core Identity + Execution Engine | Project instructions / CLAUDE.md | Custom GPT instructions | System prompt |
| Capability Module | Skill / Knowledge doc | Knowledge file | Context document |
| Execution Module | Slash command / Skill | Assistants API workflow | Prompt template |
| Platform integration | MCP | Actions / function calling | Native tooling |

---

## Planned Adapters

| Adapter | Target | Status |
| ------- | ------ | ------ |
| Claude Adapter | Claude Projects, Claude Code (Skills, CLAUDE.md), MCP | Planned |
| GPT Adapter | Custom GPTs, Assistants API | Planned |
| Generic Adapter | Gemini, local models, any system-prompt-capable platform | Planned |

Each adapter SHALL be an official document (`DOC-PLAT-NNN`) registered in the AI-OS Document Registry.

---

## Governance Rules

- Adapters SHALL NOT duplicate or restate Core/Capability/Execution content — they reference and assemble it (DP-001, DP-003).
- Platform limitations SHALL be documented in the adapter, not worked around by editing Core documents.
- An adapter SHALL be validated by deploying it and verifying behavior against the Core Execution Engine's quality criteria.

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.1.0              |
| Status         | Draft              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-11         |
| Created date   | 2026-07-10         |
| Change Summary | Expanded stub into full layer description with adapter concept and planned adapters |

---

## Related Documents

- Core Identity
- Core Execution Engine
- AI-OS Design Principles (DP-009)
- AI-OS Document Registry

