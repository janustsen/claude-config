# Calendar and time

Calendar apps on the iPhone: a parser-and-agenda calendar for people with many accounts (Fantastical), a calendar that doubles as a to-do list for time-blockers (Amie) and a meeting-heavy professional's grid-first companion (Notion Calendar, formerly Cron). Users judge them on one question: "Where is now, what is next, and can I fit this in?" All three answer it the same way at the base: red for today and now, a calendar-coloured block, a large month title, and a floating bottom control cluster instead of a tab bar, because the app is one object (your time) seen at different zooms. They split on what the home screen leads with: an agenda (Fantastical), to-dos beside the grid (Amie) or the grid (Notion Calendar).

Studied (no live app was driven):
- **Fantastical** v4.2.4: 10 framed renders cut to 393pt (±2%), the 39s App Store preview video (2022 UI) cut into frames, Flexibits iOS help read in full.
- **Amie** iOS 1.15.20: 5 posed marketing compositions on a 414pt canvas (proportions reliable, absolute pt ±20%), the changelog and docs, and a public booking page measured as exact CSS at 393pt.
- **Notion Calendar** v2.2.0: 6 unframed screen crops scaled to 393pt (±2%), Notion help, Cron-era blog images. Where the help ("one, two, or three-day view") conflicts with the 2.x screens (Schedule to 1 day), the screens are trusted.

Tags: [meas] measured, [obs] seen in a capture, [doc] the maker's docs, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **Today found instantly**: a red now line and a today chip (Fantastical category note).
2. **An agenda or a day readable in one scroll.**
3. **Creation in a few seconds, one tap away.**
4. **Nothing moves that they did not ask to move** (Amie category note).
5. **The next meeting one tap from joining**, because it is opened two minutes before it starts (Notion Calendar).
6. **Direct manipulation on the grid**: long-press to create, drag to move, handles to resize.
7. **Private details hidden on the Lock Screen when asked** (Notion Calendar).

## The theses to choose from

### Fantastical: the date strip is the navigator and the overview
Core bet: a density strip over an agenda, and creation by typing one sentence that you watch form into an event.
- DayTicker: 5.4 day columns at a 72-73pt pitch under the large title; each event a 6.6pt pill placed by time of day, so one glance shows how busy each day is and when [meas, doc].
- Zoom on one axis: swipe up for tasks, pull down for month, pull again for Day / Week / Month / Quarter / Year [doc].
- Natural-language entry with a live mini day-view preview; recognised tokens turn bold and a ghost of each travels into the block in about 200-270ms [meas].
- No tab bar: a floating glass toolbar of menu, a named calendar-set pill, and search + [obs].
- Weather sits in each day header ("74°/60°", high bold) [obs].

Choose this when users have several accounts, think in "what's coming", and type fast.

### Amie: a to-do is an event that has not been placed yet
Core bet: to-dos and the time grid share one screen, and scheduling is a drag from the list into the grid.
- Split View: day grid above, collapsible list cards (Today, Emails, Linear) below [obs].
- Lifting a to-do turns it saturated and physical; the source row stays as a dashed ghost; the drop slot is a dashed outline labelled "Release to schedule" [obs].
- Events as same-hue pairs: Tailwind-200 fill, 800 title, 400 duration, no stripe or border [meas].
- A joy layer (Memoji, pastels, "Enjoy Your Tomorrow!" empty days) that users quote, though the 3.39 rating and reviews keep returning to sync and flicker [doc].

Choose this when the user time-blocks and their to-dos are the real agenda.

### Notion Calendar: the time grid is the home screen
Core bet: for meeting-heavy users the gaps between meetings are the decision, so the app opens on the grid, with join always close.
- 1- or 3-day grid with a 7-day week strip; today a red rounded square [obs].
- Up to three labelled time-zone gutters side by side (EDT / GMT / PDT) [obs].
- Event sheet: "Join Google Meet" as the only full-width filled button, right after who and when [obs].
- Unanswered invites drawn as dashed outlines with no fill [obs].
- Hour height varies by view (about 44, 61.5 and 98pt), so density is a user choice [meas].

Choose this when users live in meetings across time zones and the phone is a viewer and joiner first.

