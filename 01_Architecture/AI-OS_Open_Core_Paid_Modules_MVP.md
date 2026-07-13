# AI-OS Open-Core Paid Modules MVP

Version: 1.0.0
Status: Draft
Layer: Architecture
Document Type: Specification
Document ID: DOC-ARCH-010
Owner: AI-OS Architecture

---

## Purpose

This specification defines the first commercial MVP for AI-OS paid capability modules.

It sets explicit scope boundaries, deliverables, acceptance criteria, and rollout sequencing for two launch packs:

1. Governance Pack;
2. PromptOps Pack.

---

## Scope

Included:

- MVP composition of Governance Pack and PromptOps Pack;
- deliverables required for each pack at v1.0;
- acceptance criteria for pilot readiness;
- package-level rollout and upgrade policy.

Excluded:

- pricing and contract terms;
- platform adapter internals;
- managed-service operating procedures.

---

## 1. Product Boundary

Open Core remains free and adoption-oriented.

Paid modules SHALL provide value through:

- enterprise governance depth;
- operational reliability;
- faster deployment with standardized artifacts.

Paid modules SHALL NOT duplicate baseline Open Core content verbatim.

---

## 2. Governance Pack (MVP v1.0)

### 2.1 Objective

Provide a reusable governance control layer for teams running AI-OS in production-like environments.

### 2.2 Required Deliverables

1. Governance control matrix (policy -> control -> evidence mapping).
2. Architecture review checklist with pass/fail criteria.
3. Documentation quality gate template for release readiness.
4. Risk register template for AI workflow changes.
5. Monthly governance review cadence template.

### 2.3 Acceptance Criteria

- A pilot team can execute one end-to-end governance review without creating custom templates.
- Control matrix covers at least quality, traceability, and change governance.
- Review outcomes are reproducible between two independent reviewers.

---

## 3. PromptOps Pack (MVP v1.0)

### 3.1 Objective

Provide a repeatable lifecycle for prompt assets from design to release monitoring.

### 3.2 Required Deliverables

1. Prompt lifecycle workflow (draft -> review -> release -> monitor).
2. Prompt test matrix template (functional, edge-case, adversarial checks).
3. Output contract template (schema-first integration mode).
4. Prompt change log format with impact tracking.
5. Regression checklist for prompt updates.

### 3.3 Acceptance Criteria

- A pilot team can ship one prompt release using only pack-provided artifacts.
- Regression checks detect at least one synthetic failure case before release.
- Prompt changes are traceable by version, reason, and impact.

---

## 4. Packaging and Delivery Model

| Package | Delivery Unit | Primary Buyer Value |
| ------- | ------------- | ------------------- |
| Governance Pack | Templates + governance workflows | Compliance confidence and release quality control |
| PromptOps Pack | Templates + lifecycle workflows | Faster, safer prompt releases |

Delivery rules:

1. Each pack SHALL include a minimum onboarding guide.
2. Each pack SHALL include one pilot execution example.
3. Each pack SHOULD be deployable independently.

---

## 5. Rollout Sequence

1. Pilot with Governance Pack first when compliance pressure is high.
2. Pilot with PromptOps Pack first when release velocity is the primary blocker.
3. Offer combined deployment when both governance and release reliability are required.

---

## 6. KPI Baseline for MVP

| KPI | Target for MVP |
| --- | -------------- |
| Pilot completion rate | >= 80% |
| Artifact reuse rate | >= 60% |
| Time to first governed release | <= 14 days |
| Detected pre-release defects | Increasing trend during early pilots |

---

## 7. Upgrade Path (Post-MVP)

After MVP validation, expansion MAY include:

- Security and Compliance Pack;
- Orchestration Pack;
- cross-pack analytics dashboard.

Any expansion SHALL preserve Open Core boundary discipline.

---

## Version Information

| Field          | Value |
| -------------- | ----- |
| Version        | 1.0.0 |
| Status         | Draft |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14 |
| Created date   | 2026-07-14 |
| Change Summary | Initial MVP specification for paid Open-Core capability modules |

---

## Related Documents

- AI-OS Document Registry
- AI-OS Open-Core Commercial Blueprint
- AI-OS Open-Core 90-Day Roadmap
- Capability Registry
- AI-OS Design Principles
