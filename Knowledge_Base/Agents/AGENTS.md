# AI-OS Agent Instructions

This repository is a documentation-focused architecture repository for the AI Operating System (AI-OS). AI coding agents should use this file as the primary guide for making changes, authoring new documents, and preserving repository conventions.

## Purpose

- Help AI agents understand the repository structure and contribution rules.
- Avoid duplication by linking to existing AI-OS standards and registries.
- Ensure every document change follows AI-OS governance requirements.

## Repository overview

- `00_Core/` — Core identity and execution engine foundation documents.
- `01_Architecture/` — Architecture standards, registries, glossary, and templates.
- `02_Capability_Layer/` — Capability governance and capability module artifacts.
- `03_Execution_Layer/` — Execution module templates, category READMEs, and execution workflow documentation.
- `04_Platforms/` — Platform-layer documentation.
- `05_Templates/` — Repository template-layer documentation.
- `Change_Log_day.md` — Required daily change log for every repository change.
- `01_Architecture/AI-OS_Document_Registry.md` — Authoritative registry of all official AI-OS documents.

## Agent guidance

- Treat this repository as a document governance project, not a software project.
- Author and edit Markdown documentation with clear sections and consistent structure.
- Prefer linking to existing official documents rather than copying content.
- Always preserve the repository's Single Source of Truth (SSOT) approach.
- When creating or modifying official documents, update the document registry and `Change_Log_day.md`.
- Do not create or modify files outside the repository’s documentation scope without explicit user direction.
- Use the `AI_Operation_system` custom agent for repository-wide AI-OS governance, documentation review, and repair tasks when a focused agent is needed.

## Document conventions

- Every official document must include metadata fields such as:
  - Version
  - Status
  - Owner
  - Document ID
  - Last Updated
  - Change Summary
- Use RFC 2119 terminology (`SHALL`, `MUST`, `SHOULD`, `MAY`) for normative requirements.
- Use Markdown with hierarchical headings, numbered sections, and bullet lists.
- Keep document content concise, precise, and implementation-neutral.

## Autonomous repair guidance

- When asked to review or correct AI-OS, proactively scan the repository for governance issues, metadata defects, and documentation inconsistencies.
- Prioritize:
  - `Change_Log_day.md` log-first policy
  - Document metadata compliance (`01_Architecture/AI-OS_Document_Metadata_Standard.md`)
  - Registry accuracy (`01_Architecture/AI-OS_Document_Registry.md`)
  - Internal Markdown link integrity and filename consistency
  - Duplicate or outdated content vs the repository’s Single Source of Truth
- Use the `fixedthis` custom agent pattern for targeted repairs, but retain the broader repository context when the user asks the agent to self-run and fix AI-OS.
- Do not change non-documentation files unless explicitly requested.

## Change governance

- Before making any repository changes, add a planned entry to `Change_Log_day.md`.
- When a change is complete, update the corresponding status entry to `done`.
- If adding an official document, assign a unique `Document ID` and add it to `01_Architecture/AI-OS_Document_Registry.md`.

## Key references

- `01_Architecture/AI-OS_Documentation_Standards.md`
- `01_Architecture/AI-OS_Document_Metadata_Standard.md`
- `01_Architecture/AI-OS_Document_Registry.md`
- `01_Architecture/AI-OS_Design_Principles.md`
- `01_Architecture/AI-OS_Principles_Registry.md`

## Best practices

- Use the repository’s own conventions over general assumptions.
- Preserve existing metadata and document IDs for established files.
- Avoid introducing duplicate terminology or conflicting definitions.
- Keep the document hierarchy and registry consistent with the current repository layout.

---
