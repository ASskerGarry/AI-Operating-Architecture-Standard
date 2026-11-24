# AI-OS — Product Requirements & MVP Scope

Document ID: TBD — assign only after approval and registry reservation  
Version: 0.1.1  
Status: Draft  
Layer: Product Specification (proposed; must map to a canonical AI-OS layer before registration)  
Document Type: Specification (proposed)  
Owner: AI-OS Product  
Last Updated: 2026-11-24

---

## 1. Purpose

Define the product requirements and the first deliverable scope for turning the existing AI-OS repository into a bilingual digital product: public documentation portal, authenticated private features, mobile-first web experience, and AI Chat capability.

This document is a Phase 2 working specification. It does not authorize implementation, changes to canonical AI-OS standards, deployments, publication, or mobile store submissions.

## 2. Product Vision

Provide a reliable, accessible bilingual portal for public AI-OS adopters and internal/project users to understand AI-OS, navigate its architecture, discover/read authoritative documents, and use an AI Chat assistant grounded in repository content. The product combines a public portal with authenticated private features.

The repository remains the canonical source of truth. The product is a presentation and access layer, not a replacement governance system.

## 3. Evidence Baseline

The following are confirmed in the inspected repository (main, inspected head 7763b22c, 2026-07-28):

- AI-OS has seven documented layers: Core, Architecture, Capability, Execution, Platform, Templates, Memory.
- The Document Registry is described as the SSOT for official documents and contains 81 entries (73 Active, 8 Draft in the audit snapshot).
- Official document metadata fields are defined by DOC-ARCH-006: title, version, status, layer, document type, Document ID, owner, and the required Version Information table.
- A static documentation site exists under docs/.
- A dependency-free read-only MCP server exists with list_documents, get_document, and search_documents, using stdio.
- A compliance validator, Working Kit generator, behavioral evaluation assets, and four GitHub Actions workflows exist.
- Claude Adapter is Active. GPT, Gemini, and Copilot adapters are Draft according to 04_Platforms/README.md.
- No product backend / public HTTP API or Android/iOS app project was found in the inspected repository tree.

These are audit-time observations, not a guarantee that the repository has not changed since the inspected commit.

## 4. Target Users

### Primary audiences

1. AI practitioners and developers — need to understand AI-OS concepts, platform adapters, reusable capabilities, and execution patterns.
2. Technical leads and solution architects — need to evaluate architecture, governance, compatibility, version status, and implementation boundaries.
3. Teams evaluating AI governance — need a clear explanation of the standard and access to authoritative documentation.
4. Existing AI-OS adopters — need to locate the right source document, check whether it is Active or Draft, and open its canonical GitHub location.

### User needs

- Understand what AI-OS is and what it is not.
- Browse all seven architecture layers.
- Find documents by ID, title, layer, status, and content where supported.
- Read official content without losing source attribution.
- Distinguish Active standards from Draft or historical materials.
- Access the experience on desktop, tablet, and mobile.

## 5. Core User Journeys

### UJ-01 — Discover AI-OS
A visitor opens the portal, understands the product purpose, sees the seven layers, and navigates to a layer.

### UJ-02 — Browse a layer
A visitor selects a layer, sees a description and its official documents, and can distinguish their lifecycle statuses.

### UJ-03 — Find a document
A visitor searches by Document ID or title, optionally filters by layer/status, opens a result, and sees metadata plus the original source link.

### UJ-04 — Read and verify
A visitor reads a document and can identify its ID, version, status, owner, source repository path, and last-updated information where available.

### UJ-05 — Use on mobile
A visitor opens the same Web product on a phone and can browse, search, and read documents with a touch-friendly responsive interface. Native mobile apps are a later phase.

## 6. MVP Scope

### 6.1 Website MVP — Required

- Public home / product overview.
- Seven-layer navigation, including Memory.
- Layer overview pages.
- Official document catalogue driven from a defined content model based on the Document Registry.
- Search by Document ID and title.
- Filters by layer and lifecycle status.
- Document detail / reading view.
- Display of official metadata and source attribution.
- Link to the canonical GitHub source document.
- Responsive layout for desktop, tablet, and mobile.
- Loading, empty, and error states.
- Accessible semantic navigation, keyboard support, focus indicators, and readable contrast.

### 6.2 Mobile Companion MVP — Proposed scope

The first release SHALL be a responsive, mobile-first Web experience. Native Android/iOS applications are planned for a later phase, subject to architecture and product validation.

Required mobile journeys:
- Browse layers.
- Search and filter documents.
- Read document content.
- View version, status, Document ID, and source link.
- Navigate back to layer / search results.

PWA installation and Offline Mode are open research items for Phase 3; they are not commitments.

### 6.3 Document Reading — Both Modes Required

- Built-in Markdown reader/rendering for a seamless portal experience.
- Direct link to the canonical GitHub source for verification or alternate reading.
- Source metadata and provenance remain visible in both modes.
- Rendered content must safely handle untrusted Markdown/HTML.

