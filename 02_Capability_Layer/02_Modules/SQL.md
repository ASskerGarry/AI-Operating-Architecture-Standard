# SQL

Version: 1.0.1
Status: Active
Layer: Capability
Document Type: Capability Module
Document ID: DOC-CAPA-015
Owner: AI-OS Architecture

---

## Module Metadata

| Field | Value |
| ----- | ----- |
| Module Name | SQL |
| Module ID | DOC-CAPA-015 |
| Category | Data & Analytics |
| Capability Domain | Relational data querying and modeling |
| Version | 1.0.1 |
| Status | Active |
| Owner | AI-OS Architecture |
| Role Eligibility | Independent / Primary / Secondary / Supporting |
| Recommended Partners | Statistics, Power BI |
| AI Platforms | All |
| Created | 2026-07-11 |
| Last Updated | 2026-07-14 |

---

## 1. Purpose

Provide expertise in writing correct, readable, and performant SQL, and in relational data modeling, across major dialects (PostgreSQL, MySQL, SQL Server, SQLite, BigQuery, Snowflake).

---

## 2. Scope

**Included:** query design (joins, aggregation, window functions, CTEs), query optimization and reading execution plans, data modeling and normalization, dialect differences, data quality checks in SQL.

**Excluded:** database administration (backups, replication), analytical interpretation of results (Data Analytics), teaching methodology (Teaching).

---

## 3. Responsibilities

- Produce queries that are provably correct against the schema and stated intent.
- Optimize queries with reasoning about indexes, join order, and scan volume.
- Design schemas balancing normalization, query patterns, and maintainability.
- Flag dialect-specific behavior whenever the target dialect is not fixed.

---

## 4. Core Expertise

- Joins and set logic; NULL semantics and their traps.
- Window functions, CTEs, subquery strategies and their performance profiles.
- Aggregation correctness: grain awareness, fan-out and double-counting prevention.
- Indexing strategy and execution plan interpretation.

---

## 5. Decision Framework

1. Correctness first: verify grain and join cardinality before optimizing.
2. Readability over cleverness — CTEs with clear names beat nested subqueries.
3. Optimize only against evidence (plan, row counts), not assumptions.
4. State the assumed dialect when it changes syntax or semantics.

---

## 6. Best Practices

- Comment non-obvious business logic in queries.
- Validate with row-count sanity checks at each transformation step.
- Prefer explicit column lists over `SELECT *` in production queries.

---

## 7. Quality Standards

- Query result grain is stated and correct.
- NULL handling is deliberate and documented where it affects results.
- No fabricated functions or dialect syntax.

---

## 8. Output Standards

Deliverables: formatted SQL in code blocks, dialect noted, brief logic explanation, verification query or expected-result description where applicable.

---

## 9. Constraints

- Cannot verify against a live database unless one is provided; verification steps are supplied instead.
- Performance advice is directional without real execution plans.

---

## 10. Integration

- Primary for query writing/optimization; Supporting for Data Analytics and Power BI work.
- Feeds Execution Modules: Generate, Optimize, Validate, Teach SQL.

---

## 11. Typical Execution Scenarios

User asks why a query double-counts revenue → SQL (Primary) → Analyze → fan-out diagnosis with corrected join and verification check.

---

## 12. Examples

- Simple: aggregate orders per customer with correct NULL handling.
- Intermediate: rewrite a nested subquery report as readable CTEs with window functions.
- Complex: design a star-schema model and the queries for a monthly KPI report.

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

