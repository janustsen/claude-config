# States, copy and safety

Design every state before styling anything. Then write the words, deleting first. Then make every action reversible or honestly gated.

## 1. The state set

Every list, panel and AI surface defines all of these. A state nobody designed is a state that looks broken.

| State | What it shows | Rule |
|---|---|---|
| Empty (zero) | A question plus the primary input, or one muted line with the first action | No illustrations, no fake suggestions in a returning-user tool. "No archived threads." "Nothing needs you. Agents finished 4 things since yesterday →" |
| No results | One muted line and "Clear filters" | Distinct from zero: the user caused it, so offer the undo |
| Loading | A skeleton in the final shape plus a text label, after 400ms | Avatar circle, two bars of varied width, right-side meta bars, under "Loading pull requests…"; pulse 2.4s stepped |
| Partial or streaming | Reserved final footprint; finished blocks fade in | Min-height on streaming answers; hidden action rows stay mounted with `pointer-events: none` |
| Busy action | The button changes its verb and disables | "Importing…", reduced opacity, no spinner in the button |
| Error | What failed, why, the exact fix, a retry, where it happened | "Codex CLI is not authenticated. Run `codex login` and try again." Amber alert, warning icon, command in code style |
| Offline or waiting | Its own state, not an error | Banner after a 2s grace; an escape hatch after 20s |
| Disabled | Visible, with the prerequisite on hover | "Available for Git repositories." "Select a pull request first." Missing permission disables rather than hides |
| Unavailable feature | Listed, dimmed, with how to enable | An orange outline "Setup Required" badge; a lock and plan badge for paid features |
| Calibrating | No score until there is enough data, and what will unlock it | A confident wrong number does more damage than "calibrating" |
| Success | Confirmed at the point of action, with undo | Icon morph and anchored "Copied!" for 1000ms; "Archived 1 thread, ⌘Z to undo" inline for 5s; no global toast for a local action |
| Stopped | Marked as stopped, naming what stopped, with Continue | "You stopped after 45s." "Work interrupted." Never a silent truncation |
| Gated | A locked door in place, with the unlock path | "Log in to use…" with the click carrying `?next=` so it is remembered |

### Rules
1. Every list ships four separate states: skeleton loading, zero with a first action, no results with clear filters, and error with retry. Filter by collapsing rows in place.
2. Delay loading UI by 400ms, then escalate slow waits with an explanation (15s: "Some requests are slow · 1 request waiting longer than 15s") and an escape hatch (20s).
3. Errors appear where they happened, as a single Retry pill under the failed item. Global error pages are for global failures only. Retry transient failures once automatically.
4. Error recoveries are specific to the cause and ranked (retry without the attachment, edit, start new), with technical details collapsed.
5. Error titles use one prefix consistently ("Could not X"), then the raw message.
6. Surface provider, quota and auth problems as banners with the fix action, at the input they block: "Claude provider status: Timed out after 25s while checking account status. [Refresh] ✕".
7. Never let a skeleton or blank region stand in for content that failed to load; replace it with the error.
8. Safety stops (health, money, legal) are unmissable and actionable: fire on the first red-flag message, make phone numbers one-tap `tel:` links, end visibly without covering the instruction.

## 2. Copy

### Delete before you word
The first question about any string is whether it should exist, and only then how it reads. Walk each string through four gates in order and act at the first one it fails. (Paraphrased, with credit, from the clean-copy agent skill shared by Rachel on X; its licence is not stated, so none of its text is copied.)

1. **Would the user ever have wondered about this?** If not, delete it. Copy that answers a question nobody asked does not inform; it plants a worry.
2. **Does the value need a label to make sense?** Keep a caption only when the bare value is meaningless without it. "Session timeout" needs no sentence saying it controls when sessions time out; a lone "15" beside it does need "minutes".
3. **Is it ruling out a problem rather than describing a behaviour?** Delete it: reassurance that a past bug is gone (shipping the fix is enough), text that argues for a design decision, hedges written to pre-empt a complaint.
4. **Rewrite to cut the offending part; if nothing is left, remove the element.** An empty hint is removed, not left blank.

What survives is copy the user cannot act without: a real consequence at the moment of choosing, a scope or compatibility fact not visible on screen, what a blank state means and what to do next, units or format on a bare value. Keep the warning about what happens; drop the copy that asks permission or apologises.

Method: judge each string next to what is on screen, cut whole clauses, leave passing copy alone, move rare-state copy into that state, and report each finding as location, current string, rewrite or "cut", and the gate it failed. Put the consequence on the button ("Apply 3 changes") so the helper text fails gate 1 and can go.

### Voice rules
1. Sentence case everywhere. Verb plus object: "New thread", "Open diff", "Restore device defaults".
2. Name the real target: "Copy prompt link", not "Copy". Action names agree across label, tooltip, menu and accessible name.
3. Statuses are one word: Working, Approval, Input, Limited, Failed, Done. Durations are compact and tabular: "Worked for 18m 3s", "7s", "5m", "3h", "2d".
4. Put the count in the label: "Import 1 project", "Show 25 more", "Update 1 provider", "10 of 12 on".
5. Progress copy is present tense while running and past tense with counts when done ("Running" then "Ran 2 commands").
6. Questions as invitations: "What should we build in **project**?", "or start without a project". "We" only in invitations (the app as collaborator); "you" for the user's actions ("You stopped after 45s").
7. Destructive dialogs state the consequence: "This stops the running process and clears its history."
8. Errors state the fix. Be mechanically honest: "These estimates are not your subscription bill."
9. The middle dot `·` separates clauses inside one line ("Waiting for approval · Decline · Approve").
10. One term per concept (do not call one server environment, machine and computer on different screens), one ellipsis character (…), one error prefix.
11. No em dashes in UI copy.
12. Personality goes around numbers, never inside them. Persona belongs in empty states and nudges; figures, fees and legal text stay plain. Product copy is literal; cheek belongs to the marketing site.
13. Placeholders teach input syntax and name the scope: "Ask anything. @ files, $ skills, / commands", "Ask about NVDA".
14. In anxious domains (health, money), validate before instructing, and use ordered words ("Most likely", "Possible") instead of false-precision percentages.
15. Translate into personal units where it helps decide: a per-day allowance, a debt-free date.
16. Never use a greeting headline in a work tool. A functional line ("Since Tuesday: 3 new leads, 1 invoice overdue") replaces it.
17. Say each fact once per screen. If the page header says sending is on, the sidebar and the controls do not repeat it.

## 3. Safety and reversibility

1. Every lifecycle verb has an inverse, and every list action gets a 5s inline undo bound to ⌘Z.
2. Confirm only what is irreversible. Confirmation defaults follow data loss: delete on, unpin and archive off.
3. Destructive actions come last, in red, separated, with the trash glyph; their dialogs focus Cancel and make shortcuts inert.
4. Remote irreversible actions get arm-then-confirm in place (3s disarm). Local data loss gets a modal.
5. Never let a keystroke meant for one surface trigger a decision on another: hold incoming prompts while the user is typing (1.5s), swallow shortcuts inside dialogs, never approve on Enter in a field that just received focus.
6. Archive is disabled while the item is running; say why on hover.
7. Default anything that publishes outward to off.
8. Never move what the user is touching: expanding a group pins the clicked row; tooltips do not open mid-scroll; content does not reflow under the pointer.
9. Show a pending state on the clicked decision when a confirmation is slow to process, so Approve never looks stuck.
10. Money and send approvals are single-use, time-boxed and void if anything changes (see `ai-interaction-patterns`).
