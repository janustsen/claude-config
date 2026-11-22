# Notes and documents

Writing and page apps on the iPhone: a block workspace authored mostly on desktop (Notion), the system's notes app (Apple Notes), a calm Markdown writer (Bear), a native block editor with styled output (Craft) and a local-first linked-notes vault (Obsidian). Users judge them on one question: "Can I find my page and get words onto it without the chrome getting in the way?" The apps split on whether a note is one text (Apple Notes, Bear, Obsidian) or a set of blocks with child pages and databases (Notion, Craft), but on the phone the block apps converge on the same answers: no visible drag handles, structure tools on the keyboard, child pages that push, databases as lists.

Studied (App Store shots, makers' help and blogs; no live app was driven):
- **Notion** v1.7.356: 7 framed renders cut and measured at 393pt, help and release notes, one third-party image of the 2026 top-tab home. notion.site measurement was blocked by a bot check.
- **Apple Notes** v2.12: 5 raw 430pt @3x screens that measure exactly, the iPhone User Guide.
- **Bear** v3.0.4: 10 framed renders (absolute pt ±5%, ratios exact), bear.app FAQ and blog.
- **Craft** v3.7.1: 10 framed renders, help-center GIF frames (low resolution), one public Craft doc measured in headless Chrome (type values exact, layout x-values desktop).
- **Obsidian** v1.15.1: 7 raw 414pt @3x screens (older status bar), help docs, the Publish site at 393pt.

Tags: [meas] measured, [obs] seen in a capture, [doc] the maker's docs, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **The document owns the screen**, because reading and writing need the width and the top of the page (Apple Notes, Bear).
2. **No title field**: the first line is the title (Apple Notes, Bear).
3. **Recent pages first**, because most phone sessions return to something opened minutes ago (Notion, Apple Notes).
4. **Structure and formatting one tap from the keyboard**, without dismissing it.
5. **Capture from outside the app** that lands in a known place (Apple Notes Quick Note, Craft Quick Entry).
6. **Silent sync that speaks only when something needs them** (Bear, Obsidian).
7. **Desktop-authored structure readable on the phone**, without the phone pretending to be a page-tree or database designer (Notion).

## The theses to choose from

### Notion: desktop structure, phone verbs
Core bet: the workspace is built on desktop; the phone jumps back in, reads, captures and checks off.
- Home: "Jump back in" cards (about 132x132pt, the third cut off at the edge) above a Favorites page tree in an inset card, rows about 47pt with chevron, emoji, title and + [meas].
- "There are no hover states on mobile. Instead, ••• and + icons are always visible" [doc].
- Databases shown as List views: title plus one indented property line (about 69pt), or one line (about 36pt) [meas]. The App Store set shows no table and no board [obs].
- A context-aware keyboard toolbar; + swaps the keyboard for an insert grid [doc, obs].
- 2026: a top row of pill tabs (Home, Chats, Meetings, Inbox) where only the selected one shows its label, swiped sideways [doc, 3p].

Choose this when the content is a team workspace authored elsewhere and the phone is a companion.

### Apple Notes: the note is the screen, the system is the chrome
Core bet: no custom bars and no title field; every control is system glass; everything is findable without filing.
- Editor: a 44pt back circle and one 158x44pt action capsule on top; one tool capsule (about 173x50pt) and a compose circle at the bottom; 0 non-content words [meas, obs].
- Lists grouped by recency by default (Pinned / Yesterday / Previous 7 Days / Previous 30 Days); search is a bottom capsule beside compose [obs].
- Search covers handwriting, objects in photos and scanned text [doc].

Choose this as the baseline: iOS 26 users judge every notes app against it.

### Bear: structure lives in the text, power waits underneath
Core bet: one flat pool of notes organised by inline #tags, a normal keyboard by default, and every formatting tool behind one BIU key.
- No nav bar: a back circle and one ⓘ ⋮ capsule float over the page [meas].
- BIU swaps the keyboard for a same-height 6x4 formatting keyboard; a corner ▾ marks long-press variants [doc].
- Any tag can become the whole app's scope (Workspace) [doc].
- Healthy sync is invisible; conflicts float above pinned notes [doc].

Choose this when the user is one person writing, and calm matters more than structure.

### Craft: a document is an object you style
Core bet: native block editing with touch-first gestures, and every doc a finished card on a backdrop.
- Blocks are selected by swiping across them, anywhere on the block; selection circles appear only after [doc].
- The floating tab bar splits destinations (Home, Tasks, Calendar) from an action capsule (AI, +) [obs].
- The + opens Quick Entry in the mode of the current screen, with the destination shown and changeable [doc].
- Inline collections zoom to full screen on iPhone; tables scroll sideways [doc].
- Total offline on Apple platforms, merged block by block [doc].

Choose this when documents are the product's output and need Notion-like structure with native feel.

### Obsidian: the desktop model, folded into drawers
Core bet: the same app on every platform; sidebars become edge-swipe drawers and the user configures the editing surface.
- Breadcrumb "folder / title" in the top bar; a bottom bar (back, forward, create-or-find, tab count, menu) that hides while typing [obs, doc].
- One ⊕ both finds and creates a note (Quick switcher) [doc].
- A user-reorderable keyboard toolbar that can hold any command [doc].
- Bases List layout indents chosen properties under each record [doc].
- Sync as one coloured icon in the right drawer, with a filterable log behind it [doc].

Choose this when users own their files, link heavily and want to customise.

## Comparison

| Dimension | Notion | Apple Notes | Bear | Craft | Obsidian |
|---|---|---|---|---|---|
| Model | blocks, pages, databases | one text per note | one text, inline #tags | blocks, sub-pages, collections | Markdown files, links, Bases |
| Shell | top pill tabs (2026) [3p] | push stack, no tabs [obs] | push stack, tag sidebar [obs] | 3 tabs + action capsule [obs] | drawers + bottom bar [doc] |
| Top of a page | back, icon + 15pt title, share, comments, ••• [meas] | back circle + one capsule [meas] | floating back + ⓘ ⋮ capsule [meas] | back, title with parent breadcrumb [obs] | drawer toggle, breadcrumb, read/edit toggle, ⋮ [obs] |
| Title | about 25-26pt bold [meas] | first line, 28pt bold [meas] | first line, about 28pt bold [meas] | 24/29 bold [meas web] | inline 30-31pt bold [meas] |
| Body / leading | rows 15pt, properties 13pt [meas] | 17pt, pitch about 24pt [meas] | about 16pt at 1.7 [meas] | 16/24 [meas web] | 16pt, pitch 23-24pt [meas] |
| Text margin | 21-24pt [meas] | 30pt on 430 [meas] | about 30pt [meas] | 32pt (12 card + 20) [meas web] | 20-21pt on 414 [meas] |
| Keyboard tools | context-aware row, + → insert grid [doc] | bottom tools ride up; Aa panel [doc, know] | BIU → 6x4 keyboard [doc] | accessory + 3x3 "Rich blocks" grid [obs] | user-ordered row, swipe for more [doc] |
| Moving blocks | move up / down buttons [obs] | text cut and paste [know] | move-line keys [doc] | swipe to select, swipe to indent [doc] | fold chevrons, indent guides [obs] |
| Database on the phone | List view [obs] | none | none | full screen, sideways table [doc] | List with indented properties [doc] |
| Sync shown | none | silent [know] | Settings only; conflicts in list [doc] | offline fades unopened docs (web) [doc] | coloured icon in right drawer [doc] |
| Editor words | 0 [obs] | 0 [obs] | 0 [obs] | none | 0 [obs] |

## Category rules

### Shell and finding

1. **Put "Jump back in" recent pages at the top of Home, cut off at the right edge**, because most phone sessions return to a page opened minutes ago and the cut card says it scrolls. Notion [meas].
2. **Group a notes list by recency by default (Pinned / Yesterday / Previous 7 Days / Previous 30 Days)**, because "what did I write lately" needs no setup. Apple Notes [obs].
3. **Put list search at the bottom beside compose**, because both are thumb actions and the top is for the title. Apple Notes [obs].
4. **Show the page tree as a collapsible inset list with a + on every row**, because "add inside this" is the tree's main action. Notion [meas].
5. **Offer saved filters (tags + dates + mentions, any/all) beside folders, or let any node become the app-wide scope**, because on a phone a narrower world beats drilling a tree. Apple Notes [doc], Bear [doc].
6. **Split the floating tab bar into destinations and an action capsule (+, AI)**, because "go somewhere" and "make something" are different intents. Long-press a tab for its create action. Craft [obs, doc].
7. **If the shell has several surfaces, a top row of swipeable pill tabs where only the selected one shows its label fits 4-5 destinations without truncation.** Notion [3p].
8. **Make one button both find and create** (type a name; open it if it exists, create it if not), because that saves a whole screen. Obsidian [doc].
9. **When the product has a desktop sidebar, make it a full-height edge-swipe drawer of about 80% width with the page dimmed behind**, so left = files and right = context survives. Use bottom sheets for short pick lists (open tabs). Obsidian [obs, meas].

### The page

10. **Drop the nav bar on reading and writing screens and float two glass controls (back; one capsule of ⓘ + ⋯)**, because the document's own title is the real header. Bear [meas], Apple Notes [meas].
11. **On a pushed page, show the page's own icon and title small and left-aligned in the nav bar, with the parent as a grey breadcrumb**, because the big title is already in the content and the breadcrumb is the only sign of where a deep page lives. Notion [meas], Craft [obs], Obsidian [obs].
12. **Make the first line the title, styled as Title (about 28pt bold)**, because it removes a field and a tap from every new note. Apple Notes [doc, meas], Bear [obs].
13. **Use a 20-30pt text margin and 1.5-1.7 leading for long text**, because a 40-45 character measure reads comfortably at 16pt. Bear 30pt at about 1.7, Apple Notes 30pt on 430, Obsidian 20-24pt at 1.5 [meas].
14. **Use 17pt body with 28pt title and 22pt heading for plain notes (the system scale), or 16/24 body, 24/29 title and 19/23 heading for styled documents.** Apple Notes [meas], Craft [meas web].
15. **Make headings collapsible and put an outline (ToC) one tap away in long documents**, because collapse and outline are the phone's substitute for a side panel. Apple Notes [doc], Bear [doc].
16. **Put per-document metadata (stats, outline, backlinks) in one segmented panel off ⓘ**, because three panels would add three controls to a screen that has two. Bear [doc].
17. **Show raw syntax (brackets, Markdown markers) only on the active line, or faint around styled text while the caret is in it**, so the rest reads as finished text. Obsidian [obs], Bear [obs].
18. **When users colour content, check contrast at pick time and offer a one-tap fix; tint a coloured heading's background and darken its text in the same hue.** Craft [doc, meas].
19. **Keep one app accent for every done, link and active signal** (Notes gold, Bear red #DE5254, Obsidian purple). Apple Notes [obs].
20. **Let user-chosen page icons (emoji) carry identity in every list, nav title and breadcrumb.** Notion [obs].

### Keyboard and structure

21. **Lift the bottom toolbar onto the keyboard when editing starts, same tools in the same order**, because the user learns one row, not two. Show a Done button while editing. Apple Notes [doc].
22. **Make the keyboard toolbar context-aware**: indent, outdent, move up, move down first when the caret is in a list; insert and media first in plain text. Pin keyboard-dismiss at the right outside the scroll. Notion [doc, obs].
23. **When tools exceed one toolbar (about 8), swap the keyboard for a same-height tool panel instead of scrolling**, so every tool is visible in the thumb zone. Bear's 6x4 grid puts undo and redo first; Notion's insert panel is a 2-column grid; Craft's is 3x3. Mark long-press variants with a corner ▾. Bear [doc], Notion [doc], Craft [obs].
24. **If the toolbar scrolls, lead with the app's signature act (Obsidian: [[link]]) and let a cut-off last icon be the only overflow cue.** Let power users reorder it. Obsidian [obs, doc].
25. **Keep the editing toolbar the page's colour with no divider**, so it reads as part of the document. Obsidian [meas].
26. **Replace block drag handles with move-up/move-down buttons, or with whole-block swipes**: a handle is a 20pt target, the whole block a 350pt one. Show selection circles only after the first selection. Notion [obs], Craft [doc].
27. **Separate editing and non-editing gestures** (swipe with the caret visible = indent; otherwise = select), and give every hidden gesture a visible twin, because gestures on a text surface collide with selection. Craft [doc], Bear [doc].
28. **Never let a tap on the keyboard toolbar blur the editor**, because a dismissed keyboard mid-edit is the most visible failure of a non-native editor. Obsidian [3p].
29. **Dock find-in-note at the bottom with an n/N count and arrows**, because matches are in the body above and the thumb is at the bottom. Bear [obs].

### Databases on the phone

30. **Default a database to a List view even when desktop uses a table: the title plus one property line indented under it**, because a table on 393pt shows two columns at best and List never scrolls sideways. Notion [meas], Obsidian [doc].
31. **Put the view switcher ("☰ List ⌄" pill), search, filter (accent when active), settings and a split "+ ⌄" on one 32pt row under the title.** The accent filter icon is the only sign the list is not showing everything. Notion [meas, obs].
32. **When the table is the point, open the embedded database full screen with a zoom from its block, keep horizontal scroll and open each row as a page.** Craft [doc].
33. **Show a board as one column about 85% wide with the next peeking.** Notion [know].
34. **Make row height and column summaries per-view settings** (short to extra tall; summaries at the column foot or each group's top). Obsidian [doc].

### Capture, sync and states

35. **Make + context-aware (the current screen decides what it creates and where) and show the destination as a changeable chip on the capture sheet or nav bar.** Craft [doc], Notion [doc].
36. **Let a capture surface float over any app and land in a known inbox (Quick Notes), and let share-extension captures auto-apply a tag.** Apple Notes [doc], Bear [doc].
37. **Keep healthy sync silent; surface only conflicts, at the top of the list, above pinned items.** Bear [doc]. If you show sync, use one coloured icon in a secondary place (green synced, purple working, red disconnected) with a log behind it. Obsidian [doc].
38. **When offline, fade items that cannot open with one line on what restores them ("Get back online to view this document") and grey out online-only actions rather than hide them; merge concurrent edits per block.** Craft [doc].
39. **Keep locked items in the list as title plus a lock or grey placeholder bars**, because the user must find them to open them. Apple Notes [obs], Bear [obs].
40. **List what the phone cannot do and route it to desktop explicitly**, because a missing action with no explanation reads as a bug. Notion [doc].
41. **Put pin on swipe right and destructive actions on swipe left, and recover from Recently Deleted instead of confirming.** Apple Notes [doc].
42. **Ship a capture widget before a dashboard widget, and put a + on every widget that lists items.** Notion [doc], Craft [obs].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Editor top controls | back 44x44pt at x 19; capsule 158x44pt; y 60-104 (430pt) | Apple Notes [meas] |
| Editor bottom tools | capsule about 173x50pt; compose circle about 50-58pt | Apple Notes [meas] |
| Floating controls | back circle 46-48pt at x 15; ⓘ ⋮ capsule 105x46pt | Bear [meas ±5%] |
| Note type | title 28pt bold, heading 22pt bold, body 17pt, line pitch about 24pt; checklist circles 20pt on about 31pt | Apple Notes [meas] |
| Writer type | H1 about 28, H2 about 19, body about 16 at about 27.6pt pitch; to-dos 18-20pt on about 35pt | Bear [meas] |
| Document type | H1 24/29 700, heading 19/23 600, body 16/24; meta 14/20 at 55% alpha; ink #1F2225 | Craft [meas web] |
| Markdown type | title 30-31pt bold, H2/H3 about 20pt semibold, body 16pt at 23-24pt; tag pills 25pt #F3F0FD | Obsidian [meas] |
| Page type | title 25-26pt bold, H2 about 18pt semibold, rows 15pt, properties 13pt; ink #37352F | Notion [meas] |
| Notes list | large title 34pt bold; count 15pt grey; section headers about 22pt bold; rows about 59pt with 36pt thumbnail; cards inset 19.7pt, about 12pt radius on #F2F2F6 | Apple Notes [meas] |
| Home | Jump back in cards about 132x132pt, about 10pt radius; tree rows about 47pt, child indent 28pt; Favorites card inset 18.7pt | Notion [meas] |
| Database header | view pill about 84x32pt; split "+ ⌄" about 55x29pt, about 6pt radius | Notion [meas] |
| Database rows | about 69pt two-line, about 36pt one-line | Notion [meas] |
| Keyboard toolbars | Notion 44pt row, 10 slots at 40pt pitch, glyphs about 20pt #898985; Obsidian 44pt row, 8 icons at 50pt pitch | [meas] |
| Document card | inset 12pt, radius 16px, padding 16/0/40px | Craft [meas web] |
| Craft task rows | 20pt checkbox (red outline when overdue), pitch about 34pt | Craft [obs] |
| File tree rows | about 33pt, 17pt text | Obsidian [obs] |
| Drawers | about 82% of the width (to x≈340 of 414) | Obsidian [meas] |
| Callout | 3pt rule #EF8A31, fill #FFFBF7, about 6pt radius | Bear [meas] |
| Non-content words | editors 0 (Notes, Bear, Obsidian, Notion); Notion page 2, Home 3; Notes list about 12; Obsidian reading 2; Craft calendar about 17 | [obs] |

## Anti-patterns seen

- **The same chip on every row.** Craft's calendar repeats an "Inbox" chip on 7 rows, about 17 non-content words in all [obs]. Fix: say it once in a section header.
- **AI in the editor toolbar's first slot.** Notion's AI slot pushes structure tools one place right on every edit [obs]. Fix: one floating AI circle or one tab, unless AI editing is the core.
- **Toolbar taps that dismiss the keyboard.** "Rapid tapping in the toolbar area causes it to dismiss" in Obsidian [3p].
- **Gesture and selection races.** Craft's 3.7.0 fixed "selection bar actions sometimes opening the wrong menu when tapped immediately after swiping a block" [doc].
- **Web-styled bars next to iOS 26 glass.** Obsidian's toolbar and bars look dated beside system glass (Obsidian category note).
- **Gesture-only routes.** Bear's two- and three-finger swipes (history, Quick Open) are undiscoverable on their own; Bear keeps a visible twin for each [doc].

## Steal list

1. Make the first line the title, because it removes a field from every new note.
2. Float back and one ⓘ ⋯ capsule over the document, because the document's title is the best header.
3. Use 20-30pt text margins and 1.5-1.7 leading for long text, because a narrower measure reads better.
4. Lift the same bottom tools onto the keyboard, context-aware, with dismiss pinned right, because one learned row beats two.
5. Swap the keyboard for a same-height tool grid when tools exceed one row, because every tool is then visible under the thumb.
6. Replace drag handles with move buttons or whole-block swipes, because handles are tiny targets in a scrolling text view.
7. Put Jump back in recents at the top of Home, because the phone mostly reopens.
8. Default databases to a List of title plus one indented property line, with a one-row header (view pill, filter, split +), because tables do not fit.
9. Open a real table full screen with a zoom from its block, because it needs the width.
10. Make + context-aware with a visible destination chip, because the user is usually already where the thing belongs.
11. Split the tab bar into destinations and an action capsule, because creating is not a place.
12. Keep sync silent and surface only conflicts, at the top, because only conflicts need action.
13. Fade what offline cannot open, with one line on how to get it back, because users need to know why.
14. Let one button find or create, because it saves a screen.

## For a business dashboard app (HQ)

Copy Apple Notes' chrome exactly for HQ's notes pages, because it is what iOS 26 users expect, and borrow structure from Notion and Craft only where pages and databases are needed (Apple Notes category note). Home is Jump back in plus a favourites tree; pages push with a small icon-and-title nav bar; the lead database is a List view with a view pill, filter and sort icons and a split + (Notion category note), using Obsidian's indented-property rows and its create-or-find switcher (Obsidian category note). When a lead table must be a table, use Craft's full-screen collection, and split the tab bar into destinations and a + capsule (Craft category note). A notes page can carry zero non-content words if the controls are icons and metadata lives in one ⓘ panel (Bear category note).
