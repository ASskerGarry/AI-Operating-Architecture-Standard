# AI-OS — System Architecture Proposal

Document ID: TBD — Draft product working document; not an official AI-OS standard  
Version: 0.1.0  
Status: Draft  
Layer: Product Specification (proposed; mapping to the canonical AI-OS layer requires owner approval)  
Document Type: Specification (proposed)  
Owner: AI-OS Product  
Last Updated: 2026-11-24

---

## 1. Purpose and Status

This document proposes a product-level system architecture for the AI-OS Digital Product MVP. It is a non-binding Phase 3 design artifact, not an approved technical decision, official AI-OS standard, implementation instruction, or deployment authorization.

The design is constrained by the owner-confirmed product scope: bilingual English/Ukrainian; public portal and authenticated private features; public visibility of clearly labelled Draft documents; responsive Web first and Native Android/iOS later; built-in Markdown reading plus canonical GitHub source; content refresh after each merge; AI Chat in MVP; Offline/PWA research only; hosting choice deferred to evaluation.

## 2. Verified Repository Baseline

The inspected main branch is a documentation-focused repository with seven architecture layers, a canonical Markdown Document Registry, a static site under docs/, a standard-library Python MCP server using read-only stdio, deterministic validators/generators, and GitHub Actions gates. The current website is static HTML/CSS/JavaScript; the home page does not yet represent all seven layers consistently (Memory is absent from its six cards), and its navigation/interface is English-only.

The MCP server (Knowledge_Base/aios_mcp_server.py, DOC-PLAT-005) offers list_documents, get_document, and search_documents, with a path sandbox and no write surface. Its documented transport is stdio. It is not a network API and SHALL remain so unless a separately approved design supersedes that boundary.

Governance evidence: root AGENTS.md is Active DOC-CORE-008 1.1.0 and points to Knowledge_Base/Agents/AGENTS.md as canonical; that canonical file is currently Draft DOC-CORE-007, while the Registry assigns DOC-CORE-007 to Security Policy. Treat as a governance conflict; do not use or change its ID. The Registry is Active DOC-ARCH-001 1.16.1. DOC-ARCH-009 Orchestration Standard is Active 1.1.0. GPT/Gemini/Copilot adapters remain Draft; Claude adapter is Active.

## 3. Architecture Drivers

1. SSOT: the repository and registered source documents remain authoritative.
2. Separation of concerns: product presentation, content ingestion, identity/private features, and AI Chat must have separate boundaries.
3. Read-only public surface: no public ability to change canonical repository content.
4. Provenance: every document and AI answer must link to source metadata and source revision where possible.
5. Bilingual UX: interface labels and document translation state must be explicit; no silent translation treated as authoritative.
6. Secure private features: authentication alone is not authorization; server-side checks are required on every private operation.
7. Freshness: merge-triggered sync must be reliable, observable, idempotent, and recoverable.
8. AI grounding: AI Chat must retrieve from an approved corpus, cite the evidence, and abstain when evidence is insufficient.
9. Portability: avoid premature coupling to one hosting or AI provider.
10. Quality: architecture choices must be testable and fit the existing CI and governance system.

## 4. Logical System Context

**Actors:** anonymous visitor, authenticated user, product administrator/content maintainer, AI Chat user, GitHub repository/Actions, identity provider, selected LLM provider.

**Logical components:**

- Web Client: responsive bilingual portal, catalogue/search, Markdown reader, Draft badges, GitHub source links, private workspace UI, AI Chat UI.
- Product Backend / BFF: server-side session validation, authorization, private feature endpoints, AI Chat orchestration, rate/cost controls; no repository mutation.
- Content Sync Worker: triggered by canonical-branch merges; fetches/validates source revision, builds derived content records, updates search/RAG indexes, publishes a sync result.
- Content Read Model: derived, versioned records keyed by Document ID and repository path, with source commit SHA, status, version, language/translation state, content hash, timestamps.
- Search Index: derived from public-eligible documents; private-by-reference records are excluded unless access rules are explicit and tested.
- RAG Index: derived chunks with document ID, source URL/path, source commit SHA, section/heading, language, status, access classification, and content hash.
- Identity & Access: external identity provider or managed auth; product-side roles/authorization policy and secure server-side sessions.
- Observability: sync job state, error telemetry, request metrics, AI token/cost usage, security events, privacy-conscious audit trail.