## Comparison

| Dimension | Fantastical | Amie | Notion Calendar |
|---|---|---|---|
| Home | DayTicker over an agenda list [obs] | day grid over list cards [obs] | 1- or 3-day grid under a week strip [obs] |
| Bottom controls | menu circle · calendar-set pill · search + capsule [obs] | none seen; tab bar not verified [know] | hamburger (view menu) left; search, compose right [obs] |
| Hour height | about 63pt [meas] | about 66pt [meas ±20%] | about 44 / 61.5 / 98pt by zoom [meas] |
| Gutter | 40pt, 11pt labels; "noon" in red [meas] | 76pt, about 13pt, 24h labels [meas] | about 48pt, 13pt labels; 45pt per extra zone [meas] |
| Event block | 15-20% tint, 3pt stripe, 12pt dark same-hue text [obs] | pastel fill, same-hue 800 title, no stripe, about 10pt radius [meas] | pale tint, 4pt stripe, 14pt semibold dark text, about 6pt radius [meas] |
| Now | red 1pt line, about 11pt dot, red time replaces the hour label [obs] | 2pt red line with a 1.3x9pt tick, overshooting into the gutter [meas] | red capsule time in the gutter + red 1.5pt line [obs] |
| Pending / tentative | availability glyph shape [doc] | none | dashed outline, no fill [obs] |
| Create | sentence + live preview; Show More for the form [obs] | drag from list; NL claimed [3p] | event sheet of icon-led rows; no NL seen [obs] |
| Detail | push, tap a field to edit [doc] | stacked sheets with a date badge [obs] | large sheet, X, Save only when changed [obs] |
| Past | dimmed to about 40% [obs] | none | none |
| Empty | empty days omitted [doc] | "Enjoy Your Tomorrow!" [obs] | "No upcoming meeting" strip [obs] |

## Category rules

### Shell and navigation

1. **Use a floating bottom toolbar instead of a tab bar when the app is one screen seen at different zooms**, because tabs would split one object into fake places. Fantastical [obs], Notion Calendar [obs].
2. **Put the current scope (calendar set, workspace) in the toolbar as a named pill**, because it changes what every view shows. Fantastical [obs].
3. **Make the large title the month and a picker (title plus chevron), and put a today chip showing today's date number top-right**, because the title is the only place with room and the chip both informs and acts. Notion Calendar [obs].
4. **Put the view switcher (Schedule, Month, Week, 3 / 2 / 1 days) in a popover anchored to a bottom-left glass button, icon plus one word per row**, because views are a setting, not a destination. Notion Calendar [obs].
5. **Or order zoom levels along one gesture axis (pull down = zoom out), with a visible grabber and a floating ^ chevron**, so users learn one motion instead of a menu. Fantastical [doc, obs].
6. **Make the overview and the navigator the same control**: a strip of 5 day columns plus a partial sixth, events as tiny time-positioned pills. The cut sixth column says the strip scrolls. Fantastical [meas].
7. **Synchronise the strip and the list both ways**, because two independent scrollers make the user hold the date in their head. Fantastical [doc].
8. **Show a navigation control only when it has content** (an invitations inbox icon appears only with pending invites). Fantastical [doc].
9. **Put the two things the user moves between on one screen, split vertically (grid above, list cards below), when scheduling is a drag from one to the other**, and let each list card collapse so the user sets the split. Amie [obs].

### The time grid

