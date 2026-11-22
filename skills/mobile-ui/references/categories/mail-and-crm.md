# Mail and CRM

Mail clients and a relationship database on the iPhone: a speed-first triage client (Superhuman), a multi-account client that sorts by kind of sender (Spark), Google's search-first client (Gmail), the system baseline (Apple Mail) and a data-model CRM (Attio). Users judge them on one question: "Can I clear this with my thumb and trust that nothing is lost?" Every studied mail app answers with rows that say who, what and how long ago in 3-4 lines, a swipe that archives, an undo after anything fast, compose at the bottom right and search within reach. Attio answers the CRM half: a table you can still read on a phone and a record page that is tabs of one thing.

Studied (headless and logged out; no app was driven):
- **Superhuman Mail** v5.11.0: 8 framed renders cut to 402pt (about 2% error), the 2026 and 2022 redesign posts, help snippets via search (the help site blocked headless access).
- **Spark** v3.20.9: 10 framed renders cut to 393pt, Readdle help pages.
- **Gmail** v6.0.261109: 10 framed renders plus raw 375pt @3x screenshots from 9to5Google (exact), Google help, Workspace Updates.
- **Apple Mail** (iOS 26) v2.11: 3 framed renders calibrated to 440pt (±3%), the iPhone User Guide.
- **Attio** v2.18.0: 5 framed renders cut to 393pt, two changelog renders of the real app, help and changelog.

Tags: [meas] measured, [obs] seen in a capture, [doc] the maker's docs, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **A list cleared by thumb**, because mail on a phone is triage (Apple Mail category note).
2. **One swipe that archives ("Done") and never deletes**, because a swipe happens at speed.
3. **Undo after anything fast**: done, archive, send.
4. **Compose one tap away at the bottom right, search reachable without scrolling up.**
5. **People mail as full rows, machine mail collapsed**, because 15 newsletters deserve one decision.
6. **AI that drafts or summarises but never sends**, because the user must see the words first (Spark).
7. **For records: the table still readable, the record's identity always visible** (Attio).

## The theses to choose from

### Superhuman: every email is a decision, and the decision is one gesture
Core bet: the inbox shows only what helps you decide, and a swipe settles it.
- Swipe left = Done, right = Remind Me; Done is archive and the thread returns if someone replies [doc].
- Split Inbox: user-named streams as a text strip above the tab bar with grey counts ("Important 6 · VIP 5") [obs].
- No avatars in rows; unread is a 6-7pt dot, never bold; a reminder replaces the date in muted red [meas, obs].
- Icon-only tab bar of Mail, Calendar, Search plus the account avatar in its own circle [obs].
- Pull down anywhere = search; swipe anywhere = back [doc].
- Auto Draft cards in the thread with one send button, and a voice-first AI prompt ("Speak to outline your email") [obs].

Choose this when users live in mail, pay for speed and aim for Inbox Zero.

