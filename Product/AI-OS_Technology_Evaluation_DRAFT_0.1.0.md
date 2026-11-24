# AI-OS — Technology Evaluation

Document ID: TBD — Draft product working document; not an official AI-OS standard  
Version: 0.1.0  
Status: Draft  
Layer: Product Specification (proposed; mapping to the canonical AI-OS layer requires owner approval)  
Document Type: Specification (proposed)  
Owner: AI-OS Product  
Last Updated: 2026-11-24

---

## 1. Purpose

Record a transparent technology evaluation plan for the AI-OS Digital Product. This document separates repository evidence from candidate options and records criteria before selecting a stack. All comparisons are preliminary; current vendor capabilities/prices must be re-verified before a final decision.

## 2. Constraints from the Source Repository and Product Scope

- Existing public site: static HTML/CSS/JavaScript under docs/; no package manifest or frontend build tool was found at docs/package.json.
- Backend, authentication service, persistent product database, HTTP API, and AI Chat are not evidenced as implemented in the inspected tree.
- Content source: GitHub Markdown and 01_Architecture/AI-OS_Document_Registry.md, with existing read-only stdio MCP server.
- Existing utilities are Python standard-library scripts and GitHub Actions workflows.
- Product scope requires both public anonymous access and authenticated private features.
- AI Chat must be included in MVP and must not acquire repository write capabilities.
- Bilingual UI is required; translation strategy remains open.
- After-merge content refresh is required.
- Hosting is explicitly undecided by owner.

## 3. Evaluation Criteria and Weighting Proposal

Scores use 1 (poor) to 5 (strong). Proposed weights are an evaluation aid, not an approved business priority:

| Criterion | Weight | What to verify |
|---|---:|---|
| Security and private-feature fit | 18% | Server-side authorization, session security, secret management, webhook verification |
| Content sync and background jobs | 15% | Merge triggers, retries, atomic publish, scheduled repair/reindex |
| AI/RAG integration | 14% | Provider abstraction, streaming, retrieval, observability, budget controls |
| Operations and deployment | 12% | Monitoring, backups, rollback, logs, deploy previews |
| Data and search support | 10% | Relational metadata, full-text/vector capability, migrations, consistency |
| Portability / lock-in | 9% | Export, standard interfaces, replaceable services |
| Bilingual/mobile Web delivery | 8% | i18n tooling, responsive delivery, caching strategy |
| Cost transparency | 7% | Free-tier assumptions, usage metering, predictable spend |
| Developer experience | 7% | Type safety, testing, docs, CI integration |

## 4. Hosting / Platform Patterns to Compare

### Option H1 — Static frontend + separately hosted application backend

Frontend remains statically deployable (potentially GitHub Pages or equivalent). Backend provides auth/session, private features, AI Chat, webhooks, and content APIs. Background sync may be a worker/serverless job. Strengths: separation, static delivery, ability to keep public pages CDN-backed. Risks: multiple services, CORS/session complexity, operational split, preview environment coordination.

### Option H2 — Integrated full-stack hosting platform

Single platform hosts frontend, server-side routes/functions, database integration, background/event jobs, and preview deployments. Strengths: fewer moving parts and tight deploy integration. Risks: vendor coupling, limits on execution duration/background processing, region and data residency constraints, pricing growth.

### Option H3 — Cloud-native container/service deployment

Containerized frontend/backend/worker deployed to a general cloud runtime with managed database and object storage. Strengths: maximum control and portability. Risks: highest operational burden, infrastructure/security work, monitoring/backup responsibility.

### Option H4 — Self-hosted / VPS

A small number of services on a managed VPS/container host. Strengths: low fixed cost and control. Risks: operational responsibility, patching, backup/restore, availability, scaling and secrets management.

No option is selected here.

## 5. Application Stack Candidates

