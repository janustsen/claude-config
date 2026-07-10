---
name: journal-sort
description: Use when raw notes, journal entries, or captured thoughts have piled up in the Janus vault's 00-INBOX and need filing into the right brain — triggers include "sort my inbox", "process my journal", "clear my inbox", "file my notes", "sweep stale items", or the scheduled nightly inbox sort. Also when a single capture mixes tasks, ideas, decisions, and reflections that belong in different places.
---

# Journal Sort

## Overview
Files unsorted captures from the Janus three-brain vault's `00-INBOX/` into the correct brain, links them, **keeps state fresh**, and leaves an audit trail. **Capture is dumb, sorting is smart** — the human dumps everything in one place; this skill untangles it.

- Vault root: `/Users/janustsen/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Janus`
- Sorting spec: `99-SYSTEM/autosorter-spec.md`
- Freshness rules (status, amend-in-place, sweep, anti-bloat): `99-SYSTEM/freshness-protocol.md`

## When to use
- Inbox has notes without a `#sorted` tag — daily journal or quick captures.
- A single capture mixes types (task + idea + decision) belonging in different brains.
- Running the nightly scheduled sort, or a weekly staleness sweep ("sweep stale items").

Do NOT use to reorganize already-filed notes. Don't touch anything outside `00-INBOX/` except the amend-in-place and sweep steps below.

## Close open loops first (anti-rot — do BEFORE filing new items)
Janus forgets to record solutions, so the brain accumulates problems that read as forever-open. Fix it by asking, not waiting:
1. Read the `## Open threads (live state)` table in each `_BRAIN.md` + main-brain `goals.md`.
2. Present the currently `open`/`blocked` items back to Janus: **"Are any of these resolved or changed since [date]?"**
3. For each one he closes: **amend in place** — flip `status` to `resolved`/`superseded` with today's date, link the solution, and move the row out of current-state into the matching `decisions-log.md` (or `_archive/`). Never leave a solved item sitting as "open."

## Git audit trail (wrap every run)
The vault is git-backed, so bracket every run with commits — the autosorter's edits become one isolated, revertible diff. Set `VAULT="/Users/janustsen/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Janus"`, then:
- **Before filing (start of run):** clean the tree so the sort stands alone —
  `git -C "$VAULT" add -A && (git -C "$VAULT" diff --cached --quiet || git -C "$VAULT" commit -q -m "pre-sort snapshot $(date +%F)")`
- **After reporting (end of run):** capture the sort as one labeled commit —
  `git -C "$VAULT" add -A && (git -C "$VAULT" diff --cached --quiet || git -C "$VAULT" commit -q -m "journal-sort: <one-line summary>")`
Each sort = a single commit you can `git revert` if it mis-files. **Don't push** — let the Obsidian Git plugin handle pushing.

## Procedure (filing new captures)
1. **Snapshot, then load context.** Run the *pre-sort* commit above, then read `CLAUDE.md` (incl. boundaries + State & freshness), `01-MAIN-BRAIN/_SELF.md`, and each project `_BRAIN.md`.
2. **Gather.** List notes in `00-INBOX/` lacking a `#sorted` tag. Oldest first.
3. **Split.** Break each note into atomic items (a line/paragraph = one item).
4. **Classify** each item (see table).
5. **File it with state.** Append to the destination with today's date + a backlink to the source. For any problem / decision / open item, tag `status: open` + `since: <today>` and add a row to that brain's `## Open threads (live state)` table. Add `[[wikilinks]]` to related notes.
6. **Handle uncertainty.** Low confidence / ambiguous → leave in place, tag `#needs-review`. Never guess.
7. **Respect boundaries.** MS-internship MNPI / employer-confidential / live client credentials → `#needs-review`, do NOT distribute. FStea facts route to FStea but stay confidential.
8. **Mark the source.** When every item is filed, tag the note `#sorted` + a "filed to: …" backlink list. **Never delete or rewrite the original.**
9. **Report.** Count filed, where each went, what you closed in the loop-check, any `#needs-review`, and 1–2 non-obvious cross-brain connections.
10. **Commit the run.** Run the *after* commit (Git audit trail) so the sort is one revertible commit.

## Classification quick reference
| Item type | Destination |
|---|---|
| Task / next-action | project task list (or `01-MAIN-BRAIN/` if personal) |
| Decision (made or pending) | that area's `decisions-log.md` — capture the WHY + alternatives |
| Problem / open question | the brain's `## Open threads (live state)` table — `status: open` + date |
| Reusable idea | `80-IDEAS/` as an atomic note, linked |
| Project fact (status / contact / requirement) | matching `_BRAIN.md` or `context-bank/` |
| Personal reflection / value | `01-MAIN-BRAIN/` (feeds the voice profile) |
| Reference / link / clip | `80-IDEAS/` or project `context-bank/` — summarize, don't dump |
| Ambiguous / sensitive | stays in `00-INBOX/`, tag `#needs-review` |

**Routing by keywords:** FStea / Duna / consultancy / artifact / outreach → `10-DUNA/`. Trus / Lattice / Freeform / Gen-UI / workspace / Diego / module → `20-TRUS/`. Personal / values / health / reflection → `01-MAIN-BRAIN/`.

## Staleness sweep (weekly mode — trigger: "sweep stale items")
Per `99-SYSTEM/freshness-protocol.md`:
1. Across every `## Open threads (live state)` table, find `open`/`blocked` items whose `since` is older than 14 days.
2. Ask Janus "still true?" → reconfirm (bump the date), resolve (amend in place + move to log), or archive (move to the brain's `_archive/`).
3. Compact the loaders while you're there: merge redundant lines, move resolved rows to `_archive/`, tighten wording. **Condense the loaders; never compress `decisions-log.md`.**

## Common mistakes
- **Deleting or rewriting the original.** Never. Append/link only; tag `#sorted`.
- **Leaving solved problems as "open."** Run the loop-check; amend in place.
- **Force-filing low-confidence items.** Use `#needs-review`.
- **Dumping raw links/clips.** Summarize into a note.
- **Siloing.** Add `[[wikilinks]]` so ideas connect across brains.
- **Bloating loaders.** Keep `_BRAIN.md`/`_SELF.md` lean; push detail to warm files, dead items to `_archive/`.
