#!/usr/bin/env bash
# Language-agnostic live scan: secrets + SAST on the file Claude just edited.
set -uo pipefail
input=$(cat)
file=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
[[ -n "$file" && -f "$file" ]] || exit 0

findings=""

# Secrets — dedicated scanner, works on any file type.
# gitleaks emits its report to stderr (not stdout); -v adds per-finding detail,
# and 2>&1 captures it so a hit actually reaches $findings and blocks.
if command -v gitleaks >/dev/null 2>&1; then
  if ! out=$(gitleaks detect --no-git --no-banner --redact -v --source "$file" 2>&1); then
    [[ -n "$out" ]] && findings+="[gitleaks]"$'\n'"$out"$'\n'
  fi
fi

# SAST — auto-detects language; --error makes a finding a non-zero exit
if command -v semgrep >/dev/null 2>&1; then
  if ! out=$(semgrep --config auto --error --quiet --skip-unknown-extensions "$file" 2>/dev/null); then
    [[ -n "$out" ]] && findings+="[semgrep]"$'\n'"$out"$'\n'
  fi
fi

if [[ -n "${findings//[[:space:]]/}" ]]; then
  { echo "Security scan flagged $file — please address before continuing:";
    printf '%s\n' "$findings"; } >&2
  exit 2
fi
exit 0
