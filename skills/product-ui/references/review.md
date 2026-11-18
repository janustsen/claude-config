# Review

Review the real build, not the code. Screenshot it, score it, fix the weakest thing, repeat on the same commit. Run in this order: cut words, the ship checklist, the per-screen checklist, worst-case data, then the scored loop until it passes.

## 0. Cut words; show, don't label (always first)

1. Screenshot the screen at 1440x900 in light mode.
2. Count every visible word that is not the user's data: labels, metadata, status words, section headers, helper lines, button text, placeholders. Count each number or timestamp as one word.
3. Targets (from the reference apps, see slop-vs-good.md): at most 15 in the reading lane, zero facts said twice. Navigation and settings labels do not count against the lane; whole screens with navigation measure 30-60 on the reference apps.
4. For each word, run in order and stop at the first that applies: is it said elsewhere on screen (delete)? Is it the default (delete)? Can position, section, icon, avatar or ink carry it (replace)? Does the user act differently because of it (keep)?
5. Recount. Then count containers (at most 3 boxed or filled in the lane), columns (at most 2 persistent), text sizes (at most 4) and filled buttons (one per region).

Before and after, from a generated agent inbox:

| Before | After |
|---|---|
| Detail header "Approval · Quill drafted this for you · Halden Freight · 4m ago" under the title | The title alone; the selected row already says all four |
| Sidebar "Since yesterday 17:40: 4 need you, 11 done, 1 failed" | Deleted: the section badge, the shelf count and the red row say it |
| Row "Approval · Quill · Halden Freight" under each title | A kind icon or the client's logo; the section header says the state |
| "Based on · 3" over three source cards | Inline source chips; one "3 sources" control that opens them |
| "Check before sending." before a caveat | The caveat sentence, on an amber highlight |
| "From sam@ferrowell.example · 1 recipient · 5s to undo after sending" | Deleted: "Send to Mira Okafor" says it, the undo appears after sending |
| "To", "Subject" labels | Recipient as an avatar chip, the subject as the draft's first line |
| "Live · checked 12:12" | Deleted; "Offline · last synced 12:12" appears only when it is true |

Credit for sections 3-5: **heydamir/unslop** by Damir Sokolovsky (CC BY 4.0), **checklist.design** by George Hatzis and its agent skill (MIT), and a public T3 Code design-review run by Theo shown on X. Tags: [obs] seen in source or screenshots, [doc] the resource's own text, [inf] inference. Laws are cited by ID from [laws.md](laws.md).

## 1. Ship checklist

Each item must be true, checked on a screenshot or by driving the app.

**Structure**
- [ ] The first screen is the primary input (or a "what changed, what needs you" summary), not a dashboard of tiles or a greeting.
- [ ] The main list is ordered by attention state, and background activity does not reorder it.
- [ ] Done items collapse into a shelf with a count. "Done for now" is reversible, with undo.
- [ ] Secondary areas (settings, usage, account) open as sheets over the work and return to the same scroll position.
- [ ] The top-left slot switches workspace, account or model, or is the home button; no static logo-and-name block
- [ ] Each fact is said once per screen. The detail view does not repeat the selected row.
- [ ] Non-content words: at most 15 in the reading lane (section 0).

**Placement**
- [ ] Every control that configures the next action sits on the input that triggers it.
- [ ] The primary button has one position and changes its icon and label with state.
- [ ] There is exactly one filled button per region (ink by default), and the accent appears nowhere decorative.
- [ ] Non-default values are visible; default values are hidden.
- [ ] Hover actions replace metadata in place with no layout shift, and are visible on touch.
- [ ] Commit buttons name their consequence ("Send to Alex", "Apply 3 changes").

**States**
- [ ] Every list has loading (skeleton in the final shape, after 400ms, with a label), zero (with a first action), no results (with clear filters) and error (with retry).
- [ ] Every error names the cause and the fix, where it happened. Unavailable options say how to enable them.
- [ ] Long processes show a receipt, a summary sentence with counts and typed rows; failures stay expanded; stopped work says it stopped.
- [ ] Every reversible action has a 5s ⌘Z undo; only irreversible ones confirm.
- [ ] Destructive dialogs: question title naming the object, consequence body, Cancel focused, red confirm last.

**Craft**
- [ ] Selected rows use neutral alpha (and reach 3:1 via fill, outline or weight), not accent colour.
- [ ] 12-13px chrome, 14px body, 15-16px reading prose, 500/600 weights, `tabular-nums` on changing numbers, middle-truncated identifiers.
- [ ] Radii come from one ladder and nest concentrically. Glass appears only on floating layers.
- [ ] Menus open instantly; popovers 150ms; dialogs 200ms; nothing loops except one working indicator, paused off-screen.
- [ ] Focus rings are visible (inset where content scrolls). Focus returns to the primary input after transient surfaces close. Escape closes only the top layer.
- [ ] ⌘K lists every action with its shortcut; tooltips show chords in one format.
- [ ] Dark mode is designed (true or near black, white-alpha borders), not inverted. Both themes screenshotted.
- [ ] Inputs are at least 16px on touch, hit areas at least 44px on coarse pointers, panels become sheets on phones.
- [ ] Copy: sentence case, verb + object, each count once on the thing it counts, one term per concept, one "…" style, no em dashes, no restating captions, no narration of what the screen shows.

