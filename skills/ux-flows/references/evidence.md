# Evidence register

What each rule in ux-flows rests on, how strong that is, what was dropped, and what the study could not settle. Use it to decide how hard to push a rule when it conflicts with a product's own evidence: a rule from live walks and many corrections beats a local preference; a rule from documentation alone yields to a measured walk of the product itself.

## The study

| Track | What was done | Yield |
|---|---|---|
| Desktop walks | 25 apps × 14 jobs, walked in a signed-in browser where an account existed (synthetic items, created and deleted), otherwise from public demos, recordings and vendor procedures | 350 cells: 19 completed live jobs (ChatGPT 7, Notion 7, Claude 5), 23 partial live traces, 5 public demo, 12 recording, 266 documented, 25 without sufficient evidence. 33 retained screenshots |
| iPhone | The same 25 apps and 14 jobs from public recordings and vendor documentation; no phone was operated | 350 rows: 18 recording, 214 documented, 11 documented limits, 32 capability only, 75 unknown; 108 action counts (55 bounded, 53 partial). 337 pairs still need a real-device walk |
| iPhone, real device | One pass on a real iPhone through iPhone Mirroring, owned test notes only, all removed afterwards (firstmate `data/ux-phone-device/report.md`, 2026-11-21) | 8 of the 24 native study apps were installed; 4 yielded multi-step walks (Notion, Apple Notes, Granola in part, Slack in part); Gmail and ChatGPT landing only; Reminders and Claude never reached a verified app screen. Seven lessons, below |
| Product proof | All 14 jobs walked live before and after fixes on one real CRM (Hayes), from named starts on seeded data | Dead ends 4 → 0; three corrections to budgets and rules, two questions left open (below) |
| Owner corrections | Every design correction one product owner gave across about ten of their own products (CRMs, an internal ops hub, an analysis tool, a consumer app, agent tooling, mail triage), plus structured interview answers | 224 corrections, 96 interview answers, generalized into 23 rules; 12 were already in product-ui or the emil-* skills, 11 were not |

Apps: Linear, Notion, Things 3, Todoist, Apple Reminders, Apple Notes, Superhuman, Gmail, Granola, ChatGPT, Claude, Perplexity, Cursor, Raycast, Arc, Figma, Attio, HubSpot, Stripe dashboard, Vercel dashboard, Slack, Notion Calendar, Airtable, Obsidian, Shopify admin.

**Weighting.** Live walk over recording or demo over documentation. A count on documentation is a reading of the vendor's procedure; it proves the route exists, not that people find it. A rule supported by a single documented source was dropped. Corrections count occasions in reviews, not usage frequency; a rule needed corrections across more than one product, or corrections plus app evidence, to be kept as a general rule. Product-specific choices (which page a given product lands on, a given scoring scale) were generalized or left out.

## The rules and what they rest on

