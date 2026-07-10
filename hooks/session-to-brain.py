#!/usr/bin/env python3
"""
Claude Code SessionEnd hook: extracts key insights from a session
and writes a structured summary to the janus-brain vault.

Sessions flagged for sensitive content (FStea/Morgan Stanley/MNPI markers,
or an obvious PII pattern) are written locally only and never auto-pushed --
they sit as untracked files in the vault repo, visible via `git status`,
until someone deliberately `git add`s and pushes them.
"""

import json, os, re, subprocess, sys
from datetime import datetime
from pathlib import Path

BRAIN_PATH = Path(os.environ.get("JANUS_BRAIN_PATH",
    os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/Downloads/janus-brain")))

SENSITIVE_MARKERS = ["fstea", "斐素", "fs-ai", "morgan stanley", "mnpi"]
SSN_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")


def is_flagged(info):
    haystack = " ".join([
        info["goal"], info["cwd"], info["result_text"],
        " ".join(info["files_changed"]),
        " ".join(info["commands_run"]),
    ]).lower()
    hits = [m for m in SENSITIVE_MARKERS if m in haystack]
    if SSN_PATTERN.search(haystack):
        hits.append("ssn-pattern")
    return hits


def notify(title, message):
    print(f"{title}: {message}")
    if sys.platform == "darwin":
        try:
            safe_msg = message.replace('"', "'")
            safe_title = title.replace('"', "'")
            subprocess.run(
                ["osascript", "-e", f'display notification "{safe_msg}" with title "{safe_title}"'],
                capture_output=True, timeout=5,
            )
        except Exception:
            pass


def main():
    raw = sys.stdin.read()
    hook = json.loads(raw)
    tp = hook.get("transcript_path", "")
    if not tp or not Path(tp).exists():
        return
    messages = []
    with open(tp) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    messages.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    if not messages:
        return

    info = {"goal": "", "files_changed": [], "commands_run": [], "git_ops": [],
            "tool_counts": {}, "model": "", "total_turns": 0,
            "total_input_tokens": 0, "total_output_tokens": 0, "cwd": "",
            "stop_reason": "", "result_text": "", "session_id": ""}
    seen = set()
    for msg in messages:
        t = msg.get("type", "")
        info["session_id"] = info["session_id"] or msg.get("sessionId", "")
        info["cwd"] = info["cwd"] or msg.get("cwd", "")
        if t == "user":
            c = msg.get("message", {}).get("content", "")
            if isinstance(c, list):
                c = "".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
            if c and not info["goal"]:
                info["goal"] = c[:800]
        elif t == "assistant":
            info["total_turns"] += 1
            m = msg.get("message", {})
            info["model"] = info["model"] or m.get("model", "")
            u = m.get("usage", {})
            info["total_input_tokens"] += u.get("input_tokens", 0)
            info["total_output_tokens"] += u.get("output_tokens", 0)
            for block in m.get("content", []):
                if block.get("type") != "tool_use":
                    continue
                name = block.get("name", "")
                inp = block.get("input", {})
                info["tool_counts"][name] = info["tool_counts"].get(name, 0) + 1
                if name in ("Edit", "Write"):
                    p = inp.get("file_path", "") or inp.get("path", "")
                    if p and p not in seen:
                        seen.add(p)
                        info["files_changed"].append(p)
                elif name == "Bash":
                    cmd = str(inp.get("command", ""))
                    if cmd:
                        info["commands_run"].append(cmd)
                        if cmd.strip().startswith("git"):
                            info["git_ops"].append(cmd)
        elif t == "result":
            rc = msg.get("message", {}).get("content", "")
            if isinstance(rc, list):
                rc = "\n".join(b.get("text", "") for b in rc if isinstance(b, dict) and b.get("type") == "text")
            info["result_text"] = rc[:1000]
            info["stop_reason"] = msg.get("message", {}).get("stop_reason", "")

    if not info["files_changed"] and not info["commands_run"]:
        return

    now = datetime.now()
    ds = now.strftime("%Y-%m-%d")
    ts = now.strftime("%H%M%S")
    inbox = BRAIN_PATH / "00-INBOX" / "_claude-sessions"
    inbox.mkdir(parents=True, exist_ok=True)
    slug = "".join(c if c.isalnum() or c in "-" else "" for c in info["goal"][:45].lower())[:30].rstrip("-")
    fname = f"{ds}-{ts}{'-'+slug if slug else ''}-summary.md"
    sp = inbox / fname

    flags = is_flagged(info)

    lines = ["---", "type: claude-session-summary", f"date: {ds}", "source: claude-code",
             f"session_id: '{info['session_id']}'", "status: unsorted",
             "tags: [claude-session, unsorted]"]
    if flags:
        lines.append(f"flagged: [{', '.join(flags)}]")
    lines += ["---", "", f"# Claude Session — {ds}", ""]
    if flags:
        lines += [f"> ⚠ Held locally, not pushed — matched: {', '.join(flags)}. Review and push manually if appropriate.", ""]
    if info["goal"]:
        lines += ["## Goal", "", info["goal"], ""]
    cwd = info["cwd"].replace(os.path.expanduser("~"), "~") if info["cwd"] else ""
    if cwd:
        lines.append(f"- Project: {cwd}")
    if info["model"]:
        lines.append(f"- Model: {info['model']}")
    if info["total_turns"]:
        lines.append(f"- Turns: {info['total_turns']}")
    tt = info["total_input_tokens"] + info["total_output_tokens"]
    if tt:
        lines.append(f"- Tokens: {tt:,} total ({info['total_input_tokens']:,} in / {info['total_output_tokens']:,} out)")
    if info["stop_reason"]:
        lines.append(f"- Outcome: {info['stop_reason']}")
    lines.append("")
    if info["tool_counts"]:
        nr = {k: v for k, v in info["tool_counts"].items() if k != "Read"}
        if nr:
            lines.append("## Activity Summary")
        for k, v in sorted(nr.items()):
            lines.append(f"- {k}: {v}")
        ec, wc, bc = info["tool_counts"].get("Edit", 0), info["tool_counts"].get("Write", 0), info["tool_counts"].get("Bash", 0)
        if ec + wc + bc:
            lines.append(f"- Operations: {ec} edits, {wc} writes, {bc} commands")
        lines.append("")
    if info["files_changed"]:
        lines.append("## Files Changed")
        for f in info["files_changed"]:
            lines.append(f"- {f}")
        lines.append("")
    if info["git_ops"]:
        lines.append("## Git Operations")
        for c in info["git_ops"]:
            lines.append(f"- {c[:200]}")
        lines.append("")
    ng = [c for c in info["commands_run"] if not c.strip().startswith("git")]
    if ng:
        lines.append("## Commands Run")
        for c in ng[:8]:
            lines.append(f"- {c[:200]}")
        if len(ng) > 8:
            lines.append(f"- ...and {len(ng)-8} more")
        lines.append("")
    if info["result_text"]:
        lines += ["## Result / Outcome", "", info["result_text"], ""]
    lines += ["## Extracted Insights", "", "Populated by Hermes cron processor.", ""]
    lines += ["## Raw Transcript", "", f"Session ID: {info['session_id']}", ""]

    with open(sp, "w") as f:
        f.write("\n".join(lines))

    if flags:
        rel = sp.relative_to(BRAIN_PATH)
        notify(
            "session-to-brain: held for review",
            f"{rel} flagged ({', '.join(flags)}) - not pushed. "
            f"Run: cd {BRAIN_PATH} && git add \"{rel}\" && git commit -m 'claude-session: {rel.name}' && git push",
        )
        return

    # Push to GitHub (only for unflagged sessions)
    os.chdir(str(BRAIN_PATH))
    subprocess.run(["git", "pull", "--rebase", "--autostash"], capture_output=True, timeout=30)
    subprocess.run(["git", "add", str(sp)], capture_output=True, timeout=30)
    rel = sp.relative_to(BRAIN_PATH)
    subprocess.run(["git", "commit", "-m", f"claude-session: {rel.parent.name}/{rel.name}"], capture_output=True, timeout=30)
    subprocess.run(["git", "push"], capture_output=True, timeout=30)
    print(f"→ session-to-brain: {sp.name}")


if __name__ == "__main__":
    main()
