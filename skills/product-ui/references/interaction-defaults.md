# Interaction defaults and AI-native primitives

Measured defaults for the behaviors an agent usually guesses at (delays, thresholds, focus, layers), plus the anatomy of the primitives an AI product needs (thinking, tool chips, task rows, streaming answers, approval and diff surfaces). Two sources:

- **vercel-labs/ui** ("UI SDK", `@ui-sdk/core`, beta): a headless behavior library with React, Vue, Svelte, Solid and Web Components adapters. Defaults below were read from its source and its `ui-sdk` skill text [obs] [doc].
- **Beautiful UI** (beautifului.dev, built by Turbo): 21 live, themed primitives for AI-native interfaces. Timings were measured in a headless browser with `document.getAnimations()` and computed transitions [obs].

Tags: [obs] read in source or measured live, [doc] the resource's own docs or skill text, [inf] inference. Cross-app laws are cited by ID (L1-L20) and not restated.

## Motion tokens (Beautiful UI)

L19 gives the ladder. These are the exact curves and keyframes behind it.

| Curve | Use | Tag |
|---|---|---|
| `cubic-bezier(0.23, 1, 0.32, 1)` | Main ease: every entrance, expand, glide | [obs] |
| `cubic-bezier(0.16, 1, 0.3, 1)` | Width changes, sidebar collapse | [obs] |
| `cubic-bezier(0.22, 1, 0.36, 1)` | Approval card height | [obs] |
| `cubic-bezier(0.77, 0, 0.175, 1)` | One on-screen slide (selection pill) | [obs] |
| `cubic-bezier(0, 0, 0.2, 1)` | Press | [obs] |
| `cubic-bezier(0.4, 0, 0.2, 1)` | Color and hover | [obs] |
| `cubic-bezier(0.38, 0.7, 0.125, 1)`, 250ms | iOS sheet following the keyboard (vercel-labs/ui) | [obs] |

| Keyframe | Definition | Tag |
|---|---|---|
| fade-up | opacity 0, translateY(8px) → rest | [obs] |
| pop-in | opacity 0, scale(0.95) → rest | [obs] |
| fade-in | opacity only | [obs] |
| shimmer-text | background-position 150% → -50%, 1.4s linear, infinite | [obs] |
| pixel-on | 0.65s, staggered 90ms | [obs] |
| caret-blink | 1s step-end (idle only, see streaming) | [obs] |
| spin | 1.1s linear | [obs] |

| Behavior | Value | Tag |
|---|---|---|
| Hover color | 100-150ms, `(0.4,0,0.2,1)` | [obs] |
| Press | transform, background, opacity over 150ms, `(0,0,0.2,1)` | [obs] |
| Table cell hover | 120-140ms ease-out | [obs] |
| Pop-in (citation chip, selection pill) | 220-250ms | [obs] |
| Card and chip entrance | fade-up 320-450ms, stagger 80-120ms | [obs] |
| Disclosure | `grid-template-rows: 0fr → 1fr` plus opacity, 300-400ms main ease; chevron rotates 180° over 300ms | [obs] |
| Section entrance, first load only | fade-up 600ms, stagger 60ms | [obs] |
| Counter digit roll | top, height, opacity over 220ms | [obs] |
| Panel height (vercel-labs/ui) | 200ms ease-out, with a reduced-motion rule | [obs] |
| Exit (vercel-labs/ui) | unmount waits for the exit animation, with a timeout | [obs] |
| Reduced motion (Beautiful UI) | every duration 0.01ms, stream-tail blur and mask removed, caret stops | [obs] |

- Use one main curve for every entrance, expand and glide, because one curve makes the whole app read as one hand.
- Make exits about half the entrance (300ms in, 150ms out), because the UI must not lag behind intent [doc, Emil Kowalski `animate` calibration pair].
- Unmount only after the exit animation finishes, with a timeout fallback, because cutting an exit mid-frame reads as a glitch and a stuck animation must not leave a ghost layer.
- Do not animate what the keyboard drives (roving focus, list highlight, command palette selection), because a 300ms ease trails behind repeated key presses.
- Animate `height` or `grid-template-rows` for one small disclosure at a time only, never across many rows at once, because layout animation is cheap for one element and janky for fifty [inf].

## Popups, layers and focus (vercel-labs/ui)

