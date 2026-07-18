#!/usr/bin/env python3
"""
AI-OS Live Behavioral Recorder (DOC-EXEC-024, Live Evaluation).

Sends every case in cases.jsonl to a live model and records its answers as a
responses file ({case_id: response_text}) for the deterministic gate
(run_behavior_eval.py + compare_eval.py). This is the drift-detection input:
provider model updates change answers even when no document changed.

Providers (selected with --provider; the API key comes from the environment):
  claude  ANTHROPIC_API_KEY   Anthropic Messages API
  openai  OPENAI_API_KEY      OpenAI Chat Completions API
  gemini  GEMINI_API_KEY      Google Gemini generateContent API
  mock    (no key)            echoes the golden answers — offline pipeline test

The system prompt is the deployed artifact AI-OS_AI_Working_Kit_lean.md,
assembled per the platform's adapter convention: Claude receives it wrapped
in XML tags (DOC-PLAT-002), OpenAI/Gemini receive it as Markdown system
instructions (DOC-PLAT-006/007). Stdlib-only.

Usage:
  python3 record_live.py --provider claude --output live_claude.json
  python3 record_live.py --provider mock  --output live_mock.json
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CASES = os.path.join(HERE, "cases.jsonl")
LEAN_KIT = os.path.join(ROOT, "AI-OS_AI_Working_Kit_lean.md")

DEFAULT_MODELS = {
    "claude": os.environ.get("MODEL_CLAUDE", "claude-sonnet-5"),
    "openai": os.environ.get("MODEL_OPENAI", "gpt-4o-mini"),
    "gemini": os.environ.get("MODEL_GEMINI", "gemini-2.0-flash"),
}
KEY_ENV = {"claude": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY",
           "gemini": "GEMINI_API_KEY"}


def http_json(url, payload, headers, timeout=90, retries=2):
    body = json.dumps(payload).encode("utf-8")
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, data=body, method="POST",
                                         headers={"Content-Type": "application/json", **headers})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == retries:
                raise
            time.sleep(2 ** (attempt + 1))


def system_prompt(provider):
    with open(LEAN_KIT, encoding="utf-8") as fh:
        kit = fh.read()
    if provider == "claude":  # XML structure per the Claude Adapter
        return f"<identity_and_rules>\n{kit}\n</identity_and_rules>"
    return kit  # Markdown headings per the GPT/Gemini Adapters


def ask_claude(system, user, key, model):
    r = http_json("https://api.anthropic.com/v1/messages",
                  {"model": model, "max_tokens": 1024, "system": system,
                   "messages": [{"role": "user", "content": user}]},
                  {"x-api-key": key, "anthropic-version": "2023-06-01"})
    return "".join(b.get("text", "") for b in r["content"])


def ask_openai(system, user, key, model):
    r = http_json("https://api.openai.com/v1/chat/completions",
                  {"model": model, "messages": [
                      {"role": "system", "content": system},
                      {"role": "user", "content": user}]},
                  {"Authorization": f"Bearer {key}"})
    return r["choices"][0]["message"]["content"]


def ask_gemini(system, user, key, model):
    r = http_json(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
        {"system_instruction": {"parts": [{"text": system}]},
         "contents": [{"role": "user", "parts": [{"text": user}]}]},
        {})
    return "".join(p.get("text", "") for p in
                   r["candidates"][0]["content"]["parts"])


ASK = {"claude": ask_claude, "openai": ask_openai, "gemini": ask_gemini}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True,
                    choices=["claude", "openai", "gemini", "mock"])
    ap.add_argument("--output", required=True)
    ap.add_argument("--cases", default=CASES)
    args = ap.parse_args()

    with open(args.cases, encoding="utf-8") as fh:
        cases = [json.loads(l) for l in fh if l.strip()]

    if args.provider == "mock":
        responses = {c["id"]: c["golden"] for c in cases}
    else:
        key = os.environ.get(KEY_ENV[args.provider], "")
        if not key:
            print(f"{KEY_ENV[args.provider]} is not set — nothing recorded.")
            sys.exit(3)  # distinct exit code: not configured
        model = DEFAULT_MODELS[args.provider]
        system = system_prompt(args.provider)
        responses, errors = {}, 0
        for i, c in enumerate(cases, 1):
            try:
                responses[c["id"]] = ASK[args.provider](system, c["input"], key, model)
            except Exception as exc:
                errors += 1
                responses[c["id"]] = f"[RECORDING ERROR: {exc}]"
            print(f"  [{i}/{len(cases)}] {c['id']}", flush=True)
        if errors:
            print(f"WARNING: {errors} case(s) failed to record — they will "
                  "score as failures, which is intended (an unreachable model "
                  "is a regression).")

    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(responses, fh, indent=2, ensure_ascii=False)
    print(f"Recorded {len(responses)} responses ({args.provider}) -> {args.output}")


if __name__ == "__main__":
    main()