### 6.4 Public Portal and Private Features

- Public, anonymous access to core portal navigation, catalogue, document reading, and public AI-OS information.
- Authenticated private features are in scope for MVP; feature set, roles, data storage, session management, and authorization boundaries SHALL be designed in Phase 3.
- Public content and private user data must remain separated. Private functionality must not expose private-by-reference documents or user data to anonymous visitors.

### 6.5 Shared Content Foundation — Required

- Repository remains the canonical source.
- Registry metadata and document bodies are not manually duplicated as independent authoritative content.
- Each displayed document carries a stable Document ID and canonical source path.
- Content imports must preserve status and version metadata.
- Draft documents must be visibly distinguished from Active content.
- Any derived search index or cache must be reproducible from repository data and safely refreshable.

## 7. Later-Stage Candidates — Not MVP Commitments

- Native Android application.
- Native iOS application.
- Offline-first document library and synchronization (pending Phase 3 research and feasibility decision).
- Native Android and iOS apps.
- Expanded authenticated workspaces or saved reading lists beyond the MVP private-feature baseline.
- User annotations, bookmarks, and personal collections.
- Advanced full-text search with relevance ranking.
- API access for external consumers.
- Rich visual architecture maps.
- Additional platform-specific deployment workflows after adapters are validated.

Each candidate requires evidence of user value, architecture review, security assessment, and explicit scope approval.

## 8. Out of Scope for MVP

Unless a later product decision justifies them, MVP excludes:



- Subscriptions, payments, and monetization.
- Collaboration, comments, editing, or user-generated documents.
- Public write API or repository write access.
- Automatic changes to the canonical repository.
- Deployment of the MCP server as a network-facing service.
- Claims of production-ready integrations for platform adapters currently marked Draft.
- Separate native mobile binaries in the first release.

## 9. Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| FR-01 | Show AI-OS overview | Must | Visitor can identify the product purpose and navigate to the layer catalogue. |
| FR-02 | Browse seven layers | Must | All seven canonical layer names are present and each opens a layer view. |
| FR-03 | List official documents | Must | Catalogue records are traceable to the Document Registry and expose ID, title, layer, status, and version. |
| FR-04 | Search by Document ID | Must | Exact known ID returns the matching registered document. |
| FR-05 | Search by title | Must | Query returns matching titles; empty result state is explicit. |
| FR-06 | Filter by layer and status | Must | Filters can be combined and cleared. |
| FR-07 | Read a document | Must | Detail view displays the document body and required metadata. |
| FR-08 | Show source provenance | Must | Each document view links to the canonical GitHub path. |
| FR-09 | Distinguish lifecycle status | Must | Draft and Active are visually distinguishable and never conflated. |
| FR-10 | Responsive navigation and reading | Must | Primary journeys work on phone, tablet, and desktop viewports. |
| FR-11 | Provide UI states | Must | Loading, empty, not-found, and error states are defined and usable. |
| FR-12 | Install as PWA | Research | Phase 3 evaluates installability, manifest/service worker, update, and stale-content strategy. |
| FR-13 | Offline Mode | Research | Phase 3 evaluates scope, cache invalidation, freshness, storage, privacy, and limitations. |
| FR-14 | Bilingual UI and documentation navigation | Must | English and Ukrainian are available at launch; untranslated content is clearly labelled. |
| FR-15 | Markdown reader and GitHub source link | Must | Content renders safely and includes canonical source link. |
| FR-16 | Public portal | Must | Core portal/catalogue/document access is available without authentication. |
| FR-17 | Private features | Must | Private features require authentication and authorization; details are defined in Phase 3. |
| FR-18 | AI Chat | Must | Answers are grounded in retrieved sources, cite documents, disclose insufficient evidence, and cannot modify repository content. |

## 10. Non-Functional Requirements

### NFR-01 — Source integrity
The product MUST preserve Document ID, title, version, lifecycle status, and canonical repository source. It MUST NOT silently rewrite official source content.

### NFR-02 — Security
Public portal functions MUST be read-only. Private features MUST use authentication/server-side authorization, secure sessions, and least privilege. AI Chat MUST be retrieval-grounded, resistant to prompt injection from source content, and separated from write-capable tools. Source paths must be validated, path traversal prevented, Markdown/HTML safely rendered, and secrets kept out of client code.

### NFR-03 — Privacy
Because private features are in scope, the MVP will collect the minimum data required for authentication and those features. Data retention, deletion, privacy notices, analytics, and access controls must be defined in Phase 3 before implementation.

### NFR-04 — Performance
Core navigation, search, and document reading SHOULD remain usable on typical mobile connections. Numeric performance budgets are to be set in Phase 3 after a deployment model is selected.

### NFR-05 — Accessibility
The product SHOULD target WCAG 2.2 AA, including keyboard access, semantic structure, visible focus, contrast, and responsive zoom behavior.

