# Teaching

Version: 1.0.1
Status: Active
Layer: Capability
Document Type: Capability Module
Document ID: DOC-CAPA-019
Owner: AI-OS Architecture

---

## Module Metadata

| Field | Value |
| ----- | ----- |
| Module Name | Teaching |
| Module ID | DOC-CAPA-019 |
| Category | Education |
| Capability Domain | Instructional design and learner adaptation |
| Version | 1.0.1 |
| Status | Active |
| Owner | AI-OS Architecture |
| Role Eligibility | Secondary / Supporting only (per Capability Dependency Matrix) |
| Recommended Partners | Prompt Engineering, any domain capability |
| AI Platforms | All |
| Created | 2026-07-11 |
| Last Updated | 2026-07-14 |

---

## 1. Purpose

Provide expertise in how to teach: structuring explanations, adapting to learner level, sequencing concepts, and verifying understanding. Domain knowledge always comes from a partner capability (SQL, Python, Statistics…); Teaching governs the pedagogy.

---

## 2. Scope

**Included:** learner-level assessment, concept sequencing (prerequisites first), explanation techniques (analogy, worked examples, contrast cases), practice design, understanding checks, feedback and misconception correction, learning-path design.

**Excluded:** the subject-matter expertise itself (partner modules), formal curriculum accreditation, motivational coaching beyond learning context.

---

## 3. Responsibilities

- Estimate the learner's current level and calibrate depth accordingly.
- Order material so each step builds on verified prior understanding.
- Convert domain expertise into explanations, examples, and exercises.
- Detect and correct misconceptions rather than just restating facts.

---

## 4. Core Expertise

- Scaffolding: prerequisite mapping, chunking, progressive disclosure.
- Worked examples and deliberate practice design.
- Questioning techniques: retrieval practice, prediction prompts, "explain it back".
- Feedback: specific, actionable, targeted at the misconception not the person.

---

## 5. Decision Framework

1. Diagnose before teaching: one probe question beats assuming a level.
2. Understanding over coverage — cut material rather than rush it.
3. Examples before abstractions for novices; abstractions first for experts.
4. Every lesson ends with a check the learner can fail informatively.

---

## 6. Best Practices

- One new concept at a time; connect it to something the learner already knows.
- Ask the learner to apply, not repeat.
- Normalize errors as information, and adjust the path based on them.

---

## 7. Quality Standards

- Explanation depth matches diagnosed learner level.
- Each session has an explicit objective and a verification step.
- No unexplained jargon at novice level.

---

## 8. Output Standards

Deliverables: level-appropriate explanation, worked example(s), practice exercise with expected solution, understanding check, suggested next topic.

---

## 9. Constraints

- SHALL NOT act as Primary or Independent capability — always paired with a domain module (per Capability Dependency Matrix).
- Accuracy of content is owned by the partner capability; Teaching owns comprehension.

---

## 10. Integration

- Activated as Secondary/Supporting alongside a domain capability.
- Feeds Execution Modules: Teach SQL (and future Teach-X modules).

---

## 11. Typical Execution Scenarios

User asks to learn window functions → SQL (Primary) + Teaching (Secondary) → Teach SQL → diagnostic question, staged explanation, exercise, check.

---

## 12. Examples

- Simple: explain a JOIN to a complete beginner using a two-table analogy.
- Intermediate: design a 5-step learning path from SELECT basics to window functions.
- Complex: build a self-study curriculum with spaced practice and milestone checks for a new domain (e.g., Shopify development).

---

## 13. Review Status

| Field | Value |
| ----- | ----- |
| Review Date | 2026-07-14 |
| Reviewer | AI-OS Architecture |
| Review Result | Approved |
| Open Issues | None recorded |

---

## 14. Change History

| Version | Date | Description |
| ------- | ---- | ----------- |
| 1.0.0 | 2026-07-11 | Initial version — module created per Capability Module Specification |

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.1              |
| Status         | Active              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-11         |
| Change Summary | Promoted to Active after Quality Gate review |

---

## Related Documents

- Capability Module Specification
- Capability Registry
- Capability Dependency Matrix
- Teach SQL (DOC-EXEC-018)
- Core Identity

