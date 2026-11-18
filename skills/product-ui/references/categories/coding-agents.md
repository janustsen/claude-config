# Coding agents

Coding agents are products where an AI writes, edits and runs code on the user's behalf: AI editors that grew an agent workbench, and prompt-to-app builders. The work itself is cheap for the machine; the scarce resource is the human's attention. Users judge the category on one question: how fast can I tell whether what the agent did is right, and get back if it is not? The two studied apps answer it differently. Cursor treats the human as a reviewer of code and optimizes reading and rejecting diffs. v0 treats the human as a judge of outcomes and optimizes seeing and nudging the rendered result. Both converge on the same skeleton: a composer with mode and model pills, a compressed work log, a reserved output surface, and cheap rollback.

Studied:
- **Cursor** (AI code editor plus Agents Window, CLI, web, iOS). Logged out, the marketing site renders the real product UI as live HTML mocks built on the product's own tokens (`--text-product-*`), so sidebar, transcript, tool rows, Plan-mode question card, model menu, chips and checkpoint timeline were measured from the DOM [obs]. Docs, help center and changelog [doc]. The desktop app and the web agents page (behind auth plus a bot challenge) were not reachable, so per-hunk Keep/Undo details are [doc] or [know].
- **v0 by Vercel** (prompt-to-app builder). Submitting a prompt logged out runs a real anonymous generation, so the builder, streaming, work log, workspace tabs, preview toolbar, device toggle, Design mode and every menu were observed [obs]. The preview iframe failed to load, the code tree stayed on its skeleton, and Publish, versions and settings need an account [doc]/[know].

## What users expect

1. **A review surface with accept and reject**, because agent output is only useful once a human has judged it. Engineers expect a diff; outcome owners expect a live preview.
2. **The active model always visible**, because cost, speed and quality follow the model.
3. **Undo at more than one size** (hunk, file, whole turn or version), because people reject at the level where they noticed the problem.
4. **Terminal and tool execution with an approval policy** (ask, allowlist, run everything), because commands can do damage outside the repo.
5. **Proof of work without reading the work**: a compressed, auditable log of what the agent read, ran and changed.
6. **A way to talk to a running agent** (queue, steer, stop), because runs last minutes to hours.
7. **Exact context attachment** (files, lines, elements, screenshots), because "change this" needs a precise referent.
8. **Familiar foundations**: VS Code bindings and extensions for editors; templates, device toggles and one-click deploy for builders. These are table stakes; users notice only when missing.
9. **Visible cost and limits**, because metered agent runs can burn a budget silently (see L15).
10. **Parallel work that stays legible**: several agents or best-of-N runs in isolated worktrees, each showing its own state and model, because the newest bottleneck is supervising many runs at once. (Cursor `/best-of-n`, subagent cards [doc][obs])

## The theses to choose from

### Cursor: the human is a reviewer of code
Core bet: apply the agent's edits immediately and make review-after-the-fact fast and safe, with autonomy as a slider rather than separate products.
- **Ready-for-review queue as home.** The Agents Window sidebar's first section is "READY FOR REVIEW 5"; each row has a status glyph, a 12px title, a right-aligned relative time and a second line in 40% ink with colored diff stats (`+20 -3`) or a one-line outcome [obs]. Implements L17 for agent runs.
- **Autonomy as one pill.** Mode pill (Agent / Plan / Ask / Debug) cycled with Shift+Tab, model pill cycled with Cmd+/ [obs][doc]. Each mode has its own context window, so switching starts fresh [doc].
- **Transcript as a compressed log.** One 12px gray line per tool call, verb and object in two tones (60% and 40% ink), finished runs collapsed into counts ("Explored 12 files, 4 searches", "Worked for 14m 22s") [obs].
- **Three undo granularities.** Per-hunk Keep/Undo, per-file Keep File/Undo File with "N of M" navigation, whole-turn checkpoints; Cmd+Return accepts all, Cmd+Shift+Backspace rejects all [doc][know].
- **Queue, steer, interrupt.** Enter queues while busy, Cmd+Enter sends now, steer messages land at the agent's next tool-call boundary [doc].
- **Context ring.** A fill ring next to the input opens a token breakdown (System prompt / Tools / Rules / Skills / MCP / Subagents / Summarized conversation / Conversation) [doc].

