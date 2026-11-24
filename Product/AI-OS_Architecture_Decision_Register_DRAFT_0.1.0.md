# AI-OS — Architecture Decision Register

Document ID: TBD — Draft product working document; not an official AI-OS standard  
Version: 0.1.0  
Status: Draft  
Layer: Product Specification (proposed; mapping to the canonical AI-OS layer requires owner approval)  
Document Type: Specification (proposed)  
Owner: AI-OS Product  
Last Updated: 2026-11-24

---

## 1. Purpose

This register tracks Phase 3 architecture decisions. Proposed means analysis is available but not approved. Accepted requires explicit owner approval and supporting evidence. Rejected records a considered option that will not be used. No entry authorizes implementation unless the owner separately approves the implementation phase.

## 2. Status Vocabulary

| Status | Meaning |
|---|---|
| open | No recommendation yet |
| proposed | Recommendation prepared; awaiting evidence or owner approval |
| accepted | Explicitly approved by product owner |
| rejected | Considered and not selected |
| deferred | Intentionally moved to a later phase |

## 3. Decision Register

| ID | Decision | Current status | Options / evidence needed | Proposed direction | Approval |
|---|---|---|---|---|---|
| ADR-P3-001 | Application architecture | proposed | Static + BFF; integrated full-stack; cloud-native. Verify private server-side auth, SSR/SEO, sync worker, ops. | Modular Web app + distinct backend boundary; retain portability. | Pending |
| ADR-P3-002 | Frontend stack | open | TypeScript React framework vs Vue vs static enhancement; benchmark i18n, Markdown, accessibility, tests. | Select after a proof-of-concept against the actual user journeys. | Pending |
| ADR-P3-003 | Backend/API | proposed | TypeScript BFF vs Python API vs platform functions. Test auth, streaming AI, worker and webhooks. | Product API is separate from stdio MCP server. | Pending |
| ADR-P3-004 | Primary database | open | PostgreSQL/managed relational vs alternatives; test user private data, sync state, audit, backup. | Relational store likely; no provider selected. | Pending |
| ADR-P3-005 | Search | proposed | Relational full-text vs dedicated search; corpus scale and EN/UK accuracy. | Begin with deterministic ID/title + filters; benchmark before semantic search. | Pending |
| ADR-P3-006 | Vector retrieval / RAG | open | pgvector vs managed vector; compare hybrid retrieval, language, metadata filters, cost and isolation. | Do not select before representative retrieval evaluation. | Pending |
| ADR-P3-007 | Authentication | open | Managed OIDC, platform auth, self-managed. Compare MFA, roles, session model, privacy, region and cost. | OIDC-compatible interface with server-side authorization. | Pending |
| ADR-P3-008 | Authorization / private features | proposed | Actual feature inventory and resource ownership. | Deny-by-default public/user/maintainer/admin boundaries; define only roles needed. | Pending |
| ADR-P3-009 | AI model provider | open | Candidate providers and models; benchmark quality, citations, cost, privacy, streaming, data controls. | Provider abstraction; pick one initial deployment after evaluation. | Pending |
| ADR-P3-010 | AI Chat safety | proposed | Retrieval-only vs tool-enabled designs; prompt-injection, citation-validation, abstention tests. | Retrieval-only, no write/execute tools, source content treated as untrusted data. | Pending |
| ADR-P3-011 | Content sync trigger | proposed | GitHub webhook vs GitHub Actions dispatch vs scheduled poll; verify auth, replay, retries, idempotency. | Canonical merge triggers pinned-SHA sync plus scheduled reconciliation. | Pending |
| ADR-P3-012 | Content data model | proposed | Registry rows + file body, translation state, access classification, commit provenance. | Derived immutable/versioned read model; repository remains SSOT. | Pending |
| ADR-P3-013 | Hosting | open | H1 static+backend, H2 integrated, H3 cloud-native, H4 VPS. Score region, jobs, privacy, cost, ops. | No provider chosen until comparison. | Pending |
| ADR-P3-014 | Internationalization | proposed | UI translation vs source document translations; reviewed vs machine translation. | Separate UI locale from document language and translation status. | Pending |
| ADR-P3-015 | Offline / PWA | deferred | Evaluate installability, offline public corpus, cache invalidation, shared-device privacy. | No offline MVP promise. Research only. | Pending |
| ADR-P3-016 | Native Android/iOS | deferred | Validate demand and reuse after Web MVP. | Later phase only. | Pending |
| ADR-P3-017 | Observability / operations | proposed | Logs/metrics/traces, alerting, backup, restore, rollback, cost budgets. | Define operational SLOs and data-minimizing telemetry before implementation. | Pending |
| ADR-P3-018 | Product data privacy | open | Data inventory, purpose, retention, deletion, analytics, consent/notice, region. | Minimize collection; no conversation retention by default until approved. | Pending |

## 4. Blocking Questions for Product Owner

1. What exact private features must exist in MVP? The Phase 2 draft says private features are required but does not specify the feature inventory.
2. Are private features user-owned workspaces/preferences, or do they include team/project collaboration? Collaboration is currently excluded by Phase 2.
3. Is account creation self-service or invitation-only for the MVP?
4. Should AI Chat be anonymous for public documents, or require sign-in? Phase 2 requires the portal to be public but does not settle AI Chat access policy.
5. Is conversation history required? Phase 2 does not define persistence; privacy baseline recommends minimum retention.
6. May users submit private documents to AI Chat in the MVP, or is retrieval restricted to public AI-OS repository content?
7. Who reviews and approves Ukrainian translations of canonical documents?

These are unresolved requirements, not inferred owner decisions.

## 5. Exit Criteria

- Every selected component has evidence, trade-off, operational responsibility, and cost assumption.
- Trust boundaries and role enforcement are defined.
- Sync architecture demonstrates idempotency, failure handling and last-known-good publish.
- AI Chat meets grounding/citation/abstention/injection/privacy gates on a fixed evaluation set.
- Hosting and deployment path supports required auth, jobs, storage, monitoring and backup.
- Product owner explicitly accepts all decisions marked accepted.
- All unresolved risks are either mitigated or explicitly accepted/deferred.


---

## Version Information

| Field | Value |
|---|---|
| Version | 0.1.0 |
| Status | Draft |
| Owner | AI-OS Product |
| Last Updated | 2026-11-24 |
| Created date | 2026-11-24 |
| Change Summary | Initial Phase 3 architecture decision register draft based on inspected repository evidence and owner-confirmed MVP decisions |

---

## Related Documents

- AI-OS Design Principles (DOC-ARCH-004)
- AI-OS Document Metadata Standard (DOC-ARCH-006)
- AI-OS Document Registry (DOC-ARCH-001)
- AI-OS Orchestration Standard (DOC-ARCH-009)
- AI-OS MCP Server (DOC-PLAT-005)
- AI-OS Product Requirements & MVP Scope (Draft 0.1.1, PR #11)
