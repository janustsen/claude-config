#!/bin/bash
# Blocks catastrophic shell commands. Patterns: dangerous-patterns.txt beside this script. (one ERE per line).
# Claude/Codex: exit 2 + reason on stderr blocks. Arg "cursor": JSON permission output.
PATTERNS_FILE="$(dirname "${BASH_SOURCE[0]}")/dangerous-patterns.txt"; MODE="${1:-exitcode}"
allow() { [ "$MODE" = "cursor" ] && printf '{"permission":"allow"}\n'; exit 0; }
command -v jq >/dev/null 2>&1 || allow
INPUT=$(cat)
CMD=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // .toolInput.command // .command // empty' 2>/dev/null)
[ -z "$CMD" ] && allow; [ -f "$PATTERNS_FILE" ] || allow
while IFS= read -r pattern; do
  case "$pattern" in ''|\#*) continue ;; esac
  if printf '%s\n' "$CMD" | grep -qE -- "$pattern" 2>/dev/null; then
    msg="Blocked by the global dangerous-command guard. Matched pattern: $pattern. Do not retry or work around it; explain the block to the user."
    if [ "$MODE" = "cursor" ]; then jq -cn --arg m "$msg" '{permission:"deny",user_message:"Command guard blocked a dangerous command.",agent_message:$m}'; exit 0; fi
    echo "$msg" >&2; exit 2
  fi
done < "$PATTERNS_FILE"
allow