10. **Give the grid about 1pt per minute (60-66pt per hour)**, because a 15-minute event then gets about 15-16pt (one 11-12pt line) and 30 minutes fits a title plus duration. Fantastical [meas], Amie [meas].
11. **Offer at least two densities (about 44pt per hour compact, 60-98pt comfortable) and let pinch switch them**, because a phone cannot show a whole day and readable 15-minute events at once. Notion Calendar [meas].
12. **Use a 40-48pt gutter with 11-13pt labels; 24-hour labels without AM/PM save about 20pt.** Fantastical [meas], Notion Calendar [meas], Amie [meas].
13. **Mark now with one red system: a line across the day plus a dot, tick or capsule in the gutter, with the current time replacing the nearest hour label so the two never collide.** Fantastical [obs], Notion Calendar [obs]. Amie's tick at the leading end never covers a label the way a dot can [meas].
14. **In week view, run the now line across all days with the dot in today's column only.** Fantastical [obs].
15. **Draw event blocks as a 15-20% tint of the calendar colour with a 3-4pt full-colour left stripe and dark same-hue text, about 6pt corners and 2-3pt gaps**, because full saturation on a dense week is noise and white text fails on light calendar colours. Fantastical [obs], Notion Calendar [meas]. Amie drops the stripe and uses a 200 / 800 / 400 hue triple instead [meas].
16. **Inset blocks about 8pt from the hour-line start and 2pt below their hour line**, so stacked blocks separate without borders. Amie [meas].
17. **In columns under about 60pt, wrap titles mid-word rather than ellipsising**; in a 1-day view put short events on one line (bold title, lighter inline time). Fantastical [obs], Notion Calendar [obs].
18. **Draw a needs-your-response event as a dashed outline with no fill, or encode availability in the leading glyph's shape (solid busy, ring free, dotted tentative)**, because shape survives dimming and colour-blindness. Notion Calendar [obs], Fantastical [doc].
19. **Collapse the all-day area with a chevron in the gutter past about 3 rows.** Notion Calendar [obs].
20. **Give secondary time zones their own labelled gutters, at most three**, because mental conversion is the error the feature prevents. Notion Calendar [obs].
21. **At year scale show a heat map of event density**, because only density is legible there. Fantastical [obs, doc].

### Agenda and rows

22. **Build an agenda row as a coloured dot plus time (15pt semibold grey), title (17pt) and location (15pt grey), 55-70pt pitch, no separators**, because the dot column already aligns the list. Fantastical [meas].
23. **Head sections "TODAY" / "TOMORROW" followed by the date in a lighter weight**, because the relative word is read first and the date confirms. Fantastical [obs].
24. **Attach ambient context (weather, counts) to the header it describes, at header size, with the key number bold**, because a separate widget costs a scroll. Fantastical [obs].
25. **Dim the past to about 40% instead of hiding it, and hide empty days by default.** Fantastical [obs, doc].
26. **Put a contextual action (Join) on a row only when it applies, as a small trailing filled capsule.** Fantastical [obs].
27. **Show a to-do's time as a grey chip, a date-only due as plain grey text, and overdue as a 6pt red dot before the date**, so three states read with no words. Use a progress pie as the list's icon. Amie [obs].
28. **Mark a row's state with a coloured word inside its own sentence ("Draft to Dennis Müller") rather than a badge.** Amie [obs].
29. **Cap the top priority tier (3 Super Priorities across all lists)**, because uncapped urgency means nothing. Amie [doc].

### Create, edit and detail

30. **Offer one sentence field that parses, with a live visual preview of the object below; bold each recognised token; mirror the parsed title in the sheet's nav title; keep "Show More" to the full form one tap below.** Users verify by recognition, and parsing must never trap them. Fantastical [obs, doc].
31. **Use prefix words and sigils for scoping ("at" place, "with" person, "/calendar")**, because they are typeable without leaving the keyboard. Fantastical [doc].
32. **Make long-press on empty time or a date create there, and long-press on a block give move and resize handles.** Fantastical [doc], Amie [doc].
33. **When dragging a list item into time, make the lifted copy physical and saturated (a 3-6° tilt on device), keep a dashed ghost at the source, and label the drop slot with a two-word verb ("Release to schedule")**, because the finger hides the item. Amie [obs].
34. **Offer durations and reminders as presets (15m / 30m / 1h) before any wheel**, and default a 15-minute buffer between auto-scheduled blocks. Amie [doc].
35. **When an edit affects other people, ask once ("Notify guests?") and remember the answer as the next default.** Amie [doc].
36. **Put the one live action (Join) as the only filled, full-width button in the event sheet, right after who and when.** Notion Calendar [obs].
37. **Lay out event fields as icon-led rows on the sheet background, and show empty optional fields (Location, Docs and links, Description) as grey placeholder rows that are also the add buttons; drop the label once filled.** Notion Calendar [obs].
38. **Summarise RSVPs in the section header ("1 yes, 1 awaiting") and badge each avatar.** Notion Calendar [obs].
39. **Use an X, not Cancel, on sheets that view, and show Save only when there are changes**, so a viewer sheet never looks like an unsaved form. Notion Calendar [obs]. Fantastical's create sheet uses Cancel / Add in red [obs].
40. **Make every field in a pushed detail tappable to edit in place, and put Delete in red, centred, at the end.** Fantastical [doc, obs].
41. **Give a detail sheet a date badge (weekday initial over the day number, red when today) at the leading edge of its header**, so no "Date:" row is needed. Amie [obs].
42. **Give share-able objects bare copy and share icon buttons on their card**, and make booking pages a list of full-width time slots under a small date grid that jumps to the first available day. Notion Calendar [obs], Fantastical [obs], Amie [doc].