### NFR-06 — Maintainability
Product UI, document content ingestion, and source governance MUST remain separated. Reusable components and automated validation SHOULD be used.

### NFR-07 — Availability and resilience
The service SHOULD provide clear failure states when the repository or content source is unavailable. Availability targets and recovery objectives are TBD in Phase 3.

### NFR-08 — Freshness
The product MUST refresh derived catalogue/index/content after each merge to the canonical source branch. It MUST display source/version information and commit provenance where feasible. Stale cache must be identified; Phase 3 must design and test merge-triggered update, failure, and retry behavior.

### NFR-09 — Portability
The content model and product logic SHOULD avoid unnecessary vendor lock-in and preserve the platform-agnostic AI-OS core.

## 11. Content Model — Conceptual

The following is a proposed application read model, not a replacement for the official AI-OS Document Registry.

### Document
- document_id (stable key)
- title
- layer
- category / document_type
- status
- version
- owner
- repository_path
- source_url
- last_updated (when available)
- rendered_content (derived from source, not authoritative)
- source_commit (optional provenance)
- indexed_at (derived metadata)

### Layer
- layer_id / canonical layer name
- display_name
- repository_directory
- description (source-backed)
- document_count (derived)

### Content rules
- Document Registry remains authoritative for registration metadata.
- Document body remains authoritative in its source file.
- Application indexes and rendered pages are derived artifacts.
- Missing or inconsistent metadata must be surfaced for review, not guessed.
- Private-by-reference registry entries must not be exposed as if their private content were available.

## 12. Assumptions and Constraints

- Assumption A-01: The product has a public read-only portal plus authenticated private features.
- Assumption A-02: A single responsive application can serve desktop and mobile MVP needs.
- Assumption A-03: The existing repository and current GitHub Pages deployment path may be reusable, subject to Phase 3 validation.
- Constraint C-01: Current MCP server remains stdio and read-only.
- Constraint C-02: GPT, Gemini, and Copilot adapters are Draft in the inspected source.
- Constraint C-03: Native Android/iOS implementation is not justified by repository evidence alone.
- Constraint C-04: AI Chat and authenticated private features are approved for MVP scope, but implementation details and authorization boundaries remain subject to Phase 3 design. Billing, collaboration, and repository write access remain out of scope unless separately approved.

## 13. Product Decisions — Owner Confirmed

1. **Target audience:** Both public adopters/developers and internal/project users.
2. **Launch languages:** English and Ukrainian.
3. **Draft visibility:** Draft documents are visible to everyone and must carry a prominent Draft label.
4. **Mobile strategy:** Web first; Native Android/iOS later.
5. **Offline Mode:** Research required in Phase 3; not yet committed.
6. **Document reading:** Both built-in Markdown reader and direct canonical GitHub source link.
7. **Content freshness:** Refresh after every merge to the canonical source branch.
8. **Hosting:** Compare options in Phase 3; no hosting choice made yet.
9. **Access model:** Public portal plus authenticated private features.
10. **AI Chat:** Included in MVP from the start.

### Phase 3 Design Questions (not product-decision blockers)

- Define private feature set, user roles, identity/authentication provider, authorization model, session security, and data minimization.
- Define AI Chat retrieval corpus, indexing, citations, fallback/abstention, prompt-injection defenses, privacy boundary, model/provider strategy, cost controls, and evaluation suite.
- Decide whether translated document bodies are maintained in-source or translated with review; do not silently claim full translation coverage.
- Research Offline Mode/PWA and establish freshness, invalidation, and storage constraints.
- Compare hosting, deployment, and merge-triggered synchronization options.

## 14. Phase 2 Exit Criteria

Phase 2 is complete only when:
- Target users and user journeys are reviewed.
- Website/Web-first mobile scope and Native-later strategy are defined.
- Public portal versus authenticated private features is defined.
- AI Chat is included with grounding, citation, and safety requirements.
- MVP, later-stage candidates, and exclusions are explicit.
- Functional requirements have testable acceptance criteria.
- Non-functional requirements and open decisions are recorded.
- The content model respects existing AI-OS SSOT rules.
- The product owner reviews and approves this specification.

No implementation is authorized by this draft.

---

## Version Information

| Field | Value |
|---|---|
| Version | 0.1.1 |
| Status | Draft |
| Owner | AI-OS Product |
| Last Updated | 2026-11-24 |
| Created date | 2026-11-24 |
| Change Summary | Updated MVP scope with owner-confirmed decisions: bilingual, public Draft visibility, Web-first/Native-later, offline research, dual reading modes, merge-triggered freshness, public/private access, and AI Chat |

---

## Related Documents

- AI-OS Document Registry (DOC-ARCH-001)
- AI-OS Document Metadata Standard (DOC-ARCH-006)
- AI-OS Design Principles (DOC-ARCH-004)
- Platform Layer README (DOC-PLAT-001)
- AI-OS MCP Server (DOC-PLAT-005)
- Memory Architecture (DOC-MEM-002)
