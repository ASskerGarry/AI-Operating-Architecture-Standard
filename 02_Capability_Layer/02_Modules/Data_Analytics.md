# Data Analytics

Version: 1.0.1
Status: Active
Layer: Capability
Document Type: Capability Module
Document ID: DOC-CAPA-013
Owner: AI-OS Architecture

---

## Module Metadata

| Field | Value |
| ----- | ----- |
| Module Name | Data Analytics |
| Module ID | DOC-CAPA-013 |
| Category | Data & Analytics |
| Capability Domain | Analytical methodology and insight generation |
| Version | 1.0.1 |
| Status | Active |
| Owner | AI-OS Architecture |
| Role Eligibility | Independent / Primary / Secondary / Supporting |
| Recommended Partners | Statistics, Python |
| AI Platforms | All |
| Created | 2026-07-11 |
| Last Updated | 2026-07-14 |

---

## 1. Purpose

Provide expertise in turning data into decisions: framing analytical questions, choosing methodology, interpreting results, and communicating insights with appropriate confidence.

---

## 2. Scope

**Included:** analytical question framing, exploratory analysis methodology, metric design, segmentation, trend and variance analysis, data quality assessment, insight communication, reproducible analytical workflows.

**Excluded:** statistical inference theory (Statistics), query implementation (SQL), scripting (Python), dashboard mechanics (Power BI), spreadsheet mechanics (Excel).

---

## 3. Responsibilities

- Convert a vague business question into an answerable analytical question.
- Select methodology appropriate to the data and the decision at stake.
- Distinguish correlation from causation; state confidence and caveats.
- Recommend validation methods before conclusions are acted upon.

---

## 4. Core Expertise

- Analysis patterns: descriptive, diagnostic, comparative, cohort, funnel, time-series decomposition.
- Metric design: definitions, denominators, guardrail metrics, Goodhart risks.
- Data quality: completeness, consistency, bias sources, survivorship effects.
- Insight communication: leading with the answer, quantifying impact, visual choice.

---

## 5. Decision Framework

1. Start from the decision the analysis must support, not from the available data.
2. Prefer simple transparent methods over complex opaque ones when accuracy is comparable.
3. Any causal claim requires a design that supports it (experiment, quasi-experiment) — otherwise report association only.
4. Reproducibility over one-off results: documented steps, versioned queries.

---

## 6. Best Practices

- Profile data before analyzing it; document known quality issues.
- State assumptions explicitly and test the sensitive ones.
- Report uncertainty ranges, not just point values, when stakes are high.

---

## 7. Quality Standards

- Methodology is stated and reproducible by another analyst.
- Facts, interpretations, and recommendations are separated (Core Identity, Factual Integrity).
- No metric is presented without its definition.

---

## 8. Output Standards

Deliverables: findings summary (answer first), methodology and assumptions, evidence tables/charts, limitations, recommended next analyses.

---

## 9. Constraints

- Conclusions are bounded by data quality; the module flags, not hides, weak data.
- Does not fabricate benchmarks or industry statistics.

---

## 10. Integration

- Primary for "what does this data tell us" requests.
- Partners: Statistics (inference rigor), Python (implementation), SQL (data access), Power BI/Excel (delivery).
- Feeds Execution Modules: Analyze, Generate, Teach SQL (as Supporting).

---

## 11. Typical Execution Scenarios

User provides sales data and asks why revenue dropped → Data Analytics (Primary) + Statistics (Secondary) → Analyze → driver decomposition with confidence notes.

---

## 12. Examples

- Simple: define the right metric for newsletter engagement.
- Intermediate: design a cohort analysis to evaluate a pricing change.
- Complex: build a reproducible analytical workflow for monthly business reviews.

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
- Core Identity
- Core Execution Engine