### States and system surfaces

43. **Write an empty day as a small reward ("Enjoy your tomorrow!") or a plain fact that keeps the slot ("No upcoming meeting")**, never "No events" rows. Amie [obs], Notion Calendar [obs].
44. **When a feature is off, remove its slot rather than show a placeholder** (weather off, headers lose the temperature). Fantastical [know].
45. **Never let auto-placed items jump on launch: render the last-known placement and reconcile quietly.** Amie fixed exactly this flicker [doc].
46. **Ship Up Next widgets and Live Activities for time-bound items, showing time left ("1h 35m left") for the current item, with a red weekday plus black day number header.** Fantastical [doc], Amie [obs].
47. **Let each source opt out of loud surfaces (per-calendar Live Activity off), offer hide-titles on Lock Screen widgets, and put a + in medium and large widgets.** Fantastical [doc], Notion Calendar [doc].
48. **Consider a persistent bottom peek for "what's next" (countdown, title, Join).** Notion Calendar's Cron era did it [obs].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Large title | 34pt bold at x 16; year in red #fb1215 (Fantastical) | Fantastical, Notion Calendar [meas] |
| DayTicker | about 125pt tall; columns 72-73pt, 5.4 visible; pills and all-day bar 6.6pt; weekday about 10pt caps; date about 20pt; today in a 34pt #0095ff circle; grabber 35x4.5pt | Fantastical [meas] |
| Week strip | weekday about 14pt, date 17pt; today red rounded square about 27pt, radius about 6pt | Notion Calendar [meas] |
| Today chip | about 30x32pt, grey fill, today's number | Notion Calendar [obs] |
| Agenda | section header about 44pt, 13pt bold caps; dot 13pt at x 25, text at x 40; rows 55pt (2 lines), 70pt (3 lines); Join capsule about 60x29pt, inset 18pt | Fantastical [meas] |
| Hour height | Fantastical about 63pt; Amie about 66pt; Notion Calendar 44 / 61.5 / 98pt; Amie booking grid 56pt | [meas] |
| Gutter | Fantastical 40pt, 11pt; Notion Calendar about 48pt, 13pt, about 45pt per extra zone; Amie 76pt with 24pt right margin | [meas] |
| Week view | 7 columns of about 50pt; text 12pt; 30-minute block about 31pt holds two lines | Fantastical [meas] |
| Event block | Fantastical 3pt stripe, 15-20% tint; Notion Calendar 4pt stripe, about 6pt radius, 14pt text, 2-3pt gaps, 30 min about 46pt at 98pt/h; Amie about 10pt radius, inset 9pt, 2pt below the line, 15pt semibold title | [meas, obs] |
| Now line | Fantastical red #fb0003 1pt + about 11pt dot; Amie 2pt #ef4444 + 1.3x9pt tick; Notion Calendar red 1.5pt + about 36x16pt capsule | [meas, obs] |
| Month | Fantastical cells about 63x60pt, date 13pt, up to 4 lines at 11pt, "2 more…"; Notion Calendar columns about 56pt, date 17pt, 2-3 events, "3 more" | [meas] |
| All-day rows | Fantastical 22.8pt; Notion Calendar about 22-24pt | [meas] |
| Event sheet | X about 44pt at x 24; title about 24pt bold; field rows about 40pt, 20pt icons at x 34, text at x 56; avatar rows 28pt; Join about 48pt tall, corner about 14pt, x 12-380 | Notion Calendar [meas] |
| View menu | rows about 37pt, 17pt labels; card corner about 24pt | Notion Calendar [meas] |
| Link cards | corner about 24pt, inset about 24pt, about 125pt pitch, 32pt copy and share circles | Notion Calendar [meas] |
| Amie cards | list cards about 20pt radius, inset 21pt; to-do rows about 36pt, 20pt checkbox; detail sheets about 30pt top radius, grabber about 39x6pt | Amie [meas ±20%] |
| Amie booking page | cards 361pt, 12px radius, 20px padding, 10px gap; shadow `0 1px 2px rgba(0,0,0,.04), 0 2px 6px rgba(0,0,0,.08)`; slot pills 240x24pt at 28pt pitch; press `transform .15s cubic-bezier(.4,0,.2,1)` | Amie [meas CSS] |
| Parse ghost | about 200-270ms per token | Fantastical [meas] |
| Colours | Fantastical red #fb1215, blue #0095ff, dark list #101010; Amie page #f5f5f5, ink #171717; Notion Calendar red about #d6383e, page about #fbfbfa | [meas] |
| Non-content words | Fantastical NL sheet 4, week grid 0 inside the grid; Amie grid 3-5, lists about 6, booking page about 15 per viewport; Notion Calendar event sheet about 18, links 7 | [obs] |