## 5. Proposed Data Flow

### 5.1 Content Publication / Sync

1. A merge lands on the canonical source branch.
2. GitHub Actions sends a signed/verified event or triggers a controlled workflow.
3. Sync worker pins the exact commit SHA; it does not read a moving branch ref during the same job.
4. Worker fetches the registry and eligible Markdown documents from that commit.
5. Validate schema, unique IDs, canonical status, repository path containment, document size, and supported Markdown.
6. Build a deterministic content manifest and derived read model.
7. Update search and RAG indexes idempotently using source commit + file hash as the version key.
8. Publish new content snapshot atomically; retain last-known-good snapshot if validation or indexing fails.
9. Record sync status, source SHA, start/end time, counts, rejected records, and retry state.
10. Expose freshness timestamp and source SHA in the product UI/health endpoint.

A merge must not result in partially updated document catalogue/search/RAG state. Snapshot swap or a transactional index version pointer is recommended.

### 5.2 Document Read

Client requests a Document ID. Backend reads the published snapshot, enforces public/private visibility, returns safe rendered content plus metadata and canonical GitHub URL. Markdown is treated as untrusted input; raw HTML must be disabled or sanitized with a strict allowlist. Source link must point to the same pinned commit used by the read model where possible; the canonical branch URL can be shown separately.

### 5.3 AI Chat

1. Validate session and rate/cost limits.
2. Normalize question and user language preference.
3. Retrieve only documents/chunks allowed for that user and product scope.
4. Apply metadata-aware filters for language, lifecycle status, and visibility.
5. Pass retrieved snippets as untrusted evidence to the model; source content cannot override system/developer policy.
6. Require citations containing Document ID, title, section, source URL, and indexed source commit.
7. Validate cited sources exist in the retrieved set; reject unsupported citations.
8. If retrieval is weak, conflicting, stale, or insufficient, state uncertainty/abstain rather than inventing.
9. Store only minimal operational telemetry; do not retain conversation content by default unless the approved private-feature requirements explicitly require it.

AI Chat has no repository write tool, no shell/execute tool, and no admin action capability in the MVP architecture.

## 6. Trust Boundaries and Security Controls

- Browser is untrusted. Never put provider secrets, GitHub tokens, privileged API keys, or service credentials in client bundles.
- Backend is the policy enforcement point. Check authorization server-side for every private object and action; never rely on hidden UI controls.
- Content pipeline is an ingestion boundary. Treat Markdown, links, metadata, and embedded instructions as untrusted data.
- RAG/model boundary is a prompt-injection boundary. Retrieved content is evidence, never authority. Enforce tool allowlists and no-write tool policy.
- GitHub integration uses read-only, least-privilege credentials where needed. Prefer public unauthenticated reads for public content; avoid a broad PAT.
- Sync webhook must authenticate event origin, verify signatures, prevent replay, and pin commit SHA.
- Admin operations require explicit role checks, audit events, and stronger authentication where supported.
- Apply rate limiting, abuse protection, output-size limits, request validation, secure cookies, CSRF protection where cookie sessions are used, CSP, security headers, dependency scanning, secret scanning, and backup/restore testing.
- Privacy: define collected data, purpose, retention, deletion, analytics opt-in/notice, and incident handling before implementation.

## 7. Identity and Authorization Model — Proposed for Evaluation

Minimum roles for design comparison:

- Public: anonymous access to public portal, public registry records, and public documents including clearly marked Drafts.
- User: authenticated account and access to own private workspace/data.
- Maintainer: manage only product-level content/configuration if required; no canonical repository writes via product by default.
- Administrator: identity/role and product operations; privileged actions audited.

