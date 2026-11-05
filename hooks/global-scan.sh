#!/usr/bin/env bash
# Secrets (gitleaks) + SAST (semgrep) on the file just edited. Exit 2 blocks, including when a scanner breaks.
set -uo pipefail
file=$(jq -r '.tool_input.file_path // .tool_input.notebook_path // empty' 2>/dev/null)
[[ -n "$file" && -f "$file" ]] || exit 0
findings=""
repo=$(cd "$(dirname "$file")" 2>/dev/null && git rev-parse --show-toplevel 2>/dev/null) || repo=""
cfg=""; [[ -n "$repo" && -f "$repo/.gitleaks.toml" ]] && cfg="$repo/.gitleaks.toml"   # repo rules and allowlists
if command -v gitleaks >/dev/null; then
  out=$(gitleaks detect --no-git --no-banner --redact -v ${cfg:+--config "$cfg"} --source "$file" 2>&1) || findings+="[gitleaks]"$'\n'"$out"$'\n'
fi
command -v semgrep >/dev/null || { echo "semgrep missing: edit NOT scanned (fail closed)" >&2; exit 2; }
[[ -z "${SSL_CERT_FILE:-}" ]] && export SSL_CERT_FILE=/etc/ssl/cert.pem
err=$(mktemp); out=$(semgrep --config auto --error --quiet --skip-unknown-extensions "$file" 2>"$err"); rc=$?
if [[ $rc -eq 1 ]]; then findings+="[semgrep]"$'\n'"$out"$'\n'
elif [[ $rc -ge 2 ]]; then echo "semgrep failed (rc=$rc), edit NOT scanned:" >&2; tail -5 "$err" >&2; rm -f "$err"; exit 2; fi
rm -f "$err"
[[ -n "${findings//[[:space:]]/}" ]] && { echo "Security scan flagged $file:"; printf '%s\n' "$findings"; } >&2 && exit 2
exit 0
