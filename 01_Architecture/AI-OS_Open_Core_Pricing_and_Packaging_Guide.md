# AI-OS Open-Core Pricing and Packaging Guide

Version: 1.0.0
Status: Draft
Layer: Architecture
Document Type: Guide
Document ID: DOC-ARCH-012
Owner: AI-OS Architecture

---

## Purpose

This guide defines the commercial packaging and pricing logic for AI-OS Open-Core offerings.

It establishes clear offer tiers, value boundaries, and buying paths so prospects can move predictably from Open Core usage into paid modules and services.

---

## Scope

Included:

- package structure and tier definitions;
- pricing logic and value metrics;
- upgrade and expansion path between offers.

Excluded:

- legal terms and commercial contract wording;
- region-specific tax treatment;
- discount approval workflow details.

---

## 1. Packaging Model

| Package | Access | Core Value | Typical Buyer |
| ------- | ------ | ---------- | ------------- |
| Open Core | Free | Standards and baseline framework adoption | Builders and early evaluators |
| Governance Pack | Paid | Governance controls and quality assurance | Teams with compliance and reliability requirements |
| PromptOps Pack | Paid | Prompt lifecycle and release reliability | Teams with high prompt iteration velocity |
| Combined Pack | Paid | Governance + PromptOps operating model | Teams scaling to production |
| Diagnostic Service | Paid | Entry assessment and adoption roadmap | Teams needing architecture clarity before rollout |

---

## 2. Pricing Logic

Pricing SHOULD follow value-based tiers, not token-based consumption.

Recommended pricing dimensions:

1. organizational scope (team, department, multi-team);
2. governance depth (baseline, advanced, enterprise);
3. support intensity (self-serve, guided, managed).

Pricing SHALL remain simple enough for first-call qualification.

---

## 3. Commercial Tiers

| Tier | Offer Composition | Positioning |
| ---- | ----------------- | ----------- |
| Entry | Diagnostic Service + one pack | Fast path to first governed release |
| Growth | Governance Pack + PromptOps Pack | Repeatable cross-team delivery model |
| Scale | Combined Pack + advisory cadence | Enterprise operating layer for AI workflows |

---

## 4. Upgrade Path

1. Open Core adoption.
2. Diagnostic Service.
3. First paid pack (Governance or PromptOps).
4. Combined Pack.
5. Optional advisory retainer.

Each upgrade step SHALL provide measurable incremental value.

---

## 5. Packaging Rules

- Paid offers SHALL not duplicate Open Core baseline artifacts without additional operational depth.
- Each paid package SHALL include onboarding, template set, and rollout checklist.
- Combined Pack SHALL include a unified KPI scorecard.

---

## 6. KPI for Pricing and Packaging

| KPI | Target |
| --- | ------ |
| Diagnostic-to-paid conversion | >= 30% |
| First pack expansion to second pack | >= 40% |
| Time from first call to commercial decision | <= 21 days |

---

## Version Information

| Field          | Value |
| -------------- | ----- |
| Version        | 1.0.0 |
| Status         | Draft |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14 |
| Created date   | 2026-07-14 |
| Change Summary | Initial pricing and packaging guide for AI-OS Open-Core offers |

---

## Related Documents

- AI-OS Document Registry
- AI-OS Open-Core Commercial Blueprint
- AI-OS Open-Core Paid Modules MVP
- AI-OS Open-Core Diagnostic Service Specification

