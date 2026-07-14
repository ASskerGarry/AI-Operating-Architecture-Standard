# AI-OS Document Registry

Version: 1.9.0
Status: Active
Layer: Architecture
Document Type: Registry
Document ID: DOC-ARCH-001
Owner: AI-OS Architecture

---

# Purpose

This document serves as the authoritative registry of all official documents within the AI Operating System (AI-OS).

The registry provides centralized governance for document identification, ownership, versioning, lifecycle management, architectural classification, and repository organization.

## This document is the Single Source of Truth (SSOT) for all AI-OS documentation.

# Scope

This registry applies to every official document maintained within the AI-OS repository, including:

- Core documents
- Architecture standards
- Governance documents
- Capability Modules
- Execution Modules
- Templates
- Platform Integrations
- Reference documentation
- Future AI-OS extensions
  Every official document SHALL be registered before its status is changed to Active.

---

# Registry Structure

Each registered document SHALL include the following metadata.

| Field               | Description                         |
| ------------------- | ----------------------------------- |
| Document ID         | Globally unique document identifier |
| Document Title      | Official document title             |
| Layer               | Architectural layer                 |
| Category            | Document classification             |
| Status              | Current lifecycle status            |
| Owner               | Responsible authority               |
| Version             | Current version                     |
| Repository Location | Relative repository path            |

---

# Document Registry

