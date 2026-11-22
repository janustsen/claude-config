# Navigation, layers and gestures

Where things live on an iPhone screen, how the user moves between them, and which layer each task belongs on. Evidence tags: [doc] Apple or maker docs, [meas] measured, [obs] seen in captures, [know] prior knowledge. Case files are in firstmate `data/mobile-design-skill/evidence/cases/`.

## 1. The two layers

iOS 26 split every screen into a **content layer** (lists, cards, documents, maps, media) and a **control layer** of Liquid Glass floating above it (nav buttons, tab bar, toolbars, sheets, menus) [doc WWDC25 219, 356].

- Content runs edge to edge and scrolls under the bars. Brand colour, imagery and washes live in the content, so they show through the glass [doc 251].
- Bars have no background colour, no border, no hairline. The scroll-edge blur is the separator; a 1px divider under a floating bar stacks two separators [doc 356].
- Never make content glass, never put glass on glass. A card, row or page background is a solid semantic colour [doc materials].
- Only one control per screen is tinted: the prominent action. Everything else on glass is monochrome [doc toolbars].
- The old look cannot be opted into once an app is built with Xcode 27 [doc WWDC26 102]. In Expo SDK 58 the header is transparent glass by default on iOS 26+.

## 2. Top-level structure

### Tab bar (the default shell)

- **3-5 destinations, Search counted as one** and placed trailing [doc tab-bars]. Fewer is better: Superhuman 3 + avatar, Cash App 3, Attio 4, Wise 4, Revolut 5 [obs].
- Native floating glass bar: filled SF Symbols, one-word labels, minimizes on scroll and re-expands on reverse scroll [doc]. Icon-only bars exist (Superhuman, Linear, Attio) but cost clarity: in blind reviews an icon-only Mail / Chat / Meet bar lost to the labelled one both times. Keep labels.
- Never put an action in the tab bar (Compose, Add, New). Create sits outside it: Craft splits the floating bar into a destination capsule and an action capsule (+, AI); Oura floats + as its own circle; Reminders and Things float a + bottom-right [obs]. Expo: `NativeTabs` plus an overlay `Pressable`, or a bottom toolbar.
- Never hide a tab when its section is empty; show its empty state [doc].
- **Bottom accessory** for app-wide live status: Music's mini player, a running sync, an active timer. Never a screen-specific action [doc 356].
- **Prominent tab** (iOS 27): one tab stays visible when the bar collapses [doc 278].
- Let users choose tabs only in power tools with many surfaces (Todoist pins any view to the tab bar, up to 5; TickTick assembles its bar from a tool list) [doc]. Default to the 3-4 most used.

### When not to use tabs

- **Single-object apps** (a calendar, a weather app, a camera, a map) use a floating bottom toolbar with the current scope as a named pill and a few glass buttons: Fantastical, Notion Calendar, Apple Weather's page dots, Apple Maps' sheet [obs].
- **Thread-first apps** (ChatGPT, Claude, Perplexity) have no tab bar: the thread is the home, history is a drawer or a pushed list, new chat is a top-right button [obs].
- **Swipeable top tabs** for peer feeds: Notion's 2026 Home has pill tabs at the top (Home, Chats, Meetings, Inbox) where the selected pill expands with its label and you swipe between them [doc/3p]. Copilot uses a scrolling pill strip for 6+ equal sections, user-reorderable [obs].
- **Drawers** only for a large tree the user rarely changes (Obsidian's file drawer at about 80% width from the left edge; Claude's history) [obs]. A drawer hides navigation; never put the main destinations in one.

### Stacks

- Each tab is its own push stack; the tab root has a 34pt large title that collapses to a 17pt inline title on scroll [doc]. Deeper screens use a minimal back chevron (no back-title text).
- A pushed object can drop the nav bar title and float a back circle and one action capsule over the content, letting the document's own title be the header (Bear, Apple Notes, Things) [obs].
- Show a page's place in a hierarchy with a small icon + title or a breadcrumb in the nav bar ("folder / title" in grey: Obsidian; breadcrumb under the title: Craft) rather than repeating parents on screen [obs].
- Keep the visible back button even though back-swipe works from anywhere in the content on iOS 26; long-press on back shows the history menu [doc/know].
- Deep links set an anchor so Back goes somewhere sensible (`unstable_settings = { anchor: 'index' }`).

### Search

- **At the bottom** by default: a bottom toolbar field that rises above the keyboard, or a trailing Search tab [doc WWDC26 292]. Apple Mail's bottom row is filter circle · search pill · create circle [meas]. Top only when a bottom sheet owns the bottom (Maps, Stocks) or search is the main way in (Gmail and Airbnb's 56pt top pill) [doc/meas].
- Pull down to search when a list is the whole screen (Superhuman) [doc].
- Focused search shows recent searches (each removable) and suggested filters as chips; empty results repeat the query: "No Results for 'dana'" [doc 292].
- A scope bar only for 2-4 clear categories; structured filters as tokens or chips [doc].

## 3. Which layer for which task

