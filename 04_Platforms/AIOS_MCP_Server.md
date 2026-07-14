# AI-OS MCP Server

Document ID: DOC-PLAT-005
Version: 1.0.0
Status: Active
Layer: Platform
Document Type: Platform Asset
Owner: AI-OS Architecture

---

# Purpose

Define the AI-OS Model Context Protocol (MCP) server — the first executable
integration layer of AI-OS. It lets any MCP-capable AI client (Claude Desktop,
Claude Code, other MCP hosts) pull the official AI-OS documents **on demand
through tool calls**, instead of carrying the Document Registry, capability
specifications and process definitions statically in the model's context
window.

This implements the dynamic tool-calling pattern: the model keeps only a
three-tool description in context (~a few hundred tokens) and fetches
registry rows, Capability Modules or Execution Modules only when a task
actually needs them (DP-002 Separation of Concerns, DP-009 Platform Agnostic
Design — the served content stays platform-neutral; only this access layer is
platform-facing).

# Scope

- Implementation: `Knowledge_Base/aios_mcp_server.py` (Python 3, standard
  library only — no third-party dependencies, no supply-chain surface).
- Transport: stdio (newline-delimited JSON-RPC 2.0), MCP protocol version
  `2025-06-18`.
- Content served: official AI-OS markdown documents only — the same scope the
  compliance validator enforces (`Knowledge_Base/`, `Archive/` and
  dot-directories are excluded per DOC-ARCH-006).

# Tools

| Tool | Arguments | Returns |
| ---- | --------- | ------- |
| `list_documents` | `layer?`, `status?` | Live Document Registry index: ID, title, layer, category, status, version, location |
| `get_document` | `id` (Document ID) or `path` (repo-relative `.md`) | Full text of one official document |
| `search_documents` | `query` | Official files containing the query, with matching lines |

All tools are **read-only**. The server exposes no write, delete, or execute
surface by design.

# Security Model

Per the 2026 MCP stdio-transport risk analysis (unauthenticated stdio servers
exposed as command processors), this server applies defense in depth:

1. **Read-only by construction** — there is no tool that mutates state; a
   compromised or confused client cannot write through this server.
2. **Path sandbox** — every path is resolved with `realpath` and must stay
   inside the repository root; only `.md` files in the official scope are
   served. Traversal (`../`), non-markdown files and out-of-scope directories
   are refused.
3. **No network listener** — stdio only; the server is spawned by the client
   process and is not reachable from the network.
4. **Container isolation (recommended for shared hosts)** —
   `Knowledge_Base/Dockerfile.mcp` runs the server as a non-root user with a
   read-only repository mount and `--network none`:

   ```bash
   docker build -f Knowledge_Base/Dockerfile.mcp -t aios-mcp .
   docker run -i --rm --read-only --network none -v "$(pwd)":/repo:ro aios-mcp
   ```

Any future tool with a write surface MUST go through an explicit
human-confirmation gate and MUST NOT be added to this server (new Document ID,
separate review).

# Client Configuration

Claude Desktop / Claude Code (`.mcp.json` or `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "aios": {
      "command": "python3",
      "args": ["Knowledge_Base/aios_mcp_server.py", "/path/to/AI-OS"]
    }
  }
}
```

On Windows use `py` instead of `python3` if the `python` alias is not
configured.

# Validation

The server ships with an end-to-end protocol test (executed at acceptance):
initialize handshake, `tools/list`, all three tools against live repository
content, path-traversal refusal, out-of-scope refusal, unknown-ID and
unknown-method error handling — 9/9 checks passed on 2026-07-14.

# Relation to the Orchestration Standard

DOC-ARCH-009 (AI-OS Orchestration Standard) is Draft pending implementation
evidence (DP-015). This server is the first such evidence: it provides the
tool-access layer an Orchestrator needs to route Capability and Execution
content to Specialist agents without copying files by hand. Multi-agent
handoff itself remains out of this server's scope.

---

# Version Information

| Field          | Value              |
| -------------- | ------------------ |
| Version        | 1.0.0              |
| Status         | Active             |
| Owner          | AI-OS Architecture |
| Last Updated   | 2026-07-14         |
| Created date   | 2026-07-14         |
| Change Summary | Initial release: three read-only tools, sandboxed stdio server, container isolation guidance; 9/9 acceptance checks passed |

---

# Related Documents

- Platform Layer README (DOC-PLAT-001)
- Claude Adapter (DOC-PLAT-002)
- AI-OS Orchestration Standard (DOC-ARCH-009)
- AI-OS Document Metadata Standard (DOC-ARCH-006)
- Security Policy (DOC-CORE-007)