| Document ID  | Document Title                     | Layer        | Category          | Status | Version | Owner              | Repository Location                         |
| ------------ | ---------------------------------- | ------------ | ----------------- | ------ | ------- | ------------------ | ------------------------------------------- |
| DOC-CORE-001 | Core Identity                      | Core         | Standard          | Active | 1.1.0   | AI-OS Architecture | /00_Core                                    |
| DOC-CORE-002 | Core Execution Engine              | Core         | Standard          | Active | 1.2.0   | AI-OS Architecture | /00_Core                                    |
| DOC-ARCH-001 | AI-OS Document Registry            | Architecture | Standard          | Active | 1.9.0  | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-002 | AI-OS Documentation Standards      | Architecture | Standard          | Active | 1.0.1  | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-003 | AI-OS Glossary                     | Architecture | Reference         | Active | 1.1.0   | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-004 | AI-OS Design Principles            | Architecture | Registry          | Active | 1.1.0   | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-005 | AI-OS Principle Registry           | Architecture | Registry          | Active | 1.0.1  | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-006 | AI-OS Document Metadata Standard   | Architecture | Standard          | Active | 1.3.0   | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-007 | AI-OS Document Template            | Architecture | Template          | Active | 1.1.1   | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-008 | AI-OS Reasoning Patterns           | Architecture | Reference         | Active | 1.0.1  | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-009 | AI-OS Orchestration Standard       | Architecture | Standard          | Draft  | 1.0.0   | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-010 | AI-OS Open-Core Paid Modules MVP   | Architecture | Specification     | Draft  | 1.0.0   | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-011 | AI-OS Open-Core Diagnostic Service Specification | Architecture | Specification | Draft | 1.0.0 | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-012 | AI-OS Open-Core Pricing and Packaging Guide | Architecture | Guide    | Draft  | 1.0.0   | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-013 | AI-OS Open-Core GTM and Sales Playbook | Architecture | Guide         | Draft  | 1.0.0   | AI-OS Architecture | /01_Architecture                            |
| DOC-ARCH-014 | AI-OS Open-Core Pilot Delivery Kit | Architecture | Guide             | Draft  | 1.0.0   | AI-OS Architecture | /01_Architecture                            |
| DOC-CAPA-001 | Capability Module Specification    | Architecture | Specification     | Active | 1.0.2  | AI-OS Architecture | /02_Capability_Layer/01_Templates           |
| DOC-EXEC-001 | Execution Module Specification     | Architecture | Specification     | Active | 1.1.1  | AI-OS Architecture | /03_Execution_Layer/01_Templates            |
| DOC-EXEC-002 | Execution Module Template          | Architecture | Template          | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/01_Templates            |
| DOC-EXEC-003 | Analysis Execution Module README   | Execution    | README            | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/02_Analysis/README.md   |
| DOC-EXEC-004 | Generation Execution Module README | Execution    | README            | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/03_Generation/README.md |
| DOC-PLAT-001 | Platform Layer README              | Platform     | README            | Active | 1.1.2  | AI-OS Architecture | /04_Platforms/README.md                     |
| DOC-PLAT-002 | Claude Adapter                     | Platform     | Platform Adapter  | Active | 1.0.2  | AI-OS Architecture | /04_Platforms/Claude_Adapter.md             |
| DOC-MEM-001  | Memory Layer README                | Memory       | README            | Active | 1.0.1  | AI-OS Architecture | /06_Memory/README.md                        |
| DOC-MEM-002  | Memory Architecture                | Memory       | Standard          | Active | 1.0.1  | AI-OS Architecture | /06_Memory/Memory_Architecture.md           |
| DOC-CORE-004 | AI-OS — Daily Change Log           | Core         | Change Log        | Active | 1.1.0   | AI-OS Architecture | /Change_Log_day.md                          |
| DOC-CORE-005 | AI-OS — AI Operating Architecture Standard | Core | README            | Active | 1.2.0   | AI-OS Architecture | /README.md                                  |
| DOC-CORE-006 | Contributing to AI-OS              | Core         | Guide             | Active | 1.1.0   | AI-OS Architecture | /CONTRIBUTING.md                            |
| DOC-CORE-007 | Security Policy                    | Core         | Standard          | Active | 1.1.0   | AI-OS Architecture | /SECURITY.md                                |
| DOC-CORE-008 | AI-OS Agent Instructions           | Core         | Guide             | Active | 1.1.0   | AI-OS Architecture | /AGENTS.md                                  |
| DOC-CORE-009 | AI-OS — AI Working Kit             | Core         | Reference         | Active | 2.1.0   | AI-OS Architecture | /AI-OS_AI_Working_Kit.md                    |
| DOC-CORE-010 | AI-OS — AI Working Kit (Lean)      | Core         | Reference         | Active | 1.0.0   | AI-OS Architecture | /AI-OS_AI_Working_Kit_lean.md               |
| DOC-PLAT-003 | CLAUDE                             | Platform     | Platform Asset    | Active | 1.1.0   | AI-OS Architecture | /CLAUDE.md                                  |
| DOC-PLAT-004 | Prompt Generator (AI-OS)           | Platform     | Platform Asset    | Active | 4.0.2   | AI-OS Architecture | /04_Platforms/Claude/prompt-generator.skill.md |
| DOC-TMP-001  | Templates Layer README             | Templates    | README            | Active | 1.1.1  | AI-OS Architecture | /05_Templates/README.md                     |
| DOC-CAPA-002 | Capability Registry                | Capability   | Registry          | Active | 1.0.1   | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-CAPA-003 | Capability Blueprint               | Capability   | Standard          | Active | 1.0.1   | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-CAPA-004 | Capability Writing Guide           | Capability   | Guide             | Active | 1.0.1   | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-CAPA-005 | Capability Review Standard         | Capability   | Review Standard   | Active | 1.0.2  | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-CAPA-006 | Capability Lifecycle               | Capability   | Lifecycle         | Active | 1.0.1   | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-CAPA-007 | Capability Dependency Matrix       | Capability   | Dependency Matrix | Active | 1.0.1   | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-CAPA-008 | Capability Index                   | Capability   | Index             | Active | 1.0.1   | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-CAPA-009 | Capability Change Log              | Capability   | Change Log        | Active | 1.0.1   | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-EXEC-005 | Execution Registry                 | Execution    | Registry          | Active | 1.0     | AI-OS Architecture | /03_Execution_Layer/00_Execution_Governance |
| DOC-EXEC-006 | Execution Blueprint                | Execution    | Standard          | Active | 1.1     | AI-OS Architecture | /03_Execution_Layer/00_Execution_Governance |
| DOC-EXEC-007 | Execution Writing Guide            | Execution    | Guide             | Active | 1.1     | AI-OS Architecture | /03_Execution_Layer/00_Execution_Governance |
| DOC-EXEC-008 | Execution Review Standard          | Execution    | Review Standard   | Active | 1.0.2  | AI-OS Architecture | /03_Execution_Layer/00_Execution_Governance |
| DOC-EXEC-009 | Execution Lifecycle                | Execution    | Lifecycle         | Active | 1.0     | AI-OS Architecture | /03_Execution_Layer/00_Execution_Governance |
| DOC-EXEC-010 | Execution Dependency Matrix        | Execution    | Dependency Matrix | Active | 1.0     | AI-OS Architecture | /03_Execution_Layer/00_Execution_Governance |
| DOC-EXEC-011 | Execution Index                    | Execution    | Index             | Active | 1.0     | AI-OS Architecture | /03_Execution_Layer/00_Execution_Governance |
| DOC-EXEC-012 | Execution Change Log               | Execution    | Change Log        | Active | 1.0     | AI-OS Architecture | /03_Execution_Layer/00_Execution_Governance |
| DOC-EXEC-013 | Analyze                            | Execution    | Execution Module  | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/02_Analysis             |
| DOC-EXEC-014 | Generate                           | Execution    | Execution Module  | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/03_Generation           |
| DOC-EXEC-015 | Validate                           | Execution    | Execution Module  | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/04_Validation           |
| DOC-EXEC-016 | Optimize                           | Execution    | Execution Module  | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/05_Optimization         |
| DOC-EXEC-017 | Develop AI Assistant               | Execution    | Execution Module  | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/06_Development          |
| DOC-EXEC-018 | Teach SQL                          | Execution    | Execution Module  | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/07_Education            |
| DOC-EXEC-019 | Validation Category README         | Execution    | README            | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/04_Validation           |
| DOC-EXEC-020 | Optimization Category README       | Execution    | README            | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/05_Optimization         |
| DOC-EXEC-021 | Development Category README        | Execution    | README            | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/06_Development          |
| DOC-EXEC-022 | Education Category README          | Execution    | README            | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/07_Education            |
| DOC-EXEC-023 | Custom Category README             | Execution    | README            | Active | 1.0.1  | AI-OS Architecture | /03_Execution_Layer/99_Custom               |
| DOC-CAPA-010 | Capability Governance README       | Capability   | README            | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/00_Governance          |
| DOC-CORE-003 | Core Change Log                    | Core         | Change Log        | Active | 1.0.0   | AI-OS Architecture | /00_Core                                    |
| DOC-CAPA-011 | Prompt Engineering                 | Capability   | Capability Module | Active | 1.0.2  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-012 | AI Strategy                        | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-013 | Data Analytics                     | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-014 | Statistics                         | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-015 | SQL                                | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-016 | Python                             | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-017 | Power BI                           | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-018 | Excel                              | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-019 | Teaching                           | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-020 | Technical Writing                  | Capability   | Capability Module | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |
| DOC-CAPA-021 | Capability Modules README          | Capability   | README            | Active | 1.0.1  | AI-OS Architecture | /02_Capability_Layer/02_Modules             |

