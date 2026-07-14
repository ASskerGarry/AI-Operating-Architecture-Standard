# Analyze

Version: 1.0.1
Status: Active
Layer: Execution
Document Type: Execution Module
Document ID: DOC-EXEC-013
Owner: AI-OS Architecture

---

# Module Metadata

| Field | Value |
|------|------|
| Module Name | Analyze |
| Module ID | DOC-EXEC-013 |
| Category | Analysis |
| Version | 1.0.1 |
| Status | Active |
| Owner | AI-OS Architecture |

---

# Purpose

Provide a standardized execution process for analyzing an input artifact — a prompt, document, dataset, system, or problem statement — and producing structured, evidence-based findings. This module governs *how* analysis is performed; the domain expertise applied is supplied by the active Capability Modules.

---

# Scope

Applies to any request whose primary objective is to understand, assess, diagnose, or decompose an existing artifact rather than create a new one. Supported scenarios: prompt review, document/architecture review, data profiling, root-cause investigation, gap analysis.

Out of scope: generating new deliverables (see Generate), verifying against acceptance criteria (see Validate), improving an existing artifact (see Optimize).

---

# Inputs

- The artifact to analyze (text, file, dataset, or reference).
- The analysis objective and the decision it must support.
- Optional: evaluation criteria, constraints, target audience, prior context.

---

# Outputs

- A structured findings report separating verified facts, assumptions, interpretations, and recommendations.
- Prioritized issues (by severity/impact) with supporting evidence.
- Explicit statement of uncertainty and information gaps.

---

# Preconditions

- The artifact is accessible and readable.
- The analysis objective is defined, or a reasonable objective can be assumed and stated explicitly.

---

# Execution Process

1. Restate the analysis objective and the decision it supports.
2. Inventory the artifact: structure, components, boundaries.
3. Select evaluation criteria (explicit if provided; otherwise derived from objective and stated).
4. Examine the artifact against each criterion; collect evidence for every observation.
5. Classify findings as verified fact, assumption, interpretation, or recommendation.
6. Prioritize findings by severity and impact on the objective.
7. Identify uncertainty, missing information, and their effect on conclusions.
8. Summarize conclusions before recommendations.

---

# Validation

- Every finding is traceable to specific evidence in the artifact.
- Facts, assumptions, and interpretations are clearly separated.
- Conclusions follow logically from the evidence; correlation is not presented as causation.

---

# Quality Gates

- Objective addressed and stated.
- No fabricated facts, references, or statistics.
- Findings prioritized and actionable.
- Uncertainty made explicit.

---

# Error Handling

- Artifact incomplete or unreadable -> state the limitation, analyze what is available, flag gaps.
- Objective ambiguous -> proceed on a stated assumption or ask at most one high-impact question.
- Insufficient evidence -> mark the finding as an assumption, not a fact.

---

# Dependencies

- Core Identity, Core Execution Engine.
- Execution Registry (routing), Execution Blueprint (structure).
- Active Capability Modules (domain expertise).

---

# Related Modules

- Validate (DOC-EXEC-015), Optimize (DOC-EXEC-016), Generate (DOC-EXEC-014).

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
- Execution Registry
- AI-OS Glossary

