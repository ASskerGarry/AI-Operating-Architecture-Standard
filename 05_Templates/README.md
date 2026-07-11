# Templates Layer

Version: 1.1.0
Status: Draft
Layer: Templates
Document Type: README
Document ID: DOC-TMP-001
Owner: AI-OS Architecture

---

## Purpose

This layer holds shared, cross-layer templates and reusable document structures for AI-OS.

Layer-specific templates remain owned by their layers (Single Source of Truth, DP-001); this directory only hosts templates that apply to more than one layer, and this README serves as the navigation index to all templates in the repository.

---

## Template Index

| Template | Applies To | Location | Document ID |
| -------- | ---------- | -------- | ----------- |
| AI-OS Document Template | Any official document | `01_Architecture/AI-OS_Document_Template.md` | DOC-ARCH-007 |
| Capability Module Specification | Capability Modules | `02_Capability_Layer/01_Templates/00_Capability_Module_Template.md` | DOC-CAPA-001 |
| Execution Module Specification | Execution Modules | `03_Execution_Layer/01_Templates/00_Execution_Module_Specification.md` | DOC-EXEC-001 |
| Execution Module Template | Execution Modules | `03_Execution_Layer/01_Templates/01_Execution_Module_Template.md` | DOC-EXEC-002 |

---

## Usage Rules

- Always start a new official document from the relevant template — never from a copy of an existing document (prevents metadata drift).
- Metadata fields and canonical values are governed by the AI-OS Document Metadata Standard.
- A new shared template SHALL be added here only when at least two layers need it; otherwise it belongs to its layer's `01_Templates` directory.

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.1.0              |
| Status         | Draft              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-11         |
| Created date   | 2026-07-10         |
| Change Summary | Expanded stub into full layer description with template index and usage rules |

---

## Related Documents

- AI-OS Document Template
- AI-OS Document Metadata Standard
- AI-OS Documentation Standards
- AI-OS Document Registry

