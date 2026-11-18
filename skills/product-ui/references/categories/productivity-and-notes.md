# Productivity and notes

This category covers AI added to a tool people already own and use all day: an issue tracker (Linear), a doc and database workspace (Notion AI), a meeting notepad (Granola). The user arrived for the tool, not for the AI, and already has objects, habits and words in it. The question users judge it on: does the AI make my existing work faster without taking ownership of it away from me? Every studied app answers by putting AI on the objects users already know (rows, blocks, notes; see L11) and keeping the human visibly in charge of what is true. Linear is also this guide's reference for any dense, keyboard-first work tool, so its anatomy and measurements are given in full below.

Studied:
- **Linear** (issue tracker with its own agent and third-party agents). Logged out, the homepage renders a 1320x720 live HTML/CSS replica of the app (sidebar, issue detail, activity feed, agent panel, board, grouped list, diff) on the real tokens, which is the source of most measurements [obs]. Feature pages, changelog and docs, plus vendor screenshots of the real logged-in app (list, multi-select, composer, context menu, inbox, delegation, filters, display options) [doc]. The real ⌘K menu, settings and onboarding were not reachable [know].
- **Notion AI** (AI layer inside Notion's editor and databases). Marketing pages including a live HTML replica of the AI Meeting Notes block, public read-only `notion.site` pages with Notion's real renderer and tokens [obs]. The logged-in inline AI bar, chat panel, Autofill, version history and model picker come from Notion's help screenshots, release images and a marketing video [doc].
- **Granola** (AI meeting notepad, desktop and mobile). The homepage hero is a live HTML replica of the note window cycling through typing, transcribing, generating and the enhanced note [obs]. App states come from Granola's help-center screenshots [doc]. The app itself was not opened.

## What users expect

1. **AI where the work already is**: on the row, the selection, the block, the note, because leaving the work to "go to the AI" breaks flow.
2. **Output that lands as native objects** (rows, properties, blocks, notes), because users edit, move and share with tools they already know.
3. **Their own words and records never silently overwritten**, because their notes and issues are their proof and memory.
4. **A visible answer to "who did this?"** for every AI or agent change, because these are shared team records.
5. **Speed as a felt quality**: instant hover, single-key verbs, no waiting on the tool itself, because they live in it for hours.
6. **AI suggestions they can accept field by field**, not all or nothing, because trust in automation is earned per property.
7. **Privacy by default for content about other people** (meeting notes, transcripts), because it holds other people's words.
8. **A model choice that is visible but not demanded**, because most users never want to pick one.
9. **Import and familiar shortcuts from the incumbent**, because switching cost is muscle memory and data, not features.

## The theses to choose from

### Linear: agents are teammates on the same rails
Core bet: a fast, near-monochrome instrument where every object is a row with inline properties, every property is a keyboard verb, and agents appear inside the existing rails (assignee, activity feed, status) instead of an AI area.
- **Agents as delegates under a human.** The properties rail nests the agent under the human assignee with a tree connector (assignee └ "Linear" agent) [doc]. Agent Interaction Guidelines: "An agent cannot be held accountable" and must never be "mistaken for a person" [doc].
- **One timeline.** Agent and automation actions write into the same activity feed with the same grammar, plus provenance: "Linear created the issue via Slack on behalf of <person> · 2min ago", "Triage Intelligence added the labels Performance and iOS" [obs].
- **Explicit agent state.** Session states `pending / active / error / awaitingInput / complete / stale` ("visible to users"); card pills "Working…", "Waiting", "Error", "Finished" [doc][obs].
- **Dashed means proposed.** Triage Intelligence suggestions are dashed-outline chips; accepted ones go solid with a check (applies L8) [obs].
- **Fake-busy is a bug.** "Coding sessions now show an error when their sandbox fails to start ... instead of looking busy" [doc].

Choose this when the product is a shared system of record with many objects, power users and agents doing assignable work.

### Notion AI: AI is a guest in the document
Core bet: AI is attached to an existing object at the distance that fits the task (cursor, page, workspace), returns proposals, and once accepted its output is ordinary content with attribution kept in history.
- **Three distances.** Space or selection opens an inline bar under the selected text; a 48px face button bottom-right opens a floating or sidebar chat with the page as context; "Notion AI" in the sidebar opens full-page chat and agents (the L11 pattern, built out) [doc].
- **Proposals, then attribution.** Inline edits come back as accept / discard / try again; "suggest edits" mode lets the user step through each change top to bottom; external writes ask for confirmation; the agent appears in version history as an author ("Notion App") with its own color dot [doc].
- **Column-level AI marking.** Autofill fills ordinary cells; the only mark is a small gray "AI" badge after the property name in the header, and "Try on this view" runs before "Fill all pages in Tasks" [doc].
- **Narrated work and citations.** Meeting summaries show a step checklist with one shimmering live step, then numbered 18px citation chips that preview and jump to the transcript line [obs].

Choose this when content is collaborative and multi-author, and AI output should become the user's own text once accepted.

### Granola: the human writes first, the AI writes around them
Core bet: capture is ambient (no bot), the user types sparse notes, and afterwards the AI expands them while keeping the user's own words visibly theirs.
- **Authorship by ink.** Human-derived lines in `#292929`, AI-added lines in `#72726E`, same font, size and weight [obs][doc].
- **Original always one click away.** A "My notes | Enhanced" two-state toggle; raw notes are never overwritten, and editing them then regenerating uses the edits [obs][doc].
- **One morphing spot.** A white "Transcribing" pill bottom-center becomes a dark "Generate notes" pill in the same place and shape, then the note shows the "My notes | Enhanced" toggle [obs].
- **Generation at the frontier.** An "Enhancing notes" pill rides just below the newest line; each line arrives with a colored write-head and settles into its final ink in 0.4-0.9s [obs].
- **Line-level provenance.** Hover a bullet, click 🔍, get "TRANSCRIPT SUMMARY": one reasoning sentence plus a verbatim quote box (applies L7) [doc].

Choose this when the content is personal, about other people, and must be verified before it is trusted: summaries, notes, pre-reads.

## Comparison

| Dimension | Linear | Notion AI | Granola |
|---|---|---|---|
| Where AI lives | Assignee menu, activity feed, triage card, ⌘J agent chat panel (400x520) [obs][doc] | Inline bar at selection, `/` AI blocks, corner face to chat, sidebar destination, property header (Autofill), meeting block [doc] | One floating bottom bar (record, transcript, chat, recipe chip) plus one top-right toggle [doc] |
| Who writes first | Human files, agent works on delegated issues | Either; AI can generate from nothing | Human, sparsely; AI after the meeting |
| AI marking | Dashed chips until accepted; agent badge; "on behalf of" in feed [obs][doc] | None on accepted text; "AI" header badge, citations, history author color [doc][obs] | Permanent gray ink `#72726E` vs `#292929` [obs] |
| Accept flow | Accept / decline / view reasoning per suggestion; 1 / 2 / 3 / H in triage [doc] | Accept / discard / try again; step-through suggest edits; confirm external writes [doc] | No accept step; safety from the untouched original plus regenerate [doc] |
| Automation dial | Per team and property: show, auto-apply or hide [doc] | Dry run "Try on this view" before "Fill all" [doc] | Templates pick the lens; auto-generate on call end [doc] |
| Progress | "Thinking…" shimmer, "Setting up … 00:07" timer, state pills, "Worked for 10 sec ▸" [obs] | Named step checklist with one shimmering step [obs] | Traveling status pill plus write-head [obs] |
| Provenance | Activity feed with actor, "via Slack", "on behalf of" [obs] | Numbered citation chips, version history diff [obs][doc] | Hover 🔍 with reasoning plus quote [doc] |
| Accountability | Human owner with nested agent delegate [doc] | Agent is a named author in history [doc] | User is the only author; AI is secondary ink |
| Default privacy | Workspace permissions; agent "operates within your existing permissions" [doc] | Agent "has the same permissions you do" [obs] | Private by default; viewers get summary, not transcript [doc] |
| Command surface | ⌘K for everything, single keys, `?` sheet [doc] | `/` menu for AI and blocks, space for AI [doc] | `/` templates in notes, `/` recipes in chat, ⌘J chat [doc] |
| Model choice | Model tag on agent panel ("Opus 5.5"), BYOK [obs][doc] | "Auto: Balances speed, effort, and cost." default [doc] | Named in the chat pill; free plan Auto only [doc] |
| Hover feedback | 0ms in, 150ms out [obs] | 20-80ms [obs] | 200-300ms (marketing) [obs] |

## Reference anatomy: Linear as the dense keyboard-first work tool

Build any dense work tool (tracker, CRM, ops console) from these measurements. The general laws are L1-L3, L17-L19; what follows is the exact anatomy.

### Shell [obs]
- Inverted L: one left sidebar plus one header row per view; content sits in an inset view card (1px `rgba(255,255,255,.05)` border, 8px radius, 1% white fill, outer ring `0 0 0 2px rgba(0,0,0,.2)`), because a stable frame lets content change without re-orienting.
- App frame 1320x720, 12px radius, 8px inner padding, bg `rgb(9,10,11)`. Main view card 1072x704, 8px radius.
- Z-index as named tokens: header 100, overlay 500, popover 600, command menu 650, dialog 700, toasts 800, tooltip 1100, context menu 1200, skip-nav 5000, because ad-hoc z-indexes collide.

### Sidebar [obs][doc]
- Width 232px, padding 8px 16px 16px 8px. Header row: workspace switcher "Name ▾", search and new-issue as 28px circles (new-issue bordered 1px `#24282c`, 2% white fill).
- Order: personal (Inbox, My issues, Pulse, Reviews) → "Workspace ▾" (Initiatives, Projects, Views, More) → "Favorites ▾" → "Your teams ▾" (team ▾ with Triage, Issues, Cycles, Projects, Views).
- Nav item 208x28, 2px gap (30px pitch), padding-inline 7px, 14px icon with 8px gap, label 13px/510. Section header 24px, 12px/510 quaternary, padding 4px 0 4px 6px, about 18px of space before it.
- Icons a tier dimmer than labels (`#62666d` vs `#d0d6e0`); hover 2% white, active 4% white. The 2026 refresh made the sidebar "a few notches dimmer, so main content takes precedence" [doc].
- Counts only where action is pending (Inbox "1", Triage "39"), right-aligned in small rounded squares. Rarely used items can be set to "always appears, only when badged, or never" [doc].

### Row anatomy [obs]
- **List row**: 40px tall (36-44px in the real app [doc]), full width, padding 0 28px 0 36px, cells with 8px gap: `[priority glyph][ID][status icon][title…]`, then right-aligned labels, PR number, date, avatar.
- ID 13px/400 `#8a8f98` in a fixed column about 72px wide, so titles start on one vertical line. Title 13px/510 `#d0d6e0`, truncates first. Right-side meta 12px `#8a8f98`.
- **Group header**: 36px, 2% white fill, 8px radius, 8px padding, title 13px/510 plus count (estimate sums like "2 / 11" [doc]). Hover shows "+" and "⋯"; `T` on a hovered header collapses it.
- **List panel**: `#0f1011` with inset ring `0 0 0 1px #23252a`, top radius 12px, inside an outer 1px 8% white container with 22px radius and 8px padding (concentric double bezel).
- **Board card**: 300x96, `#0f1011`, 1px `rgba(255,255,255,.08)`, 9px radius, padding 8px 10px 12px 12px; 300px columns, 8px gap. ID drops to 10px quaternary on cards (title first), stays 13px tertiary on lists (scan by ID).
- **Status icons encode progress by fill**: dashed circle Backlog `rgb(156,157,161)` → empty circle Todo `#62666d` → half-filled In Progress `#f2c94c` → In Review green → filled check Done `#5e6ad2`. Legible in grayscale.
- **Priority** is a 12px gray signal-bar glyph (`#9c9da1`); only Urgent is an orange "!" square, so priority never competes with status color.
- **Selection**: no row selected on open; `X` shows a left checkbox and an indigo row tint; a bulk toolbar appears at the bottom only while something is selected [doc].
- The same anatomy serves lists, inbox, triage and agent tasks. The agent task board adds a 52px action bar with 29px pill tabs (padding 6px 10px) and project columns.

### Detail view and properties rail [obs][doc]
- Location bar about 44px: "DRV-8852 Title ☆ ⋯" plus a position counter "1 / 84" with ↑/↓, so the detail view is a cursor over the list you came from. Esc returns.
- Quiet secondary actions top-right of the body (copy URL, copy ID, copy branch, split "Delegate to an agent ▾"): 28px pill icon buttons, 2% fill, inset 1px 5% ring, `#8a8f98` icons, hover to 5% fill and `#d0d6e0` in 160ms.
- Content column 662px, 19px top and 16px side padding. Title 20px/590, line-height 26.6px; description 14px/21px; "Activity" heading 16px/590/28px.
- Properties rail about 280px, label-on-top by category (Properties, Labels, Project); category title 12px `#8a8f98`; rows 24px tall, 6px gap, padding 0 8px 0 7px. Label pills 24px tall, 16px radius, 1px `#2e2e32`, padding 0 11px 0 7px, 6px color dot.
- Empty properties read as verbs in muted text ("Set priority", "Set estimate", "Assign", "Add to project"), so state and affordance are one (L20).
- Activity events are 12px quaternary with actor and values in 510 weight: "Actor verb object · time", "via X / on behalf of Y". Relative times "2min ago", "13h"; dates "Oct 9".

### Triage [obs][doc]
- A Triage status and queue per team. The Triage Intelligence box sits under the description: "Suggestions" (dashed chips, accepted chip solid with ✓), "Duplicate" and "Related" rows, each an issue link. Hover a suggestion for why; "view reasoning" on demand. Suggestions take 1 to 4 minutes on new issues.
- Keys follow the on-screen order of actions: `1` accept, `2` decline, `3` (or `MM`) duplicate, `H` snooze. Accept and decline take an optional comment; duplicate merges attachments into the canonical issue.
- Per team and per property, AI suggestions are set to show, auto-apply or hide. Routing rules read as sentences ("When Customer name includes … Then Set priority Urgent"). A triage-owner rotation can follow an on-call schedule.

### Command menu, menus and verbs [doc][obs][know]
- **⌘K** opens pages or runs actions; with rows selected it acts on the selection. Fuzzy search; exact command matches rank above same-titled issues. Prefixes: `i ` issues, `p ` projects, `u ` users, `t ` teams, `l ` labels, `f ` favorites, `d ` documents [doc]. Anatomy [know]: centered near the top third, about 640px wide, selection context chip, grouped rows with right-aligned shortcut hints, 100-150ms scale and opacity open.
- **Context menu**: 16px icon, label, right-aligned chord hint in tertiary gray ("Status P then S"), submenu caret; the current value has a check and a filled row [doc].
- **Menus**: 210px, bg `rgb(23,23,24)`, 1px `rgba(255,255,255,.08)`, 8px radius, 4px vertical padding, no shadow; items 32px, 13px/510 `#d0d6e0`, padding 0 12px [obs].
- **Filter vs Display**: Filter (which items) is segmented chips `[field][operator][value][×]` plus "Match all filters"; Display (how shown) is a popover with List | Board, Grouping, Ordering, toggles (Show sub-issues, Show empty groups) and Display-property chips (filled = on), with "Set as default" / "Reset to default". Filters serialize into the URL.
- **Keys**, all acting on the hovered or selected row:

| Area | Keys |
|---|---|
| Global | ⌘K command menu · `/` search · `?` searchable shortcut sheet · ⌘J agent chat · ⌘F filter current view (Esc clears) · ⌘-click new tab |
| Go to | `G I` Inbox · `G M` My issues · `G T` Triage · `G B` Backlog · `G X` Archive |
| Open | `O T` team · `O I` issue · `O V` views · `O L` label view · `O U` users · `O F` favorites |
| Create | `C` new issue · `⌥C` from template · ⌘⇧O sub-issue · ⌘⇧Enter create another with same values · Esc save as draft |
| Lists | `J`/`K` or ↑/↓ move · Enter open · `X` select · ⇧X or ⇧-click multi · ⇧↑/↓ extend · ⌘A all · Space peek (hold for temporary) · ⌥↑/↓ reorder · ⌥⇧↑/↓ top/bottom · `T` collapse group · `F` filter · ⇧V display · ⌘B list/board · ⌥V save view · ⌘I details sidebar · ⌘⇧I Insights |
| Properties | `A` assign (person or agent) · `I` assign to me · ⇧P project · `P P` priority · ⌘⇧P parent · ⌘⇧M move team · ⌥F favorite · ⇧S subscribe · `H` snooze · `W O` work on issue in a coding tool · [know] `S` status, `L` labels, `P` priority, ⇧D due date, ⌘. copy ID |
| Undo and archive | ⌘Delete delete · ⌘Z undo · `#` restore from archive (30 days) |
| Inbox | `J`/`K` · `U` read/unread · ⌥U all read · Backspace delete · ⇧Backspace delete all read · `H` snooze |
| Editor | `@` mention (notifies and subscribes) · `/` blocks · ⌘Enter post comment · ⇧Enter line break · markdown `#`, `-`, `[]`, `>`, `>>>` |

- Focus ring 2px indigo with 2px offset. `<kbd>` hints: 20px tall, 11.2px, `#08090a` fill, 1px `#3e3e44` ring, 5px radius, padding 3px 6px.

## Category rules

### Placement
1. **Put agents in the assignee menu with a badge and keep a human owner on top, the agent nested under it as a delegate**, because accountability cannot be delegated and the layout should show it. Make "Delegate" filterable. (Linear [doc])
2. **Put AI commands in the same `/` menu as formatting blocks, with "New" / "Beta" badges and the shortcut on the row**, because one command surface builds one habit. (Notion [doc])
3. **Keep AI out of the document's top bar and give it one persistent corner button (about 48px)**, because the top bar belongs to the document's identity (breadcrumb, Share) and a corner stays reachable without claiming layout. (Notion [doc])
4. **For a live session, put every AI verb (record, transcript, chat, one suggested recipe chip) in one floating bar at the bottom center**, because the writing surface at the top stays clean and the controls stay within reach. (Granola [doc])
5. **Scope AI chat by where it was opened (row, page, meeting, folder, home, selection) and show that scope as a removable chip in the composer**, because users should not configure context, but must see what the model will read. (Notion, Granola [doc])
6. **Store AI artifacts inside the existing object model** (a meeting note is a block that can "Open as page", filed into a meetings database; a chat is pinned like a page), because filing, sharing and search then need no AI-specific IA. (Notion [doc])
7. **Configure recurring AI jobs in a side panel next to live data, as a form (output type, prompt, scope, Done) rather than a chat**, because users judge a rule by its output on real rows and will re-read it later. (Notion [doc])

### Authorship and ownership
8. **Decide up front whether AI text is a draft or a contribution.** Draft (summaries, notes about others): mark it persistently by ink tone, one step lighter at the same size and weight (`#292929` vs `#72726E`). Contribution (rewrites in a shared doc): gate it with accept, then let it be ordinary text and keep attribution in history. Never lose the original and skip review at once. Refines L8. (Granola [obs], Notion [doc])
9. **Never overwrite the user's raw input; keep it behind a two-state toggle ("My notes | Enhanced")**, because the original is the user's proof and fallback. (Granola [doc])
10. **Place the user's own lines inside the AI's structure, still in their ink**, because the user's input becomes the skeleton the AI must honor and shows where their note went. (Granola [doc])
11. **Mark AI-managed fields once, at the column header (small gray "AI" badge), never on each cell**, because per-cell marks turn a table into noise. (Notion [doc])
12. **Record agent edits in version history as a named author with its own color dot, with an inline diff (deletions struck through, insertions tinted in the author color)**, because "who changed this?" must have an answer for agents as for people. (Notion [doc])
13. **Write agent and automation events into the object's one activity feed with "via X" and "on behalf of Y"**, because one auditable timeline beats a separate AI log. (Linear [obs])

### Review and automation
14. **Let teams set each AI-suggested property to show, auto-apply or hide**, because trust in automation is earned field by field. (Linear [doc])
15. **Run bulk AI on the visible slice first ("Try on this view") before "Fill all pages"**, because bulk mistakes are expensive and the visible rows are a free test set. (Notion [doc])
16. **For multi-change AI edits, offer a "suggest edits" mode the user steps through top to bottom**, because bulk accept hides the one bad change. (Notion [doc])
17. **Give every AI proposal three exits (keep, discard, try again) and offer regenerate in two flavors in one menu: same lens (🔁 on the current template row) and a different lens (another template)**, because "try again" and "try differently" are the two real recovery moves. (Notion, Granola [doc])
18. **Let users fix AI output by hand or by instruction** ("Niall is actually spelt Nyal"), showing an "Editing note…" banner and the new version over the faded old one, because small fixes are faster by hand and sweeping ones by asking. (Granola [doc])
19. **When users delete source material (a transcript chunk), prompt to regenerate everything derived from it**, because a stale summary leaks what the user removed. (Granola [doc])
20. **Number decision keys in the order the actions appear on screen** (1 accept, 2 decline, 3 duplicate), because spatial and numeric order must match. (Linear changed its own keys to follow this [doc])

### Progress and provenance
21. **Show AI work where its output will land**: a status pill riding the frontier of generated text (Granola), a step checklist inside the block (Notion), a state pill on the card (Linear), not a detached spinner. Specializes L5. (all [obs])
22. **Arrive AI text with a short colored write-head that settles to its final ink (0.4-0.9s per line), at line level, not per character**, because it shows exactly where the AI is writing and reads as calm composition. (Granola [obs])
23. **End each generated claim with a numbered citation chip (18px circle, 10px/550 digits, 1px hairline) that previews on hover and jumps to the source line on click; or give each line a hover 🔍 with a reasoning sentence plus a verbatim quote**, because summaries are only used when each line can be traced. Implements L7. (Notion [obs], Granola [doc])
24. **Treat a fake-busy state as a bug: long setup shows a label and a ticking timer ("Setting up … 00:07"), and a failed start shows an error**, because a spinner can lie and a timer cannot. (Linear [obs][doc])
25. **Make "waiting on a human" its own agent state with its own pill**, because blocked-on-human is the most actionable state in the system. (Linear [obs][doc])

### Capture, privacy and interruptions
26. **Make capture ambient: no bot in the call, a small draggable edge indicator shown only when another app is in front, auto-stop on call end or 15 minutes of silence**, because the tool must not change the meeting. (Granola [doc])
27. **Bundle consent into the start action ("Start transcribing" means everyone consented) and repeat the reminder inside the transcript panel**, because a separate consent dialog gets clicked through. (Notion, Granola [doc])
28. **Default AI artifacts about other people to private, make sharing a visible act (Share is the only black button), and give outside viewers the summary and hover context, not the raw transcript**, because notes contain other people's unfiltered speech. (Granola [doc])
29. **Mark system-initiated prompts with a visual code: solid event-colored bar for scheduled ("Join & take notes"), dashed gray bar for detected ("Huddle detected · Slack", "Take Notes")**, because the user needs to know why the app is interrupting. (Granola [doc])
30. **Morph a live-session indicator into the next action in the same spot ("Transcribing" → "Generate notes")**, because the eye is already there when the session ends. (Granola [obs])

### Cost, model and mobile
31. **Default the model to one plain-language "Auto" line ("Balances speed, effort, and cost.") above a short curated list, and keep high-cost models off until an owner enables them**, because model choice should be visible but rarely needed. (Notion [doc])
32. **Show social proof on shared prompts (author face, usage count like "154k")**, because users pick reusable prompts by who made them and how many use them. (Granola [doc])
33. **Hide an AI entry point until there is enough data for it to help (chat appears after 3 notes on Android)**, because an empty AI on a phone wastes scarce space. (Granola [doc])
34. **On narrow screens collapse view tabs into one dropdown but keep live controls (Pause, Stop) on the row, with Stop the rightmost and only tinted control**, because state controls matter more than navigation during a live task. (Notion [obs])
35. **Keep the artifact's typography identical across devices (serif title, metadata chips, gray AI text)**, because cross-device recognition matters more than density. (Granola [doc])

## Measured constants

Linear layout and anatomy values are in the reference section above.

| Item | Value | App, tag |
|---|---|---|
| Text roles (dark) | `#f7f8f8` / `#d0d6e0` / `#8a8f98` / `#62666d`; in-app titles use `#d0d6e0`, never pure white | Linear [obs] |
| Surfaces (dark) | `#08090a` base; level 1/2/3 `#0f1011` / `#141516` / `#191a1b`; panels `rgb(22,23,24)`; elevation steps 2-4% lightness | Linear [obs] |
| Borders | `#23252a` / `#34343a` / `#3e3e44`; hairlines 5% and 8% white; floating panels 12% | Linear [obs] |
| Shadows | `none` at :root; only floating panels, e.g. agent panel `0 2px 32px rgba(0,0,0,.25)` | Linear [obs] |
| Accent | indigo `#5e6ad2` (commit button, Done, focus ring); selection `color-mix(in lch, brand, black 10%)` | Linear [obs] |
| Type | Inter Variable `cv01`, `ss03`; weights 400 / 510 / 590 / 680; app sizes 11 / 12 / 13 / 15px; workhorses 12, 13, 14, 16, 20px; Berkeley Mono for IDs and dates | Linear [obs] |
| Radii | 4 / 6 / 8 / 12 / 16 / 24 / 32 / 9999; cards in agent output 6px, board cards 9px, label pills 16px | Linear [obs] |
| Motion | hover in 0s, out .15s; quick .1s, regular .25s; buttons `.16s cubic-bezier(.25,.46,.45,.94)`; press scale .97; tooltip 120ms scale .9→1; context menu 100ms; dialog 175ms scale .96→1; refusal bounce 150ms scale .98 | Linear [obs] |
| Live motion | "Working…" shimmer 2.4s linear; agent badge border sweep 2s; dot-grid `steps(1)` loops 1.6 / 2.8 / 3.2s | Linear [obs] |
| Agent panel | 400x520, 12px radius, 1px 12% white; header 48px; result card 6px radius, 11px padding | Linear [obs] |
| Tap size | `--min-tap-size: 44px`; mobile sheets `.5s cubic-bezier(.32,.72,0,1)` | Linear [obs] |
| Text (light) | `#2C2C2B` / `#7D7A75` / `#A19E99` / disabled `#BCBAB6`; warm alphas on `#2A1C00` | Notion [obs] |
| Surfaces and borders | `#FFF` / `#F9F8F7` / `#F0EFED`, hover `#F4F3F3`; borders `#E6E5E3`, `#F0EFED`, strong `#D4D3CF` | Notion [obs] |
| Accent | blue `#2383E2`, pressed `#105FAD`; tints from 3.5% | Notion [obs] |
| Shadow ending in a ring | small `0 2px 4px #0000000a, 0 0 0 1px #2a1c0012`; focus `0 0 0 2px #f8f8f7, 0 0 0 4px #2383e2, 0 0 0 6px #ffffff40` | Notion [obs] |
| Menus and rows | popover 282px, 28px rows, 6px radius; list rows 32px; table header about 36px | Notion [obs] |
| Reading column | about 700px; full-width pages 96px side padding at 1440 | Notion [obs][know] |
| Chat panel | floating about 380-400px, about 16px margin, about 16px radius; switch to sidebar | Notion [doc] |
| Citation chip | 18x18 circle, 10px/550 digits, 1px border oklch 0.95 | Notion [obs] |
| Motion | hover 20-80ms; menus 100-200ms; panels 200ms; summary sections enter 250ms; waveform bars 480-620ms each | Notion [obs] |
| Ink | human `#292929`, AI `#72726E`, same size and weight | Granola [obs] |
| Accent | olive `#5B6F00` fill, `#788C15` hover, `#B2C248` focus, lime `#D1E043` live/new | Granola [obs] |
| Write-head | `bg-slide` 0.9s ease-in-out per line (0.4s in demo); gradient `#FEBE29` → `#FF91E0` → `#CEBEF8` → `#D2E4F8` → `#D1E043` | Granola [obs] |
| Voice bars | 3px rounded, `voice-wave` 0.9s linear, scaleY 0.45 → 1 | Granola [obs] |
| Bottom bar | recorder about 56px circle; chat pill about 56px; recipe chip about 40px; 16-24px above window bottom | Granola [doc] |
| Note column | about 600-650px; sidebar about 200px, rows 28-30px | Granola [doc] |

## Anti-patterns seen

- **Looking busy while broken.** Linear coding sessions used to look busy when the sandbox failed to start; they now show an error [doc]. Fix: label plus timer for real progress, error for failure.
- **Empty state for "too many".** Linear boards used to show an empty state when too many issues matched; they now show an error [doc]. Fix: "none", "too many to show" and "failed" are three states.
- **Keys out of screen order.** Linear's triage keys once did not match the on-screen order of actions; they were renumbered [doc].
- **Two credit types.** Notion meters AI as Standard credits (Auto, Autofill, meeting notes) and Select credits (picked models, owned agents) on top of plan credits [obs]. Fix: one quota, or make the default path spend only one kind and say which.
- **No glanceable provenance on accepted text.** Once accepted, Notion AI prose looks identical to typed text, so trust needs a trip to history [doc]. Fine for contributions; wrong for drafts about other people, where Granola's ink step is the fix.
- **No accept step on generation.** Granola generates automatically when the call ends [doc]. It is safe only because the raw notes are untouched and one toggle away; without that toggle this would be an anti-pattern.

## Steal list

1. Do build every object as one row anatomy (`[priority][fixed-width ID][status][title…]` + right-aligned pills, 40px) reused across lists, inbox, triage and agent tasks, because one anatomy makes the whole app learnable at once.
2. Do fix the ID column width (about 72px), because aligned titles are the biggest scanning win in dense lists.
3. Do give detail views a "1 / 84" counter with ↑/↓ and Space-to-peek from lists, because triage is sequential.
4. Do separate Filter (segmented sentence chips) from Display (layout, grouping, ordering, visible properties), because users confuse them whenever they share a control.
5. Do encode status progress by icon fill (dashed, empty, half, check) and priority by gray bars, because both stay legible in grayscale and leave color to alarms.
6. Do put agents in the assignee menu as delegates nested under a human owner, with state pills including "Waiting", because accountability and "is it running" are the two agent questions.
7. Do log agent actions in the object's one feed with "via X / on behalf of Y", because one timeline is auditable.
8. Do let each AI-suggested field be show, auto-apply or hide per team, and dry-run bulk AI on the visible rows first, because trust is earned per field and bulk mistakes are expensive.
9. Do decide draft vs contribution: gray ink for drafts, accept-then-ordinary-text plus history for contributions, because the marking must match who is responsible.
10. Do keep the user's raw input untouched behind a "My notes | Enhanced" toggle, because the original is the user's proof.
11. Do mark AI-managed columns once in the header, because per-cell marks are noise.
12. Do show AI progress at the frontier where output lands, with a line-level write-head that settles to final ink, because the user sees where the AI is and what is final.
13. Do end each generated claim with a citation chip or a hover 🔍 that shows reasoning plus the quote, because traceability is what makes summaries usable.
14. Do prompt to regenerate derived AI content when its source is deleted, because the AI layer must not remember what the user removed.
15. Do bundle consent into the start action, default notes about others to private, and share summaries instead of transcripts, because the content holds other people's words.
16. Do mark system interruptions solid for scheduled and dashed for detected, because users need to know why they are prompted.
17. Do morph a live indicator into the next action in the same place, because attention returns there when the session ends.
18. Do treat fake-busy as a bug and show a ticking timer on long setup, because timers prove progress and spinners can lie.