Choose this when the user owns the codebase, reads code fluently, and rollback is cheap (local checkpoints, git).

### v0: the human is a judge of outcomes
Core bet: show the result, not the code; let anyone generate before signing up; make every change a version so "going back" is never scary.
- **Generate before sign-up.** The landing page is one 690px composer under "What do you want to create?"; submitting it logged out runs a full generation under an anonymous identity. Only save, share and publish are gated (L13) [obs].
- **Layout flips on first output.** Before an artifact exists the chat is a centered column (about 740px). When it lands, the chat shrinks to a 320px left rail and the right pane becomes a tabbed workspace defaulting to the rendered artifact or App Preview; Code, Diff, Database, Logs, Terminal and Settings hide behind "+" [obs].
- **Append-only versions.** Each code-changing message makes a version; restoring v2 creates v5; Design-mode Apply also makes a version [doc].
- **One live step.** Only the current step label shimmers (650ms linear); finished steps freeze to static `#8f8f8f`; the turn collapses to "Worked for 1m 8s" with steps and "used 0.224 credits" inside [obs].
- **Reserved artifact card.** "Creating artifact… / Your artifact will appear here." in a card the size of the final preview, with a 1500ms diagonal sweep (L14) [obs].
- **Staged visual edits.** Design mode holds tweaks as pending with Undo / Redo / Reset / before-after until Apply [obs][doc].

Choose this when the user judges by looking (designers, PMs, first-time builders) and the output is a UI whose correctness is visible.

## Comparison

| Dimension | Cursor | v0 |
|---|---|---|
| Where the proposal appears | In the code: ghost text, inline diff hunks, file-change cards (`+52 -0`), review queue [obs][doc][know] | In a rendered preview: artifact card in chat, App Preview tab with device frame; code and diff are opt-in tabs [obs] |
| How the human approves | After the fact: edits already written; Keep/Undo per hunk or file, accept-all/reject-all chords, checkpoints [doc] | By looking and iterating: follow-up prompts, staged Design edits, restore a version; "approval" is Publish [obs][doc] |
| Default right pane | Editor or Agent Changes; preview is a tab [doc] | Rendered artifact or App Preview [obs] |
| Progress display | One-line two-tone tool rows, grouped counts, persistent todos, subagent cards with model names, all working rows shimmer in sync on 1.6s [obs] | Single active step shimmering at 650ms, collapsible "Worked for X" with credits, reserved placeholder card [obs] |
| Context attachment | Inline type-colored chips (@files, @Terminals, @Chats, @Branch, @Browser), selection to chat, Design Mode element notes [obs][doc] | Drop-to-attach on the whole composer, code-line comments as removable annotations, element screenshots [obs][doc] |
| Autonomy control | Mode pill (4 modes), run modes Auto-review / Allowlist / Run Everything [doc] | Model pill, terminal permission Ask / Auto (default) / Full [doc] |
| Talking to a running agent | Queue (Enter), send now (Cmd+Enter), steer at next tool call, Esc stops in CLI [doc][obs] | Queue (⌥↵, shown in placeholder), Send morphs to Stop [obs] |
| Recovery unit | Hunk → file → checkpoint (files only) → fork (conversation) [doc] | Version (append-only), Duplicate chat, Design Undo/Reset before Apply [doc][obs] |
| Cost display | Model name in composer, context % in CLI, Switch Model next to Buy Credits at the limit [obs][doc] | Credits used per turn inside the work-log disclosure [obs] |
| UI density | 11-13px product text, 16px leading, 219px sidebar [obs] | 13-14px UI text, 26-28px controls, 320px chat rail [obs] |
| First-run gate | Download for detected OS, no form; web agents behind auth [obs] | Full generation anonymous; Free plan 7 messages/day [obs][doc] |
| Phone | Separate iOS/web app with Agent and Dashboard tabs [obs][doc] | Segmented "Chat \| Preview" toggle; Design mode removed [obs][doc] |

