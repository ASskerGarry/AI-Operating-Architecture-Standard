# Prompt Engineering

Version: 1.1.0
Status: Draft
Layer: Capability
Document Type: Capability Module
Document ID: DOC-CAPA-011
Owner: AI-OS Architecture

---

## Module Metadata

| Field | Value |
| ----- | ----- |
| Module Name | Prompt Engineering |
| Module ID | DOC-CAPA-011 |
| Category | AI Engineering |
| Capability Domain | LLM prompt design and optimization |
| Version | 1.1.0 |
| Status | Draft |
| Owner | AI-OS Architecture |
| Role Eligibility | Independent / Primary / Secondary / Supporting |
| Recommended Partners | AI Strategy, Teaching |
| AI Platforms | All |
| Created | 2026-07-11 |
| Last Updated | 2026-07-14 |

---

## 1. Purpose

Provide professional expertise in designing, analyzing, and optimizing prompts and prompt-based systems for large language models, so that AI-OS can produce robust, reusable, and platform-portable prompt artifacts.

---

## 2. Scope

**Included:** prompt design and structure, system prompts, instruction hierarchies, role definition, few-shot examples, output formatting contracts, prompt evaluation criteria, modular prompt architecture, prompt debugging.

**Excluded:** model training/fine-tuning, platform deployment (Platform Layer), execution sequencing (Execution Layer), general software development (Python module).

---

## 3. Responsibilities

- Design prompts that are unambiguous, testable, and reusable.
- Diagnose why a prompt underperforms and identify the failure mode.
- Define measurable acceptance criteria for prompt outputs.
- Keep prompt artifacts modular and platform-independent (DP-009).

---

## 4. Core Expertise

- Instruction design: clarity, ordering, constraint specification, negative instructions.
- Context management: what to include, reference, or omit; context budget awareness.
- Output contracts: format specification, schemas, examples, edge-case behavior.
- Evaluation: criteria design, failure taxonomy (ambiguity, conflict, underspecification, overconstraint).
- Robustness: input variation, adversarial phrasing, graceful degradation.

---

## 5. Decision Framework

1. Identify the task type and the output contract first; structure follows.
2. Prefer the simplest prompt that reliably meets acceptance criteria (KISS).
3. Add examples only when instructions alone are insufficient.
4. Resolve conflicts by priority: correctness > robustness > brevity > style.
5. When a prompt grows past one responsibility, split it into modules (SoC).

---

## 6. Best Practices

- State the objective, audience, constraints, and output format explicitly.
- Separate stable identity content from task-specific content.
- Test with representative and boundary inputs before declaring done.
- Version prompts and record why each change was made.

---

## 7. Quality Standards

- Instructions are unambiguous: two competent readers derive the same expectation.
- Every requirement is verifiable against the produced output.
- No redundant or conflicting instructions.

---

## 8. Output Standards

Deliverables include: prompt text (marked code blocks), design rationale, assumptions, acceptance criteria, and known limitations. Findings reports follow the Analyze module output structure.

---

## 9. Constraints

- Does not guarantee model behavior — defines the highest-probability instruction set and validates empirically.
- Platform-specific syntax belongs to Platform Adapters, not to this module's artifacts.

---

## 10. Integration

- Activated by the Capability Registry; typically Primary for prompt-related requests.
- Feeds Execution Modules: Analyze Prompt, Generate Prompt, Validate Prompt, Optimize Prompt, Develop AI Assistant.
- Partners: AI Strategy (system-level design), Teaching (explanatory delivery).

---

## 11. Typical Execution Scenarios

User asks to improve a weak prompt → Registry activates Prompt Engineering (Primary) → Execution Registry selects Optimize Prompt → optimized prompt with rationale returned.

---

## 12. Examples

- Simple: rewrite a vague instruction into a testable one.
- Intermediate: design a system prompt with role, constraints, and output contract for a support assistant.
- Complex: decompose a monolithic prompt into a modular Core + Capability + Execution structure (AI-OS style).

---

## 13. Context Engineering Recommendations (2026)

1. **Evidence mode (required for governance-sensitive outputs).**
   - Prompt artifacts SHALL define source tiers: Tier 1 (official vendor docs/specs), Tier 2 (peer-reviewed or formal technical publications), Tier 3 (community/blog/forum content).
   - Normative claims MUST be justified by Tier 1 or Tier 2 sources.
   - Any unsupported claim SHALL be labeled as a hypothesis, not a fact.

2. **Platform profile blocks (for portability).**
   - Prompt artifacts SHOULD include a compact profile for Gemini, Claude, and NotebookLM.
   - Each profile SHALL define: allowed patterns, disallowed patterns, and default output mode (narrative vs schema-first).

3. **Reasoning policy (privacy and reliability).**
   - Prompts SHALL request concise rationale and verifiable steps, not unrestricted internal reasoning traces.
   - For reasoning-capable models, instructions SHOULD focus on task decomposition and acceptance checks rather than forcing explicit chain-of-thought output.

4. **Output contract hardening (integration-safe).**
   - Machine-consumed outputs MUST be schema-bound (JSON/XML/table contracts) with explicit required fields and value constraints.
   - Decorative wrappers and ambiguous dual formats (e.g., "table or list") SHALL be avoided in integration mode.

5. **Batch sizing heuristic (large-scale prompt operations).**
   - For large datasets, prompts SHOULD define batch size as a function of token budget and average item weight.
   - Recommended initial heuristic:
     - `batch_size = floor((token_budget * 0.35 - fixed_overhead_tokens) / (avg_item_tokens * 1.25))`
   - If `avg_item_tokens` is unknown, use conservative defaults and tune after the first batch.

6. **Promptware lifecycle gates (quality governance).**
   - Every substantial prompt update SHOULD pass requirements, design, testing, and monitoring gates.
   - Change records MUST include expected impact, known risks, and rollback guidance.

---

## 14. Review Status

| Field | Value |
| ----- | ----- |
| Review Date | — |
| Reviewer | — |
| Review Result | Pending |
| Open Issues | None recorded |

---

## 15. Change History

| Version | Date | Description |
| ------- | ---- | ----------- |
| 1.1.0 | 2026-07-14 | Added context-engineering recommendations: evidence mode, platform profiles, reasoning policy, output hardening, batch sizing heuristic, and lifecycle gates |
| 1.0.0 | 2026-07-11 | Initial version — module created per Capability Module Specification |

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.1.0              |
| Status         | Draft              |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-11         |
| Change Summary | Added 2026 context-engineering recommendation set for production prompt governance |

---

## Related Documents

- Capability Module Specification
- Capability Registry
- Capability Dependency Matrix
- Core Identity
- Core Execution Engine
