# Teach SQL

Version: 1.0.0
Status: Draft
Layer: Execution
Document Type: Execution Module
Document ID: DOC-EXEC-018
Owner: AI-OS Architecture

---

# Module Metadata

| Field | Value |
|------|------|
| Module Name | Teach SQL |
| Module ID | DOC-EXEC-018 |
| Category | Education |
| Version | 1.0.0 |
| Status | Draft |
| Owner | AI-OS Architecture |

---

# Purpose

Provide a standardized execution process for teaching SQL concepts adapted to the learner's level, emphasizing understanding over rote answers. Serves as the reference example of an Education-category Execution Module.

---

# Scope

Applies to requests to explain, teach, or build understanding of SQL: concepts, query construction, optimization reasoning, and common pitfalls.

Out of scope: writing production queries as a deliverable (that is Generate) and reviewing a query for correctness (that is Validate).

---

# Inputs

- The topic or question, and the learner's current level (assumed if unstated).
- Optional: schema/data context, preferred depth, target dialect.

---

# Outputs

- A clear, level-appropriate explanation with worked examples.
- Checks for understanding (questions or small exercises).
- Common pitfalls and next-step suggestions.

---

# Preconditions

- The topic is identified, or a reasonable starting point is assumed and stated.

---

# Execution Process

1. Identify the concept and estimate the learner's level.
2. State the objective of the lesson in one sentence.
3. Explain the concept from first principles, then a concrete example.
4. Progress from simple to complex; connect to prior knowledge.
5. Provide a check for understanding (question or exercise).
6. Highlight common mistakes and how to avoid them.
7. Suggest the next concept to learn.

---

# Validation

- Explanation is accurate and dialect-correct (or dialect noted).
- Depth matches the learner's level.
- Examples are runnable and illustrate the concept.

---

# Quality Gates

- Objective clear; explanation step-by-step.
- No fabricated syntax or behavior.
- Understanding checked, not assumed.

---

# Error Handling

- Level unknown -> start intermediate, adjust from response.
- Dialect ambiguous -> state the assumed dialect and note key differences.
- Topic too broad -> scope to one concept and offer a learning path.

---

# Dependencies

- Core Identity, Core Execution Engine.
- Execution Registry.
- Active Capability Modules (Data Analytics / Education expertise).

---

# Related Modules

- Analyze (DOC-EXEC-013), Generate (DOC-EXEC-014).

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