### Spark: sort by kind of sender, then collapse the noise
Core bet: people get full rows; notifications and newsletters collapse into one row per category with sender chips and counts, cleared with one check.
- Swipe right = Done (green #81D134, 132pt reveal) with a 5-second Undo [meas, doc].
- Gatekeeper: a "New Senders" card with 👍 / 👎 above the list [obs].
- A 3pt account colour bar before each sender in a unified inbox [obs].
- An "Ask me anything…" AI pill permanently at the bottom beside compose; AI text lands in drafts only via Insert [obs, doc].

Choose this when users run several accounts and most of their mail is automated.

### Gmail: search is the navigation
Core bet: the header is a 56pt search pill, rows are dense and identical, and everything is reversible by default.
- No title bar: hamburger, "Search in mail" and the account avatar in one pill [meas].
- 84.7pt three-line rows, 40pt avatar, no separators; unread by weight only [meas].
- Archive is the default swipe both ways; "Sent · Undo" after every send [doc, obs].
- Other categories show as summary rows at the top of Primary ("Promotions · 2 new") instead of tabs [obs].

Choose this when the archive is huge and finding beats filing.

### Apple Mail: the system toolbar is the chrome
Core bet: no tab bar; a bottom glass row of filter, search and compose sits over the list, and categories are filters, not tabs.
- Bottom row: filter circle 48pt · Search pill 266x48pt · compose circle 48pt, 12pt gaps [meas].
- Category capsules where only the selected one shows its label; machine mail opens as a digest per sender [meas, doc].
- The Apple Intelligence summary replaces the row preview, marked by a glyph [obs].
- Sync status as the title's subtitle ("iCloud · Updated Just Now") [obs].

Choose this as the baseline: it is where every iPhone user's thumbs are trained.

### Attio: keep the table a table
Core bet: a database stays a grid on the phone, glyphs replace field labels, and a record is tabs of one thing.
- People table: frozen first column (checkbox, avatar, name), 46pt rows, horizontal scroll, aggregate footer [meas].
- View bar of chips: saved view, sort, filter showing only its count in blue [obs].
- Record: avatar + name in the nav bar, tab chips (Overview, Activity, Emails, Notes, Tasks, Calls, Files), Overview as a 2-column widget grid [doc image].
- Activity as one timeline of sentences with grey verbs and black entities [obs].
- Icon-only 4-tab bar: Home, Notifications, Tasks, Search [obs].

Choose this when the phone must read and act on a relationship database.

## Comparison

| Dimension | Superhuman | Spark | Gmail | Apple Mail | Attio |
|---|---|---|---|---|---|
| Shell | icon-only tabs + avatar circle [obs] | no tabs; sidebar [obs] | Mail / Chat / Meet icons [meas] | no tabs; bottom glass row [meas] | 4 icon-only tabs [obs] |
| Search | pull down anywhere [doc] | header icon [meas] | 56pt top pill [meas] | bottom 48pt pill [meas] | tab [obs] |
| Row pitch | 135pt with chip row (402) [meas] | 78-79pt (393) [meas] | 84.7pt (375) [meas] | about 102pt (440) [meas] | table 46pt, task 64pt [meas] |
| Avatar | none | 38pt [meas] | 40pt [meas] | about 44pt [meas] | 20pt in table [meas] |
| Unread | 6-7pt dot, no bold [meas] | about 7pt dot [meas] | bold sender, subject, time [obs] | dot + bold [know] | none |
| Time | sender line; reminder replaces it in red [obs] | preview line, right [meas] | sender line [obs] | sender line with › [obs] | due date in meta, coloured [meas] |
| Separators | inset to the text [meas] | none [obs] | none [meas] | inset to the text [meas] | grid / grouped card [obs] |
| Default swipes | left Done, right Remind [doc] | right Done; left undocumented [doc] | archive both ways [doc] | right read/unread, left More/Flag/Trash [know] | not documented |
| Machine mail | user splits [obs] | one row per category, sender chips [obs] | "N new" summary rows [obs] | icon capsules + digest per sender [doc] | none |
| AI | Auto Draft card, voice prompt [obs] | bottom Ask pill, Insert to draft [obs, doc] | auto summary card in thread [doc] | summary replaces preview [obs] | none |
| Undo | none | 5s after Done [doc] | after send, about 5s [obs, 3p] | send delay up to 30s [doc] | none |

## Category rules

### Shell and search

1. **Put search, filter and create in a bottom glass row of 48pt controls over the list**, because that is where iOS 26 trains users to reach. Apple Mail [meas].
2. **When search is the main way in, make the header a 56pt full-round search pill holding the menu and the account avatar.** Gmail [meas]. When the list is the whole screen, pull-down-anywhere can be search instead, freeing about 50pt at the top. Superhuman [doc].
3. **Show filter chips as dropdowns directly under a focused search field (Label, From, To, Attachment, Date), then suggestions and quick results as full rows**, because a phone query is refined by tapping, not typing operators. Gmail [obs].
4. **Put the account switch on the user's avatar** (its own glass circle, or inside the search pill), not in a tab. Superhuman [obs, doc], Gmail [meas].
5. **Name the current view under the title in small grey text with a chevron on the title**, and put sync status in the same subtitle slot ("Updated Just Now"), not a toast. Spark [meas], Apple Mail [obs].
6. **Let back be a swipe from anywhere, and compose custom gestures from one start (pull down, then a direction)**, because edge reach is hard one-handed and unrelated gestures are undiscoverable. Superhuman [doc].

### Rows

7. **Build a mail row as who, what, how long ago in 3-4 lines (sender, subject, 1-2 preview lines) at 79-102pt, or 135pt when a chip row is added.** Gmail 84.7pt, Spark 78-79pt, Apple Mail about 102pt, Superhuman 135pt [meas].
8. **Use one unread cue: weight only when rows have avatars, a 6-7pt dot in a left gutter when they do not.** A dot next to a 40pt avatar is noise; bold on every unread row of a three-weight row is a wall of black. Gmail [obs], Superhuman [meas].
9. **Inset separators to the text column, or drop them and let an even rhythm do the work**, so the avatar or unread gutter reads as part of the row. Superhuman [meas], Apple Mail [meas], Gmail [meas].
10. **Put a row's pending state (reminder time) where the date sits, in a warning colour**, because it answers the same question. Superhuman [obs].
11. **Mark the receiving account with a 3pt colour bar before the sender in a unified inbox, and move the time to the preview line so the sender line never truncates.** Spark [obs, meas].
12. **Show attachments as chips under the snippet and labels inline at the end of the snippet line**, so a file opens from the list. Gmail [obs].
13. **Let the AI summary replace the preview, marked by a glyph, not a word.** Apple Mail [obs].

### Triage and grouping

14. **Give the two swipe directions the two outcomes of triage (done and later, or archive both ways) and nothing destructive by default**, and make each side configurable. All four mail apps do both [doc, know].
15. **Make Done mean archive, and bring the thread back when someone replies**, because Done must never mean lost. Superhuman [doc].
16. **Show an undo for 5 seconds after every Done, and an undo window after send** (Gmail "Sent · Undo"; Apple Mail configurable up to 30s). Spark [doc], Gmail [obs], Apple Mail [doc].
17. **Keep people mail as full rows and collapse machine mail**: one row per category with sender chips, per-sender counts, "+N" overflow and one check to clear it (Spark); summary rows with colour "N new" pills (Gmail); a digest per sender (Apple Mail). Nobody uses five tabs on a phone. [obs, doc].
18. **Put a handful of user-named streams as a text strip just above the tab bar, with grey counts after each name and no badge shape**, because streams are chosen often and the thumb is there. Superhuman [obs].
19. **In a category row, show the label only on the selected capsule and icons on the rest.** Apple Mail [meas].
20. **Screen new senders with an accept/block card above the list**, because screening is one decision per sender. Spark [obs].
21. **Let tapping the avatar enter multi-select**, because the avatar has no other job in a row. Gmail [doc]. Selecting one promotional message can select the sender's whole category. Apple Mail [doc].

### Threads, compose and AI

22. **Collapse the middle of a long thread into a divider with a circled count; show first and last expanded.** Gmail [obs].
23. **Open compose as a sheet: X top-left, the From account or the subject as the title, send top-right; no field dividers; Cc/Bcc as one capsule toggle; tools on a row above the keyboard.** Spark [obs], Apple Mail [obs].
24. **Hide send later behind a long-press on Send, with concrete presets ("Send 8:00 AM Tomorrow")**, so one tap still sends. Apple Mail [obs, doc].
25. **In a snooze or remind picker, show each relative option with its resolved time right-aligned ("next week · Mon, 8:00 AM"), and put "if no reply" in a separate group below.** Superhuman [obs].
26. **Show smart replies as three equal-width buttons under the last message, or 2-3 word intent chips under an AI draft; each opens a draft, never sends.** Gmail [obs], Superhuman [obs], Spark [doc].
27. **Make AI output land in the draft through an explicit Insert, cite source emails under assistant answers, and accept voice first in the prompt field.** Spark [doc, obs], Superhuman [obs].
28. **Put an automatic AI summary card at the top of long threads, collapsible from its top-right.** Gmail [doc].

### CRM records and tables

29. **Keep a database table a table when columns matter: frozen first column (checkbox, avatar, name), 46pt rows, horizontal scroll, an aggregate footer, column headers kept.** Attio [meas].
30. **Put a view bar of chips under the nav: the saved view with its colour icon, sort, and filter showing only its active count in the accent.** Attio [obs].
31. **Replace field labels on cards with attribute-type glyphs**, so a card of five facts carries zero label words. Attio [obs].
32. **Put the record's avatar and name in the nav bar and its facets in a scrolling, swipeable chip row of tabs** (selected chip filled grey), so content starts with the tabs. Attio [doc].
33. **Make Overview a 2-column grid of the key fields as widget cards (about 174pt wide, 12pt gap, 16pt margins, about 12pt radius; 13pt grey label, 17pt semibold value), each long-pressable for field-aware actions (call, copy, message).** Attio [meas, doc].
34. **Show history as one timeline: a 24pt icon circle on a rail, a sentence with a grey verb and a black entity, a nested card for meetings and notes, dashed period dividers ("This week").** Attio [obs].
35. **Build a task row at 64pt: circle check, one-line title, a 13pt meta line of due date coloured by urgency (red overdue, orange today, grey later), assignee and "↗ 2 linked".** Move completed tasks to a Completed section. Attio [meas, obs].
36. **Put "All / Mine" in a pull-down menu from the nav, not a segmented control**, and put decision buttons (Grant / Deny) inline in request notifications. Attio [obs].
37. **Show a kanban as horizontally scrolling columns with the count and a + in each header; drag cards between stages.** Attio [obs].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Bottom toolbar | filter 48pt at x 27-75 · search 266x48pt · compose 48pt; 12pt gaps; about 26pt side insets; 25pt above the bottom (440pt) | Apple Mail [meas] |
| Category capsules | selected about 152x36pt with label; others about 73pt icon-only | Apple Mail [meas] |
| Search pill header | x 16-322pt, 56pt tall, full round, #E9ECF3; avatar 36pt | Gmail [meas] |
| Gmail row | 84.7pt, 40pt avatar at x 16, text from x 72, 16/14/14pt, time 12pt, no separators | Gmail [meas] |
| Spark row | 78-79pt, 38pt avatar, text from x≈78, sender 16 semibold, subject 16, preview 15 grey; unread dot about 7pt at x≈17 | Spark [meas] |
| Superhuman row | 135pt with chip row; text from x 24, right margin 21; sender and subject about 15pt, preview about 13pt, line pitch 21-22pt; unread dot 6-7pt | Superhuman [meas] |
| Apple Mail row | about 102pt, avatar about 44pt, text from x≈88; sender 17 semibold, subject and preview 15 | Apple Mail [meas] |
| Label chip | about 66x18pt, radius about 4pt | Superhuman [obs] |
| Compose | Gmail extended FAB 136x56pt, radius about 16pt, #D3E3FD, 12pt above the bar; Spark FAB about 46pt #147DFA | [meas] |
| Tab bars | Gmail 50pt bar, active pill 64x32pt; Superhuman selected pill about 94x49pt, bar about 26pt above the bottom | [meas] |
| Swipe reveal | Done 132pt, #81D134 | Spark [meas] |
| Remind sheet rows | 48pt | Superhuman [meas] |
| Send-later menu rows | about 42pt | Apple Mail [meas] |
| Unified-inbox cards | inset 8pt on #EEF0FC | Spark [meas] |
| Attio table | 46pt rows; 20pt checkbox at x 12; 20pt avatar; name 16pt; second column from x≈236; view chips about 32pt | Attio [meas] |
| Attio task | 64pt; 20pt circle at x≈32; title 16pt; meta 13pt; 16pt avatar | Attio [meas] |
| Record Overview | tab chips 33pt; widget cards about 174pt, 12pt gap, 16pt margins, radius about 12pt | Attio [meas] |
| Undo | Done 5s (Spark); send about 5s (Gmail [3p]); send delay up to 30s (Apple Mail) | [doc] |
| Non-content words | Superhuman inbox 6; Gmail inbox 5, thread about 9; Apple Mail inbox about 8, thread about 2; Spark home about 12, thread about 8; Attio table about 4, tasks about 14, record about 15 | [obs] |

## Anti-patterns seen

- **The same word on every row.** Attio's Tasks repeats "You" six times and "linked" four times, about 14 non-content words [obs]. Fix: drop "You" on your own tasks and keep the ↗ count.
- **Two unread cues.** Apple Mail marks unread with a dot and bold [know]. Fix: one cue.
- **A label-heavy record page.** Attio's Overview carries about 15 non-content words (tab names, card labels, "See all") [obs]. Fix: glyphs on the tabs, as on its kanban cards.
- **Settings text in the reading view.** Gmail's thread carries about 9 non-content words, among them "Always show images from this sender" [obs]. Fix: put per-sender settings in the message menu.
- **An extra-long-press gesture.** Superhuman dropped its extra-long-press in threads as "slow, hard to discover"; long-press now just selects text, and message actions sit on a swipe and the bottom triage bar [doc].

## Steal list

1. Default one swipe to Done (archive), the other to Remind, nothing destructive, because triage has two common outcomes.
2. Return a Done thread when someone replies, because Done must never mean lost.
3. Show a 5-second undo after every Done and an undo window after send, because fast must be reversible.
4. Collapse machine mail into one row per category with sender chips, because noise deserves one decision.
5. Use one unread cue (dot without avatars, weight with them), because two cues are noise.
6. Put the pending reminder where the date sits, in a warning colour, because it answers "when does this matter".
7. Put search, filter and compose in the bottom glass row, because the thumb lives there.
8. Show resolved times next to relative snooze options and "if no reply" as its own choice, because "next week" is ambiguous.
9. Long-press Send for schedule presets with concrete times, because one tap must still send.
10. Collapse the middle of long threads to a counted divider, because you read the latest reply.
11. Make AI drafts land through Insert, cite sources, and take voice first, because the user owns the words.
12. Keep a CRM table a table (frozen first column, 46pt rows, footer), because columns are the point.
13. Put the record's identity in the nav bar and its facets in swipeable tab chips, because the record stays named while you move.
14. Replace field labels with glyphs on cards, because five facts need no five labels.
15. Show record history as one sentence timeline with grey verbs and bold entities.

## For a business dashboard app (HQ)

For HQ's lead database and email to-dos, copy Attio's record page (identity in the nav bar, tab chips, a widget Overview, one Activity timeline) and Spark and Superhuman's Done / Remind triage (Apple Mail category note). The lead list itself is Attio's frozen-column table with a view bar of saved view, sort and filter-count chips, and its task rows (64pt, due date coloured by urgency, linked-record count) fit email to-dos that point back to a lead (Attio steal list).