| Rule (where in SKILL.md) | App evidence | Corrections | Strength |
|---|---|---|---|
| Name the start before comparing counts (rule zero 1) | Claude Unpin 1 with menu open vs ChatGPT 2 from closed [live]; Things shortcut vs Obsidian setup [rec, doc] | the walk rule itself [corr 1] | Strong |
| Count the return separately (rule zero 2) | ChatGPT Recents 2, search 3; deleted chat stayed in search and opened to an access error [live] | resume [corr 11 + 5] | Strong |
| Count decisions without taps (rule zero 3) | Shopify Review changes [doc]; Linear "viewed" is not "approved" [rec]; Gmail recipient suggestion is a decision [rec] | queue [corr 9 + 6] | Medium |
| Verify the consequence (rule zero 4) | Claude edit regenerates the answer; Notion edit appears in a second view with no Save [live] | trust: claims and counts must match records [corr 12 + 6] | Strong |
| One home per job (decision 2) | Attio, HubSpot record actions from the open record [doc] | depth [corr 19 + 11] across 6 products | Strong |
| Trigger on the object (decision 3) | Things Magic Plus, Attio record notes [rec, doc]; Notion block edit in place [live] | point [corr 18 + 6] | Strong |
| The product does routine work it can (thesis 1, step-count table) | Notion autosave [live] | auto [corr 17 + 1]; not in prior skills | Strong (corrections) |
| Merge duplicate entry points (decision 4) | — | depth, point [corr 4 + 4] | Medium |
| Who starts, spends, commits; approval executes (decision 5) | Claude scheduled task reviewed then Schedule [doc]; Cursor Approve vs Request changes sheet [doc] | agency [corr 12 + 18] | Strong |
| Next action visible, named, not behind hover or fold (next-action 1) | Obsidian empty canvas [rec]; Attio buried manual path [rec] | point, depth [corr 4] | Strong |
| Land where the next job starts (next-action 4) | Things returns to the project [rec]; ChatGPT chat moves into Pinned [live] | priority [corr 9 + 5] | Strong |
| Failure's next action is the fix (next-action 5, decision 9) | Linear names the empty field [demo] | recover [corr 7 + 4] | Strong |
| Gestures are accelerators (next-action 6) | Things, Superhuman pull-down [rec]; Gmail, Slack, Notes swipes [doc] | — | Medium |
| User's words, enough context (next-action 8) | — | meaning [corr 17 + 4] | Strong (corrections) |
| Show running stage and item (next-action 9) | Granola Live Activity [doc] | progress [corr 7] | Medium; detail in ai-interaction-patterns |
| Confirm with the promised scope (decision 7) | Vercel rollback names both deployments and confirms each domain [doc with dialog images]; Things shows the moving stack [rec]; Shopify Review changes [doc] | agency: cost and scope [corr 12 + 18] | Medium |
| Inverse in the verb's own slot (decision 8) | ChatGPT Pin/Unpin, Claude Pin/Unpin [live] | — | Strong |
| ⌘Z restores exactly (decision 8) | Notion reorder and ⌘Z against a known order [live]; Gmail Sent-banner Undo reopens the draft [rec]; Apple Notes Recently Deleted [rec] | — | Strong |
| One intended change, one approval, one undo (decision 8) | Things one operation on three tasks [rec] | undo [2 interviews] | Medium; not in prior skills |
| Return to the same object with history (decision 10) | ChatGPT Recents [live]; Claude, Notion second view [part] | resume [corr 11 + 5] | Strong |
| Settled stays settled (thesis 5, decision 11) | ChatGPT stale search result for a deleted chat [live] | state [corr 12 + 6]; not in prior skills | Strong (corrections) |
| Escalate only genuine uncertainty (step-count table) | — | queue [corr 9 + 6]; not in prior skills | Strong (corrections) |
| Route an interruption once, to who can finish it (J9) | Attio opens the comment itself [doc]; Figma quick reply from Activity [doc] | notify [corr 9 + 3]; not in prior skills | Medium |
| Repair machine output before the reader sees it (J13) | — | repair [corr 6], one product | Weak; kept as a J13 note only |
| Mixed-kind list rows lead with object and waiting action (next-action 8) | Hayes attention list: draft rows showed only the email subject, kind and recipient on a hover dot [live proof] | meaning [corr 17] | Medium |
| Bulk action +1 for a chosen destination (J6) | Hayes bulk add to a list 5 vs 4; Things destination step (J2) [rec] | — | Medium |
| Refused input stays typed; Esc restores (J3) | Hayes in-place phone edit: keeping the prior value visible would discard the typed text J8 keeps [live proof] | recover [corr 7] | Medium |
| Undoing a removal restores its values (J7) | Hayes list entry holds stage, priority, dates; re-adding membership alone loses them [live proof] | undo [2 interviews] | Medium |
| Undo reached inside the notice's lifetime (walk step 7) | Hayes 4s toast expired before a scripted walk reached Undo [live proof] | — | Medium; timing in product-ui |
| Ordinary results without a second command (J5) | Notion and Granola: magnifier, type, results (2); Slack: tab, field, query, then a workspace-or-AI choice (4) [device] | — | Medium |
| Query and no-results state survive leaving (J5) | Notion restored populated results; Granola restored No results [device] | resume [corr 11 + 5] | Medium |
| Count shown wherever the destination is picked (J6) | Apple Notes "2 Selected" in select mode and "2 Notes" in the folder picker [device] | — | Medium |
| Recovery is a labelled verb naming its destination (J7) | Apple Notes Recently Deleted: the only recovery cue on the open note was a folder icon [device] | recover [corr 7] | Medium |
| Predictable landing after a delete (next-action 4) | Apple Notes: deleting the open note exposed a different note, twice; the list took Back [device] | — | Medium |
| Saved and back-where-I-started are separate finishes (walk step 2) | Apple Notes: checkmark ended editing in place, Back returned to the list; Back alone also saved [device] | — | Medium |
| Count a step only at a verified object and destination landmark (walk step 3) | Spotlight's Reminders hit opened a system privacy list; after a Notes bulk move the source still showed both titles, the destination proved the move [device] | trust [corr 12] | Medium |
| Keep personal, shared and out-of-scope apart (J12) | Apple Notes collaborator recovery needs the owner's link [doc] | scope [corr 8 + 9] | Medium |

