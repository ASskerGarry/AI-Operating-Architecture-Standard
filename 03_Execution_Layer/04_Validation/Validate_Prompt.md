# Validate

Version: 1.0.1
Status: Active
Layer: Execution
Document Type: Execution Module
Document ID: DOC-EXEC-015
Owner: AI-OS Architecture

---

# Module Metadata

| Field | Value |
|------|------|
| Module Name | Validate |
| Module ID | DOC-EXEC-015 |
| Category | Validation |
| Version | 1.0.1 |
| Status | Active |
| Owner | AI-OS Architecture |

---

# Purpose

Provide a standardized execution process for verifying that an artifact meets its acceptance criteria, quality standards, and applicable architectural principles before it is accepted or published.

---

# Scope

Applies to any request whose objective is to check correctness, completeness, consistency, or compliance of an existing artifact: prompt QA, document/architecture review against standards, data-quality checks, pre-publish gating.

Out of scope: open-ended assessment (see Analyze), improvement (see Optimize).

---

# Inputs

- The artifact under validation.
- Acceptance criteria and/or the governing standard.
- Optional: prior review notes, test data.

---

# Outputs

- A pass/fail verdict per criterion with evidence.
- A defect list prioritized by severity.
- A clear statement of what must change before acceptance.

---

# Preconditions

- Acceptance criteria or a governing standard exist, or a reasonable set is defined and stated.
- The artifact is complete enough to evaluate.

---

# Execution Process

1. Confirm the acceptance criteria / standard to validate against.
2. Derive a checklist from those criteria.
3. Evaluate the artifact against each checklist item; record evidence.
4. Assign a verdict (pass/fail/partial) per item.
5. Classify each failure by severity and impact.
6. Where possible, verify programmatically or with a second pass for high-stakes items.
7. State the minimum set of changes required for acceptance.

---

# Validation

- Every verdict is backed by concrete evidence.
- No criterion is skipped without justification.
- Severity classification is consistent and defensible.

---

# Quality Gates

- All criteria evaluated.
- Defects prioritized and actionable.
- Verdict unambiguous.

---

# Error Handling

- No criteria provided -> define and state a reasonable set before validating.
- Artifact incomplete -> validate available parts, flag the rest as blocked.
- Conflicting standards -> surface the conflict; validate against the authoritative source (SSOT).

---

# Dependencies

- Core Identity, Core Execution Engine.
- Execution Registry, Execution Review Standard.
- Applicable standards/specifications; active Capability Modules.

---

# Related Modules

- Analyze (DOC-EXEC-013), Optimize (DOC-EXEC-016), Generate (DOC-EXEC-014).

---

# Change History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-07-10 | Initial version — module populated from template |

---

# Version Information

| Field | Value |
|------|------|
| Version | 1.0.1 |
| Status | Active |
| Owner | AI-OS Architecture |
| Last Updated | 2026-07-14 |
| Created date | 2026-07-10 |
| Change Summary | Promoted to Active after Quality Gate review |

---

# Related Documents

- Core Identity
- Core Execution Engine
- Execution Module Specification
- Execution Review Standard
- AI-OS Glossary

