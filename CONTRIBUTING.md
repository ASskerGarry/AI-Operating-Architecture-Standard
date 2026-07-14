# Contributing to AI-OS

Document ID: DOC-CORE-006
Version: 1.1.0
Status: Active
Layer: Core
Document Type: Guide
Owner: AI-OS Architecture

AI-OS is a **documentation governance repository**, not a codebase. Contributions are documents, and documents follow rules. This guide is the practical checklist; the authoritative standards it points to are the SSOT (DP-001).

---

## The One Non-Negotiable Rule: Log First

Every change MUST be recorded in [`Change_Log_day.md`](Change_Log_day.md) **before or as** the change is made — never only after. Use the entry format defined at the top of that file (time, author, scope, change, reason, files, status) and update the status as work proceeds (`planned → in-progress → done`). No change is complete until it is logged.

---

## Contributing a Change to an Existing Document

1. Add the change-log entry (see above).
2. Make the edit.
3. Bump the document's semantic version and update its **Version Information** table (Last Updated, Change Summary).
4. If the version/status changed, sync the document's row in the [Document Registry](01_Architecture/AI-OS_Document_Registry.md).
5. Run the validator (below) — your change must not add new flags.

## Contributing a New Official Document

1. Add the change-log entry.
2. Copy the structure from the [AI-OS Document Template](01_Architecture/AI-OS_Document_Template.md) (`DOC-ARCH-007`).
3. Comply with the [Document Metadata Standard](01_Architecture/AI-OS_Document_Metadata_Standard.md) (`DOC-ARCH-006`): header fields, canonical status/type values, `DOC-<LAYER>-<NNN>` ID format.
4. Register the document in the [Document Registry](01_Architecture/AI-OS_Document_Registry.md) — IDs are assigned at registration and are immutable.
5. New Capability or Execution modules must additionally follow their layer's Blueprint, Writing Guide, and Review Standard (see `02_Capability_Layer/00_Governance/` and `03_Execution_Layer/00_Execution_Governance/`).

---

## Validate Before You Finish

```bash
python3 Knowledge_Base/validate_aios.py .
```

CI (`.github/workflows/validate.yml`) runs this on every push with a ratchet baseline: builds fail if the flagged-item count regresses. If you fix existing flags, lower the `BASELINE` in the workflow to lock in the improvement.

---

## Style Essentials

- English, objective technical language; RFC 2119 terms (SHALL/MUST/SHOULD/MAY) for normative rules.
- Reference authoritative documents instead of copying their content (DP-001, DP-003).
- One responsibility per document (DP-002); no hidden dependencies (DP-007).
- No fabricated facts, references, or sources — ever.

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.1.0              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-14         |
| Change Summary | Registered as DOC-CORE-006 and promoted to Active |

---

## Related Documents

- AI-OS Document Metadata Standard (DOC-ARCH-006)
- AI-OS Document Template (DOC-ARCH-007)
- AI-OS Document Registry (DOC-ARCH-001)
- AI-OS Documentation Standards (DOC-ARCH-002)