# Document Categories

Official AI-OS documents SHALL belong to one of the following categories.

| Category          | Description                                           |
| ----------------- | ----------------------------------------------------- |
| Standard          | Defines mandatory architectural rules or requirements |
| Registry          | Centralized catalog of architectural assets           |
| Template          | Reusable document structure                           |
| Specification     | Defines a module, capability, or workflow             |
| Guide             | Provides implementation guidance                      |
| Lifecycle         | Defines lifecycle management                          |
| Review Standard   | Defines review requirements                           |
| Dependency Matrix | Defines architectural dependencies                    |
| Index             | Navigation document                                   |
| Change Log        | Records document evolution                            |
| Reference         | Informational documentation                           |
| README            | Repository overview                                   |
| Platform Adapter  | Assembles AI-OS content for one concrete AI platform  |
| Platform Asset    | Deployable artifact governed by a Platform Adapter     |

---

# Lifecycle Status

Every document SHALL use one of the following lifecycle states.

| Status     | Description                      |
| ---------- | -------------------------------- |
| Draft      | Initial development              |
| Review     | Under architectural review       |
| Active     | Approved for production use      |
| Deprecated | Scheduled for replacement        |
| Archived   | Retained for historical purposes |

Only Active documents SHALL be considered authoritative.

---

# Document Identification Rules

Every official document SHALL:

- receive a globally unique Document ID;
- have one official title;
- belong to exactly one architectural layer;
- belong to exactly one primary category;
- define one responsible owner;
- maintain semantic versioning;
- include mandatory document metadata;
- comply with AI-OS Documentation Standards.

Document IDs SHALL remain immutable throughout the document lifecycle.

---

# Governance

AI-OS Architecture is responsible for:

- assigning Document IDs;
- approving new documents;
- maintaining registry consistency;
- preventing duplicate identifiers;
- governing lifecycle transitions;
- ensuring repository integrity.

---

# Maintenance Rules

The registry SHALL be updated whenever:

- a new document is created;
- a document changes lifecycle status;
- document ownership changes;
- document location changes;
- a document is archived;
- a document is removed from active governance.

Registry updates SHALL occur before publishing architectural changes.

---

# Version Information

| Field          | Value                                                                                                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Version        | 1.9.0                                                                                                                              |
| Status         | Active                                                                                                                             |
| Owner          | AI-OS Architecture                                                                                                                 |
| Last Updated   | 2026-07-14                                                                                                                         |
| Created date   | 2026-07-10                                                                                                                         |
| Change Summary | Registered the Lean Working Kit (DOC-CORE-010, Active 1.0.0); Working Kit bumped to 2.1.0; registry now 75 documents |

---

# Related Documents

- Core Identity
- Core Execution Engine
- AI-OS Documentation Standards
- AI-OS Document Metadata Standard
- AI-OS Document Template
- AI-OS Glossary
- AI-OS Design Principles
- AI-OS Principles Registry