| Layer | Candidate families | Evaluation notes |
|---|---|---|
| Frontend | React + TypeScript framework; Vue + TypeScript; retain static vanilla site with gradual enhancement | Compare routing, SSR/SEO, accessibility, Markdown rendering, i18n, mature testing, contributor learning curve. |
| Backend | TypeScript server framework/BFF; Python FastAPI service; platform-native server functions | Python aligns with existing repo scripts; TypeScript may share types with Web client. Choose based on async jobs, AI SDK integration, auth, operational fit. |
| Database | PostgreSQL; managed relational database; SQLite only for local/prototype use | Private user data, roles, sync metadata, audit records need durable transactional storage. SQLite is not presumed suitable for multi-instance production. |
| Search | PostgreSQL full-text first; dedicated search service if corpus/relevance needs justify it | Document ID/title exact search and layer/status filters are initial musts; advanced semantic search is later. |
| Vector retrieval | pgvector or managed vector search | Evaluate metadata filters, hybrid retrieval, language performance, backup, cost and isolation. Do not select before RAG benchmark. |
| Authentication | Managed OIDC provider / platform auth / self-managed OIDC | Compare provider lock-in, Ukrainian availability, MFA, account lifecycle, sessions, roles, data location and pricing. |
| AI model access | Provider abstraction layer with one initial production provider and evaluation harness | GPT/Gemini adapter documents are Draft; do not assume their claims are validated. Include timeouts, retries, streaming, token budgets, and redaction. |
| Content ingestion | GitHub Actions event + authenticated sync endpoint/worker; scheduled reconciliation | Pin commit SHA, verify events, idempotency, atomic snapshot, last-known-good rollback. |
| Markdown | Strict Markdown parser + sanitized HTML allowlist | Disable raw HTML by default; prevent XSS, unsafe links and script execution. |
| Deployment | H1–H4 | Select after cost, auth, background jobs, region and security comparison. |

## 6. Preliminary Recommendation (Not Approved)

Use a modular Web-first application with a separately enforceable backend boundary, relational source/read-model metadata, a deterministic GitHub-merge content pipeline, and an AI Chat service separated from content ingestion. Prefer a portable interface around the LLM provider and retrieval engine. Do not expose the existing MCP server over HTTP.

A credible first comparison shortlist is:

- TypeScript Web + BFF on an integrated platform;
- TypeScript Web + Python API/worker on managed container hosting;
- Static Web + separately hosted Python/TypeScript backend.

This is a shortlist for evidence gathering, not a final stack selection.

## 7. Required Technical Spikes

1. Content ingestion: fetch a pinned GitHub commit, parse registry rows, validate document metadata and generate a snapshot.
2. Search: exact Document ID/title plus layer/status filtering, with EN/UK examples.
3. Markdown security: adversarial raw HTML, javascript links, SVG, image URLs, and deeply nested Markdown test corpus.
4. Private access: prototype one resource and prove server-side deny-by-default enforcement across public and authenticated identities.
5. AI Chat: retrieval over a small source corpus, citations resolved only from retrieved chunks, abstention on insufficient evidence, injection test, language routing.
6. Merge update: signed event verification, duplicate event delivery, worker retry, failed build, atomic snapshot switch, stale status.
7. Cost/latency: record p50/p95, tokens per answer, index cost, sync duration, and estimated monthly cost under explicit traffic scenarios.
8. Backup/restore and observability: prove that state can be restored and sync/AI errors are visible without logging unnecessary personal data.

## 8. Evaluation Protocol

- Fix the acceptance scenarios and weights before scoring.
- Run technical spikes against the same dataset and cases.
- Record date, versions, assumptions, evidence, costs, and known limitations.
- Do not score a capability based only on marketing copy.
- Distinguish public product features from features available only on paid plans or selected regions.
- Re-run evaluation at decision time; prices and vendor capabilities may change.

## 9. Decision Gate

No technology is selected until the Architecture Decision Register marks the decision proposed with evidence and the owner explicitly approves it. Phase 3 completion requires a coherent architecture, justified stack selection, security/privacy model, content sync design, AI/RAG design, hosting recommendation, and validation evidence.


---

## Version Information

| Field | Value |
|---|---|
| Version | 0.1.0 |
| Status | Draft |
| Owner | AI-OS Product |
| Last Updated | 2026-11-24 |
| Created date | 2026-11-24 |
| Change Summary | Initial Phase 3 technology evaluation draft based on inspected repository evidence and owner-confirmed MVP decisions |

---

## Related Documents

- AI-OS Design Principles (DOC-ARCH-004)
- AI-OS Document Metadata Standard (DOC-ARCH-006)
- AI-OS Document Registry (DOC-ARCH-001)
- AI-OS Orchestration Standard (DOC-ARCH-009)
- AI-OS MCP Server (DOC-PLAT-005)
- AI-OS Product Requirements & MVP Scope (Draft 0.1.1, PR #11)
