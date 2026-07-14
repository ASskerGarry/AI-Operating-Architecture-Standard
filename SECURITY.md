# Security Policy

Document ID: DOC-CORE-007
Version: 1.1.0
Status: Active
Layer: Core
Document Type: Standard
Owner: AI-OS Architecture

---

## Purpose

This policy defines what constitutes a security issue in the AI-OS repository, how to report one privately, and what response to expect. AI-OS is a documentation and prompt-architecture standard — its attack surface is different from executable software, and this policy is scoped accordingly.

---

## Supported Versions

Security reports are accepted against the current state of the default branch and the latest registered document versions (see the AI-OS Document Registry, DOC-ARCH-001). Superseded document versions and content under `Archive/` are not supported.

| Scope | Supported |
| ----- | --------- |
| Default branch (latest registry state) | ✅ |
| Archived / superseded document versions | ❌ |

---

## What Counts as a Security Issue Here

Because AI-OS artifacts are deployed into live AI systems (system prompts, Skills, `CLAUDE.md` instances), the following are treated as security vulnerabilities:

1. **Prompt-injection surface in Platform Assets** — content in a deployable asset (e.g. `04_Platforms/Claude/prompt-generator.skill.md`, `CLAUDE.md`) that could cause a deployed assistant to ignore its immutable rules, escalate access, or exfiltrate data when processing untrusted input.
2. **Sensitive-data leakage paths** — instructions or memory rules (Memory Architecture, DOC-MEM-002; change logs) that would cause credentials, personal data, or private document contents to be written into persistent artifacts.
3. **Unsafe operational defaults** — execution or adapter instructions that default to write/delete operations where the standard mandates read-only or confirmation gates (e.g. RP-006 Variant B situations).
4. **Governance-integrity issues** — flaws in the validator or CI gate that would let non-compliant or tampered official documents pass as authoritative.

Ordinary documentation errors (typos, broken links, outdated content) are **not** security issues — report them as regular GitHub issues.

---

## Reporting a Vulnerability

- **Preferred channel:** GitHub → repository **Security** tab → **Report a vulnerability** (private advisory). This keeps the report confidential until a fix is published.
- Include: the affected file(s) and Document ID(s), the deployment scenario (which platform/asset), a reproduction or concrete misuse example, and the impact you foresee.
- Do **not** open a public issue for an unfixed vulnerability in a deployable asset.

### What to Expect

| Stage | Target |
| ----- | ------ |
| Acknowledgement | within 7 days |
| Assessment (accepted / declined, with reasoning) | within 14 days |
| Fix for accepted reports | next change-set; logged in `Change_Log_day.md` and the affected document's Change History |

Accepted fixes follow the standard governance flow: log-first entry, version bump of the affected document, registry sync — so every security fix is traceable (DP-008).

---

## Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.1.0              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-10         |
| Change Summary | Replaced GitHub boilerplate with a real policy: AI-OS-specific threat scope, private reporting channel, response expectations; promoted to Active |

---

## Related Documents

- AI-OS Document Registry (DOC-ARCH-001)
- Memory Architecture (DOC-MEM-002)
- Claude Adapter (DOC-PLAT-002)
- AI-OS Reasoning Patterns (DOC-ARCH-008)