## Anti-patterns seen

- **A helper sentence above a disabled button.** Amie's booking page says "Select a slot and add your details to confirm the event" (11 words) over a grey Confirm [meas]. Fix: let the button state and the empty field speak.
- **Promo rows inside the work area.** Amie's lists stack adds a "Sync with Linear, Things, Notion…" row, 6 more words [obs].
- **Web inputs under 16px.** Amie's 14px booking fields trigger iOS Safari focus zoom [meas].
- **Charm over reliability.** Amie's 3.39 rating and a changelog that keeps fixing sync, flicker and duplicates show that a joy layer does not replace a calendar that holds still [doc].
- **Help that contradicts the app.** Notion Calendar's help still lists only 1-3 day views on mobile while the app offers six [doc, obs].
- **Inconsistent case.** Notion Calendar's link sheet shows "Recurring" beside "one-off" [obs].

## Steal list

1. Make the date strip both overview and navigator with time-positioned pills and a partial last column, because one glance shows how busy and when.
2. Give the grid about 1pt per minute and let pinch change density, because planning and reading need different zooms.
3. Draw blocks as a pale tint with a 3-4pt stripe and dark same-hue text, because dense weeks stay calm.
4. Mark now with one red system and let the current time replace the hour label, because the moment must be found in under a second.
5. Draw pending items as dashed outlines with no fill, because state reads without a badge.
6. Replace create forms with a sentence field and a live preview that bolds parsed tokens, because users verify by seeing.
7. Drag to-dos from a list into the grid, with a dashed ghost at the source and a verb on the drop slot, because scheduling is moving work into time.
8. Put the one live action (Join) as the only filled full-width button in the detail sheet, because it is the time-critical act.
9. Show empty optional fields as grey icon-led placeholder rows, because they are both label and add button.
10. Put the scope in a named pill and the view switcher in a bottom-left popover, because neither is a place.
11. Attach weather and counts to the header they describe, because it costs no row.
12. Dim the past and hide empty days, because placeholders cost rows.
13. Ask "notify guests?" once and remember it, because repeated confirms make editing hateful.
14. Show "time left" in widgets and Live Activities for the current item, because a glance asks how long.

## For a business dashboard app (HQ)

Two calendar patterns transfer to HQ's health and jobs views: a 7-day strip of tiny pills is a glance at jobs or health over the week, and sentence-plus-preview is the right way to add to-dos with dates (Fantastical category note). Draw status by line style: a solid block is confirmed, a dashed outline is pending or needs you; give the next due job or meeting a next-up peek, and put its one Join-style action as the single filled button in the detail sheet (Notion Calendar category note). From Amie take the to-dos-to-day split and drag, the colour-pair event anatomy, the now line and reward-style empty states, and leave out promo rows inside lists and helper sentences over disabled buttons (Amie category note).
