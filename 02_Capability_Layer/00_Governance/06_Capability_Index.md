# Capability Index
Version: 1.0.1
Status: Active
Document ID: DOC-CAPA-008
Layer: Capability Layer
Document Type: Index
Owner: AI-OS Architecture
---
# 1. Purpose
The Capability Index serves as the centralized catalog of all Capability Modules available within AI-OS.
Its purpose is to provide a single authoritative reference for module discovery, classification, version tracking, lifecycle management, and architectural governance.
The Capability Index enables both AI and human maintainers to quickly identify available competencies and their current implementation status.
---
# 2. Responsibilities
The Capability Index shall:
- maintain an inventory of all Capability Modules;
- record module metadata;
- track lifecycle status;
- identify module ownership;
- reference dependencies;
- support governance and maintenance activities.
---
# 3. Capability Record
Each Capability Module shall include the following metadata:
- Module Name
- Category
- Version
- Status
- Owner
- Primary Capability
- Dependencies
- Execution Support
- Review Status
- Lifecycle Stage
- Compatibility
- Last Updated
---
# 4. Capability Status
Every Capability Module shall be assigned one of the following statuses:
- Draft
- Review
- Approved
- Stable
- Deprecated
- Archived
---
# 5. Governance Rules
Only Capability Modules listed in the Capability Index are considered part of the official AI-OS architecture.
Modules not registered in the Capability Index shall not be activated by the Capability Registry.
---
# 6. Example Record
| Property | Value |
|----------|-------|
| Module | Prompt Engineering |
| Category | AI Engineering |
| Version | 2.0 |
| Status | Stable |
| Dependencies | AI Strategy |
| Lifecycle | Stable |
| Execution Support | Yes |
---
# 7. Version Information
| Field | Value |
|------|------|
| Version | 1.0.1 |
| Status | Active |
| Current Stage | Active |
| Last Updated | 2026-07-10 |
| Change Log | Phase 1 governance normalization (IDs, status, owner) |
---
# 8. Related Documents

- Capability Registry
- Capability Blueprint
- Capability Writing Guide
- Capability Review Standard
- Capability Lifecycle
- Capability Dependency Matrix
- Core Identity
- Core Execution Engine
- AI-OS Architectural Principles
- Documentation Standards
- Glossary