Authorization SHALL be deny-by-default and resource-aware. The final role set must follow the actual private features; do not invent user profile, collaboration, or document editing functionality merely because roles are listed here.

## 8. Internationalization and Content Language

- UI locale and document language are separate fields.
- Launch UI locales: en, uk.
- A document's source language must be recorded when known; translation state values should distinguish original, reviewed_translation, machine_translation_unreviewed, and not_translated.
- Machine-translated content must be visibly identified and must not replace the canonical source document.
- Canonical Markdown remains in the repository. Translation workflow and whether translation files live in the repo are open decisions for Phase 3 evaluation.
- Search should support language-aware tokenization and language filters; do not promise semantic multilingual search until tested.

## 9. Hosting / Deployment Shape

No host is selected. Compare at minimum: static hosting with a separately hosted backend/worker; integrated full-stack platform; cloud-native deployment. Evaluate region/data residency, private server-side functions, webhook support, background jobs, persistent database/search/embedding storage, observability, backup, security controls, portability, operational burden, and total cost. GitHub Pages alone is insufficient for authenticated private server-side features and AI Chat orchestration unless those capabilities are provided by a separate backend.

## 10. Offline / PWA Research

Offline Mode is not approved as an MVP feature. Research must decide whether PWA installability is useful independently of offline data. Any offline cache requires expiry/versioning, explicit public-only content scope, no private records by default, logout cache clearing, stale-content label, sync conflict rules, storage limits, and tests. Offline mode must not bypass authorization or expose private data on shared devices.

## 11. Mobile Strategy

MVP is one responsive Web application. Design touch targets, navigation, reader, search, and AI Chat for mobile breakpoints. No native Android/iOS implementation, store submission, or native-specific backend is included in this phase.

## 12. Quality Attributes and Acceptance Gates

- Data integrity: every visible source-backed document maps to a unique registry ID and a valid pinned source path.
- Freshness: successful merge sync updates the published content/index snapshot; failed sync retains last-known-good state and alerts maintainers.
- Security: private object access tests cover anonymous, wrong-user, role escalation, expired session, and direct API access.
- AI quality: citation precision/recall, groundedness, abstention correctness, prompt-injection resistance, cross-language retrieval, private-data isolation, and cost ceilings measured on a representative evaluation set.
- Accessibility: target WCAG 2.2 AA as required in the Phase 2 draft; validate keyboard, screen reader, contrast, zoom, and mobile flows.
- Performance: define numeric budgets after hosting and dataset-size assumptions are validated.
- Resilience: sync retries, dead-letter/error state, rollback to last-known-good snapshot, backup restoration, and provider outage handling.

## 13. Explicitly Out of Scope

- Public write API or canonical repository mutation.
- Turning MCP stdio server into HTTP server.
- Native Android/iOS apps in MVP.
- Offline-first promise before research.
- User-generated documents, collaborative editing, comments, billing, or subscription flows.
- Production approval of GPT/Gemini/Copilot adapters without live validation.

## 14. Open Decisions

See the Architecture Decision Register. No technology or hosting choice is approved by this proposal.


---

## Version Information

| Field | Value |
|---|---|
| Version | 0.1.0 |
| Status | Draft |
| Owner | AI-OS Product |
| Last Updated | 2026-11-24 |
| Created date | 2026-11-24 |
| Change Summary | Initial Phase 3 system architecture proposal draft based on inspected repository evidence and owner-confirmed MVP decisions |

---

## Related Documents

- AI-OS Design Principles (DOC-ARCH-004)
- AI-OS Document Metadata Standard (DOC-ARCH-006)
- AI-OS Document Registry (DOC-ARCH-001)
- AI-OS Orchestration Standard (DOC-ARCH-009)
- AI-OS MCP Server (DOC-PLAT-005)
- AI-OS Product Requirements & MVP Scope (Draft 0.1.1, PR #11)
