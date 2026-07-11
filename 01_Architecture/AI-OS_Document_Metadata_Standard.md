# Document Metadata Standard

Version: 1.1.0
Status: Active
Layer: Architecture Layer
Document Type: Standard
Document ID: DOC-ARCH-006
Owner: AI-OS Architecture

---

## Purpose

This standard defines the mandatory metadata that every official AI-OS document SHALL carry, and the canonical values allowed for each field.

It is the Single Source of Truth (SSOT) for document metadata. Other documents SHALL reference this standard instead of redefining metadata rules (DP-001, DP-003).

---

## Scope

Applies to every official document registered in the AI-OS Document Registry, across all layers. Working notes, exports, and archive content are out of scope.

---

## Mandatory Header Fields

Every official document SHALL begin with a header block containing:

| Field | Description | Example |
| ----- | ----------- | ------- |
| Title (H1) | Official document title, matching the Document Registry | `# Capability Registry` |
| Version | Semantic version of the document | `1.0.1` |
| Status | Lifecycle status (see Canonical Statuses) | `Active` |
| Layer | Architectural layer (see Canonical Layers) | `Capability Layer` |
| Document Type | Classification (see Canonical Document Types) | `Registry` |
| Document ID | Globally unique identifier (see ID Format) | `DOC-CAPA-002` |
| Owner | Responsible authority | `AI-OS Architecture` |

---

## Document ID Format

```
DOC-<LAYER>-<NNN>
```

| Layer Code | Layer |
| ---------- | ----- |
| CORE | Core Layer (`00_Core`) |
| ARCH | Architecture Layer (`01_Architecture`) |
| CAPA | Capability Layer (`02_Capability_Layer`) |
| EXEC | Execution Layer (`03_Execution_Layer`) |
| PLAT | Platform Layer (`04_Platforms`) |
| TMP | Templates Layer (`05_Templates`) |

- `NNN` is a zero-padded sequence number unique within the layer code.
- IDs SHALL never be reused, even after a document is archived.
- IDs are assigned at registration time in the AI-OS Document Registry.

---

## Canonical Statuses

| Status | Meaning |
| ------ | ------- |
| Draft | Under development; not authoritative |
| Review | Undergoing formal validation |
| Active | Approved and authoritative |
| Deprecated | No longer recommended; kept for reference |
| Archived | Retired from active use |

No other status values are permitted. (Module-level lifecycle stages such as Idea/Approved/Stable are defined by the layer Lifecycle documents and map onto these document statuses.)

---

## Canonical Document Types

Standard, Registry, Template, Guide, Specification, README, Change Log, Index, Capability Module, Execution Module.

New types SHALL be added to this standard before first use.

---

## Version Information Table

Every official document SHALL end with a Version Information table:

| Field | Required | Notes |
| ----- | -------- | ----- |
| Version | Yes | Must match the header |
| Status | Yes | Must match the header |
| Owner | Yes | Must match the header |
| Last Updated | Yes | `YYYY-MM-DD` |
| Created date | Yes | `YYYY-MM-DD` |
| Change Summary | Yes | One line describing the latest change |

---

## Document Structure

```
Document Header (H1 + metadata fields)
↓
Purpose
↓
Body
↓
Version Information
↓
Related Documents
```

The full structural and style rules are defined in AI-OS Documentation Standards.

---

## Compliance

Documents violating this standard SHALL NOT be promoted to Active status. Compliance is verified during document review (see the layer Review Standards).

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.1.0              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-11         |
| Created date   | 2026-07-10         |
| Change Summary | Wrote the missing body (fields, ID format, canonical values); fixed "Standart" typo |

---

## Related Documents

- AI-OS Documentation Standards
- AI-OS Document Template
- AI-OS Document Registry
- AI-OS Design Principles