| Task | Layer | Examples |
|---|---|---|
| Go deeper into an item or level | **Push** | open a project, a thread, a record |
| Do one small task and come back (add, filter, pick a date, snooze, share, quick edit) | **Sheet** with detents and a grabber; medium detent when the top half works alone | Todoist quick add, Superhuman snooze, Cash App pay steps at about 67% so the amount stays visible |
| Edit an item without losing your place in the list | **Expand in place** into an edit card | Things to-dos open inline; Reminders rows edit in place |
| A multi-step flow with its own back stack (compose, create a record with steps, checkout) | **Large sheet** (page sheet) | Mail compose, Wise send |
| An immersive or blocking context (camera, focus mode, onboarding, an alarm) | **Full-screen cover** | Halide, Opal focus timer, Reminders alarms |
| A live canvas you keep looking at while acting (map, flight, ride) | **Persistent non-modal sheet** over the canvas: peek about 120pt, open about 320pt, never fully covering it | Apple Maps, Uber, Flighty |
| Choices the user opened deliberately (sort, view as, filter, add-type) | **Pull-down menu** from a toolbar symbol | Notion Calendar's view menu from a bottom-left glass button; Attio's All / Mine from the nav title |
| Shortcuts on an item | **Context menu** on long-press, with preview, 3-6 items, destructive last, every item also reachable elsewhere | Mail, Things, Telegram |
| A choice about something just done (Discard draft? Delete 3 items?) | **Action sheet anchored to its button** (iOS 26 anchors it; no Cancel when anchored) | |
| A problem that needs a decision | **Alert**, at most 3 buttons, verbs not OK | never for undoable actions |
| A popover | not on iPhone; use a menu or a sheet | |

Rules:
- One sheet at a time. Close one before opening another; if a sheet needs a sub-choice, push inside the sheet or use a menu [doc]. Amie stacks detail sheets like a deck; treat that as a brand exception, not a default.
- Sheets that edit: X top-left, tinted ✓ top-right. Sheets that run a flow (pay, send, review a batch): one capsule commit at the bottom (Cash App, Copilot). Sheets that only show: one X (Flighty and Apple Maps put it trailing). Never Cancel + Done + Back together; in a multi-step sheet, Back replaces Cancel after step one [doc, updated March 2026].
- Swipe-down dismisses; confirm only when it would lose typed content, with an anchored Save / Discard choice [doc].
- Sheets, menus and alerts morph out of the button that opened them. Use the system presentation; do not draw your own sheet background or radius [doc 323].
- A detail sheet has exactly one filled button, for the one live action (Join in Notion Calendar, Reserve in Airbnb's sticky bar) [obs].

## 4. Placement by reach

- **Top zone (status bar to about 120pt):** title, scope, account and global settings (an avatar or ••• top-right). Things the user reads, not presses often.
- **Middle:** content. Rows are tappable across their full width.
- **Bottom zone (lowest third):** the primary action, search, the commit bar, the tab bar. The floating + sits bottom-right (Reminders 48pt, 28pt from the edges; Things about 56pt) [meas].
- A full-screen commit sits as a full-width capsule (48-56pt) pinned above the home indicator, with the facts that decide it (total, fee, arrival time) directly above it (Airbnb's sticky bar, Wise, Uber) [web/obs].
- Attach is occasional and sits far from Send to avoid mis-taps (ChatGPT's + far left, Send far right) [obs].

## 5. Gestures

### System gestures to leave alone [doc gestures]

- Leading-edge and (iOS 26) content-wide swipe right: Back. Never attach a horizontal pan to the left edge or to a whole pushed screen; put carousels inside bounded rows.
- Bottom edge: home and app switcher. Top-left and top-right pull-down: Notification and Control Center.
- Sheet swipe-down: dismiss. Three-finger swipe and shake: undo.

### App gestures that are now conventions

| Gesture | Meaning | Seen in |
|---|---|---|
| Swipe a row right (leading) | complete, archive, schedule, mark read: the positive or toggle action | Things (schedule), Spark (Done), Mail (read) |
| Swipe a row left (trailing) | defer, move, more, and the destructive set with a full-swipe commit | Superhuman (Remind), Mail (Trash) |
| Long-press a row | context menu with preview | all |
| Long-press a button | its power variant: Send → schedule or pick model, + → recent photos, a tab → its create action | Apple Mail, ChatGPT, Craft |
| Drag the + into a list | insert at that position, pre-filled from the context | Things, Todoist, TickTick |
| Drag a row onto a day or slot | schedule it | Amie (list under a time grid) |
| Pull down on a list | refresh, or search when the list is the whole screen | Mail, Superhuman |
| Pinch on a time grid | change density (44 / 62 / 98pt per hour) | Notion Calendar |
| Swipe between peers | sibling dashboards or metrics with page dots | Apple Weather locations, Oura metrics, Revolut accounts |
| Press and hold to complete | deliberate completion on big targets, ring fills in about 500ms | Streaks |
| Swipe across blocks | select text blocks without drag handles | Craft |

Rules:
- Every gesture has a visible twin (a button, a menu item) and a VoiceOver custom action [doc].
- Never reuse a system gesture's shape for a different meaning [doc].
- No drag handles on touch for text blocks: use move up/down buttons (Notion) or swipe-to-select (Craft) [obs].

## 6. Settings and account

- Settings is a pushed inset-grouped list (52pt rows, switches only inside rows), opened from an avatar or ••• top-right, not a tab, unless the app is a utility whose settings are its product [doc/obs].
- Per-item settings live on the item (its ••• menu or its sheet), not in global settings.
- Never add an in-app light/dark toggle: follow the system [doc dark-mode].
- Notification hours, swipe-action choices, tab choices and the completion sound are the settings power users look for (Linear, Todoist, Spark) [doc].

## 7. Onboarding entry and the first screen

- Land on the real home with a useful empty state, not a carousel of feature pages. If a flow is needed: one question per screen, full-width options, one bottom capsule button, skippable, never shown again (Opal) [obs/doc].
- Ask for each permission at the moment of need with a one-screen primer whose only button triggers the system prompt [doc privacy]. Details in states-and-system.md.
- The launch screen is the empty shell of the first screen (background and bar positions), no logo [doc].