## Category rules

### Layout
1. **Show the proposal where the user's judgment lives:** a diff for people who own the code, a rendered preview for people who own the outcome. Pick the default right pane accordingly, because the decision happens at the artifact, not at a chat message about it. (Cursor diff-first, v0 preview-first [obs][doc])
2. **Hold a single centered column until there is output, then split** into a fixed rail (about 320px, draggable divider) plus a fluid workspace, because an empty preview pane at t=0 makes the product look broken. (v0 [obs])
3. **Put rarely used tools (DB, logs, terminal, settings) behind one "+" tab menu**, because a permanent strip of eight tabs intimidates the users who never open them. (v0 [obs])
4. **Make every workspace tab a URL** (`/chat/<id>/diff`, `/chat/<id>/code`), because people share "look at the diff" links. (v0 [obs])
5. **Open child conversations (side chats, subagents) as tabs beside the parent, never replacing it, and persist every view's state (scroll, tabs, collapsed sections) across restarts**, because losing parent context is the cost of branching and agents run for hours while the user is away. (Cursor [doc])
6. **Center the transcript at about 580px max inside a wide pane, user-overridable**, because line length matters more than pane width. (Cursor [obs][doc])

### Composer and running-agent control
7. **Tint every affordance of a non-default mode with that mode's color** (Plan pill and the Plan question's Continue button both amber `#C08532`), because the user must know which mode is asking. Extends L12. (Cursor [obs])
8. **Give a sticky reusable instruction (skill as Custom Mode) a visible colored badge in the composer**, because invisible persistent state is the main source of "why is it doing that?". (Cursor [doc])
9. **Offer queue, steer and interrupt as three distinct key paths, and deliver steer at the next tool-call boundary, never mid-action**, because "wait", "adjust" and "stop" are different intents and a mid-action interrupt corrupts work. Print the queue chord in the busy placeholder ("⌥↵ to queue"). (Cursor [doc], v0 [obs])
10. **Morph Send into Stop only for short runs; keep Send on long orchestrators and give Stop its own place**, because a mis-click on a morphing button can kill hours of coordinated work. (Cursor Projects keep Send [doc]; v0 morphs for minute-long runs [obs])
11. **Render references as inline chips inside the sentence, colored by type** (code blue `rgb(58,106,159)` on 15%, web gray `rgb(107,114,128)` on 12%, radius 4px), because the user writes naturally while the system gets exact anchors. (Cursor [obs])
12. **Delete manual context categories once the agent can gather them itself**, because every @-type is a decision the user should not have to make. (Cursor 2.0 removed five [doc])
13. **Make suggestion chips write a full, specific, editable prompt into the composer without sending**, because it teaches what a good prompt contains and keeps the user in control. (v0 [obs])
14. **Ask for notification permission during the first long run** ("Get notified when v0 finishes", Enable / ×, above the composer), never on load, because permission converts when the value is obvious. (v0 [obs])

### Output and progress
15. **Write each tool call as a past-tense verb plus object on one 12px line, verb and object in two ink tones, and collapse a finished run into counts**, because proof of work should cost one line. This is the coding-specific form of L5. (Cursor [obs])
16. **Use present progressive for the live step and past tense once done** ("Reading contact form" → "Built contact form"), because tense alone tells the user what is live. (v0 [obs])
17. **Shimmer only live rows, and run all of them in phase on one clock** (Cursor `shimmer-synced` 1.6s linear; v0 single active step 650ms), because out-of-phase shimmers read as noise. Refines L6. (Cursor, v0 [obs])
18. **Give file changes their own card with colored counts** (green `#1f8a65`, red `#cf2d56`; inserted lines 8% green, removed 6% red) and repeat the counts in the sidebar row, because "what did it touch, and how much" is the first review question. (Cursor [obs])
19. **Keep todo lists after completion, and name the model on each parallel subagent card** ("Editing files • Opus-5.5", dimmed "Pending • …"), because a finished list is the receipt and cost follows the model per task. (Cursor [obs][doc])
20. **Let the agent ask clarifying questions as an inline numbered option card above the composer (Skip as text, Continue as the only filled button) and keep working while it waits**, because a blocking modal turns a quick clarification into dead time. (Cursor [obs][doc])
21. **End each turn with honest scope, a measurable outcome and one proposed next step** ("I haven't tested it in a browser", "280ms first paint", "I can build that next"), because concrete claims are reviewable and overclaimed code is the category's trust killer. (v0, Cursor [obs])
22. **Acknowledge a long task within a second with a short plan line, then hold noisy setup in one stable status row ("Setting up project") until real output exists**, because silence in the first 10 seconds and reflowing setup logs both read as failure. (Cursor [doc])

