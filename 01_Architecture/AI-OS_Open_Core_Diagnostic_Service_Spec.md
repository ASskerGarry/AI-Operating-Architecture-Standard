# AI-OS Open-Core Diagnostic Service Specification

Version: 1.0.0
Status: Draft
Layer: Architecture
Document Type: Specification
Document ID: DOC-ARCH-011
Owner: AI-OS Architecture

---

## Purpose

This document defines the AI-OS Diagnostic Service as the entry commercial offer for Open-Core adoption.

It standardizes service scope, delivery sequence, outputs, quality gates, and handoff logic into paid module deployment.

---

## Scope

Included:

- diagnostic engagement model (2-4 weeks);
- required inputs, execution stages, and output artifacts;
- acceptance criteria for completion;
- conversion path to Governance Pack and PromptOps Pack.

Excluded:

- implementation of full pack deployment;
- legal procurement and contract language;
- custom software development outside AI-OS artifact scope.

---

## 1. Service Objective

The Diagnostic Service SHALL provide a clear, evidence-based answer to:

1. current AI delivery maturity;
2. architecture and governance gaps;
3. prioritized path to first governed production release.

---

## 2. Engagement Structure

| Stage | Duration | Primary Output |
| ----- | -------- | -------------- |
| Discovery | Week 1 | Current-state map and constraints baseline |
| Assessment | Week 2 | Gap analysis and risk register |
| Recommendation | Week 3 | Target-state blueprint and rollout priorities |
| Handoff | Week 4 (optional) | Activation plan into paid modules |

---

## 3. Required Inputs

Client-side inputs:

- existing AI workflows and prompt assets;
- governance policies relevant to AI outputs;
- release process documentation;
- representative use cases and failure examples.

Provider-side inputs:

- AI-OS architecture standards;
- diagnostic checklist;
- scoring rubric and evidence model.

---

## 4. Required Deliverables

1. **Diagnostic Scorecard**
   - maturity scoring by domain: architecture, governance, prompt operations, release controls.
2. **Gap and Risk Register**
   - high-confidence issues with impact and urgency.
3. **Target-State Blueprint**
   - recommended AI-OS operating shape for the client.
4. **90-Day Activation Plan**
   - phased actions and measurable checkpoints.
5. **Commercial Handoff Recommendation**
   - suggested next paid pack: Governance Pack, PromptOps Pack, or combined rollout.

---

## 5. Acceptance Criteria

The diagnostic engagement is complete only when:

1. each major recommendation is linked to explicit evidence;
2. the client can identify the first 2-3 prioritized actions;
3. at least one conversion path to paid pack deployment is defined;
4. deliverables are reproducible by another reviewer using the same inputs.

---

## 6. Quality Gates

Before final handoff, the service SHALL pass:

- evidence traceability check;
- recommendation clarity check;
- non-duplication check versus Open Core baseline content;
- actionability check (owner, timeline, success measure).

---

## 7. Handoff Logic to Paid Packs

| Diagnostic Finding | Recommended Next Offer |
| ------------------ | ---------------------- |
| Weak review and control process | Governance Pack |
| Unstable prompt release lifecycle | PromptOps Pack |
| Both governance and release gaps | Combined Governance + PromptOps rollout |

The handoff SHALL include a minimum implementation outline and a first 30-day plan.

---

## 8. Service KPIs

| KPI | Target |
| --- | ------ |
| Diagnostic completion rate | >= 90% |
| Client action-plan acceptance | >= 80% |
| Diagnostic-to-paid conversion | >= 30% |
| Time to handoff decision | <= 5 business days after final readout |

---

## 9. Risks and Mitigation

| Risk | Mitigation |
| ---- | ---------- |
| Incomplete client inputs | Use intake checklist and evidence minimums before assessment |
| Overly generic recommendations | Require evidence-linked recommendations only |
| Low conversion despite diagnostic value | Add clearer economic impact framing in readout |

---

## Version Information

| Field          | Value |
| -------------- | ----- |
| Version        | 1.0.0 |
| Status         | Draft |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14 |
| Created date   | 2026-07-14 |
| Change Summary | Initial specification for AI-OS Open-Core diagnostic entry offer |

---

## Related Documents

- AI-OS Document Registry
- AI-OS Open-Core Commercial Blueprint
- AI-OS Open-Core 90-Day Roadmap
- AI-OS Open-Core Paid Modules MVP
- Capability Registry
