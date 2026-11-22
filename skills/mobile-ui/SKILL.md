---
name: mobile-ui
description: Design or build an iPhone app screen (React Native / Expo, or native) so it feels clean, native and intuitive on the first try. Gives the decision order, measured iOS 26/27 Liquid Glass defaults (bars, tabs, sheets, rows, type, colour, targets), thumb-first placement, lists and swipe editing, keyboards and quick capture, sheets vs pushes vs full screens, live status, empty/loading/error states, widgets and notifications, dark mode, a review checklist, ten category playbooks drawn from about 40 well-made iPhone apps (Things, Todoist, Linear, Notion, Apple Notes, Bear, Craft, ChatGPT, Claude, Perplexity, Superhuman, Spark, Attio, Fantastical, Apple Weather, Copilot, Cash App, Robinhood, Flighty, Apple Maps, Gentler Streak, Oura, Streaks, Telegram, Spotify, Halide and others), and how each rule maps to Expo SDK 58. Use when starting, redesigning or reviewing any iPhone app screen or shell. For desktop and web app screens use product-ui; for motion mechanics in Expo use animate-expo; for web apps on a phone use mobile-native.
license: MIT
---

# Mobile UI (iPhone)

Build iPhone screens that feel like the best apps on the phone. The method comes from case studies of about 40 iPhone apps (App Store screenshots measured in points, makers' docs, mobile web, video frames), Apple's current Human Interface Guidelines and WWDC sessions for iOS 26 and 27, and the current Expo SDK. It is written as decisions to make in order, with a default for every decision nobody makes on purpose. It is the phone companion of `product-ui`: same thesis, different hand.

## Rule zero: cut words; show, don't label

The best phone apps say almost nothing. A phone screen holds a third of a desktop screen, so every label costs a row of content. Measured non-content words (labels, metadata words, status words, helper copy, button text; not the user's data; tab labels counted separately):

| Screen | Non-content words |
|---|---|
| Streaks home, Bear and Apple Notes editors, Obsidian editing | 0 |
| Notion page, Robinhood stock, Todoist Today, Obsidian reading | 1-2 |
| Things Today, Linear inbox, Attio table, Revolut home, Cash App pay | 3-4 |
| Gmail inbox, Apple Reminders, Flighty list, Airbnb home, Apple Maps place | 5 |
| Apple Mail inbox, Copilot review, Gmail thread, Spark thread | 8-9 |
| Apple Notes list, Spark home, Carrot home, Apple Weather home | 9-12 |
| The noisiest screens studied (Craft calendar with a chip repeated on 7 rows, Superhuman snooze sheet, Wise send review) | 17-20 |

**Targets:** at most 12 non-content words on a list or home screen and at most 15 on a detail screen, excluding tab bar labels; zero facts said twice. Count on the screenshot before calling a screen done.

How the references carry facts without words:

| Fact | Show it with |
|---|---|
| Which list or bucket | a fixed glyph and colour used everywhere: Things ★ Today, ☾ Evening, ⚑ deadline; Reminders tints the title, add button and tick in the list colour |
| Priority, urgency | the tick circle stroked in the priority colour (Todoist), a date chip coloured by nearness, a red dot for overdue (Amie) |
| Unread | one cue only: a 6-7pt dot (Superhuman, Spark) or bold (Gmail), never both plus a word |
| Status of a live thing | the section it sits in, a trailing coloured glyph (Linear), dashed outline for "needs your answer" (Notion Calendar), a filled tile only for the one past its threshold (Carrot) |
| Kind, sender, app | avatar, logo, app icon (Opal shows apps as icons, not names) |
| Field names | position and glyphs: Attio puts attribute icons where labels would go; the first line of a note is the title |
| Who did it | an avatar plus a small action badge (Linear activity rows) |
| Freshness | nothing while live; a word only when stale ("Offline · showing 09:41 data") |
| Money direction | sign and arrow plus colour on the change line only; rows stay neutral |

Generated phone UI does the opposite: a header that names the tab the tab bar already names, a "Recent activity" label over an obviously recent list, a status pill on every row of a list already sectioned by status, "Tap to view details" helper lines, a card around every row, a filled button for every action. Cut those first. Decoration is not text: glyphs, avatars, app icons, category colours and imagery stay and do the work words did. Over-correcting is also slop: tab labels stay (one word each; Superhuman, Linear and Attio go icon-only, and blind judges marked that down every time), mode and filter chips keep their word, a table with more than two value columns keeps its headers.

Full evidence and the slop signature with tests: [references/slop-vs-good.md](references/slop-vs-good.md).

### Region rules from side-by-side reviews

From builds judged blind against the real apps (Reminders, Gmail, Copilot, Attio, Flighty), where the real app won a region:

- **Hierarchy:** the screen title is the only large text. Section headers are 15pt semibold in secondary grey (Reminders' Morning / Afternoon), never black 20pt headings competing with the title.
- **Rhythm:** rows inside a section have no rule, or a hairline inset to the text; sections are separated by space or one inset divider, never both a rule under every row and a large gap.
- **Identity colour on the tick** only when the whole screen is one list. In a mixed view (Today, All) ticks stay neutral, so the overdue red is the only colour cue.
- **Dense rows truncate the title to one line** (two at most); the detail shows the rest. Wrapped titles break the scan.
- **Chips in dense rows** are glyph + text with no box; when chips are filled, each takes its own identity tint (Copilot's orange Restaurants, green Groceries), never identical grey pills.
- **An in-card batch action** (accept 2 reviewed) is a light tinted capsule; the filled button is only for the screen's commit.
- **Pushed list and database screens with a toolbar row** (view, sort, filter) use the inline title beside Back ("People"), so the content starts higher; large titles stay on tab roots and list destinations.
- **Sort and filter buttons stay neutral glyphs;** only an active filter is tinted, with its count.
- **Two complete columns beat a third that truncates the second.** Hint at more fields with the scroll itself, not a sliver of a header.
- **Avatars and glyphs stay even when the filter makes them redundant** (decoration, not text); a bare glyph with a number keeps its noun when the glyph is ambiguous ("2 linked").
- **A two-option menu** is text plus a checkmark, no icons per item, no selected fill. It hangs from the title's chevron or a header button, keeps that trigger visible, and never covers the first row of the list.
- **Stack multi-field blocks vertically on a phone;** never two legs, two accounts or two records side by side in columns (the values wrap and compete). **In a live detail block** one size jump: the identity line small (airport, code), the value large (the time), status and gate as one line or badge beside it. Colour only the value in a status sentence ("in **1h 42m**"), never the whole sentence.
- **Sheet actions sit in the sheet's footer** in reach (Share as the one filled capsule), not as a rail of buttons at the top of the canvas.
- **A section strip gets its own row;** never squeeze navigation pills between two utility buttons.
- **A title that is also a switcher** (mailbox, account, view) is compact: the name with a chevron and the mode as a subtitle ("Inbox ⌄ / Focused List", Spark), not a 34pt large title under floating controls. Content starts high.
- **A section that ranks above the rest** (Priority) is set apart by a faint tint band and its own glyph and colour; small grey headers are for equal sections.
- **Say the day once,** in the section header; times inside it stay bare ("6:21 PM", not "Yesterday 6:21 PM").
- **Grouped machine mail keeps its senders' identity:** avatar or logo chips with names and per-sender unread dots, not a wrapped grey sentence.
- **Health or status per row is a fixed-width trailing column of distinct glyphs** (check, warning, cross in their colours), no words for exceptions; tinted icon tiles plus separators plus counts are three treatments where one does (Linear).
- **A secondary id** (I-32, a code) sits small above the title, never as its own centred slot.
- **On a pushed screen, add lives in the header capsule;** the floating + is for root lists, where adding is the main act.
- **The hero gets room:** at least 24pt before the first module.
- **Repeated axes drop repeated units:** an hourly strip reads Now, 10, 11, 12 with AM/PM only where it changes; degree signs on values, not a unit on every label.
- **Module controls group at the header's trailing edge** (Weather's metric switch), never a wide pill that mixes a word with unlabelled glyphs.

## The thesis

**One thing at a time, under the thumb, on the content layer; controls float above it on glass.** A phone screen shows one object or one list. The content runs edge to edge and under the bars; navigation and controls sit on a separate floating Liquid Glass layer that never becomes content. The top of the screen is for reading and orientation, the bottom third is for acting. The phone's jobs are glance, capture, triage, approve and steer; long authoring stays on the big screen unless the product is a phone-first tool (ChatGPT's Spaces are read-only on the phone; Linear's iPhone app is for triage and capture).

Every element passes five tests (the same as `product-ui`):

1. **Is it needed right now?** If not, push it one level down, into a sheet, a menu or a long-press.
2. **Does it differ from the default?** If not, hide it.
3. **Is it where the thumb makes this decision?** If not, move it there.
4. **Does it need a human?** Then it gets the hero slot or an inserted card at the top. Otherwise it recedes.
5. **Is it already said?** By the tab bar, the title, the section, a glyph or a colour? Then delete it.

## Decision order

Write each decision down in a line or two before writing code.

0. **Fill in what the request left out.** Who opens this, how often, for how long (a 5-second glance, a 2-minute triage, a 20-minute session), the screen's one job, 8-15 realistic records with one long value and one failure, and the states present now. Never fill a gap with filler or labels.
1. **Category and centre of gravity.** Read the chapter in [references/categories/README.md](references/categories/README.md). Each category is judged on one question (tasks: can I capture and clear fast; money: can I trust this number; live status: what is happening and what do I do next). The richest components go to that question.
2. **The phone's job and the core loop.** Pick which of glance, capture, triage, approve, steer and author this app does on the phone, and name the loop (Superhuman: open, swipe done or later, repeat). If authoring is not the phone's job, show it read-only and say nothing about it.
3. **Shell.** 3-5 top-level destinations in the native tab bar, Search counted as one (trailing). Each tab is its own push stack with a large-title root. Create is an action, not a place: a separate floating + circle or a bottom toolbar button, not a tab. The exception is a social or media app where creating opens its own composer destination (Threads, Spotify). A single-object app (a calendar, a weather app, a camera) uses a floating bottom toolbar instead of tabs. Navigation and settings in [references/navigation-and-gestures.md](references/navigation-and-gestures.md).
4. **The hero.** Decide the one thing the screen leads with: the number (Robinhood, Weather), the verdict (Oura, Flighty), the input itself (Cash App's amount, ChatGPT's composer), or the list (Things, Mail). One hero per screen; everything else sits in uniform modules or rows below it.
5. **Objects and their state vocabulary.** One noun per concept; a closed set of states, each with a glyph and a semantic colour; the word appears once (the section header, or the row in an unsectioned list). Each lifecycle verb gets its inverse (done/undo, snooze/wake, pin/unpin).
6. **Text budget.** List every fact the screen shows and give each a home: position or section, glyph or avatar, colour, a chip, and only then a word. Write the non-content word target (rule zero).
7. **Placement by thumb.** The primary action sits bottom-right or bottom-centre in reach (floating + at 48-56pt, a bottom toolbar, a sticky commit bar). Search goes at the bottom. When search and create share that row, give each its own target without equal widths: search the long labelled capsule, create a small icon circle beside it (Apple Notes: 249 and 37 wide, 9 apart). Sheets that edit something commit with the tinted checkmark top-right and cancel with X top-left; sheets that run a flow (pay, send, review a batch) commit with one capsule at the bottom (Cash App, Copilot); display-only sheets have one ✕. A full screen commits with a 48-56pt capsule pinned above the home indicator, full width or sharing a sticky bar with the total (Airbnb). Destructive actions are never the default single swipe and never the filled button.
8. **Layer for each task.** Push to go deeper; a sheet with detents for a detour that returns (quick add, filter, pick); a full-screen cover only for immersive or blocking flows (camera, focus mode, onboarding); a pull-down menu for choices the user opened deliberately; a context menu on long-press that duplicates visible actions; an anchored action sheet for a choice about something just done; an alert only for a problem that needs a decision. Never a sheet on a sheet. A sheet that changes height keeps its object identifiable at every detent and restores the same object and state as it shrinks or closes (Apple Maps' place title went from y=470 to 159 and back); test both directions before adding a navigation level. Details in [references/navigation-and-gestures.md](references/navigation-and-gestures.md).
9. **Rows, swipes and editing.** Row anatomy, density and the swipe pair for each list; inline add at the end of the list; long-press menu; reorder and multi-select only where they earn it. [references/lists-and-editing.md](references/lists-and-editing.md).
10. **Input.** Keyboard type, return key and autofill on every field; a one-line quick add that parses as you type; the most frequent capture type reaches a focused editor in one tap, since a type menu in front of it adds a step to every capture (Notion's three-choice menu before Page); a keyboard accessory bar for structure; the keyboard never covers the commit. [references/input-and-forms.md](references/input-and-forms.md).
11. **Every state, before styling.** First run, permission primer, empty, loading, partial, error, offline, stale, paywall or gated. [references/states-and-system.md](references/states-and-system.md).
12. **Tokens.** System font through the Dynamic Type styles, semantic system colours, one tint, light and dark, concentric radii, 20pt margins for module layouts and 16pt for dense lists, glass only on the control layer. [references/visual-system.md](references/visual-system.md) and [references/constants.md](references/constants.md).
13. **Motion and haptics.** System transitions for navigation; custom motion only for rare meaningful moments; haptics only for meanings (success, warning, selection, snap). Mechanics in `animate-expo`.
14. **System surfaces.** Only the ones the product really has: notification actions that finish the job, one widget around one glanceable fact, a Live Activity for a bounded process. [references/states-and-system.md](references/states-and-system.md).
15. **Copy.** Delete first, then word it: sentence case, verb plus object, one-word statuses, the consequence on the commit button, empty states as one line plus the action.
16. **Build it native.** Map every choice to the Expo API in [references/react-native-expo.md](references/react-native-expo.md): native tabs and stacks, form sheets with detents, `@expo/ui` controls, semantic colours, `dynamicTypeRamp`.
17. **Review.** Run [references/review.md](references/review.md) on screenshots at 393pt, then 375pt and 440pt, in dark mode and at the largest text size. Count words first.

If the product has AI in it, load `ai-interaction-patterns` at step 5 and read the AI chapter.

## Twelve moves to carry everywhere

1. **One hero, then uniform modules.** One number, verdict, input or list leads at 2-5x body size; everything else uses one module or row component (Weather, Robinhood, Oura, Cash App).
2. **The bottom third is for acting.** Primary action, search and the commit bar live where the thumb rests; the top is for title and orientation.
3. **Create is an action, not a place.** A floating + beside or above the tab bar, draggable to choose where the new item lands (Things, Todoist, TickTick), pre-filled from where it was made.
4. **Swipe is the verb, and every verb is reversible.** One direction completes (done, archive), the other defers or toggles; delete is a second step or a trailing full swipe with undo, never a confirm dialog.
5. **Long-press is a faster twin of a visible path.** A context menu with a preview on every content row, its items also reachable elsewhere.
6. **Parse, don't form.** One line that understands "Call Dana tomorrow 3pm #Sales p1", highlights what it understood in place, and lets a tap undo a parse (Todoist, Fantastical, Reminders). The full form is one tap away.
7. **Push to go deeper, sheet to step aside, full screen to change rooms.** Sheets use system detents and a grabber; one at a time.
8. **Live things are phases with a verdict and a cause.** Lead with the value for the current phase, say why in one line, leave unknown slots empty, strike through the old value when it changes (Flighty, Uber, Apple Maps).
9. **Colour means identity or state; one tint means "tap".** Category colours carry labels' jobs; green and red only for direction, health, now or real failure; the accent only for interactive things and the one primary action.
10. **Glass is for controls, never content.** Bars, floating buttons and sheets are glass; rows, cards and pages are solid semantic backgrounds. No glass on glass.
11. **Calm by default; celebrate the set, not the tap.** Completion gets a short beat (a fill, a tone, a success haptic); the big moment is reserved for the whole day or a milestone (Streaks' gold page). Money and work tools celebrate nothing and show a receipt.
12. **The app reaches past itself.** Notifications that act (Done, Snooze, Reply), a widget around the one glanceable fact, a Live Activity while something runs.

The full laws with reasons and evidence: [references/laws.md](references/laws.md).

## Defaults when nothing else decides

| Thing | Default |
|---|---|
| Design width | 393 or 402pt; test 375 and 440. Lay out against safe areas and size classes, never device models (iOS 27 apps are resizable; iPhone Duo exists) |
| Margins | 20pt content inset for modules and cards (Apple's iOS 26 apps), 16pt in dense edge-to-edge lists; text-heavy reading 20-30pt |
| Safe areas | top 59-62pt on Dynamic Island phones, bottom 34pt; content scrolls under the bars, controls stay inside |
| Nav bar | large title 34pt bold on tab roots, collapsing to 17pt semibold inline; a destination title on a pushed object can be 26-28pt with its glyph; one subtitle line for a live count |
| Tab bar | native, floating glass, 3-5 items incl. Search, filled SF Symbols, one-word labels, minimizes on scroll; persistent status (player, running job) in its bottom accessory |
| Type | system font only; Dynamic Type styles: Body 17/22, Callout 16, Subhead 15, Footnote 13, Caption 12 and 11 min; no letter-spacing on SF; rounded SF for health and habit numbers; `tabular-nums` on every number |
| Rows | 44pt minimum target; dense task rows 44pt two-line, mail rows 79-102pt (3-4 lines, 38-44pt avatar), settings rows 52pt; separators inset to the text column or none |
| Cards and modules | 16pt margin, 8-12pt gap, 16pt padding, 12-26pt continuous corners (inset grouped list 26pt; small modules 12-16pt; health cards about 25pt); nested radius = parent minus padding |
| Buttons | one prominent per screen; capsules; full-width commit 48-56pt; icon buttons 44pt glass circles; hit area at least 44x44pt (`hitSlop`) |
| Floating + | 48-56pt circle, bottom-right, 16-28pt from the edges, above the tab bar |
| Sheets | system form sheet; medium (about 50%) and large detents; grabber; editing sheets X top-left and tinted ✓ top-right, flow sheets one bottom capsule; partial sheets float inset about 6pt; never stacked |
| Colour | semantic system colours by name; one tint (system blue is #0088FF since iOS 26, not #007AFF); light and dark for every custom colour; dark can tint toward the brand hue |
| Motion | system push and sheet transitions; critically damped springs; pickers about 130ms, inserts about 300ms; nothing loops except live indicators |
| Haptics | success on completion, warning/error on failure, selection while scrubbing or picking, light impact on a snap; never on plain taps or navigation |
| Undo | a 5s undo snackbar above the tab bar after archive, done, delete and send; shake-to-undo works by default |
| Waits | nothing for 400ms, then a skeleton or the live line; a pull-to-refresh spinner under the large title |

## Which skill does what

| Need | Skill |
|---|---|
| Desktop or web app screens, the shared thesis | `product-ui` |
| AI composer, streaming, approvals, citations, agent status | `ai-interaction-patterns` (plus the AI chapter here) |
| Motion in Expo: springs, gestures, press feedback, haptic timing, 120fps | `animate-expo` (its `NativeTabs` import and `Gesture.Pan()` recipes predate SDK 58: use `expo-router/native-tabs` and the RNGH 3 hook API) |
| Motion physics and Apple's design principles | `apple-design` (its material and tracking advice is web-only; on native, follow this skill) |
| Custom drag mechanics | `gestures` (web), `animate-expo` (native) |
| A web app or PWA on a phone (100vh, tap highlight, input zoom) | `mobile-native` |
| Colour ramps, contrast | `emil-color` |
| Worst-case data stress test | `break-ui` |
| Driving the real app to verify | the project's `verify-<app>` skill |

## Where this skill differs from product-ui, and why

| Topic | product-ui (desktop) | On an iPhone |
|---|---|---|
| Chrome text size | 13px meta, 14px body | 17pt body, 15pt secondary, 13pt meta, 11pt floor; Dynamic Type scales all of it |
| Columns | two persistent columns at most | one column; a second pane only as a sheet or a push |
| Navigation | sidebar plus ⌘K | 3-5 tabs plus a Search tab; the palette's job goes to search and long-press |
| Hover-revealed actions | metadata swaps for actions on hover | swipe actions and long-press menus; the always-needed action is visible |
| Modals | centred dialog, dimmed | bottom sheet with detents; alerts only for problems |
| Undo | ⌘Z for 5s | an undo snackbar for 5s, shake, three-finger swipe |
| Primary button | ink-filled | the system tint or brand colour on one prominent capsule; ink-filled works for money commits (Cash App, Uber) |
| Press feedback | scale .97, hover instant | the native highlight; scale only on custom cards; no hover |
| Title scale | detail titles 24-32px | tab roots 34pt large title (collapsing); object titles 26-28pt; destination titles never repeat the tab label |
| Keyboard | shortcuts in every tooltip | keyboard type, return key and an accessory bar on every field |
| Depth | no shadows on content | same; cards may use a soft shadow on a tinted page (Amie, Todoist) but never glass |

## Reference map

- [references/slop-vs-good.md](references/slop-vs-good.md): word counts per app, the generated-phone-UI signature and its tests.
- [references/laws.md](references/laws.md): the laws with why, evidence and anti-pattern.
- [references/constants.md](references/constants.md): every measured number (layout, bars, type, colour, rows, cards, sheets, targets, motion, haptics).
- [references/visual-system.md](references/visual-system.md): Liquid Glass layer model, type, colour roles, dark mode, numbers and charts, icons.
- [references/navigation-and-gestures.md](references/navigation-and-gestures.md): tabs, stacks, drawers, search, sheets vs pushes vs full screens, gestures, settings.
- [references/lists-and-editing.md](references/lists-and-editing.md): row anatomy, swipe actions, context menus, inline create, drag to place, reorder, multi-select, databases and tables on a phone.
- [references/input-and-forms.md](references/input-and-forms.md): quick capture, parsing, keyboard config and accessory bars, composers, pickers, forms, search.
- [references/states-and-system.md](references/states-and-system.md): first run, permissions, empty, loading, error, offline, celebration; notifications, widgets, Live Activities, app icon.
- [references/react-native-expo.md](references/react-native-expo.md): each pattern in Expo SDK 58, the default package set and the traps that make an RN app feel non-native.
- [references/review.md](references/review.md): the ship checklist and the screenshot review loop.
- [references/categories/](references/categories/README.md): ten category playbooks (tasks, notes and documents, AI assistants, mail and CRM, calendar, glance dashboards and system health, money, live status and maps, health and habit, media and social).