### Review and recovery
23. **If edits are applied before review, ship three undo sizes (hunk, file, turn) and bind accept-all and reject-all to chords**, because apply-then-review is only safe when rejection is instant at every scale. Specializes L9. (Cursor [doc][know])
24. **Separate "restore files" from "rewrite the conversation"** (checkpoint restore keeps messages; fork shortens the chat), because users want the code back without losing the reasoning trail. (Cursor [doc])
25. **Make restore append-only** (restoring v2 creates v5; deploy uses the latest), because non-technical users understand "go back to v3" only if it never deletes v4. Specializes L10. (v0 [doc])
26. **Stage direct-manipulation edits as pending with Undo, Redo, Reset and before/after, then Apply them as one normal version**, because visual tweaks need a sandbox before they touch code. (v0 [obs][doc])
27. **Pause manual editing while the agent writes, and show an "Unsaved Changes" bar with Save (⌘S) or Discard for hand edits**, because two writers on one file produce silent conflicts. (v0 [doc])
28. **Offer "go back to the plan" and a one-click "Fix" that carries the logs** (Fix with v0 on deploy errors; Bugbot "Fix in Cursor"), and refuse an apply that would write broken output (an oversized cloud diff warns and blocks Apply), because re-running a corrected spec beats patching, users cannot be expected to paste stack traces, and a silent partial apply is worse than none. (Cursor, v0 [doc])

### Trust and cost
29. **Put the cheaper-model escape next to the upsell at the limit** (Switch Model beside Buy Credits), because "pay" as the only option at a hard stop feels like extortion. Extends L15. (Cursor [doc])
30. **Show per-turn cost inside the turn's collapsed work log, next to the timestamp**, because a balance that only drops on a settings page is a hidden meter, and the default view should still be the result. (v0 [obs])
31. **Surface sandbox status in the preview toolbar overflow** ("● Running · 4m" with a power button) and say when a command runs outside the sandbox, because users need to know why a preview is blank and when the safety net is off. (v0 [obs], Cursor [doc])
32. **State the limits of your own safety features in plain words** ("Auto-review is not a security boundary"), because overclaimed safety erodes trust the first time it fails. (Cursor [doc])

### Mobile and first run
33. **On phones, replace the side-by-side split with a full-width "Chat | Preview" segmented toggle and keep the composer docked at the bottom; drop precision tools like visual editing**, because both panes need full width and a cramped editor costs more trust than a missing one. (v0 [obs][doc])
34. **Decay a discovery label to icon-only after repeated use** ("Try Annotate" shrinks after more than 5 notes), and keep the incumbent's default shortcuts, because novices need words, experts need space, and switching cost is muscle memory. (Cursor [doc])
35. **Offer a lightweight single-file output with an explicit upgrade action** ("Build App: Build this artifact into a project"), because most first prompts do not need a database and a full sandbox is slow. (v0 [obs])

## Measured constants

