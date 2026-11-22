# Tasks

Personal and work to-do apps on the iPhone: a personal planner (Things), a parse-first cross-platform manager (Todoist), a many-tools productivity app (TickTick), the system's own to-do layer (Apple Reminders) and the phone companion of an issue tracker (Linear). Users judge them on one question: "Can I capture this in a second and clear my list fast?" Every studied app answers it with a one-tap add, a tickable circle or box, and a list that shows only what is left.

Studied (all from App Store shots, makers' docs and support pages; no live app was driven):
- **Things 3** v3.25.3: 8 framed renders calibrated to 402pt, Cultured Code support pages and blog, feature videos cut into frames at 30fps (gestures current, visuals pre-2025).
- **Todoist** v26.11.12: 7 renders calibrated to 402pt (three measurable), help center, the developer colour table.
- **TickTick** v8.3.00: 10 renders on a 5.5-inch canvas, the weakest measurement source here (±10%), help center and blog.
- **Apple Reminders** (iOS 26) v2.10: ten raw 430pt @3x screens that measure exactly, Apple's iPhone User Guide.
- **Linear Mobile** v1.109.0: 7 dark renders calibrated to 402pt, linear.app/mobile, docs, changelog, the "Linear spin on Liquid Glass" post and the redesign video.

Tags: [meas] measured on a capture, [obs] seen in a capture, [doc] the maker's docs, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **A one-tap add that asks for nothing but a title**, because capture happens mid-thought (Things category note).
2. **Today as the landing view**, because the question on opening is "what now".
3. **A circle or box to tick, with a satisfying beat**, because finishing is the reward moment.
4. **A date picker with Today, Tomorrow and Someday above a calendar**, because most dates are near.
5. **Capture from outside the app** (widget, Lock Screen, Control, Action Button, Siri), because capture speed is why people pick a task app (Todoist).
6. **No data lost to a stray swipe**, because a list triaged daily gets swiped by accident (Things).
7. **Completed items out of the way**, because a list is about what is left (Reminders).

## The theses to choose from

### Things: position is the input
Core bet: you decide where a to-do lives by putting it there, and the page stays paper-calm.
- The + (Magic Plus) is draggable; the drop point picks list, heading and date, and the new to-do is pre-filled from it (drop in Today → ★ Today; under "18 Thursday" → May 18) [obs].
- While dragging, a real 44pt grey gap (#e3e5e8) opens at the insertion point [meas].
- Two-line rows on a 44pt pitch, no separators, no boxes; about 4 non-content words on Today [meas, obs].
- Tapping a to-do expands it in place into a card; nothing pushes a third screen [obs].
- The title field never parses; natural-language dates live inside the When picker [doc].
- No tab bar: one scrolling root list of views and projects [obs].

Choose this when the user is one person planning their own days and you can afford a custom gesture model.

### Todoist: type it once, in one line
Core bet: one text field parses everything, and colour carries priority, project and nearness instead of words.
- Quick Add parses dates, #project, /section, %label, p1-p4, +assignee, !reminder and {deadline} as you type; each token gets a peach #fde7d8 background in place and an editable chip below [doc, meas].
- The completion circle is stroked in the priority colour with a 10% tint fill (p2 #eb8909) [meas].
- The + (Dynamic Add) can also be dragged to insert, nest or reschedule [doc].
- Tab bar of 3-5 the user can pin views to; Browse holds the rest [doc].

Choose this when users are keyboard-fluent, items carry many properties, and the app spans teams and platforms.

### TickTick: many tools, a tab bar the user builds
Core bet: tasks, calendar, matrix, Pomodoro, habits and countdowns in one app, with the breadth hidden until the user adds a tool to the tab bar.
- Tab bar assembled from a tool list; lists live in a drawer [doc].
- Inbox grouped into date cards ("Tue, Today 4 ⌄") with the time right-aligned in brand blue #4772fa [obs, meas].
- One spoken sentence becomes several parsed task cards before saving; the transcript is drawn in a blue-to-magenta gradient until parsed [doc, obs].
- Pomodoro runs as a Live Activity [doc].

Choose this when the app has more than five tools and different users need different ones.

### Apple Reminders: the iOS 26 baseline, tinted by the list
Core bet: the list's colour is its identity and tints the screen, every list ends in a blank row, and the Lock Screen is a first-class surface.
- Title, floating + and completion fill all take the list colour (Groceries green #19c658, Today blue #0086fc) [meas].
- Every list and section ends with a dotted-circle placeholder row for inline add [obs].
- Smart lists as 2-column gradient count tiles, 191x80pt, 8pt gaps [meas].
- Roomy rows: 42pt single line, 67pt two lines [meas].
- Parsed phrases turn blue in the text, with a "Title: Water the plants" preview pill [obs].

Choose this when the app should feel like part of iOS, or as the chrome baseline any task list is compared to.

### Linear Mobile: the phone is for triage, not planning
Core bet: the home is an inbox about people and events, creation is a composer with property chips, and boards and roadmaps stay on desktop.
- Inbox rows lead with a 40pt avatar plus an action badge; unread dot #1994fd; read rows dim [obs, meas].
- An icon-only floating glass toolbar (about 272x56pt) the user can rearrange and pin, with compose as a separate 48pt circle [meas, doc].
- The composer docks every property as a value chip above the keyboard [obs].
- Blur-only glass, no refraction, because refraction "can make dense professional interfaces harder to read" [doc].

Choose this when the to-dos are work items generated by other people and systems, and the phone's job is to clear them.

## Comparison

| Dimension | Things | Todoist | TickTick | Reminders | Linear |
|---|---|---|---|---|---|
| Shell | One root list, no tabs [obs] | 3-5 pinnable tabs + Browse [doc] | User-built tabs + drawer [doc] | Lists home, no tabs [obs] | Icon-only floating toolbar + compose circle [meas] |
| Landing | Root list; Today one push | Today tab | Inbox | Lists home | Inbox |
| Capture | Draggable + → in-place card [obs] | One parsed line + chips [doc] | + with reorderable toolbar; AI voice [doc] | Dotted inline row; sheet as slow path [obs] | Full-screen composer, chip row [obs] |
| Parsing | Date picker only [doc] | Title, tinted tokens, tap to undo [doc] | Title, blue tokens, tap to undo [doc] | Title, blue text + title preview [obs] | None; chips instead [obs] |
| Row pitch | 44pt two-line [meas] | not measured (nav rows 50pt) [meas] | about 47pt [meas ±10%] | 42 / 67pt [meas] | about 70pt two-line, 87pt three [meas] |
| Swipe right / left | schedule / select [doc] | user picks; complete / schedule [know] | Done, Pin / Move, Delete, Date [doc] | Indent / Delete, Flag, Details [doc, know] | Unread capsule [obs] |
| Priority shown as | none | stroke colour of the circle [meas] | fixed colours High, Medium, Low, None [doc] | none | priority-bars chip in the composer [obs] |
| Completion | blue fill, row lingers [doc, know] | fill, tone on by default, undo toast [doc] | tick + "ding" [know] | list-colour fill [know] | none |
| Lock Screen | list, add, progress ring [doc] | six widgets incl. Next Task [doc] | widgets, Pomodoro Live Activity [doc] | completable notification + Reschedule [obs] | notifications only [doc] |

## Category rules

### Shell and navigation

1. **Use a single scrolling root list instead of a tab bar when the destinations are views of one dataset** (Inbox, Today, Upcoming), because a tab bar implies separate apps. Things [obs], Reminders [obs].
2. **When you do use tabs, let users pin the views they live in, cap at 5, and remove a pinned view from the overflow screen** so no destination appears twice; keep Browse last for everything else. Todoist [doc].
3. **When the app has more than five tools, let the user assemble the tab bar and put lists in a drawer**, because a fixed bar forces everyone through tools they do not use. TickTick [doc].
4. **Make create an action, not a tab**: a floating + bottom-right, a separate circle beside the toolbar, or a button in the top bar of every screen. A centre + tab steals a navigation slot for something that is not a place. Linear [doc], Reminders [meas].
5. **Scope a work companion to triage and capture**, because planning needs the big screen. Linear [doc].
6. **Group secondary nav actions into one glass capsule on the right (••• + search) and keep back as an unlabelled 44pt circle on the left**, because the previous screen's title is one swipe away. Reminders [meas], Things [obs].
7. **Show smart views as a 2-column grid of coloured count tiles above the user's lists**, because count plus colour lets you triage before opening anything. Reminders [meas].

### Rows and density

8. **Put a two-line task row on a 44pt pitch with no separators when the list is scanned many times a day**, because Things fits 5 to-dos where Reminders' 67pt rows fit 3. Things [meas].
9. **Size a view's title about 28pt with a coloured glyph rather than a 34pt large title when the glyph names the view** (★ Today, ☾ This Evening). Things [meas].
10. **Give each time bucket a fixed glyph and colour and use it on the title, the picker and the row** (★ yellow Today, ☾ This Evening, ⚑ pink-red deadline), so the mark reads as "due today" anywhere with no word. Things [obs].
11. **Encode priority as the stroke colour of the completion circle**, because the thing you tap to finish then also says how urgent it is, at zero extra width. Todoist [meas].
12. **Colour the date chip by nearness** (today, tomorrow, this week, later), because nearness is what the user acts on. Todoist [obs].
13. **Write metadata as one grey line ("List · time · repeat") and turn only the time red when due or overdue.** Reminders [obs].
14. **When most tasks in a view have times, right-align the time in the accent colour**, because a column of times turns a list into an agenda. TickTick [obs].
15. **Group by part of day (Morning / Afternoon / Tonight, or day plus This Evening) instead of hours**, because most personal tasks have a part of the day, not a time. Reminders [obs], Things [doc].
16. **Lead a work-activity row with a 40pt avatar plus a small action badge, dim read rows, and show health or status as one trailing coloured glyph**, so who, what and state read before the text. Linear [obs, meas].
17. **Hide completed items by default behind one "Show Completed"**, and let emoji in titles render at text size, because users decorate. Reminders [doc, obs].

### Capture and parsing

18. **End every list and section with a tappable dotted blank row instead of a "+ Add item" button**: it costs no words and puts the item where it belongs. The dotted circle reads as an empty slot, not an unchecked item. Reminders [obs].
19. **Make the + draggable and let the drop point choose list, heading and date; open a real row-height gap at the insertion point; pre-fill the item from where it lands.** Both Things and Todoist do it, so it is a category convention. Things [obs, meas], Todoist [doc].
20. **If you parse the title, highlight the understood phrase where it was typed with a background tint, echo it as a chip, and make the highlight tap-to-undo**, because a parser will eat a real word ("monthly report"). A tint keeps the text black and readable; recoloured text (Reminders' blue) is harder to scan. Todoist [doc, obs], TickTick [doc].
21. **Or keep the title literal and parse only inside the date field**, so "Call mom monday" never loses "monday". Pick one bet per app. Things [doc].
22. **Preview the split before saving** ("Title: Water the plants" under the field), so the user sees both halves. Reminders [obs].
23. **Dock the item's properties as value chips in an accessory row above the keyboard**, each showing its current value, so setting priority or assignee never dismisses the keyboard. Name the scope (team, project) as a chip in the header, because it changes where everything else goes. Linear [obs].
24. **Show the load already on each day inside the date picker** (a count plus coloured project bars), because the user is choosing a day they can do it on. Todoist [doc].
25. **Let voice capture produce several tasks from one utterance, shown as parsed cards with their list name before saving, and draw unparsed transcript in a distinct ink.** People speak lists. TickTick [doc, obs].
26. **Let the user reorder the quick-add toolbar**, because the property set most often differs by user. TickTick [doc].

### Editing, swipes and completion

27. **Edit in place: expand the row into a card where it sits**, so the user keeps their place and sees the neighbours. Things [obs]. Todoist opens a resizable sheet over the list instead, which keeps the list visible above it [obs].
28. **Map the two swipe directions to the two most frequent non-destructive acts and keep delete in a menu or as a second step.** Things: right schedules, left selects [doc]. Linear: the primary inbox swipe is reversible (read/unread) [obs].
29. **Cap swipe buttons at three per side**, because more are too narrow to hit on a 393pt row. TickTick [doc].
30. **Let users choose what each swipe direction does from a short list** (complete, schedule, delete), because heavy users differ on whether the daily act is finishing or rescheduling. Todoist [doc], TickTick [doc].
31. **Draw swipe actions as rounded capsules inset from the edge** (Linear's "Unread" capsule inset 10pt, #7885fe), matching the glass language. Linear [obs].
32. **If long-press both opens a menu and starts a drag, cancel the menu as soon as the finger moves.** Todoist documents a manual workaround ("move it slightly to the right") [doc].
33. **Make hierarchy a gesture**: swipe right to indent, drag onto an item to nest, drag the + right of a task for a sub-task. Reminders [doc], Todoist [doc]; TickTick caps depth at five [doc].
34. **Fill the completion circle with the list colour, let the row linger a beat before it leaves, and treat re-tapping as the undo.** Things [doc, know], Reminders [know]. Todoist adds an undo toast for a few seconds and a completion tone that is on by default with a toggle [doc].
35. **Recover deletes from Recently Deleted for 30 days instead of confirming**, and support shake or three-finger undo. Reminders [doc].

### Sheets and interruptions

36. **Commit a create or settings sheet with a filled accent ✓ circle top-right and ✕ top-left** (Todoist's red ✓ about 45pt, Reminders' blue 44pt). Reminders [obs], Todoist [meas].
37. **Run a single-choice anchored picker at about 130ms and inserts at about 270-370ms**, because the picker is a tool and the insert is a change to your data the eye should follow. Things [meas].
38. **Reserve full-screen takeovers for things that must interrupt (an Urgent alarm)**; create and edit flows are sheets. Reminders [obs].

### System surfaces

39. **Put the completion control on the notification itself plus one action for the common alternative (Reschedule).** Reminders [obs].
40. **Write a work notification as identifier, outcome and the concrete change** ("Done — changed padding from 16 to 10"), and let users set notification hours. Linear [obs, doc].
41. **Ship Lock Screen list, one-tap add and progress pieces, and make widget rows completable in place**; give the Today widget a count in the header and a + in the corner. Things [doc], TickTick [obs].
42. **Put capture on every OS surface (widget, Control, Action Button, Lock Screen), each opening straight into quick add.** Todoist [doc].
43. **Publish a running timer as a Live Activity.** TickTick [doc].

### First run and gating

44. **Teach with a sample project made of real to-dos** ("Swipe right to schedule"), because the lesson sits where the gesture works. Things [know].
45. **Gate paid features at the point of use (a lock on the chip, an upsell sheet), not with a banner**, so free users still see where a feature lives. Todoist [doc].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Two-line task row | 44pt pitch, no separators; checkbox about 15pt at x≈20; title x 45; 17pt title + about 13pt grey #a0a3a8 | Things [meas] |
| Reminders rows | 42pt single line; 67pt two lines; circle 24pt, 2pt stroke #c5c5c6 | Reminders [meas] |
| TickTick row | about 47pt; 15pt square checkbox | TickTick [meas ±10%] |
| Linear rows | inbox about 70pt (2 lines), 87pt (3 lines), 40pt avatar; project rows 49pt with 18pt health glyph | Linear [meas] |
| Todoist nav rows | 50pt pitch, 24pt icon in #dc4c3e, cards inset about 17pt on #f8f5f2 | Todoist [meas] |
| View title | about 28pt bold with about 26pt glyph (Things); 34pt bold in list colour (Reminders); about 22pt bold (Linear) | [meas] |
| Floating + | 48pt, 28pt from right, 29pt bottom gap (Reminders); lifted 74pt while dragging (Things, resting about 56pt [know]) | [meas] |
| Insertion gap | 44pt, #e3e5e8 | Things [meas] |
| Nav buttons | 44pt glass circles; Reminders side inset 20pt, right capsule 108x44pt | Reminders [meas] |
| Smart-list tiles | 191x80pt, 8pt gaps, 20pt margins, count bold about 24pt | Reminders [meas] |
| Toolbar | glass capsule about 272x56pt, selected pill about 63pt, 48pt compose circle, about 29pt above the bottom | Linear [meas] |
| Swipe capsule | inset 10pt, row slides about 135pt, #7885fe | Linear [obs, meas] |
| Task detail title | about 20pt semibold after a 21pt priority circle (1.5pt stroke, 10% fill); property rows about 46pt | Todoist [meas] |
| Picker timing | When popover in and out about 130ms (4 frames at 30fps) | Things [meas] |
| Insert timing | drop to open card about 270ms main, 370ms with settle; card close about 370ms; other rows fade to about 30% | Things [meas] |
| Colours | Things blue #4d8ff9, heading #2565c5 / #73abff, dark bg #1d2229; Todoist red #dc4c3e, p1 #D1453B [3p], p2 #eb8909, p3 #246FE0 [3p], token tint #fde7d8; TickTick #4772fa; Reminders #0088fe, secondary #8a8a8d, bg #f2f2f6; Linear bg #181819, unread #1994fd, health #52b885 / #de5757 / #e9c251 | [meas] |
| Card radius | Things edit card about 28pt; TickTick date card about 12pt; Reminders New Reminder sheet about 38pt | [obs, meas] |
| Non-content words | Things Today 4, new-to-do card 2; Todoist Quick Add 1, Browse 6; TickTick Inbox 3; Reminders Today 5; Linear composer 3 | [obs] |
| Limits | subtasks 5 levels (TickTick); 9 pinned lists (Reminders); Recently Deleted 30 days | [doc] |

## Anti-patterns seen

- **Generated "who did what" text on every row.** Linear's Inbox carries about 28 non-content words, about 25 of them phrases like "Marked as completed by" across 7 rows [obs]. Fix: let the action badge carry the verb and keep the row to the item and the person.
- **Settings and create surfaces drowning in labels.** Todoist's Display sheet has about 20 non-content words, Reminders' New Reminder about 22 with a 9-word footer, Reminders' lists home about 19 [obs]. Fix: values as subtitles, no explanatory footers.
- **Recoloured parse text.** Reminders turns the parsed phrase blue, which reads worse at a glance than Todoist's background tint [obs].
- **Menu and drag on the same long-press.** Todoist tells users to "move it slightly to the right" to dismiss the menu during a drag [doc]. Fix: movement cancels the menu.
- **Parsing in one place, not another.** Todoist's Shortcuts "Create Task" name field does not parse natural language [doc]. Fix: one parser behind every capture path.
- **No offline support.** An App Store review of Linear: "There's no offline support at all" [doc].
- **Roomy rows in a daily list.** Reminders' 67pt two-line rows show 3 to-dos where Things shows 5 [meas].

## Steal list

1. Make the + draggable, open a row-height gap at the drop point and pre-fill from where it lands, because position already answers the form.
2. Expand a row into an edit card in place, because the user keeps their place.
3. Put two-line rows on a 44pt pitch with no separators in daily lists, because density is the feature.
4. Stroke the completion circle in the priority colour, because the tap target then carries urgency for free.
5. Highlight parsed phrases with a tint, echo them as chips and make each tap-to-undo, because parsers eat real words.
6. End every list with a dotted blank row for inline add, because it costs no words.
7. Tint the title, + and completion fill with the list's colour, because the screen then says which list you are in.
8. Give each time bucket one glyph and colour everywhere, because the mark replaces the word.
9. Dock property value-chips above the keyboard in a structured composer, because the keyboard never has to close.
10. Swipe to the two most frequent safe acts and keep delete second, with 30-day recovery instead of a confirm.
11. Let completion linger a beat so re-tapping undoes, and celebrate with a short tone the user can turn off.
12. Finish and reschedule from the notification and complete from the widget, because most to-dos are handled from the Lock Screen.
13. Show day load inside the date picker, because the user is choosing a day they can do it on.
14. Lead work-activity rows with an avatar plus action badge and a trailing status glyph, because who and what read before words.

## For a business dashboard app (HQ)

The case files converge on one recipe. Use the Reminders chrome (glass nav buttons, sheets, 48pt +), Things' density (44pt two-line rows) and Todoist's parsed one-line quick add with a draggable + for placement (Reminders, Todoist category notes). Email to-dos take Linear's inbox row: sender avatar plus action badge, unread dot, trailing time; structured items (projects, leads) take its chip-row composer; plain to-dos keep the circle-and-list pattern (Linear category note). With many surfaces (to-dos, email to-dos, projects, notes, database, health), let the tab bar be chosen and default to the three or four used most (TickTick category note).
