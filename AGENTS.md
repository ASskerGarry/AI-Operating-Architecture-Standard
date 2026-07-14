# AI-OS Agent Instructions

Document ID: DOC-CORE-008
Version: 1.1.0
Status: Active
Layer: Core
Document Type: Guide
Owner: AI-OS Architecture

This repository uses `Knowledge_Base/Agents/AGENTS.md` as the canonical agent guidance source.

## Primary behavior

- Treat AI-OS as a documentation governance repository, not a codebase.
- Focus on document quality, metadata compliance, registry accuracy, and the repository's Single Source of Truth.
- When asked to inspect or repair AI-OS, proactively find and fix:
  - `Change_Log_day.md` compliance and planned log entries
  - document metadata issues and missing `Document ID`
  - broken internal Markdown links and inconsistent filenames
  - registry mismatches in `01_Architecture/AI-OS_Document_Registry.md`
  - duplicate or outdated content versus the official SSOT
- Do not modify non-documentation files unless explicitly instructed.

## Canonical reference

See `Knowledge_Base/Agents/AGENTS.md` for the full repository-specific instructions and autonomous repair guidance.

## Available custom agents

- `AI_Operation_system` — repository-focused agent for AI-OS governance, documentation review, and autonomous repair tasks.