## Already covered elsewhere, pointed to instead of repeated

| Rule | Where it lives |
|---|---|
| Landing view answers what needs the user; attention-sorted list | product-ui `references/shell-and-navigation.md` §1 |
| Controls at the point of decision; one primary action per region | product-ui SKILL.md decision 6, `laws.md` L21 |
| Say each fact once; evidence one gesture away | product-ui rule zero, `laws.md` L7 |
| Every state designed; errors name cause and fix | product-ui `references/states-copy-safety.md` §1 |
| 5s undo notice bound to ⌘Z; confirm only the irreversible | product-ui `laws.md` L24, `states-copy-safety.md` §3 |
| Undo grouping (500ms merge, 100-entry stack), toast timing | product-ui `references/interaction-defaults.md` |
| Approval proportional to rollback cost | product-ui `laws.md` L9 |
| Onboarding over the real product, gate the second turn | product-ui `shell-and-navigation.md` §6, `laws.md` L13 |
| Progress stages, receipts, approvals, cost meters | `ai-interaction-patterns` |
| Explicit human choice as a compact multiple-choice control | product-ui `interaction-defaults.md` (approval card) |
| Keep controls and input stable through scrolling and validation | `mobile-ui`, `emil-ui-polish` |
| Thumb placement, swipe pairs, sheets, notification actions | `mobile-ui` |

## Dropped for weak evidence

Each of these rested on a single documented source and is not a rule in the skill:

- First sign-in for single sign-on must happen on desktop before the phone works (Granola only).
- Voice as the first useful action, and voice failing in background noise (Perplexity only).
- A sideways-scrolling toolbar to keep editor actions reachable (Obsidian only).
- Two-finger drag to multi-select (Apple Reminders only).
- Shake to undo as a pattern to copy (Things only; kept only as one example of phone undo).
- Position on the share sheet as a cost to design for (Raycast only).
- A widget completing a task in one tap as a review pattern (Apple Reminders only; kept only as an example of work outside the app).
- Time-sensitive measured thresholds (a ten-second first-result criterion and similar) from a single product's correction: speed was measured nowhere in the study, so the skill budgets steps, not seconds.

## Gaps the study could not settle

- **No live walk of a new account's first run.** Every first-run trace began in an existing signed-in account or a vendor procedure; signups were blocked by email verification or identity providers. The J1 budget is the product's own first useful result, not onboarding.
- **No live offline session.** Error recovery was walked live only in the product proof (refused input, empty create, unsent email kept) and in ChatGPT's stale search result. Offline behaviour is documented (Notion, HubSpot, Todoist), not walked.
- **No delivered notification acted on.** 8 of 25 desktop apps had no evidence at all for J9; nothing was received and followed. The J9 budget comes from documentation and corrections.
- **No handoff to another person or device.** Every handoff was a second view in the same account; Slack's recording is edited and cannot show propagation time.
- **No human time.** No elapsed time was measured anywhere. Budgets are steps and decisions.
- **Gesture discoverability.** Recordings show gestures used by people who already know them; whether a newcomer finds them is unknown.
- **One universal step limit.** The data does not support one; it supports a budget per job from a named start.
- **Phone, on a real device.** One real-device pass found only 8 of the 24 native study apps installed and got multi-step walks from 4, so the [device] rules rest on a handful of apps and mostly on one (Apple Notes). The queue still holds 337 outstanding iPhone jobs; other phone counts are lower bounds from vendor media.
- **Handing over versus adding.** Assigning work from a multi-assignee picker added the new person beside the author instead of replacing them (Hayes). Whether a handoff replaces or adds is a product call; one product is not enough for a rule.
- **Enter in a find-or-ask box.** When one input both finds a record and asks the AI, the J1 and J5 budgets cannot say what Enter does when the text exactly names one record (Hayes asks; the arrow then Enter opens). Needs products with the same box (Raycast, Arc, Notion search-or-ask).
- **Search index lag after deletion.** Observed once (ChatGPT), duration unmeasured.
