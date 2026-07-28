# MCP Publication Kit — AI-OS Documentation Server

Working note (Archival tier, not an official document). Everything the owner
needs to list the server in MCP catalogues: exact steps, and copy-paste texts.

Server: `io.github.asskergarry/ai-operating-architecture-standard`
Package: `aios-mcp-server` (PyPI) · Manifest: `server.json` (repo root)

---

## Part 1 — Owner steps, in order

### Step 1. Publish the package to PyPI (~10 min, once)

The package needs to exist before the registry can reference it.

```bash
# from the repository root
python3 -m pip install --upgrade build twine
python3 -m build                      # produces dist/aios_mcp_server-1.1.0*
python3 -m twine upload dist/*        # asks for a PyPI API token
```

Account: https://pypi.org/account/register/ → then
**Account settings → API tokens → Add API token** (scope: entire account for
the first upload). Username at the prompt is `__token__`, password is the token.

Verify afterwards: `uvx aios-mcp-server --help` should run from a clean machine.

### Step 2. Publish to the official MCP registry (~5 min)

```bash
# install the publisher CLI
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m).tar.gz" | tar xz mcp-publisher

./mcp-publisher login github        # opens a browser, proves you own the namespace
./mcp-publisher publish             # reads server.json from the current directory
```

The namespace `io.github.asskergarry/...` is verified through the GitHub login —
this is why the server name must keep that prefix.

Listing appears at https://registry.modelcontextprotocol.io/ within minutes.

### Step 3. Third-party catalogues (~15 min, optional but worth it)

| Catalogue | How | Notes |
| --------- | --- | ----- |
| **Smithery** (smithery.ai) | Sign in with GitHub → "Add server" → point at the repo | Picks up `server.json` automatically |
| **mcp.so** | Submit form on the site with the repo URL | Human-reviewed, usually a day |
| **awesome-mcp-servers** (GitHub) | Pull request adding one line to the list | Highest-traffic list; see the format below |

`awesome-mcp-servers` line (category: *Knowledge & Memory* or *Developer Tools*):

```markdown
- [AI-OS Documentation Server](https://github.com/ASskerGarry/AI-Operating-Architecture-Standard) - Serves a governed documentation deployment (registry, capability and execution modules) to any MCP client on demand. Zero dependencies, read-only, sandboxed paths.
```

---

## Part 2 — Copy-paste listing texts

### Short description (one line, ≤ 160 chars)

> Read-only MCP access to an AI-OS governed documentation deployment: registry index, module lookup by ID, and full-text search. Zero dependencies.

### Medium description (catalogue card, ~60 words)

> The AI-OS Documentation Server exposes a governed documentation set to any
> MCP client through three read-only tools: `list_documents` (live registry
> index, filterable by layer and status), `get_document` (fetch by Document ID
> or path) and `search_documents` (keyword search). The model pulls governance
> content when a task needs it instead of carrying it in the context window.

### Long description (README / registry detail page)

> **What it does.** AI-OS is a layered, platform-agnostic standard for
> operating AI assistants as governed systems — a document registry with
> immutable IDs, capability modules (domain expertise), execution modules
> (reusable processes), a memory model and platform adapters. This server makes
> that content available to a model *on demand*: instead of pasting the whole
> corpus into a system prompt, the client keeps three tool descriptions in
> context and fetches only what the current task requires.
>
> **Tools.** `list_documents(layer?, status?)` returns the registry index with
> ID, title, layer, category, status, version and location.
> `get_document(id | path)` returns one document's full text.
> `search_documents(query)` returns matching files with matching lines.
>
> **Security posture.** There is no write surface: no tool mutates anything, so
> a compromised or confused client cannot write through this server. Every path
> is resolved with `realpath` and must stay inside the served root; only
> markdown files in the official document scope are returned — traversal,
> non-markdown files and out-of-scope directories are refused. The transport is
> stdio only, so nothing listens on the network. A Dockerfile is included for
> running it as a non-root user with a read-only mount and `--network none`.
>
> **Dependencies: none.** The server is standard-library Python, which keeps
> its supply-chain surface at zero — a deliberate choice given the 2026 audits
> of MCP stdio servers.

### Client configuration snippet (for any catalogue that asks)

```json
{
  "mcpServers": {
    "aios": {
      "command": "uvx",
      "args": ["aios-mcp-server"],
      "env": { "AIOS_ROOT": "/path/to/AI-Operating-Architecture-Standard" }
    }
  }
}
```

---

## Part 3 — What to expect

Honest expectations, so the result can be judged against them:

- **Discovery, not adoption.** A listing brings visits and occasional installs;
  it does not by itself produce users of the AI-OS standard. Treat installs as
  the top of the funnel.
- **Realistic first month:** tens of registry views, single-digit installs.
  Growth comes from the catalogue plus a written case study, not the catalogue
  alone.
- **Signal to watch:** GitHub traffic (Insights → Traffic) and stars in the
  week after listing. If listing produces visits but no stars, the README's
  first screen is the thing to fix — not the server.

---

## Part 4 — Maintenance contract

When the server changes:

1. Bump the version in **three** places, they must agree:
   `pyproject.toml`, `server.json`, and DOC-PLAT-005's metadata.
2. Rebuild and re-upload to PyPI, then `./mcp-publisher publish` again.
3. Log the change in `Change_Log_day.md` (log-first) and keep the registry row
   for DOC-PLAT-005 in sync — the structural gate now enforces version
   consistency (C11–C14).
