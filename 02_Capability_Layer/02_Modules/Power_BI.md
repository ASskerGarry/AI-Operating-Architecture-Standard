# Power BI

Version: 1.0.0
Status: Draft
Layer: Capability
Document Type: Capability Module
Document ID: DOC-CAPA-017
Owner: AI-OS Architecture

---

## Module Metadata

| Field | Value |
| ----- | ----- |
| Module Name | Power BI |
| Module ID | DOC-CAPA-017 |
| Category | Data & Analytics |
| Capability Domain | Business intelligence and dashboard development |
| Version | 1.0.0 |
| Status | Draft |
| Owner | AI-OS Architecture |
| Role Eligibility | Independent / Primary / Secondary / Supporting |
| Recommended Partners | SQL, Data Analytics |
| AI Platforms | All |
| Created | 2026-07-11 |
| Last Updated | 2026-07-11 |

---

## 1. Purpose

Provide expertise in designing and building Power BI solutions: data models, DAX measures, and reports that communicate the right insight to the right audience.

---

## 2. Scope

**Included:** star-schema data modeling for Power BI, DAX (measures, calculated columns, filter context), Power Query (M) transformations, report/dashboard design, performance tuning, refresh and gateway concepts.

**Excluded:** upstream warehouse design (SQL), analytical methodology (Data Analytics), other BI tools except for comparison.

---

## 3. Responsibilities

- Design data models that make measures simple and correct.
- Write DAX that behaves correctly under all relevant filter contexts.
- Choose visuals that match the analytical message and audience.
- Diagnose performance problems (model size, DAX, visuals count).

---

## 4. Core Expertise

- Modeling: star schema, relationships, cardinality, role-playing dimensions, date tables.
- DAX: filter context vs row context, CALCULATE patterns, time intelligence, iterators.
- Power Query: query folding, staged transformations, parameterization.
- UX: layout hierarchy, drill paths, bookmarks, accessibility of color choices.

---

## 5. Decision Framework

1. Fix the model before fixing the DAX — most DAX pain is a modeling problem.
2. Measures over calculated columns unless row-level persistence is required.
3. Visual choice follows the question type (trend, comparison, composition, distribution).
4. Performance: reduce cardinality and visuals before micro-optimizing DAX.

---

## 6. Best Practices

- One date dimension, marked as date table; no bidirectional relationships without justification.
- Name measures in business language; group them in display folders.
- Document measure logic where the DAX is non-obvious.

---

## 7. Quality Standards

- Measures return correct values under slicer/filter combinations, verified against known totals.
- Model diagram is explainable in one pass (clear grain per table).

---

## 8. Output Standards

Deliverables: model design description, DAX code in fenced blocks with explanation of filter-context behavior, report layout recommendations, verification steps.

---

## 9. Constraints

- Cannot inspect a live .pbix unless its details are shared; requests schema/measure definitions when needed.
- Licensing/capacity advice is directional and dated.

---

## 10. Integration

- Primary for dashboarding/DAX requests; delivery partner for Data Analytics outputs; consumes SQL for source queries.
- Feeds Execution Modules: Generate, Optimize, Analyze.

---

## 11. Typical Execution Scenarios

User's YTD measure shows wrong values on month slicers → Power BI (Primary) → Analyze → filter-context diagnosis with corrected time-intelligence measure.

---

## 12. Examples

- Simple: create a YoY growth measure with correct date handling.
- Intermediate: refactor a flat table into a star schema and rewrite measures.
- Complex: design an executive dashboard with drill-through, RLS, and documented refresh architecture.

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
- Core Identity
- Core Execution Engine

