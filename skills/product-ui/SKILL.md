---
name: product-ui
description: Design or build an application interface (web or desktop app, dashboard, internal tool, agent or AI product screen) so it feels clean and intuitive on the first try. Gives the decision order, measured defaults for layout, type, colour, radius, motion and keyboard (from T3 Code, Linear, ChatGPT, Claude, Perplexity, Cursor, Notion and others), playbooks for ten product categories, and a review checklist. Use when starting a new app screen or shell, redesigning one, deciding where buttons, menus, panels and states go, or reviewing an app UI for intuitiveness. For marketing or personal websites use website-design. For AI surfaces (composer, streaming, approvals, citations, agent status) also load ai-interaction-patterns. For component-level polish use the emil-* skills.
license: MIT
---

# Product UI

Build app interfaces that feel obvious. The method comes from a teardown of T3 Code (live app plus source) and case studies of twenty AI-forward products, measured from their running CSS. It is written as decisions to make in order, with defaults for every decision nobody makes on purpose.

## Rule zero: cut words; show, don't label

What separates Perplexity, Granola, ChatGPT, Claude, Linear and T3 Code from generated UI is not polish. They say each thing once, and most things without words. Generated UI labels everything it shows, shows everything it knows, and boxes each piece. Measured on real screens (non-content words: labels, metadata, status words, helper copy, headers and button text, not the user's data):

| Screen | Non-content words in the work area |
|---|---|
| ChatGPT finished answer | 2 (placeholder; copy and share are bare icons) |
| Granola note | 3-5 (a date chip, an attendee chip) |
| Linear inbox | 3 (two tab counts and a title); rows carry no labels |
| T3 Code approval | about 12 |
| Perplexity answer | about 15 |
| A generated agent inbox built from the old version of this skill | 64, plus 36 in its sidebar, with 8 facts shown twice |

**Targets:** at most 15 non-content words in the reading lane, zero facts said twice. Navigation and settings labels are the content of those surfaces and do not count against the lane, but keep them to one word each. Whole screens with navigation measure 30-60 on the reference apps (Perplexity 53, T3 Code 54 with its sidebar). Count on the screenshot before calling a screen done.

Decoration is not text. Avatars, logos, favicons, kind icons, imagery and colour carry identity at a glance and *replace* words: keep them, add them where a word can go. A screen with its words cut should look richer, not emptier.

How the references carry information without words, and what the generated inbox did instead:

| Fact | Show it with | Generated version (cut) |
|---|---|---|
| Item state | the section it sits in, an icon, a colour (Linear: a status glyph at the row end, an unread dot) | "Approval", "Input" spelled on every row and again as a pill in the detail header |
| Kind and sender | a kind icon, an avatar or logo with a small glyph badge (Linear) | "Quill · Halden Freight" as text |
| Who made it | ink: AI text grey, the user's text black (Granola); the commit button names the act | "Quill drafted this for you" |
| Context of the open item | nothing: the selected row already shows it | a detail header repeating type, agent, client and age from the row |
| Counts | on the thing counted, once ("Priority 4", "Settled 100") | "Since yesterday 17:40: 4 need you, 11 done, 1 failed" above a badged section and a "Done 11" shelf |
| Sources | inline chips that name the source, one "Sources 10" pill that opens a pane (Perplexity) | a permanent "Based on · 3" rail of cards with kind, title, metadata and quote |
| A caveat | a highlight on the one claim the user must check, with the reason one gesture away; never whole sentences, never as a status marker | "Check before sending." before the sentence |
| Scope and defaults | nothing while they are the default | "From sam@… · 1 recipient · 5s to undo after sending" under the button |
| Freshness | nothing while live; a word only when stale | "Live · checked 12:12" |
| Field names | position (the subject is the first bold line; the recipient is an avatar chip) | "To", "Subject" |

The rest of the slop signature, each with its test:

- **Boxes.** The AI's output is never in a card; only inputs and the human's turn are boxed. At most 3 bordered or filled containers in the reading lane, no card in a card, no divider where space already separates.
- **One loud thing.** Blur the screenshot: the content reads first, the primary action second, nothing else. A detail title is at least 1.6x body size (Granola 2.2x), or the content itself is the headline.
- **Columns.** At most two persistent columns; a third opens on demand.
- **Primary colour.** The filled button is ink (near-black, off-white in dark) or a hue chosen in the brief; never the framework's default blue or indigo. No keycap inside a filled button: shortcuts go in the tooltip and ⌘K.
- **Typeface roles.** Each face has one role you can name in a word (the AI's prose, document titles, data). A serif used for prose, quotes and questions at once means nothing. The prose voice face is for a full reading lane; in a narrow chat rail beside an artifact or document (under about 480px), AI text stays in the UI sans at 14px.
- **Rhythm.** Lane 640-720px; at least 24px between unlike blocks, from one spacing scale.
- **Title scale follows role.** The open object's title (a note, an answer, a record) is the large one. A destination title ("Settings", "Inbox") stays at 14-16px: the navigation already says where you are.
- **Filled means consequential.** Only the action that commits the region's decision is filled (Send, Approve, Buy). Secondary and account actions (Sign in in a sidebar, Add to folder, Share) are quiet: ghost, text, or an outlined chip beside the metadata they act on. A screen with no consequential action has no filled button.
- **Never an empty pane.** With nothing selected, select the first item or let the list take the width; a pane that says "Select an item" is chrome.
- **Over-correcting is also slop.** Cutting words never means cutting decoration: tab icons, favicons on source chips, coloured project and label glyphs, avatars and logos stay. Icon-only is for universal actions (copy, share, attach, voice, more, close); modes and filters keep their one word next to the icon. A table with more than two value columns keeps its column headers: a bare value that is meaningless without its label is the one place a label always earns its words.

### Region rules from side-by-side reviews

From builds ranked level with the real product, where each side won some regions:

- **Toolbar:** name the current scope (team, project) once as a chip; view tabs keep their icons.
- **Lists:** identity glyphs (team, project, label, agent) keep their own colour; chips in dense rows are glyph + text with no outline. Groups and shelves follow the content directly, never pinned to the bottom behind a dead gap.
- **Warnings and failures:** keep the semantic colour, a one-line title and a named fix ("Refresh", "Reconnect"), however compact. Quiet is for success.
- **Approvals:** the commit action is a real button at the end of the row it affects, Decline beside it, More as an icon; not a run of equal-weight text links.
- **Ambient context** about the work (machine, branch, diff count, model) fits in a strip under the input; a third column only on demand.
- **AI answers:** split a long answer by purpose (finding, advice, warning, question) with one emphasis; a safety stop is the one tinted block allowed inside AI prose. Actions on the answer (copy, share, retry) come after it, never before. The AI's current conclusion may carry the brand colour: it is the content, not chrome.

Run `emil-unslop-design`'s "Subtract first" walk on every element (what breaks if it is gone?), then the counts above. The full analysis with per-screen evidence is in [references/slop-vs-good.md](references/slop-vs-good.md).

## The thesis

The screen is a reading lane with tools at the edges. The user's work (their document, thread, record or the agent's output) is the most important thing on screen, and the human's attention is the scarce resource. Every element passes four tests:

1. **Is it needed right now?** If not, fold it, hide it behind hover, or move it to a sidecar.
2. **Does it differ from the default?** If not, hide it.
3. **Is this where the decision is made?** If not, move it there.
4. **Does it need a human?** If yes, make it loud and pull it to the top. If not, let it recede.
5. **Is it already said?** By another element, by position, by an icon or by the section it sits in? Then delete it.

A product built this way feels calm while doing a lot. That calm is the product.

## Decision order

Write each decision down (a line or two) before writing code. Skipping one is how a screen ends up generic.

0. **Fill in what the request left out.** Requests are usually one line. Write the missing spec from the category chapter, not the prompt: who uses it, the screen's one job, 8-15 realistic records (real names and numbers, one long value, one failure), the few fields the job needs (the rest is stored, not shown), and the states present now. Never fill a gap with filler or with labels describing what would go there.
1. **Category and center of gravity.** Find the product's category in [references/categories/README.md](references/categories/README.md) and read its chapter. Each category is judged on one question (chat: can I trust the answer; coding: what changed and can I undo it; notes: is my work still mine; creative: is it beautiful and steerable; ops: what needs me and is the system working). The richest components go to that question.
2. **Scarce resource and core loop.** Name what the user runs out of (attention, time, money, trust) and the loop they repeat (T3: prompt, watch, review, settle). Everything serves the loop. Write a one-sentence design thesis.
3. **Shell.** Lay out zones from [references/shell-and-navigation.md](references/shell-and-navigation.md): an attention-sorted list on the left, one item in a centered reading lane with its primary input, on-demand tools on the right (closed by default, so at most two persistent columns), settings and analytics as sheets over the work. Land the user on the primary input, never a dashboard of tiles. When a screen has no text input (an approvals queue, a review list), the primary input is the selected item's primary action: focus and shortcuts return there.
4. **Objects and their state vocabulary.** One noun per concept. Give each object a closed set of one-word states with an icon and a semantic colour (Working, Needs you, Failed, Done). The word appears once: as the section header the items sit under, or on the row when the list is not sectioned by state; everywhere else the icon and colour carry it. Every lifecycle verb gets its inverse (pin/unpin, settle/un-settle, snooze/wake).
5. **Text budget.** List every fact the screen shows and give each one home. For each, pick the cheapest carrier in this order: position or section, icon or avatar, colour or ink, a chip, and only then a word. Write the non-content word count you are aiming for (rule zero: at most 15 in the lane).
6. **Control placement.** Put each control where its decision is made: settings for the next action on the input that sends it, context choices in a strip under the input (removed once locked), item actions in place of the item's metadata on hover, rare global destinations in the bottom-left corner. One primary action per region, in a fixed spot, whose verb changes with state.
7. **Density by urgency.** Items that need action get a rich card. Done items become one-line rows on a collapsed shelf with a count. Background work recedes (70% opacity). Needs-you items never recede.
8. **Progressive disclosure.** Outcome first, process folded: a receipt ("Worked for 2m 13s ›"), then one sentence with counts, then typed one-line rows, then the detail. Never fold a failure.
9. **Every state, before styling.** Empty, loading, partial, error, offline, disabled, success, gated. See [references/states-copy-safety.md](references/states-copy-safety.md).
10. **Tokens.** Apply [references/constants.md](references/constants.md): one tinted ink, one paper, alpha neutrals, four text roles, an ink primary button, one accent with one job (hue from the domain, never the framework default), a radius ladder, glass only on floating layers. Load `emil-color` for the ramp, `emil-typography` for the faces and scale, `emil-surfaces` for depth.
11. **Motion.** Instant for frequent things, short for occasional ones, nothing looping. Values in constants.md; mechanics in `animate` and `emil-design-eng`; gestures, sheets and springs in `apple-design`.
12. **Keyboard.** A ⌘K palette with every action and its live shortcut, conventions borrowed from the category, chords shown in every tooltip and menu row, focus returned to the primary input.
13. **Copy.** Delete first (the deletion ladder in states-copy-safety.md), then word it. Sentence case, verb plus object, each count once on the thing it counts, one-word statuses, consequences in destructive dialogs, fixes in errors. No narration of what the screen shows ("drafted this for you", "Based on", "Check before sending").
14. **Review.** Run [references/review.md](references/review.md) on screenshots of the real build before calling it done. Its first step is rule zero: count the words, cut, recount. Then `emil-unslop-design`, then `emil-ui-polish` and `emil-design-foundations`' mistakes checklist.

If the product has any AI in it, load `ai-interaction-patterns` at step 4 and define every AI surface with its full state set.

## Twelve moves to carry everywhere

1. **Inbox, not tree.** Sort the main list by what needs the user, not by where things are stored. Background activity never reorders it.
2. **Controls at the point of decision.** Model, mode, permission and attach live on the input that triggers them.
3. **One accent, one job.** The filled primary is ink; the accent marks focus and the one thing that needs the user. Everything else is neutral; colour carries state only. Selection is neutral alpha, never the accent.
4. **Density follows urgency.** Three-line cards for needs-you, one-line rows for done.
5. **Outcome first, process folded.** A receipt with counts on top, the trail one click away.
6. **Morph, don't multiply.** One send button carries send, stop, steer, queue and resume. A split button relabels to the object's state.
7. **Defaults are invisible.** A control appears only when its value differs from the default.
8. **Loud when it needs a human, quiet otherwise.**
9. **Instant for frequent, animated for occasional.** Menus and hovers are instant; popovers 150ms; dialogs 200ms; layout animation off.
10. **Words for live status and errors, nowhere else.** "Working for 12s", not a spinner. "Run `codex login` and try again", not "Error". Everything stable (state, kind, owner, freshness) is shown, not labelled.
11. **Keyboard is first class and taught where you act.** Shortcuts are data rendered into every tooltip, menu row and palette row.
12. **Every way in has a way out.** Reversible actions get a 5s ⌘Z undo instead of a confirm. Only irreversible ones confirm, with Cancel focused.

The full laws with their reasons and evidence are in [references/laws.md](references/laws.md).

## Defaults when nothing else decides

| Thing | Default |
|---|---|
| Sidebar | 240-260px, min 208px, nav rows 28-32px, list rows 36px |
| Reading lane | max 46rem (736px), centered; extra width goes to sidecars, never longer lines |
| Properties sidecar | 280px |
| Type | 13px chrome and meta, 14px body and controls, 15-16px reading prose (AI output), detail titles 24-32px (at least 1.6x body), weights 500 labels and 600 titles (or variable 510/590), no bold, at most 4 sizes on a screen |
| Controls | 24 / 28 / 32px buttons, 32px inputs, 28px menu rows, 44px hit areas on touch, 16px inputs on touch |
| Radius | 4 small chips · 6 tooltips · 8 controls, menus, and rows or cards inside a list or sidebar · 12 standalone content cards and alerts · 16 dialogs, composer, bubbles · full pills; nested = parent minus padding |
| Colour | one tinted ink and paper, text roles at about 100 / 75 / 60 / 45% ink (the third role must still reach 4.5:1; the fourth is only for placeholders, disabled text and decorative icons), borders 6-10% ink, hover 4%, selected 6-9%, an ink primary button, one accent whose hue comes from the domain |
| Chrome | at most 3 bordered or filled containers in the reading lane; at most 2 persistent columns; no card around generated output |
| Text | at most 15 non-content words in the lane; each fact once |
| Motion | hover background instant on, 100-150ms off · press scale .97 · popover 150ms opacity + scale .98 · dialog 200ms · menus and keyboard-driven highlights instant · layout animation off · ease `cubic-bezier(.16,1,.3,1)` |
| Waits | nothing for 400ms, then a label or skeleton; explain at 15s; offer an escape at 20s |
| Undo | 5s inline notice bound to ⌘Z for every reversible action |

## Which skill does what

| Need | Skill |
|---|---|
| AI composer, streaming, work log, approvals, citations, agent states, cost meters | `ai-interaction-patterns` |
| Marketing site, landing page, portfolio | `website-design` |
| Visual hierarchy, spacing, paired right/wrong calls | `emil-design-foundations` |
| OKLCH palettes, contrast, dark mode tokens | `emil-color` |
| Type selection, scales, OpenType features | `emil-typography` |
| Shadows, borders, concentric radii, elevation | `emil-surfaces` |
| Hover, press, focus, truncation, layout shift details | `emil-ui-polish` |
| Forms, inputs, buttons, validation timing | `emil-forms-and-inputs` |
| Touch, keyboard, screen readers, reduced motion | `emil-touch-and-accessibility` |
| Component API shape (React) | `emil-component-design` |
| Building one animation; coordinating several | `animate`; `choreograph` |
| Springs, gestures, sheets, Apple-style material | `apple-design`, `gestures` |
| Phone web quirks (100vh, tap highlight, zoom) | `mobile-native` |
| Strip AI-generated visual tells | `emil-unslop-design` |
| Worst-case data stress test | `break-ui` |
| Code-level UI review against a craft bar | `emil-ui-review` |
| Library choice (toasts, command menu, drawers) | `pick-ui-library` |
| Several genuinely different variants behind a picker | `prototype` |
| Turning a user's design corrections into rules | `learn-taste` |

## Where the craft skills disagree, and which wins in an app

| Topic | Other skill says | In app screens |
|---|---|---|
| Press scale, hover timing | `emil-design-eng`: .96, symmetric 150ms | .97, hover instant on and eased off (measured on dense, all-day apps); keep the emil values on marketing pages |
| Field labels | `emil-design-foundations`: a placeholder is not a label, use a persistent label | Forms with several fields keep visible labels. A single input whose job is obvious from its place (composer, search, reply) uses a placeholder only, as ChatGPT, Perplexity and Linear do |
| Status signals | `emil-design-foundations` and checklist.design: status needs a text label, never colour alone | Colour never stands alone: pair it with an icon shape or the section header. The word lives once, in the header or the row of an unsectioned list, not on every row and again in the detail |
| Empty states | `emil-design-foundations`, `emil-ui-polish`: explain why and what to do next | One short line plus the action ("No projects yet" + Create project). No paragraph, no illustration in a returning-user tool |
| Depth | `emil-surfaces`: shadows over borders for raised cards | App content is not raised: no card, no shadow. Hairline borders for inputs and dividers that separate, shadows only on floating layers (menus, popovers, dialogs) |
| Dashboard welcome | checklist.design: a since-last-visit summary and a "last updated" indicator | Only when the screen does not already show those counts and that freshness. A badge on the section and a count on the shelf already say it; freshness appears only when stale |
| Copy length | `emil-design-foundations`: specific beats generic, give context | Specific, and short: name the consequence on the button so the helper line can go |
| Craft principles | `apple-design` §16: simplicity, not minimalism; grouping and mapping | Agree: when a control needs a label to explain it, move it next to what it changes instead of adding words |

## Reference map

- [references/slop-vs-good.md](references/slop-vs-good.md): what separates the reference apps from generated UI, with word counts and a test for each difference.
- [references/laws.md](references/laws.md): the thesis and 24 laws, each with why, evidence and anti-pattern.
- [references/constants.md](references/constants.md): every measured number (layout, type, colour, radius, elevation, motion, timing, keyboard, touch).
- [references/shell-and-navigation.md](references/shell-and-navigation.md): IA, the attention inbox, action placement, menus, command palette, keyboard map, settings, onboarding, responsive and mobile.
- [references/states-copy-safety.md](references/states-copy-safety.md): empty, loading, error and offline states; copy voice and the deletion ladder; reversibility and confirmation.
- [references/interaction-defaults.md](references/interaction-defaults.md): measured behaviour defaults (tooltips, dismissal, focus, toasts, drag, undo grouping) and AI-native primitive anatomy.
- [references/review.md](references/review.md): the ship checklist, per-screen checklists and the scored screenshot review loop.
- [references/t3-code.md](references/t3-code.md): the T3 Code teardown the thesis comes from, including what not to copy.
- [references/categories/](references/categories/README.md): ten category playbooks (chat and answer engines, coding agents, productivity and notes, creative tools, AI browsers, mobile AI apps, health, finance, shopping, internal ops dashboards).
