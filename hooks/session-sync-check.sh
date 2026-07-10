#!/bin/bash
# SessionStart hook: fetch + fast-forward pull when safe, otherwise warn.
# Never touches a dirty tree and never does anything but a pure fast-forward.
set -uo pipefail

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  exit 0
fi

if ! git fetch --quiet 2>/tmp/session-sync-check.fetch-err; then
  echo "⚠️  git fetch failed — check network/auth ($(cat /tmp/session-sync-check.fetch-err | tail -1))."
  exit 0
fi

branch=$(git rev-parse --abbrev-ref HEAD)
upstream=$(git rev-parse --abbrev-ref --symbolic-full-name "@{u}" 2>/dev/null || true)

if [ -z "$upstream" ]; then
  exit 0
fi

local_sha=$(git rev-parse HEAD)
upstream_sha=$(git rev-parse "$upstream")

if [ "$local_sha" = "$upstream_sha" ]; then
  exit 0
fi

ahead=$(git rev-list --count "$upstream"..HEAD 2>/dev/null || echo "?")
behind=$(git rev-list --count HEAD.."$upstream" 2>/dev/null || echo "?")

if [ -n "$(git status --porcelain)" ]; then
  echo "⚠️  '$branch' is $behind behind / $ahead ahead of $upstream, and you have uncommitted local changes. Not auto-pulling — commit or stash first, then pull/rebase manually."
  exit 0
fi

if git merge-base --is-ancestor HEAD "$upstream" 2>/dev/null; then
  if git merge --ff-only "$upstream" --quiet 2>/tmp/session-sync-check.merge-err; then
    echo "✅ Fast-forwarded '$branch' $behind commit(s) to match $upstream before starting this session."
  else
    echo "⚠️  '$branch' is $behind behind $upstream but fast-forward failed unexpectedly ($(cat /tmp/session-sync-check.merge-err | tail -1)) — check manually."
  fi
else
  echo "⚠️  '$branch' has diverged from $upstream ($ahead ahead / $behind behind) — not a fast-forward. Pull/rebase manually before continuing."
fi