| Item | Value | App, tag |
|---|---|---|
| Product text sizes | 11 / 12 / 13px, leading 1.27-1.33 | Cursor [obs] |
| Agents sidebar | 219px; section header 11px uppercase 500, 60% ink, padding 4px 12px; two-line row about 51px | Cursor [obs] |
| Transcript max width | 580px | Cursor [obs] |
| Composer | 1px border at 10% ink, radius 8px, no shadow, padding 10px 12px 8px, 13px text | Cursor [obs] |
| Send button | 20px circle, `#e1e0db` idle | Cursor [obs] |
| Mode pill (Plan) | 11px text `#C08532` on 15% amber, padding 3px 8px, fully rounded | Cursor [obs] |
| Question Continue | 12px/500, radius 4px, padding 2px 6px, amber | Cursor [obs] |
| Mention chip | 13px, radius 4px, padding 1px 6px; code `rgb(58,106,159)` on 15%, URL `rgb(107,114,128)` on 12% | Cursor [obs] |
| Diff colors | green `#1f8a65`, red `#cf2d56`; line bg 8% green, 6% red | Cursor [obs] |
| Ink alphas | text 100 / 92 / 60 / 50 / 40%; borders 2.5 (default) / 5 / 10 / 20 / 60% | Cursor [obs] |
| Model menu | about 180px wide, 13px rows about 28px, shadow `0 0 1rem #00000005, 0 0 .5rem #00000002` | Cursor [obs] |
| Working shimmer | 1600ms linear infinite, all rows in phase; mobile dot grid 3100ms | Cursor [obs] |
| Motion | 140ms micro, 250ms panel, `cubic-bezier(.25,1,.5,1)`; hover bg 120ms; popover exit `visibility 0s linear var(--duration)` | Cursor [obs] |
| Surface and ink | bg `#f7f7f4` / dark `#14120b`; ink `#26251e` / dark `#edecec`; cards `#f2f1ed` to `#e1e0db` | Cursor [obs] |
| Spacing unit | 10px base (`calc(10rem/16)`) with fractional steps; vertical unit 22.4px | Cursor [obs] |
| Accent | orange `#f54e00` on text links only, never on buttons | Cursor [obs] |
| Radii | 2 / 4 (chips) / 8 (composer, cards) / 12 / 16 / 24px; buttons 9999px | Cursor [obs] |
| Landing composer | 690px wide, 108px tall (122px at 3 lines), radius 12px, 1px `#c9c9c9`, padding 12px, 14px/20px | v0 [obs] |
| Send button | 28x28, radius 6px; disabled `#f2f2f2` with `#c9c9c9` icon; enabled `#171717` | v0 [obs] |
| Builder | header 50px (1px `#f2f2f2` bottom); chat rail 320px, padding 20px; workspace 1120px at 1440 | v0 [obs] |
| Workspace tabs | 141x26px, radius 8px, 13px/500; unselected `#7d7d7d` | v0 [obs] |
| File tree | 176-480px, default 240px | v0 [obs] |
| Menus | radius 12px, border `rgba(0,0,0,.08)`, rows about 32px, 14px text; model menu 288px | v0 [obs] |
| Preview toolbar | centered pill about 500px, row about 44px | v0 [obs] |
| Device frame | 360px wide, radius 12px, resize 200ms `cubic-bezier(0.31,0.1,0.08,0.96)` | v0 [obs] |
| Chat prose | 14px/22.75px; work log 13px/21px `#8f8f8f` | v0 [obs] |
| User bubble | `#ebebeb`, radius 16px, padding 6px 12px, max about 600px | v0 [obs] |
| Shimmers | active step text 650ms linear; placeholder sweep 1500ms linear at 110°; skeleton pulse 2000ms | v0 [obs] |
| Default transitions | 150ms `cubic-bezier(0.4,0,0.2,1)`; composer border 200ms signature ease | v0 [obs] |
| Radii | 6px buttons, 8px tabs, 12px composer/menus/frames, 16px bubble | v0 [obs] |
| Neutrals | page `#fafafa`, ink `#171717`, secondary `rgb(77,77,77)`, muted `#8f8f8f`, disabled `#c9c9c9`; black alpha 5 / 8 / 10 / 21%, borders mostly 8% | v0 [obs] |
| Ring-plus-shadow | `0 0 0 1px` alpha-8% ring inside the elevation stack, e.g. `0 0 0 1px a8, 0 2px 1px #0000000a` | v0 [obs] |
| State color | blue `rgb(0,98,209)` only when Design mode is on; green dot = live; red = error | v0 [obs] |