**AI surfaces** (if any): the ten review questions at the end of `ai-interaction-patterns`.

## 2. Verification loop

1. **Drive the real thing.** Launch the app and click through every changed screen in a real browser or the app itself (the project's `verify-<app>` skill, `chrome-devtools-axi`, a simulator). Static reading of JSX misses most UI bugs; an agent that can see its output iterates until it is good.
2. **Screenshot a fixed set** at the same viewports each round: 1440x900 and 390x844, light and dark, plus every state (empty, loading, error, needs-you).
3. **Run worst-case data** (`break-ui`): long names, unbreakable strings, zero items, huge counts, non-Latin text, missing fields.
4. **Grade with a separate reviewer.** The builder does not grade its own work; a fresh-context reviewer scores against a rubric (a separate grader against a rubric measurably raises task success). Use the scored loop below.
5. **Pin the commit.** Every score applies to one commit hash. A review of an earlier commit does not count.
6. **Bring evidence back**: the screenshots (or a short recording) go with the report or PR, minus anything exposing private data.
7. **Turn repeated corrections into rules** (`learn-taste`), so the next build starts from them.

## 3. Redesign pass order (unslop)

Credit: heydamir/unslop, CC BY 4.0, Damir Sokolovsky. All [doc] unless tagged.

### Run flow

1. Look at the live screens (a snapshot script captures live URLs).
2. Audit against its catalogue of slop signs.
3. Decide the verdict: heavy slop, light slop, or none.
4. Write the direction in five lines (product, character, world, moments, signature) and stop for confirmation.
5. Run nine passes in order.
6. Check.
7. Report.

### Pass order

| # | Pass | Why this position [inf] |
|---|---|---|
| 1 | Spacing | Rhythm errors (gaps of 16, 24, 36, 18, 32px side by side) make every later pass look wrong |
| 2 | Color | Draining color early shows what the layout really is |
| 3 | Icons | Emoji and mixed icon sets only become obvious once color is gone |
| 4 | Copy | Run the deletion ladder (states-copy-safety.md) here |
| 5 | Type | Sizes depend on what copy survived |
| 6 | Layout | Rearrange once the content is final |
| 7 | Details | Alignment, number formats, states |
| 8 | Visuals | Imagery and effects, if any are needed |
| 9 | Motion | Last, because it decorates a finished structure |

The before/middle/after frames in the unslop repo confirm the order [obs]: the middle frame has the purple drained to graphite while the emoji icons remain, so color was fixed before icons.

- Write and confirm the five-line direction before any pass, because passes without a direction converge on a generic clean look.
- Run the passes in order and do not skip ahead to motion, because each pass changes what the next one sees.

### Dashboard and app-layout rules

| Element | Rule |
|---|---|
| Sidebar | 240-280px |
| Content width | capped at 1440-1600px |
| Nav rows | 32-36px, 2-4px gaps |
| Section labels | 24px above, 8px below |
| Stat card | label, figure, change against a reference. Numbers only, no sparkline |
| Main chart | spans at least two thirds of the width, 280-360px tall |
| Secondary block | a list or a table, not a second chart |
| Chart color | one accent per chart; muted grid; mono labels |
| Dark-theme primary button | off-white; the accent goes elsewhere |
| Button highlight (dark) | `inset 0 1px 0 rgba(255,255,255,0.12)` |
| Generated imagery | dashboards almost never need it |
| Glyph, halftone, duotone effects | 8-12fps, paused offscreen |

What the "after" frame did [obs]:

- Sentence-case section labels ("Navigation", "Plans") replaced uppercase tracked labels; Lucide line icons replaced emoji.
- "Search ⌘K" with keycaps at the top of the sidebar (L18).
- Quiet mono counts in the nav (12, 18, 64, 210, 480, 1.2k).
- Colored dots beside each plan that are also the chart's series colors.
- The active nav row is a one-step surface change.
- The page title is functional ("October 2026", year muted), not a greeting.
- "+12% vs last month" in mono green; "Overdue 07 · 3 fewer".
- A revenue chart of soft colored curves against grey comparison curves, mono axis labels.

What the "before" frame got wrong [obs]: purple gradient, emoji nav icons, "PRO" and "New ✨" badges, uppercase "NAVIGATION", a greeting headline with a waving emoji, "+12%!!", a glowing bar chart with uppercase day labels, mixed number formats ("07" next to "$124,860.40"), and misalignments of 11px and 7px.

Rules:

1. Give stat cards exactly a label, a figure and the change against a named reference with its period, because a sparkline in every card is noise and one good chart answers the trend question faster.
2. Make one main chart span at least two thirds of the width at 280-360px tall, and make the secondary block a list or table, because two competing charts split attention.
3. Use the same token for a legend dot and its chart series, because lists and charts then cross-reference without a legend lookup.
4. Title the page by function (period, scope) with the secondary part muted, never with a greeting, because a dashboard is opened to make a decision. Where checklist.design asks for a personal welcome, show nothing: the needs-you count on its section already answers "what changed". Add a since-last-visit line only when the screen shows no such counts [inf].
5. In dark themes make the primary button off-white and spend the accent elsewhere, because an accent-filled button on dark competes with status color.
6. Use one number format per figure type across the page, because "07" next to "$124,860.40" reads as two systems.

## 4. Per-screen checklists (checklist.design)

Credit: checklist.design by George Hatzis, MIT. The site holds 138 checklists across Mobile, Web app, Website, Design system and Flows. Its agent skill has two modes [doc]:

- **Audit**: item by item, mark each present, partial, missing, not needed, or can't tell.
- **Critique**: peer-style prose from a rendered screenshot that must name at least two strengths. It bans filler words such as "effectively", "leverages", "robust", "streamlined".

Run the audit for the matching screen before shipping and fix every "missing" that is not "not needed", because agents build the happy path and the checklist is where the rest lives. Condensed items, all [doc]:

### Dashboard and home

- [ ] What changed since the last visit is visible (as section counts and new-item dots, not a sentence restating them).
- [ ] 3-5 key metrics, each with its time period and a comparison.
- [ ] 3-5 quick actions, chosen from usage data.
- [ ] Recent activity, ordered by last accessed.
- [ ] "Requires action" separated from "FYI"; watch for alert fatigue (L17).
- [ ] Stale or offline data says so where it is stale; live data carries no freshness label.
- [ ] Onboarding retires once complete.
- [ ] Empty dashboard offers a first action.
- [ ] Layout control is available.
- Principle: the defaults are the product's statement of what matters.

### Tables (and lists)

- [ ] Sort indicator always visible, not only on hover.
- [ ] Column visibility and order persist.
- [ ] Selecting rows shows an "N selected" bar.
- [ ] 2-3 hover row actions at most; the rest in an overflow menu.
- [ ] Active filters show as chips.
- [ ] Pagination reads like "1-50 of 1,240".
- [ ] First column frozen, header sticky.
- [ ] Export reflects the current filters.
- [ ] Loading uses skeleton rows that mirror the layout.
- Lists: typographic hierarchy with at most 3-4 secondary fields; actions on the right, fading in on hover; sort and filter persist; "Load more" over infinite scroll for reference content; sticky group headers.

### Empty states

- [ ] Contextual visual and a plain heading ("No projects yet").
- [ ] The CTA creates the first item (L20).
- [ ] Zero state is distinct from "no results"; no results always offers an escape (clear filters).
- [ ] Error state is distinct from empty, with retry.
- Rule: ship all four states for every list and table (loading, zero, no results, error) and never let one stand in for another, because a blank table cannot tell the user whether to create, clear or retry [inf].

### Forms

- [ ] Validate on blur; clear the error when the field is refocused.
- [ ] Save stays disabled until something changes, then shows loading, then a saved confirmation.
- [ ] In documents, autosave shows "Saving… → Saved 3 seconds ago".
- [ ] No all-caps labels.
- [ ] Placeholder is lighter than the entered value.
- [ ] Toggles are for on/off only, not for choosing between two options.
- [ ] Button copy says what happens.
- Detail views: title, then only what the list row did not already show; status is not repeated from the row; related activity and back navigation; destructive actions separated from the rest.

### Navigation

- [ ] Tabs are about one word each, ordered by popularity.
- [ ] Breadcrumb: the current page is not a link; truncate at 3-4 levels.
- [ ] Dropdowns: do not mix items with and without icons; destructive items last after a divider; one level of nesting at most; disabled items explain why in a tooltip; shortcuts align trailing.
- [ ] Tooltips: inverse contrast, one at a time, never covering the subject.
- [ ] Badges: a dot for a single update, a number for a count.
- [ ] Search results: prefill the query, show the count even at zero, highlight the match, show type indicators, offer filters, suggestions on no match, and recent searches.

### Chat and feed

- [ ] Never interrupt the user's upward scroll when new messages arrive (implement with stick-to-bottom, see interaction-defaults).
- [ ] Shift+Enter inserts a newline.
- [ ] Consecutive messages group; timestamps shown.
- [ ] Feeds use a "new items" banner instead of injecting items under the reader.
- [ ] Notifications: date groups, unread state, type, relative timestamps that turn absolute, mark all read, empty state.
- [ ] Audit log: most recent first, actor ID, link to the resource, export.

### Cards

The extracted checklists have no dedicated card list; these card items come from the related lists and from unslop [doc]:

- [ ] Status is never colour alone: an icon shape or the section header carries it too; the word appears once per screen.
- [ ] Badges follow the dot-versus-number rule.
- [ ] Stat cards: label, figure, change against a reference with period, no sparkline (unslop).
- [ ] Loading skeleton mirrors the card and fades into the content.
- [ ] Loading copy is specific ("Syncing your emails"); instant transitions show no loader at all.
- [ ] Analytics cards: labeled axes; % for large values and absolute numbers for small ones in period comparisons; segment breakdown; "No data for this period" when empty.

### Foundations the checklists assume

- Modular type scale of 1.25, 1.333 or 1.5; line height 1.5 body, 1.2 headings, 1.1 display; check at 200% zoom.
- Spacing on a 4 or 8 base, with component spacing kept separate from layout spacing; offer density modes.
- Colors flow from primitives to semantic tokens; dark mode is its own system, not an inversion.

## 5. The scored screenshot review loop

Source: a public T3 Code design-review run by Theo, shown in screenshots on X [obs].

### What happened

- The goal prompt told the agent to keep improving the UI until a "council" of reviewer agents all scored a set of app screenshots at least 9/10 for design quality, working in one PR, and the critic's own posts were attached as input.
- A review subagent scored each category against two named competitors.

| Category | T3 main | T3 current | Claude Code | Codex |
|---|---|---|---|---|
| Typography | 7.2 | 7.5 | 8.4 | 8.8 |
| Hierarchy | 6.6 | 7.2 | 8.5 | 8.5 |
| Spacing & density | 7.8 | 8.0 | 7.8 | 8.2 |
| Color & contrast | 6.7 | 7.1 | 8.3 | 8.4 |
| Iconography | 7.2 | 7.7 | 8.4 | 8.5 |
| Consistency & polish | 6.9 | 7.5 | 8.5 | 8.6 |
| Clarity | 6.9 | 7.3 | 8.4 | 8.6 |
| Overall | 7.0 | 7.4 | 8.3 | 8.5 |

- The rubric later grew to 14 categories. By round 12 one reviewer gave 10/10 in all 14; another gave 9.5 and "ship it" without having re-reviewed the final commit; one was still running and one had been cancelled.
- The rule that emerged: every reviewer scores the same final commit hash.
- Fixes got as fine as a label sitting 6px short of the right column edge.
- The PR showed "Classic" next to "New design" in dark and light. One pane was left out on purpose because it exposed private model IDs.

### The loop, as a procedure

1. Screenshot every key screen in both themes, at the same viewport each round.
2. Pick 7-14 named categories (start with the seven above; add states, motion, density, copy as needed).
3. Name two benchmark products the audience already respects, and score them in the same table, because an absolute "8/10" drifts while "below Codex on hierarchy" does not.
4. Score baseline (main) and current side by side, because the delta shows whether the round helped.
5. Give the reviewer the target critic's own words as input, because the goal is "would this person approve", not abstract quality.
6. Fix the lowest category first, re-screenshot, re-score.
7. Before the final round, run the checklist.design audit (section 4) and worst-case data (long names, zero items, huge counts), because a scored screenshot of the happy path hides empty and error states.
8. Stop only when every reviewer gives at least 9/10 on every category, all scored against the same commit hash, because a stale review of an earlier commit must not count.
9. Leave out any screenshot that exposes private data, because review artifacts end up in public PRs.

### UI details visible in the reviewed app [obs]

- "Worked for 2m 56s ›" as the collapsed work summary; "Working for 35s" while running (L5).
- A "Scroll to end ⌄" pill above the composer.
- A composer placeholder that teaches the triggers: "Ask anything. @ files, $ skills, / commands". Write placeholders that teach input syntax, because the placeholder costs no space and replaces an onboarding tip.
- Send is a round ↑ that becomes a red stop square while running (L12).
- A "Pursuing goal · 1 check" banner above the composer while a goal is active.

## 6. Order of operations

1. Deletion ladder on every string (states-copy-safety.md).
2. On a redesign, write the five-line direction, then the nine unslop passes (section 3).
3. Audit each screen with its checklist (section 4).
4. Score the screenshots against two benchmarks on one commit, iterate to 9/10 (section 5).

## 7. Light review for a prototype

A single-file prototype or a spike does not need the full loop. Screenshot it in both themes at 1440 and 390, run the ship checklist (section 1) and the matching per-screen checklist (section 4), click through every control once, and note which items were checked by reading code rather than driving. Run the scored loop before the design ships for real.
