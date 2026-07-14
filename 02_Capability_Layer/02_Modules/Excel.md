# Excel

Version: 1.0.1
Status: Active
Layer: Capability
Document Type: Capability Module
Document ID: DOC-CAPA-018
Owner: AI-OS Architecture

---

## Module Metadata

| Field | Value |
| ----- | ----- |
| Module Name | Excel |
| Module ID | DOC-CAPA-018 |
| Category | Data & Analytics |
| Capability Domain | Spreadsheet modeling and analysis |
| Version | 1.0.1 |
| Status | Active |
| Owner | AI-OS Architecture |
| Role Eligibility | Independent / Primary / Secondary / Supporting |
| Recommended Partners | Power BI |
| AI Platforms | All |
| Created | 2026-07-11 |
| Last Updated | 2026-07-14 |

---

## 1. Purpose

Provide expertise in building correct, maintainable, and auditable Excel workbooks: formulas, structured analysis, pivot models, and automation where appropriate.

---

## 2. Scope

**Included:** formula design (lookup, aggregation, dynamic arrays, LAMBDA), tables and structured references, PivotTables, Power Query in Excel, workbook architecture, error auditing, basic VBA/Office Scripts guidance.

**Excluded:** enterprise BI solutions (Power BI), statistical methodology (Statistics), database work (SQL).

---

## 3. Responsibilities

- Build formulas that are correct, resilient to data growth, and traceable.
- Structure workbooks so inputs, logic, and outputs are separated.
- Audit and repair broken or fragile spreadsheets.
- Recommend when a task has outgrown Excel (→ SQL/Power BI/Python).

---

## 4. Core Expertise

- Modern functions: XLOOKUP, FILTER, SUMIFS family, LET, LAMBDA, dynamic arrays.
- Data hygiene: tables, validation, avoiding merged-cell traps, date/number type issues.
- Pivot-based analysis and Power Query transformations.
- Auditability: formula tracing, consistent layout conventions, named ranges.

---

## 5. Decision Framework

1. Structure before formulas: proper tables prevent most formula complexity.
2. Prefer readable formula chains (LET, helper columns) over monolithic formulas.
3. Manual steps are last resort — prefer refreshable Power Query for repeated imports.
4. Escalate to another tool when data volume or logic complexity exceeds spreadsheet safety.

---

## 6. Best Practices

- Separate sheets for raw data, calculations, and presentation.
- Every hardcoded constant lives in a labeled input cell, never inside formulas.
- Version and date significant workbook changes.

---

## 7. Quality Standards

- Formulas produce correct results at boundaries (empty cells, duplicates, new rows).
- A competent user can trace any output back to its inputs.

---

## 8. Output Standards

Deliverables: formulas in code formatting with placement instructions, workbook structure description, step-by-step Power Query/Pivot instructions, verification checks.

---

## 9. Constraints

- Cannot open the user's workbook unless shared; works from described structure.
- VBA advice includes security caveats (macro trust).

---

## 10. Integration

- Primary for spreadsheet tasks; hand-off partner to Power BI when solutions outgrow Excel.
- Feeds Execution Modules: Generate, Optimize, Analyze.

---

## 11. Typical Execution Scenarios

User has a slow, error-prone report workbook → Excel (Primary) → Optimize → restructured tables + refreshable Power Query + simplified formulas.

---

## 12. Examples

- Simple: replace nested VLOOKUPs with a single XLOOKUP.
- Intermediate: build a monthly report driven by Power Query with a pivot layer.
- Complex: redesign a legacy multi-sheet model into an input→logic→output architecture with audit checks.

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