| Behavior | Default | Tag |
|---|---|---|
| Tooltip open delay | 600ms | [obs] |
| Tooltip close delay | 0ms | [obs] |
| Tooltip on keyboard focus | opens instantly | [obs] |
| Tooltip warm window | 400ms: any tooltip opened within 400ms of the last one opens with no delay (`warmFor = 400`) | [obs] |
| Tooltips visible at once | 1 | [obs] |
| Hover card | opens at 600ms, closes at 300ms | [obs] |
| Submenu safe area | a triangle from the pointer to the submenu; `restTimeout = 300` before it gives up | [obs] |
| Typeahead buffer | 500ms between keystrokes before the buffer resets | [obs] |
| Escape | closes only the topmost layer; nested popups count as inside their parent | [obs] |
| Dense-tool baseline (`web.css`) | 13px type, line-height 1.5, spacing unit 4px (0.25rem), control height 32px (spacing × 8), radius 0, neutral OKLCH `light-dark()` colors, no motion | [obs] |

Rules:

1. Open the first tooltip at 500-600ms, close at 0ms, and open any tooltip within the 400ms warm window instantly with no animation, because the delay stops accidental flashes while the warm window lets someone scan a toolbar without waiting per icon. (Emil Kowalski's skills use about 500ms; both agree on the warm window, which matters more.)
2. Open tooltips immediately on keyboard focus, because a keyboard user has already declared intent and has no pointer to hover.
3. Show one tooltip at a time and never cover its subject, because two tooltips compete and a covered control cannot be read [doc, checklist.design].
4. Give hover cards a 300ms close delay, longer than tooltips, because the pointer must be able to travel into the card to use what is inside.
5. Keep a submenu open while the pointer moves inside the triangle toward it, for up to 300ms at rest, because a diagonal path to the submenu crosses sibling items and would otherwise close it.
6. Reset the typeahead buffer after 500ms, because typing "pr" fast should jump to "Projects" while a pause starts a new search.
7. Close only the topmost layer on Escape and treat nested popups as inside their parent, because Escape from a submenu must not also kill the dialog under it.
8. Return focus to the trigger when a layer closes, and when the focused row is deleted move focus to its neighbor, never to `<body>`, because lost focus is the most common keyboard bug in agent-built UI and it is invisible in screenshots.
9. Never hand-roll `role="listbox|menu|dialog"`; use a primitive that ships the keyboard model, because the role promises arrow keys, typeahead and focus trapping that ad hoc markup does not deliver [doc].

## Gestures, repeat, undo, toasts (vercel-labs/ui)

| Behavior | Default | Tag |
|---|---|---|
| Drag start threshold | 3px of movement before a press becomes a drag | [obs] |
| Hold (long press) | 500ms, with 10px movement tolerance | [obs] |
| Repeat (stepper held down) | first repeat after 400ms, then every 60ms | [obs] |
| Undo stack | limit 100 entries; edits in the same group within `groupDelay` 500ms merge into one entry | [obs] |
| Toast duration | 5000ms | [obs] |
| Loading toast | persists until updated | [obs] |
| Toasts visible | `maxVisible` 3 | [obs] |
| Toast region | F6 jumps focus to it | [obs] |
| Error toast | announced assertively (`aria-live="assertive"`) | [obs] |

1. Start a drag only after 3px, because a click with a slightly shaky hand must stay a click.
2. Fire a hold at 500ms and cancel it if the pointer moves more than 10px, because the user is scrolling, not holding.
3. Repeat a held stepper after 400ms, then every 60ms, because one tap must change the value by exactly one and a held press must still feel fast.
4. Merge edits that land within 500ms of each other into one undo entry and cap the stack at 100, because undoing a word letter by letter is useless and an unbounded stack leaks memory.
5. Show toasts for 5s, keep loading toasts until they resolve (update the same toast in place), show at most 3, and announce errors assertively, because a loading toast that times out lies about state and a stack of more than 3 covers the work.
6. Let F6 reach the toast region, because a toast with an Undo button that only a mouse can reach excludes keyboard users.

## Stick to bottom (vercel-labs/ui `createStickToBottom`)

| Property | Value | Tag |
|---|---|---|
| Threshold | within 24px of the bottom counts as at bottom | [obs] |
| Default | follows new content | [obs] |
| State exposed | `following`, `atBottom`, `unseen` | [obs] |
| `prepend()` | inserts above without moving the visible content | [obs] |

1. Follow new output while the user is within 24px of the bottom, stop following the moment they scroll up, and show a "Jump to latest (N)" pill driven by `unseen`, because yanking the scroll while someone reads earlier output is the most hated chat bug. T3 Code's "Scroll to end ⌄" pill above the composer is the same pattern [obs].
2. Preserve the scroll position when loading older items above, because the reader's place must not move when history arrives.

## Press scale by size (Beautiful UI)

L19 sets press at .97 as the general value. Beautiful UI scales press inversely to element size [obs]:

| Element | Size | Press scale |
|---|---|---|
| Icon button | 28px | 0.94 |
| Button | about 27-32px tall | 0.96 |
| Small CTA ("Notify me") | | 0.97 |
| Nav row | 208px wide | 0.98 |
| Workspace switcher | 164px wide | 0.99 |

- Scale press inversely to size (0.94 icons, 0.96 buttons, 0.98 full-width rows, 0.99 anything wider than about 160px), because the same visible displacement in pixels feels right at every size and a 200px row at 0.96 lurches.
- Pop in from 0.95, never from 0, because scale(0) reads as a cartoon and makes the element travel too far [doc, Emil Kowalski `animation-vocabulary`].

## Surfaces and state contrast

Beautiful UI dark palette, OKLCH [obs] (L2 covers the alpha-of-one-ink idea; these are the measured steps):

| Token | Value |
|---|---|
| page | `20.9% .004 264` |
| canvas | `23.1%` |
| surface | `26%` |
| hover | `28.9%` |
| hover-2 | `31.8%` |
| line | `30.8%` |
| ink / ink-2 / ink-3 | `96.4%` / `73.1%` / `54.1%` |
| accent | `68% .173 253` (blue, the only chromatic color) |
| status tints | status hue at alpha .14-.16 (green, orange, red) |
| light theme | surface white, ink 24.7%, line 94.6%, accent 62.6% |

| Elevation | `box-shadow` (edges are shadows, never `border`) |
|---|---|
| card | `0 0 0 1px oklch(100% 0 0/.11), 0 1px 2px oklch(0 0 0/.2), 0 2px 6px oklch(0 0 0/.2)` |
| raised | `0 0 0 1px /.13, 0 2px 10px /.22` |
| overlay | `0 0 0 1px /.15, 0 8px 28px /.34` |
| field | `inset 0 1px 2px` |

Radii: card 10px, chip 6px, citation chip 5px, nav highlight 7px, task-row capsule full pill that becomes 14px when expanded [obs]. Type: Inter 14px body; JetBrains Mono for meta, figures, file names, counts, timers; section headings 13px/600/-0.14px; descriptions 12.5px in ink-3 [obs].

1. Step dark surfaces by about 3 L points and keep 3-4 elevation recipes, because more steps stop being distinguishable and more recipes stop meaning anything.
2. Make every selected or active state reach 3:1 against its surroundings through a fill, a full outline or a weight change; a faint tint alone fails, and so does a stripe down one edge as the only signal [doc, vercel-labs/ui skill]. Text needs 4.5:1; control edges, focus rings and state fills need 3:1. Because low-contrast selection is the most common accessibility failure in "clean" UIs.
3. Put figures, counts, durations, file names and diffs in mono with tabular figures, and everything else in one sans, because mono digits align in columns and read as data.
4. Use 14px body and 13px for dense tables and meta, because vercel-labs/ui's 13px baseline suits dense tools and Beautiful UI's 14px suits reading; this split takes both [inf].

## Agent-ready markup (vercel-labs/ui skill)

All [doc]:

1. Label every control uniquely with verb plus object ("Actions for Jane Doe", not "Actions"), because a screen reader or an agent operating the UI must tell list rows apart.
2. Put `data-agent-confirm="<what it does>"` on the confirming button, not on the trigger, because the confirmation belongs to the moment of consequence.
3. Mark sensitive values `data-agent-secret` and hidden ones `data-agent-hidden`, because an agent reading a snapshot must not leak or act on them.
4. Style state from `data-slot` and state attributes (`data-open`, `data-pressed`, `data-starting-style`, `data-ending-style`), never inline styles, and put `@layer ui-sdk;` first, because state styling then survives theming and overrides.
5. Use controlled `value` with `onValueChange(value, details)`, where `details` carries `reason`, `source` (which can be `"agent"`) and `cancel()`, because the app can then tell an agent's change from a person's and veto it.
6. Key lists by id, never by index, and use `render` instead of an `as` prop, because index keys break focus and animation when rows move.
7. `createAgent` exposes `snapshot`, `act` and `query`, and `registerTools` exposes them to WebMCP; components expose `agent.actions`. Use these instead of screen-scraping your own UI.

## AI-native primitive anatomy (Beautiful UI)

All [obs] unless tagged. L5 (one live line then a receipt), L6 (shimmer the words) and L14 (reserve output space) are the laws; this is the part-by-part anatomy.

### Status pills

- A tinted pill: the status hue at alpha .14-.16 as fill, the full hue as text ("Completed", "7 days").
- Status icons beside them: a green check when done, a spinner ring with the step number inside while running.
- Use tints, not solid fills, because a solid status color competes with the one accent that means "act here".

### Thinking

- Collapsed: "✦ Thought for 4 seconds ⌄", one line.
- Expanded: steps fade up over 320ms, staggered 0/120/240/360ms. Each step has a check icon, a vertical guide line joining steps, and inline mono meta ("6 flavors").
- Three variants: Reasoning (prose); Search ("Searched the web", the query, results with domains, "+7 more"); Coding ("Ran 3 tools: Read flavors.ts, Edit ChurnSchedule.tsx +74 −41, Run npm run freeze").
- The status line is the only `aria-live` region found on the site; give every running state one.

### Loading state

- Three parts in one row: a pixel-grid loader (pixel-on 0.65s, stagger 90ms), shimmer text ("Churning", 1.4s linear), and a mono elapsed timer with tenths ("25.1s", "1m 14.8s", "9m 12.8s").
- Variants: Drive, Dots, Orbit, Surfer.
- Show tenths on long agent work, because a visibly moving number proves the job is alive when nothing else changes.

### Tool chips

1. A summary header that collapses the group: "4 tool calls, 2 messages".
2. Each row: icon, verb label, mono argument pill ("Write 204 lines | ChurnSchedule.tsx"). On expand the leading icon becomes a chevron and diff lines show in green mono with an ellipsis.
3. File-change chips: "flavors.css +13", "ChurnSchedule.tsx +74 -41".
4. Overflow collapses to "+2 more".
5. Chips pop in staggered by 80ms.

### Task rows

- A capsule row: status icon, title, mono meta ("12 suppliers"), tinted "Completed" pill, chevron.
- Expanding morphs the radius from pill to 14px over 300ms and reveals substeps with right-aligned mono values ("3 files", "68%").
- A Capsules / List toggle switches density.

### Streaming text

| Part | Value |
|---|---|
| Word cadence | about 60ms per word, 16-17 words per second, each word a plain inline span |
| Caret | 2px × 1.05em, fades in over 150ms, steady (no blink) while streaming, removed at the end |
| Citation chip | favicon plus mono domain, 10.5px text, 18px tall, inserted right after the sentence it supports, pops in over 250ms |
| Actions row | fades in over 400ms, about 80ms after the last word: copy, retry, thumbs up/down, stacked favicons "10 sources" |
| Follow-ups | "↵ Which flavors sell best in winter" style suggestions fade in with the actions row |
| Hidden rows | stay mounted with `pointer-events: none` until revealed |
| Container | `min-height: 15.5rem`, so nothing below jumps |
| Stream tail | `.stream-tail` class (blur 1.6px plus a gradient mask on the newest words) exists in CSS; not caught active |

- Keep the caret steady while streaming, because a blink reads as "waiting for you" while the stream is still talking.
- Insert source chips after the sentence they support, not at the end, because provenance is checked claim by claim (L7).
- Reveal the actions row only when the stream ends, because copy or retry on half an answer is a trap.

### Approval card

- A question as the title and a close X.
- Radio options plus "Something else…" as free text.
- A "1/3" pager with up/down chevrons, Skip and Continue.
- Continue stays disabled until there is an answer; picking an option auto-advances.
- On the last question Continue becomes "Send".
- Height animates over 360ms on `(0.22,1,0.36,1)`.

### Recommendation card

- A question title ("Want me to place this restock order?"), an inline entity chip (avatar plus name), a green "7 days" pill.
- A three-bar confidence meter with a text label ("High confidence").
- Alternatives (secondary) and Accept (accent).

### Diff table

- Removed rows tinted red and struck through; added rows tinted green; a checkbox per row.
- A header hint: "Click changed rows to toggle".
- A footer count, "2 removals · 1 addition", and a button "Apply 3 changes".
- Unchecking a row updates the count and the button label live ("Apply 2 changes").
- Put the consequence and the live count on the button, because the user then knows what will happen without reading helper text.

### Records table

- Row numbers, letter avatars, colored tag pills.
- A footer with a count ("60 count") and "+ Add calculation".
- Cell hover 120-140ms ease-out.

### Filter table and search

- Status chips with a dot and a count ("All 5", "To do 2").
- Non-matching rows collapse in place (`grid-template-rows` plus opacity, 300ms) instead of unmounting, because the eye can track what left.
- Long text truncates with an ellipsis.
- Search filters live; its empty state reads "No results found / Adjust your search to try again" (see L20 for empty states in general).

### Context cards

- A header count ("All chunks 32"); each chunk shows title, character count, the text and a source chip (PDF or CSV badge plus ↗).

### Sidebar nav

- Rows 208×32px.
- Workspace switcher and a collapse icon at top; New chat / Home / Invite users "3/10"; a collapsible "Chats" section with a search icon; a plain-text list; an Upgrade button.
- One absolutely positioned highlight per group glides `top` and `height` over 220ms on the main ease, with opacity over 150ms. Do not flash a background per item, because the glide shows where focus went.
- Sidebar collapse: width over 280ms on `(0.16,1,0.3,1)`.
- heydamir/unslop's app layout numbers widen this: sidebar 240-280px, nav rows 32-36px with 2-4px gaps. Use 32px rows, 2-4px gaps and a 240px sidebar as the reconciled default [inf].

### Insight cards

- An "Insights 3" pager.
- One sentence with an inline entity and mono red figures.
- Two series with big mono % and $ values, and a trend snapshot.
- A follow-up chip that asks the next question ("Should I rebalance flavors?").
- Stat cards elsewhere stay numbers only (label, figure, change against a reference); a trend belongs here only because the insight is itself the subject [inf, resolving unslop's no-sparkline rule].

### Selection actions

- A floating pill toolbar over selected text: a "Describe edits" input, Explain, Improve, and ›.
- › reveals Shorten, Tone and Grammar through 400ms `max-width` transitions.
- The pill slides on `(0.77,0,0.175,1)` and pops in over 220-250ms.

### Prompt bar and code block

- Prompt bar: a model picker with tier names and a check on the current one, a `/` menu with footer "Type to search commands", a `+` sources menu showing connectors as "Connected", a dictation mic (see L12 for the composer law).
- Code block: filename header with Copy, line numbers, a Code / Diff toggle.

## Anti-patterns seen on the sources

- Beautiful UI pops a newsletter modal after scrolling. Fix: never interrupt reading with a modal; a quiet inline signup at the end does the same job.
- Beautiful UI has only one `aria-live` region. Fix: announce stream completion, tool results and errors too, not just the status line.
- vercel-labs/ui's `web.css` ships no motion. Fix: add the curves above; headless defaults are behavior, not feel.

## Steal list

1. Use `cubic-bezier(0.23, 1, 0.32, 1)` for every entrance, expand and glide, because one curve unifies the app.
2. Open the first tooltip at 500-600ms, the next within 400ms instantly, and on focus at once, because scanning a toolbar must not cost a wait per icon.
3. Close the topmost layer on Escape and return focus to the trigger or the deleted row's neighbor, because lost focus breaks keyboard use invisibly.
4. Start drags at 3px, holds at 500ms with 10px tolerance, stepper repeat at 400ms then 60ms, because these separate intent from noise.
5. Merge undo entries within 500ms, because one undo should reverse one thought.
6. Keep toasts at 5s, loading toasts until resolved, 3 visible, errors assertive, because toasts must not lie about state or cover work.
7. Stick live feeds to the bottom within 24px and count unseen items in a "Jump to latest (N)" pill, because reading earlier output must never be interrupted.
8. Scale press 0.94 to 0.99 inversely to size, because the same pixel displacement feels right at every size.
9. Summarize finished agent work as one line with a count or duration ("Thought for 4 seconds", "4 tool calls, 2 messages"), revealed on demand with an 80-120ms stagger, because the result is the content and the trace is evidence.
10. Stream at about 60ms per word with a steady caret, chips after their sentence, actions only at the end, a reserved min-height, because each of these removes a jump or a trap.
11. Put the live consequence on the button ("Apply 3 changes" → "Apply 2 changes", Continue → Send), because then no helper text is needed.
12. Collapse filtered rows in place, because the eye tracks what left.
13. Use one gliding highlight per nav group, because it shows where focus went.
14. Show elapsed time with tenths on long agent work, because a moving number proves liveness.
15. Make selected states reach 3:1 with a fill, outline or weight change, because a tint or edge stripe alone fails.
16. Label controls with verb plus object and mark confirm buttons with `data-agent-confirm`, because agents and screen readers operate the same UI.
