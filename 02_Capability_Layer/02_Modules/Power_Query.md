# Power Query

Version: 1.0.1
Status: Active
Layer: Capability
Document Type: Capability Module
Document ID: DOC-CAPA-022
Owner: AI-OS Architecture

---

## Module Metadata

| Field | Value |
| ----- | ----- |
| Module Name | Power Query |
| Module ID | DOC-CAPA-022 |
| Category | Data & Analytics |
| Capability Domain | Data extraction, transformation, and refreshable ETL (M language) |
| Version | 1.0.1 |
| Status | Active |
| Owner | AI-OS Architecture |
| Role Eligibility | Independent / Primary / Secondary / Supporting |
| Recommended Partners | Excel, Power BI |
| AI Platforms | All |
| Created | 2026-07-19 |
| Last Updated | 2026-07-19 |

---

## 1. Purpose

Provide expertise in building refreshable, maintainable data extraction and transformation pipelines with Power Query and the M language, as used in Excel, Power BI, and Dataflows.

---

## 2. Scope

**Included:** M language development, staged query architecture, query folding preservation, data source connectivity (files, folders, databases, web/APIs), credentials and privacy levels, parameterization, query-side incremental refresh design (policy configuration: Power BI), transformation patterns.

**Excluded:** spreadsheet analysis and formulas (Excel), enterprise BI dashboards and DAX (Power BI), database querying (SQL).

---

## 3. Responsibilities

- Design refreshable ETL pipelines that survive source schema and volume changes.
- Write M code that preserves query folding wherever the source supports it.
- Connect and combine heterogeneous data sources with correct credential and privacy-level settings.
- Diagnose slow or failing refreshes and restructure the query chain to repair them.

---

## 4. Core Expertise

- M language: let expressions, custom functions, try/otherwise error handling, the M type system.
- Query folding: folding-aware step ordering, folding indicators and verification, native query trade-offs.
- Data source connectivity: connector selection, authentication modes, privacy levels and formula firewall behavior.
- Transformation patterns: staging and reference queries, unpivot/reshape, merge vs. append, parameters and query templates.

---

## 5. Decision Framework

1. Fold first: keep transformation steps foldable to the source for as long as possible.
2. Stage queries — separate connection, cleaning, and shaping layers instead of one monolithic step list.
3. Parameterize environment-specific values (paths, servers, date ranges) instead of hardcoding them.
4. Escalate when logic belongs elsewhere: heavy relational logic to the source database (SQL), reporting measures to DAX (Power BI).

---

## 6. Best Practices

- Name every applied step descriptively and remove dead steps before delivery.
- Declare column types explicitly, late enough in the chain not to break folding.
- Give each query one responsibility; reuse logic via reference queries, never copy-paste.

---

## 7. Quality Standards

- Refresh completes without manual intervention when new data arrives at the source.
- Folding status of every source-touching query is known and documented.
- Query dependencies form an acyclic staged chain that a reviewer can trace end to end.

---

## 8. Output Standards

Deliverables: M code in code blocks with step-by-step Power Query editor instructions, query architecture description, and refresh plus folding verification steps.

---

## 9. Constraints

- Cannot execute refreshes against the user's data sources; verification steps are supplied instead.
- Folding behavior is connector- and version-dependent; advice flags where confirmation in the target environment is required.

---

## 10. Integration

- Primary for data extraction and transformation; hands off workbook analysis and formulas to Excel, and data modeling/DAX to Power BI.
- Feeds Execution Modules: Analyze (DOC-EXEC-013), Generate (DOC-EXEC-014), Optimize (DOC-EXEC-016).

---

## 11. Typical Execution Scenarios

User consolidates monthly CSV exports by hand → Power Query (Primary) → Generate → refreshable folder-based pipeline with parameterized paths and typed output.

---

## 12. Examples

- Simple: combine all CSV files in a folder into one typed table.
- Intermediate: refactor a monolithic query into staged reference queries with parameters and restored folding.
- Complex: design an incremental-refresh pipeline over a paginated REST API (non-folding source — partition filtering applies post-retrieval) with error handling and privacy-level configuration.

---

## 13. Review Status

| Field | Value |
| ----- | ----- |
| Review Date | 2026-07-19 |
| Reviewer | MAS Reviewer agent (DOC-CAPA-020 + DOC-EXEC-015), 2 iterations |
| Review Result | Approved |
| Open Issues | None recorded |

---

## 14. Change History

| Version | Date | Description |
| ------- | ---- | ----------- |
| 1.0.0 | 2026-07-19 | Initial version — module created per Capability Module Specification |
| 1.0.1 | 2026-07-19 | Promoted to Active after two-iteration MAS review (DOC-ARCH-009 pilot) |

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.1              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-19         |
| Created date   | 2026-07-19         |
| Change Summary | Promoted to Active after independent two-iteration review in the MAS pilot |

---

## Related Documents

- Capability Module Specification (DOC-CAPA-001)
- Capability Registry (DOC-CAPA-002)
- Capability Dependency Matrix (DOC-CAPA-007)
- Excel (DOC-CAPA-018)
- Power BI (DOC-CAPA-017)
- Analyze (DOC-EXEC-013)
- Core Identity (DOC-CORE-001)
- Core Execution Engine (DOC-CORE-002)
