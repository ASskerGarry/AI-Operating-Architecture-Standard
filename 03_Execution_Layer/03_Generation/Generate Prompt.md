# Generate

Version: 1.0.0
Status: Draft
Layer: Execution
Document Type: Execution Module
Document ID: DOC-EXEC-014
Owner: AI-OS Architecture

---

# Module Metadata

| Field | Value |
|------|------|
| Module Name | Generate |
| Module ID | DOC-EXEC-014 |
| Category | Creation |
| Version | 1.0.0 |
| Status | Draft |
| Owner | AI-OS Architecture |

---

# Purpose

Provide a standardized execution process for creating a new deliverable — a prompt, document, code artifact, plan, or design — that satisfies a defined objective and its acceptance criteria. Domain content is supplied by the active Capability Modules.

---

# Scope

Applies to any request whose primary objective is to produce a new artifact from requirements: prompt authoring, document drafting, code/module scaffolding, structured plans.

Out of scope: assessing an existing artifact (see Analyze), improving one (see Optimize).

---

# Inputs

- The generation objective and expected deliverable type.
- Requirements, constraints, target audience, output format.
- Optional: templates, style guides, reference material, success criteria.

---

# Outputs

- The requested artifact, complete and format-compliant.
- A brief note on key design decisions and any stated assumptions.

---

# Preconditions

- The objective and deliverable type are defined, or can be reasonably assumed and stated.
- Any mandatory template or format standard is identified.

---

# Execution Process

1. Confirm objective, deliverable type, audience, and output format.
2. Gather requirements and constraints; state assumptions where information is missing.
3. Select the governing template or structure (if one applies).
4. Produce an outline / structure before full content.
5. Draft the artifact section by section, applying the relevant Capability expertise.
6. Apply SSOT/DRY: reference authoritative sources instead of duplicating them.
7. Self-review against requirements and format; refine.

---

# Validation

- Every requirement is addressed; none silently dropped.
- Output matches the requested format and any mandatory template.
- No fabricated facts, references, or sources.

---

# Quality Gates

- Objective satisfied and deliverable complete.
- Structure clear; content free of filler and redundancy.
- Assumptions stated; decisions explained where non-obvious.

---

# Error Handling

- Requirements ambiguous -> proceed on stated assumptions or ask at most one high-impact question.
- Conflicting constraints -> surface the conflict and propose the best trade-off.
- Missing template -> use the closest standard structure and note the deviation.

---

# Dependencies

- Core Identity, Core Execution Engine.
- Execution Registry (routing), Execution Blueprint (structure).
- Applicable templates and documentation standards; active Capability Modules.

---

# Related Modules

- Analyze (DOC-EXEC-013), Validate (DOC-EXEC-015), Optimize (DOC-EXEC-016).

---

# Change History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-07-10 | Initial version — module populated from template |

---

# Version Information

| Field | Value |
|------|------|
| Version | 1.0.0 |
| Status | Draft |
| Owner | AI-OS Architecture |
| Last Updated | 2026-07-10 |
| Created date | 2026-07-10 |
| Change Summary | Initial content |

---

# Related Documents

- Core Identity
- Core Execution Engine
- Execution Module Specification
- Execution Registry
- AI-OS Glossary
