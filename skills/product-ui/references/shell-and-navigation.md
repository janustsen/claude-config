# Shell, navigation, placement and command surfaces

Where things go and why. Each section gives what the best products do, the reason, and imperative rules. Numbers are in [constants.md](constants.md).

## 1. Information architecture

**The main object is the root screen, and everything else layers on it.** In a chat or agent tool the root is the thread; in a browser the page; in a shopping app the result grid; in an ops tool the day's work. Modes, tools and settings open as sheets, drawers, side panels or inline cards on top of it, never as separate destinations that drop context.

### Three zones plus overlays
- **Left: an attention inbox.** One flat list across containers, sorted by state of attention, with lifecycle shelves (T3 Code: Pinned / Active / Working / Snoozed / Settled). The container (project, team, folder) is metadata on each row (a small initials badge with an auto colour) plus a filter in the list header. Grouping by container is an opt-in setting.
- **Centre: one item** in a reading lane, its primary input at the bottom.
- **Right: on-demand tools** as tabs behind one "+" launcher (Diff, Files, Terminal, Browser, Preview). A properties sidecar floats top-right at wide widths and collapses into a toggle when the right panel opens.
- **Overlays:** settings, usage and account open as large sheets over the current item. Closing returns to the exact scroll position.

### Rules
1. Land the user on the primary input of their most recent context, never on a dashboard of tiles. A returning user's first screen answers "what changed since last time, and what needs me", with needs-action kept apart from FYI. Its counts are disjoint (an item counts once, in its most urgent bucket), each links to its items, and they are a snapshot from arrival: new events add a quiet "2 new" marker instead of silently recounting.
2. Sort the primary list by attention state (needs you, then in progress, then done). Activity never reorders rows; only a "needs you" event (finished, failed, approval, question) returns an item to the top.
3. Give "done for now" its own reversible state (T3 calls it Settle) between active and archived, shown as a collapsed shelf with a count ("Settled 100 ⌄"), about 10 rows then "Show 25 more". Auto-settle what is obviously finished (merged, inactive), and say in settings what does not auto-settle.
4. Open secondary areas as sheets over the work. Route swaps that drop context are for genuinely separate destinations only.
5. Keep the top bar to identity on the left (badge, breadcrumb "container / Item title", where the title is auto-derived and doubles as the item's menu) and view toggles on the right. Nothing else.
6. Write scope pickers as a sentence with inline selects: "Applying settings for [All projects ▾] across [All environments ▾]". Turn filters into breadcrumb segments: "Usage / All environments ▾ / All providers ▾".
7. Let the sidebar footer change with context: icon buttons for rare global destinations (Settings, Usage), which become "← Back" on utility pages.
8. Redirect legacy routes instead of returning a 404.
9. Give background agents a Tasks surface grouped Running (or Watching), Needs you, Done and Failed. Each row shows its current value and since when ("Now $640 · since today"); the empty state lists example asks.
10. Bound proactive output: a finite set of cards on a schedule, with feedback on each and a visible pause.
11. Profiles and workspaces separate what the AI knows, not just logins.

## 2. Action placement

### The composer (the primary input)
- Bottom row, left to right: attach on the far left (one button, deliberately not a "+" menu when there is only one thing to attach), flexible space, then the right cluster: model chip (effort word muted), mode or permission chip (only when non-default), and the round primary slot at the far right. Context controls go bottom-left; voice and send bottom-right, because reading order puts "what it is about" before "go".
- The primary slot is a state machine in one spot: disabled, send, stop (red, round) while running with an empty draft, steer while running with text, queue, resume, update when editing a queued message, "Submit answer" or "Implement".
- A context strip directly under the composer (12px text, 24px controls) holds where the work runs (workspace, branch, recipient). It shows only until the choice is locked.

### Lists and rows
- Hover swaps content in place and never adds. The relative time fades out over 150ms and an action icon takes its spot; a greyscale container badge regains colour. Same footprint, no layout shift, actions exactly where the eye already is.
- A rich hover card can open to the side with the full title and metadata.
- On touch, per-item actions are always visible in a quiet tertiary colour, because hover does not exist.
- Attach actions and feedback to the object being judged, first in its ⋯ menu ("Shop more like this", "Suggest less").

### Inline actions
- Put actions next to the content they act on: "Open diff" on the edited file, Approve on the exact action row, Copy and "Copy prompt link" under the message on hover.

### Buttons
- One primary action per region, in a fixed position, whose verb changes with state.
- Split buttons put the frequent action on the face and alternatives on the chevron; picking an alternative sets the new default. The label follows object state ("Commit & push" becomes "Publish repository" with no remote).
- Show the two most common options and put the rest under "More", but always keep the safe option visible (Decline next to Approve).
- Commit buttons name their consequence and update live ("Apply 3 changes", "Send to Alex", "Import 1 project").
- Consent dialogs give equal width to yes and no.
- Permission and scope reassurance goes directly under the commit button ("Read-only and encrypted."), because the fear peaks at the click.
- Outbound actions name where they go and show an outbound glyph ("Buy on Nordstrom · $233.16 ↗").
- Teach modifier variants in tooltips ("New thread (⇧⌘O) · Shift+click: in current project") instead of adding buttons.

### Panels
- A panel's toggle sits on the edge where the panel opens, carries a label, and shows the close state on the same control.
- Side-panel headers hold one create action, one layout-and-close cluster, and the current subject as the title. Secondary views become tabs with counts ("Answer | Sources · 1").
- Right panel: tabs left, a "+" launcher right after the last tab, view controls (maximise, dock, close) far right. Inside a tool, its toolbar reads scope, then stats, then display toggles ("Tool call ▾ · +1 −0 · expand, split, wrap, whitespace, tree").

### Dialogs
- Buttons right-aligned in a footer under a hairline: Cancel (outline), then Confirm. A destructive confirm is red and last.
- Focus starts on Cancel. Shortcuts are inert inside the dialog.
- Title: a question naming the object. Body: the consequence.

### Corners
- Bottom-left: rare global destinations as 32px icon-only buttons with tooltips.
- Bottom-right: transient status that appears only when relevant ("Update 1 provider", which becomes a spinner while updating).

## 3. Menus and command surfaces

### Command palette (⌘K)
- Top-anchored, about 576px wide, radius 16, glass over a blurred backdrop, 200ms scale and opacity enter. Its height morphs between pages.
- Empty query: an Actions section (the first action names the current context in bold: "New thread in **demo-shop**") then Recents.
- Rows: icon, title, optional muted subtitle, right-aligned live shortcut. Rows that open a sub-page end in "›".
- Search is typo-tolerant across actions, items, containers and settings, with message text ranked last. A `>` prefix filters to actions; ⌘1-9 pick numbered rows.
- Backspace on an empty query pops a level. Esc goes back one level, then closes. Focus returns to the primary input.
- A footer legend whose verbs change per page ("↑↓ Navigate · Enter Select · Esc Close"; on a create page "Enter Create · Backspace Back").
- Unavailable sources stay listed, dimmed, with a "Setup Required" badge.

### Anchored pickers
- Popover above the trigger, 150ms scale .98 plus opacity, then width and height transitions as content changes.
- Frequent settings get search + list + detail column. The model picker: a provider rail with an active bar; a list with an underlined search field, ✓ on current, ☆ favourite on hover and ⌘1-4 chips; a reasoning column (Low / Medium ✓ / High / Max); a speed segmented control in the footer.
- Risky modes get a stepped slider whose selected step shows its name and one-sentence consequence; hovering another step previews its description before commit. Use a crossed-shield icon for "full access", because an open lock reads like a closed one at small sizes.
- Searchable pickers mark the current value with a muted "current" suffix.

### Inline trigger menus
- `/` commands, `@` references, `$` skills, `#` linked items. They dock to the input's top edge as an attached tray (square the shared corners), not a floating popover.
- One line per item: the trigger word at weight 500, a truncated muted description, a fade at the bottom edge. About 5 items, then "View more", then "All of X" group rows. A pick becomes an inline token and a chip in the manifest of what will be sent.
- No results: one muted line ("No matching files or folders.").
- Saved prompts expand into the input on pick (with their mode and source) and stay editable; they never execute blindly.

### Other menus
- Menus and selects open instantly.
- Destructive items come last, behind a separator, with a trash glyph.
- Single-letter menu-local accelerators are right-aligned.
- Unavailable items stay visible, greyed, and say why on hover ("Available for Git repositories.").
- Irreversible remote actions (merge, close, revert) use a two-click confirm inside the menu that disarms after 3s.
- Selection verbs depend on context: reading a page, editing a field and an empty field each get a different, short list.
- Native OS context menus cannot show accelerators, so teach those chords elsewhere.

## 4. Keyboard

1. Store shortcuts as data (key, command id, optional `when` context, source: default / custom / project) and render every label from that table: matching, tooltips, menu rows, palette rows, the keybindings settings page and conflict warnings.
2. Borrow conventions from the category each surface resembles (table in [constants.md](constants.md)). Never invent a chord where a convention exists.
3. One chord means one thing per context. Overload only across contexts that cannot overlap (terminal focus vs app). Protect text inputs and terminals.
4. Shortcuts never destroy something unseen: ⌘W never closes the window; ⌘Q needs a hold or double press; ⌘Z undoes list actions only right after them; shortcuts are swallowed inside confirmation dialogs.
5. A shortcut clicks the visible control, so a hidden or disabled control disables its shortcut.
6. Teach inline: tooltips read "New thread (⇧⌘O)"; palette rows show chords; holding ⌘ for 200ms shows 1-9 badges on list rows. Pick one tooltip format and use it everywhere.
7. Focus returns to the primary input after the palette, after find, on item open and on window refocus. Typing or pasting anywhere lands in the input.
8. Escape closes only the topmost layer (IME, then menu, then palette level, then dialog), and focus returns to the trigger or the nearest neighbour, never to `<body>`.
9. Every Enter and Escape handler is IME-safe (checks `isComposing`).
10. Give agent runs a stop chord (Esc or ⌘. when the input is empty) and put it in the stop label: "Stop response (Esc)".
11. Ship a `?` cheat sheet. Block conflicting rebinds instead of only warning.

## 5. Settings

1. The shell is a large modal sheet. Left nav: "Search /" at the top, then plain groups, then maintenance and account at the bottom. Header: breadcrumb "Settings / General", "Restore defaults", close.
2. Every setting is a title (14px/500) with a one- or two-sentence consequence description (muted) on the left and the control on the right (select, switch, slider with a mono value chip, segmented control), grouped in bordered cards of radius 12 under plain section headings.
3. Write descriptions as what happens, including the edge case ("Inactivity does not settle threads with a pull request. Merge and close still do."), and mention the other place the same thing can be changed ("You can also right-click the card.").
4. Use visual pickers for anything visual: mini-UI thumbnails for colour scheme, swatch cards for themes, a live sample sentence with real chips for the interface font.
5. Summarise multi-toggles in the trigger ("Thread details: 10 of 12 on").
6. Quarantine experiments in Labs and label legacy features "(legacy)".
7. Default anything that publishes outward to off (an unchecked "Create private repository" checkbox).
8. Confirmation defaults follow data loss: delete confirms, reversible actions do not.
9. Build themes on semantic tokens, with accent (selection, focus) and action (filled calls to action) as separate roles. Expose contrast and density knobs, not just colour. Make costly effects (glass, layout animation) tunable and off-able.
10. On phones the settings nav becomes an icon rail and rows stack (description, then a full-width control).

## 6. Onboarding and first run

1. If the product is one question, the front door is that input.
2. Onboard over the real product: a glass dialog over the blurred live app, never a separate marketing screen.
3. Detect and pre-select. The user confirms instead of filling in: detect installed tools, scan existing history, pre-check the most likely choice. Show evidence on each choice (counts, recency, source icons) so the default is trustworthy, and be honest about coverage ("Scan limit reached").
4. Put the count in the CTA ("Import 1 project"). Skip is a quiet ghost button, but present.
5. A segmented stepper with filled checks for completed steps; the container height morphs (200ms ease-out) between steps.
6. Gate the second turn, not the first: deliver value, then ask for an account or consent at the point of loss ("Don't lose this chat"). Ask for permissions just in time, and warn before an OS prompt appears.
7. Onboard on the user's own content with one pre-filled real action; label sample prompts with what they will touch.
8. For products that act on the user's behalf, teach trust first (what is stored, what is sent), then one shortcut, then a time expectation.
9. End inside a working state (a real thread, a real record), not a tour.

## 7. Responsive and mobile

1. Build primitives mobile-first (16px text, 36px controls, 44px hit areas) and densify at the desktop breakpoint (14px, 24-32px controls).
2. Inputs are at least 16px on touch, which stops iOS zooming on focus.
3. Panels become full sheets on phones; side navs become icon rails or a full-screen sheet with the same rows.
4. Anything revealed on hover is always visible on `pointer: coarse`.
5. Decide what each device does, on purpose, and say so: read, approve, steer and share on the phone; author on the big screen. An honest read-only view beats a cramped editor.
6. The bottom-right thumb slot is the one primary action, and it is re-assigned when the job changes stage (composer, then "Continue → Licensed doctors available now").
7. Long-press is a faster route to something already visible, never the only route.
8. On narrow screens drop the absolute change, the seconds and the timezone first; keep the percentage and the input.
9. Make each mode a system entry point where the platform allows (widget, shortcut, action button, live activity) that opens straight into the mode.
10. Consequential actions need on-screen approve or decline, even mid-voice.

Phone-specific mechanics (100vh, tap highlight, safe areas, pull-to-refresh) are in `mobile-native`; the mobile AI playbook is in [categories/mobile-ai-apps.md](categories/mobile-ai-apps.md).
