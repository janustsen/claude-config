---
name: ai-interaction-patterns
description: Design the AI-specific surfaces of a product so delegation is legible and safe - the composer and its pills, streaming and progress, the work log and turn receipt, approvals and permission modes, stop/steer/queue, citations and provenance, AI proposals vs accepted content, versions and undo, agent status and handoff, background tasks, cost and limit meters, memory and privacy modes, and logged-out gating. Each pattern has its anatomy, states, measured values and when to use it, drawn from T3 Code, ChatGPT, Claude, Perplexity, Cursor, v0, Linear, Notion, Granola, Dia, Comet and others. Use whenever a screen has an AI input, an AI answer, an agent that acts, or AI-generated content mixed with human content. Load product-ui for the surrounding shell, tokens and review.
license: MIT
---

# AI interaction patterns

An AI surface has one job: make delegation legible. The user must see what the AI is doing, what it needs, what it changed, and what it based that on, and must be able to stop, steer, correct and undo it. Outcome first, process on demand, interruptions only when a human is truly needed.

## The universal state set

Define every one of these for every AI surface before styling. Most AI UI that feels broken is missing one.

| State | Shows |
|---|---|
| Idle | The input, focused, with a placeholder that teaches syntax and names the scope |
| Has input | The primary slot becomes Send (accent); attached context visible as removable chips |
| Working | One status line: a verb plus an elapsed timer, the verb shimmering. Stop available |
| Streaming | Output arriving into reserved space, in finished blocks; scroll does not get yanked |
| Needs input | The AI asks: a question, an approval, a choice. Loud, pulled to the top of the list, never faded |
| Done | The result visible; the process folded into a receipt with counts, time and cost |
| Stopped | Marked "stopped", naming what stopped, with Continue |
| Error | Cause plus the next action, at the place it failed, with Retry |
| Gated | A locked door in place (a limit, a plan, a sign-in) with the unlock path and the user's input preserved |

## The rules that matter most

1. **Outcome first.** While running, show one live line and a timer. When done, fold the process behind "Worked for 2m 13s ›", then one sentence with counts ("Ran 2 commands, changed 2 files"), then typed one-line rows, then detail. Keep the answer and the changed-files card outside the fold. Never fold a failure.
2. **The answer is a document.** No bubble around AI output; a reading measure of 680-768px; a distinct typographic voice for generated prose (a reading serif or style), sans for UI and data, mono for codes. Only the human's turn is boxed.
3. **One composer.** One fixed primary slot that morphs (send, stop, steer, queue, resume); mode or autonomy and model as small pills inside the composer; context as visible, removable chips; the input never locks during a run.
4. **Approval is proportional to rollback cost.** Cheap to undo: apply first, review after, undo per item, file and turn. Expensive or impossible (send, pay, post, deploy, write elsewhere): stage the result, and commit with a button that names the consequence ("Send to Alex", "Apply 3 changes", "Buy all · 3 items, $345"). Money approvals are single-use, time-boxed and void if anything changes.
5. **Approvals sit at the action.** Quote the exact command or effect on the row it affects; keep Decline next to Approve; let the input become the place to explain a decline. Show a pending state on the clicked decision.
6. **Agents prepare, people commit.** Every run with side effects ends on the prepared state and one yes/no question.
7. **Provenance one gesture away.** Every generated claim carries a quiet source marker that opens the exact source; stream sources before the prose; label every number's state (live, estimate, as of).
8. **Proposals look different from truth.** Dashed chips, grey ink or a pending state until accepted; never silently overwrite the human's original; log AI edits under a named author.
9. **Stop where the agent acts.** A stop or pause on the surface being acted on, mirrored in the input, labelled with its key ("Stop response (Esc)"). A stopped run names what stopped.
10. **Human attention is the bottleneck.** With several runs in flight, "needs you" is the first section and the only loud badge. A closed, tiny vocabulary for "your turn" states, shown on the object, its row and the notification.
11. **Cost is ambient.** Cost at the moment of choice in the plan's unit, per-run cost in the receipt, usage as a small meter; at a limit, degrade rather than dead-end.
12. **Say it in words, keep it still.** Status is a word plus a timer; only the working label moves; nothing else loops.

## Choosing the gate

| The action | Undo exists? | Pattern |
|---|---|---|
| Edit a local file, draft, document block | Yes (checkpoint, version) | Apply, then Keep / Undo per hunk, file and turn |
| Reorganise, tag, assign, link records | Yes (activity log) | Dashed suggestion chip; accept with a click or key; auto-apply only per-field opt-in |
| Bulk change across many records | Partly | Dry run on one view ("Try on this view"), then "Apply to all 240" |
| Run a shell command, call a tool with side effects | Sometimes | Permission mode (ask / auto-accept edits / auto / full access), with inline approval on the action row |
| Send, post, publish, deploy, pay, book | No | Stage, then a commit button naming recipient, amount and effect; single-use, time-boxed approval |
| Spend shared money or reputation | No | All of the above plus who handles the after-care and where the result will be listed |

## Pattern index

Full anatomy, states and measured values for each are in [references/patterns.md](references/patterns.md).

- **Input:** morphing composer slot · composer pills · attached tray menu · scoped composer · context chips and manifest · composer-as-form · steer vs queue vs stop · saved prompts that expand · intent kept through sign-in
- **Progress:** status line with timer · synced shimmer · work ledger · turn receipt · reserved output card · agent state pill · motion signature per agent state · tasks surface
- **Output:** answer-as-document · typed voice per speaker · AI answer rendered as native components · box only what has a next step · follow-up chips from the result set · stream order (sources, data, prose)
- **Trust:** citation chip and hover card · provenance magnifier · source ratings · evidence drill-down with counts · verbal uncertainty · as-of stamps · compute in code, narrate in words
- **Proposals and recovery:** dashed suggestion chip · two-ink authorship · proposal bar · step-through review · original/AI toggle · append-only versions · checkpoint rewind and fork · visible self-correction · explanation leads to correction
- **Agency:** inline approval at the action · permission modes as consequences · consequence-named commit · single-use money approval · handoff vocabulary · stop on the acted surface · control hue on the driven frame · read / write / spend permissions · contestable safety calls
- **Cost and access:** context meter · usage with pace marker · unit price at choice · locked door with `next=` · limit that degrades · value receipt instead of paywall
- **Memory and privacy:** privacy mode shown in three places · memory as named, dated, deletable items · per-object AI visibility

The rule set behind them, grouped by input, streaming, recovery, evidence, agency and trust, is in [references/rules.md](references/rules.md). The category playbooks (chat, coding, notes, creative, browsers, mobile, health, finance, shopping, ops) are in `product-ui` under `references/categories/`.

## Review questions

Before calling an AI surface done, answer each with a screenshot:
1. Is every state in the universal set designed, including stopped, gated and needs-input?
2. While it works, is exactly one thing moving, and does it say what it is doing with a timer?
3. When it finishes, is the default view the result, with the process one click away and failures unfolded?
4. Can the user see what the answer is based on, in one gesture, for every claim and number?
5. Does every irreversible action stop on a staged state with a button that names its consequence?
6. Can the user stop, steer and undo at the granularity of the work (item, file, turn)?
7. Is AI-proposed content visually distinct until accepted, and is the original always recoverable?
8. With several runs, does "needs you" sort first and nothing else badge?
9. Is cost visible where it is chosen, and does a limit degrade instead of dead-ending?
10. Does the input stay usable during a run, and does typing never trigger an approval by accident?
