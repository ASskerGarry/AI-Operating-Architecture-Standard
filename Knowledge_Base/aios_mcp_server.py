#!/usr/bin/env python3
"""
AI-OS MCP Server (DOC-PLAT-005)

A dependency-free Model Context Protocol server (stdio transport,
newline-delimited JSON-RPC 2.0) that exposes the official AI-OS documents
to AI clients as read-only tools, so a model pulls the registry, capability
and execution content on demand instead of carrying it statically in the
context window (token efficiency; DP-002, DP-009).

Tools (all read-only — this server has no write surface by design):
  list_documents    live Document Registry index, filterable by layer/status
  get_document      full text of one document by Document ID or repo path
  search_documents  keyword search across official markdown documents

Security posture (see 04_Platforms/AIOS_MCP_Server.md):
  - read-only: no tool mutates anything;
  - sandboxed: only .md files inside the repo root, official scope only
    (Knowledge_Base/, Archive/ and dot-directories are excluded — same
    scope rules as validate_aios.py, per DOC-ARCH-006);
  - containerizable: run via Dockerfile.mcp (non-root, read-only mount).

Usage:  python3 Knowledge_Base/aios_mcp_server.py [repo_root]
"""
import json
import os
import re
import sys

ROOT = os.path.realpath(sys.argv[1] if len(sys.argv) > 1
                        else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SKIP_PREFIXES = ("Knowledge_Base", "Archive")
PROTOCOL_VERSION = "2025-06-18"
SERVER_INFO = {"name": "aios-mcp-server", "version": "1.0.0"}
REGISTRY_PATH = "01_Architecture/AI-OS_Document_Registry.md"


# --- official-scope filesystem access (mirrors validate_aios.py scope) ------

def in_scope(rel):
    """True if a repo-relative path belongs to the official document scope."""
    parts = rel.replace("\\", "/").split("/")
    if any(p.startswith(".") for p in parts if p):
        return False
    return parts[0] not in SKIP_PREFIXES


def official_md_files():
    out = []
    for dp, dn, fn in os.walk(ROOT):
        rel_dir = os.path.relpath(dp, ROOT)
        if rel_dir != "." and not in_scope(rel_dir):
            dn[:] = []
            continue
        for f in fn:
            if f.lower().endswith(".md"):
                rel = os.path.normpath(os.path.join(rel_dir, f)) if rel_dir != "." else f
                out.append(rel.replace(os.sep, "/"))
    return sorted(out)


def safe_read(rel):
    """Read one official .md file; refuse anything outside the sandbox."""
    rel = rel.replace("\\", "/").lstrip("/")
    full = os.path.realpath(os.path.join(ROOT, rel))
    if not (full == ROOT or full.startswith(ROOT + os.sep)):
        raise PermissionError(f"path escapes the repository root: {rel}")
    if not full.lower().endswith(".md"):
        raise PermissionError(f"only .md documents are served: {rel}")
    if not in_scope(os.path.relpath(full, ROOT)):
        raise PermissionError(f"path is outside the official document scope: {rel}")
    with open(full, encoding="utf-8") as fh:
        return fh.read()


# --- registry / document-id resolution ---------------------------------------

def registry_rows():
    text = safe_read(REGISTRY_PATH)
    rows = []
    for m in re.finditer(
            r"^\|\s*(DOC-[A-Z]+-\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
            r"\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|", text, re.M):
        rows.append({
            "id": m.group(1).strip(), "title": m.group(2).strip(),
            "layer": m.group(3).strip(), "category": m.group(4).strip(),
            "status": m.group(5).strip(), "version": m.group(6).strip(),
            "owner": m.group(7).strip(), "location": m.group(8).strip(),
        })
    return rows


_ID_INDEX = None

def path_for_id(doc_id):
    """Repo-relative path of the file whose header carries doc_id."""
    global _ID_INDEX
    if _ID_INDEX is None:
        _ID_INDEX = {}
        for rel in official_md_files():
            m = re.search(r"^Document ID\s*:\s*(DOC-[A-Z]+-\d+)\s*$",
                          safe_read(rel), re.M)
            if m:
                _ID_INDEX.setdefault(m.group(1), rel)
    return _ID_INDEX.get(doc_id)


# --- tools -------------------------------------------------------------------

TOOLS = [
    {
        "name": "list_documents",
        "description": ("List the official AI-OS documents from the Document Registry "
                        "(SSOT): ID, title, layer, category, status, version, location. "
                        "Optional filters: layer (e.g. 'Capability'), status (e.g. 'Active')."),
        "inputSchema": {"type": "object", "properties": {
            "layer": {"type": "string", "description": "filter by architectural layer"},
            "status": {"type": "string", "description": "filter by lifecycle status"},
        }},
    },
    {
        "name": "get_document",
        "description": ("Return the full text of one official AI-OS document, by Document ID "
                        "(e.g. 'DOC-CAPA-015') or by repo-relative path (e.g. "
                        "'00_Core/Core_Identity.md'). Read-only."),
        "inputSchema": {"type": "object", "properties": {
            "id": {"type": "string", "description": "Document ID from the registry"},
            "path": {"type": "string", "description": "repo-relative .md path"},
        }},
    },
    {
        "name": "search_documents",
        "description": ("Case-insensitive keyword search across the official AI-OS markdown "
                        "documents. Returns matching files with the matching lines."),
        "inputSchema": {"type": "object", "properties": {
            "query": {"type": "string", "description": "text to search for"},
        }, "required": ["query"]},
    },
]


def tool_list_documents(args):
    rows = registry_rows()
    layer, status = args.get("layer"), args.get("status")
    if layer:
        rows = [r for r in rows if r["layer"].lower() == layer.lower()]
    if status:
        rows = [r for r in rows if r["status"].lower() == status.lower()]
    if not rows:
        return "No registry entries match the given filters."
    lines = [f"{r['id']} | {r['title']} | {r['layer']} | {r['category']} | "
             f"{r['status']} | v{r['version']} | {r['location']}" for r in rows]
    return f"{len(rows)} document(s):\n" + "\n".join(lines)


def tool_get_document(args):
    doc_id, rel = args.get("id"), args.get("path")
    if doc_id and not rel:
        rel = path_for_id(doc_id.strip())
        if not rel:
            raise ValueError(f"no official document carries Document ID '{doc_id}'")
    if not rel:
        raise ValueError("provide 'id' (Document ID) or 'path' (repo-relative .md path)")
    return f"[{rel}]\n\n{safe_read(rel)}"


def tool_search_documents(args, max_files=20, max_lines_per_file=5):
    query = args["query"].strip()
    if len(query) < 2:
        raise ValueError("query must be at least 2 characters")
    needle, results = query.lower(), []
    for rel in official_md_files():
        hits = [f"  {i}: {ln.strip()}"
                for i, ln in enumerate(safe_read(rel).splitlines(), 1)
                if needle in ln.lower()][:max_lines_per_file]
        if hits:
            results.append(f"{rel}\n" + "\n".join(hits))
        if len(results) >= max_files:
            break
    if not results:
        return f"No official document contains '{query}'."
    return f"{len(results)} file(s) match '{query}':\n\n" + "\n\n".join(results)


HANDLERS = {
    "list_documents": tool_list_documents,
    "get_document": tool_get_document,
    "search_documents": tool_search_documents,
}


# --- JSON-RPC 2.0 over stdio ---------------------------------------------------

def reply(msg_id, result=None, error=None):
    out = {"jsonrpc": "2.0", "id": msg_id}
    if error is not None:
        out["error"] = error
    else:
        out["result"] = result
    sys.stdout.write(json.dumps(out) + "\n")
    sys.stdout.flush()


def handle(msg):
    method, msg_id, params = msg.get("method"), msg.get("id"), msg.get("params") or {}
    if method == "initialize":
        reply(msg_id, {"protocolVersion": PROTOCOL_VERSION,
                       "capabilities": {"tools": {}},
                       "serverInfo": SERVER_INFO})
    elif method in ("notifications/initialized", "notifications/cancelled"):
        pass  # notifications carry no response
    elif method == "ping":
        reply(msg_id, {})
    elif method == "tools/list":
        reply(msg_id, {"tools": TOOLS})
    elif method == "tools/call":
        name, args = params.get("name"), params.get("arguments") or {}
        handler = HANDLERS.get(name)
        if handler is None:
            reply(msg_id, error={"code": -32602, "message": f"unknown tool: {name}"})
            return
        try:
            text = handler(args)
            reply(msg_id, {"content": [{"type": "text", "text": text}], "isError": False})
        except Exception as exc:  # tool errors go back inside the result, per MCP
            reply(msg_id, {"content": [{"type": "text", "text": f"Error: {exc}"}],
                           "isError": True})
    elif msg_id is not None:
        reply(msg_id, error={"code": -32601, "message": f"method not found: {method}"})


def main():
    sys.stderr.write(f"aios-mcp-server serving official AI-OS documents from {ROOT}\n")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            reply(None, error={"code": -32700, "message": "parse error"})
            continue
        handle(msg)


if __name__ == "__main__":
    main()