## Anti-patterns seen

- **Raw auth error in a popover.** v0's Share shows a red "Unauthorized" with no reason or sign-in action [obs]. Fix: "Sign in to share" with the sign-in button in the same popover (L16), because this is the moment the user is deciding to sign up.
- **Error without reason or retry.** v0's preview says "This artifact could not be loaded." [obs]. Fix: name the cause (auth, sandbox stopped, build failed) and offer Retry or Fix, because users otherwise blame the generated code.
- **Icon buttons without names.** v0's Stop button and preview toolbar icons (device, open, refresh) have no accessible name [obs]. Fix: give every icon-only button an aria-label.
- **Symptom wording on blocked runs.** Cursor once showed "Couldn't start" for blocked commands; it now says "Approval required" / "Approval denied" [doc]. Fix: word by cause.
- **Empty-looking loading.** Cursor's Library tabs used to look empty while loading or after failure; now they show a loading state or an error [doc]. Fix: three distinct states, never "empty" for "loading".
- **Silent bad apply.** An oversized cloud diff used to write empty files; now Cursor warns and blocks Apply [doc]. Fix: refuse and explain.
- **Reflowing setup.** Cursor Projects used to reflow through environment steps; now one "Setting up project" row holds until output [doc].
- **Context reset hidden in a mode switch.** Cursor starts a fresh context window on every mode change [doc]. If you copy this, say so in the mode menu, because users otherwise read the agent's lost memory as a bug.
- **Locked-looking choices.** Cursor styled disabled-but-selectable models as "not allowed"; picking one now enables it [doc]. Fix: style what is selectable as selectable.

## Steal list

1. Do group agent runs under "Ready for review (N)" with per-row colored diff stats, because the user's job in an agent product is triage.
2. Do pick the default right pane by who judges: diff for code owners, preview for outcome owners, because the decision happens at the artifact.
3. Do start in one centered column and split into a 320px rail plus workspace only when output exists, because empty panes look broken.
4. Do write tool calls as one-line, past-tense, two-tone rows and collapse finished runs into counts, because proof of work should cost one line.
5. Do tint every affordance of a non-default mode with the mode's color, because the user must know which mode is asking.
6. Do give queue, steer (at the next tool-call boundary) and interrupt separate keys and print the queue chord in the busy placeholder, because they are three different intents.
7. Do keep Send as Send on long-running orchestrators, because accidental cancellation is the costliest mis-click.
8. Do render prompt references as inline type-colored chips, and remove @-categories the agent can gather itself, because chips are exact and every category is a decision.
9. Do show a context-fill ring with a click-through token breakdown, because invisible context limits produce "it forgot" complaints.
10. Do ship hunk, file and turn undo with accept-all and reject-all chords whenever edits apply before review, because review after the fact only works when rejection is instant.
11. Do separate "restore files" from "fork conversation", and make version restore append-only, because users want the old code without losing newer work or the reasoning.
12. Do stage direct-manipulation edits as pending until Apply, with undo, reset and before/after, because visual tweaks need a sandbox.
13. Do make suggestion chips fill the composer with a rich editable prompt instead of sending, because it teaches prompting.
14. Do ask clarifying questions as inline numbered option cards and keep working while waiting, because blocking modals waste both parties' time.
15. Do end turns with what was not verified, a measured outcome and a next step, because honest scope prevents false confidence in generated code.
16. Do put per-turn credits inside the turn's work-log disclosure and a Switch Model option next to Buy Credits, because hidden meters and pay-only walls both erode trust.
17. Do request notification permission during the first long run, because value-timed prompts convert.
18. Do convert chat and preview to a "Chat | Preview" toggle on phones and drop visual editing there, because both panes need full width.
