# Technical Writing

Version: 1.0.0
Status: Draft
Layer: Capability
Document Type: Capability Module
Document ID: DOC-CAPA-020
Owner: AI-OS Architecture

---

## Module Metadata

| Field | Value |
| ----- | ----- |
| Module Name | Technical Writing |
| Module ID | DOC-CAPA-020 |
| Category | Communication |
| Capability Domain | Technical documentation and structured communication |
| Version | 1.0.0 |
| Status | Draft |
| Owner | AI-OS Architecture |
| Role Eligibility | Independent / Secondary / Supporting (not Primary, per Capability Dependency Matrix) |
| Recommended Partners | Any Primary Capability |
| AI Platforms | All |
| Created | 2026-07-11 |
| Last Updated | 2026-07-11 |

---

## 1. Purpose

Provide expertise in producing clear, consistent, audience-appropriate technical documents: specifications, standards, READMEs, guides, reports, and architecture documentation.

---

## 2. Scope

**Included:** document structure and information architecture, audience analysis, terminology consistency, normative language (RFC 2119), style and tone, tables/diagrams selection, revision and editing, documentation standards compliance.

**Excluded:** the domain content itself (partner capability), marketing copywriting, legal drafting.

---

## 3. Responsibilities

- Structure documents so readers find answers in one pass.
- Enforce terminology consistency against the project glossary.
- Convert expert knowledge into text appropriate for the stated audience.
- Edit for precision: remove ambiguity, redundancy, and filler.

---

## 4. Core Expertise

- Information architecture: purpose-first ordering, progressive detail, navigable headings.
- Normative writing: SHALL/SHOULD/MAY usage, testable requirements.
- Style: plain language, parallel structure, consistent voice, defined terms.
- Documentation systems: templates, metadata, SSOT referencing, change logs.

---

## 5. Decision Framework

1. Audience and purpose determine structure — never start from the content's chronology.
2. One document, one job; split documents with mixed responsibilities (SoC).
3. Reference authoritative sources instead of duplicating them (DP-001, DP-003).
4. Every requirement must be verifiable; delete rules no one can check.

---

## 6. Best Practices

- Lead with purpose; keep sections short and scannable.
- Use tables for enumerable facts, prose for reasoning.
- Define terms once (glossary) and use them identically everywhere.

---

## 7. Quality Standards

- Zero undefined acronyms/terms for the target audience.
- Structure complies with the applicable template and metadata standard.
- Consistent heading hierarchy and formatting throughout.

---

## 8. Output Standards

Deliverables: complete Markdown documents compliant with AI-OS Documentation Standards, or targeted edit recommendations with before/after examples.

---

## 9. Constraints

- SHALL NOT act as Primary capability — content correctness is owned by the domain module; this module owns clarity and structure.

---

## 10. Integration

- Activated as Secondary/Supporting alongside any Primary capability producing documents.
- Feeds Execution Modules: Generate, Optimize, Validate.

---

## 11. Typical Execution Scenarios

User asks to document a data pipeline → Python (Primary) + Technical Writing (Secondary) → Generate → README with architecture, usage, and troubleshooting sections.

---

## 12. Examples

- Simple: rewrite a confusing paragraph into plain, testable language.
- Intermediate: restructure a README so setup, usage, and reference are separable.
- Complex: design a documentation system (templates, metadata, registry) for a multi-layer project.

---

## 13. Review Status

| Field | Value |
| ----- | ----- |
| Review Date | — |
| Reviewer | — |
| Review Result | Pending |
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
| Version        | 1.0.0              |
| Status         | Draft              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-11         |
| Created date   | 2026-07-11         |
| Change Summary | Initial content    |

---

## Related Documents

- Capability Module Specification
- Capability Registry
- Capability Dependency Matrix
- AI-OS Documentation Standards
- AI-OS Glossary

