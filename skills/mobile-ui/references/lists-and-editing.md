# Lists, rows and editing on a phone

Most phone screens are lists. These rules cover row anatomy, density, swipe actions, long-press menus, creating and placing items, reorder, multi-select, and databases and tables on a narrow screen. Tags: [meas] measured, [doc] docs, [obs] seen, [know] prior knowledge. Case files: firstmate `data/mobile-design-skill/evidence/cases/`.

## 1. Pick the list style

- **Plain list** for long homogeneous feeds (mail, to-dos, transactions, activity): edge-to-edge rows, sticky section headers, separators inset to the text column or none.
- **Inset grouped list** for settings, forms and short structured data: 52pt rows in white cards with about 26pt corners on #F2F2F7 (iOS 26) [meas HIG].
- **Cards on a tinted page** for grouped lists that collapse (Amie's list cards with icon, name, count and chevron on #F5F5F5; Todoist's white cards on warm #F8F5F2; TickTick's date cards) [meas/obs].
- **Module grid** for dashboards (see the glance-dashboards chapter).

## 2. Row anatomy

Leading identity, then content, then one trailing signal. Each slot carries one fact.

| Slot | What goes there | Examples |
|---|---|---|
| Leading | the tick circle (stroked in priority colour), avatar, app icon, merchant logo, kind glyph | Todoist p2 circle #EB8909; Gmail 40pt avatar; Copilot merchant logos |
| Title line | the item's own words, 17pt (15-16pt in dense apps) | |
| Context line | one line of grey 13-15pt: project, snippet, "time · person" | Things project name 13pt #A0A3A8; Revolut "time · person" |
| Trailing | one signal: time, amount (right-aligned, tabular), a status glyph, a date chip coloured by nearness, an unread dot or a chevron | Linear status glyph; Fantastical "Join" capsule only when it applies |

Rules:
- **Density follows frequency.** A list scanned many times a day packs two-line rows on a 44pt pitch with no separators (Things); Reminders' 67pt two-line rows fit three where Things fits five [meas]. Mail rows run 79-102pt for 3-4 lines with a 38-44pt avatar [meas].
- **One unread cue:** a 6-7pt dot in a left gutter or bold, never both plus a word [meas].
- **A pending state replaces the timestamp** in the same slot, coloured (Superhuman shows the reminder where the time was) [obs].
- **Align chips in a fixed column**, not after variable-length names, so they scan as a column (Copilot categories) [obs].
- **Glyphs replace field labels** in rows and cards (Attio attribute icons) [obs].
- **Dim the past to about 40%** instead of hiding it when context matters (Fantastical) [obs]; hide completed items by default in task lists, one tap to show (Reminders) [doc].
- **Collapse the automated, keep people full.** Machine-made items collapse into one row per category with sender chips and counts (Spark), a summary row with an "N new" pill (Gmail), or a digest per sender (Apple Mail) [obs].
- **Group by what the user decides on:** part of day (Things This Evening; Reminders Morning / Afternoon / Tonight), date with small grey caps day headers and a large month header carrying the month total (Copilot), recency (Apple Notes Pinned / Yesterday / Previous 7 Days) [obs].
- **Upcoming above posted**, with a relative due time (Revolut) [obs].

## 3. Swipe actions

- **One swipe completes, the other defers or toggles.** Spark: right = Done (green #81D134); Superhuman: left = Done, right = Remind; Gmail: archive both ways; Things: right = schedule, left = select [doc/meas]. Pick the pair for the list's one decision.
- **Delete is never the default single swipe.** Put it second in the trailing set or behind a full swipe with undo; recover from Recently Deleted (30 days) instead of confirming (Reminders, Notes) [doc].
- **At most three buttons per side** (TickTick caps it; HIG: Delete plus two) [doc].
- **Colours:** green for done, the list or brand hue for the positive toggle, orange for flag or later, grey or blue for more, red only for delete [know/meas].
- **Full swipe performs the first action** past about 60% of the row width; a short swipe reveals the buttons (Spark's Done reveal about 132pt) [doc/meas].
- **Draw actions as inset capsules** that grow with the swipe (Linear, iOS 26 style) rather than full-height slabs [obs].
- **Let users configure each side** from a short list (Todoist, Gmail, Spark, Superhuman all do) [doc].
- **Show the undo snackbar for 5s** after any swipe that removes a row [doc].
- Mirror every swipe action in the context menu and as a VoiceOver custom action, because swipes are invisible [doc].

Expo: `ReanimatedSwipeable` on FlashList rows (build the full swipe and haptic yourself, see `animate-expo`), or `@expo/ui` `SwipeActions` inside a SwiftUI `List` for exact Mail behaviour.

## 4. Long-press and context menus

- Every content row gets a context menu with a preview: 3-6 items, grouped, the destructive item red and last, unavailable items hidden, one submenu level at most [doc].
- Every item in it is also reachable on screen (the menu is a shortcut).
- Long-press on a button gives its power variant (Send → schedule presets with concrete times "Send 8:00 AM Tomorrow"; + → recent photos; a tab → its create action) [obs/doc].
- Show reactions or quick verbs above the menu when the object is social (Telegram) [know].

Expo: `Link.Menu` + `Link.Preview` on rows that navigate; `@expo/ui` `ContextMenu` elsewhere. Set `borderRadius` on the `Link.Trigger` child so the lifted preview keeps your radius.

## 5. Creating items

- **Inline add at the end of each list:** a tappable blank row or a dotted placeholder row (Reminders) that becomes an editable row in place [obs].
- **A floating + that can be dragged** to the exact position, list, heading or date where the item should land; a real row-height gap opens at the drop point and the new item is pre-filled from where it lands (Things Magic Plus, Todoist Dynamic Add, TickTick) [obs/doc].
- **Pre-fill from context:** created in Today → today; under a date → that date; in a project → that project. The capture sheet shows the destination as a chip the user can change (Craft, Linear) [obs].
- **Quick add is one line that parses** (see input-and-forms.md); the full form is one tap away ("Show More" in Fantastical).
- After commit, reset the creation surface to zero so the next one starts clean (Cash App) [obs]; keep the keyboard up for rapid entry in task lists [know].

## 6. Editing in place

- Tapping a task or reminder expands it in place into an edit card (notes, checklist, date, tags as icons) instead of pushing a detail screen, so the user keeps their place (Things, Reminders) [obs].
- Records with many fields push a detail screen whose header is the record (avatar + name in the nav bar: Attio), facets as a scrolling chip row of tabs, an overview of the key fields as a 2-column grid of tappable widgets, and history as one timeline [doc/obs].
- Empty optional fields show as grey icon-led placeholder rows that are also the add buttons (Notion Calendar) [obs].
- Show an AI or auto-detected value as a proposal with Confirm / Edit / × inline, in a distinct ink until accepted (Oura, TickTick) [obs].

## 7. Completion

- The tick circle fills with the list or priority colour, the row lingers a beat (so a second tap undoes), then leaves; add a success haptic and, in task apps, an optional short tone (Todoist on by default with a toggle) [doc/know].
- Deliberate completion on big targets: press and hold (Streaks, ring fills in about 500ms) [meas].
- Never confetti per item. Celebrate the whole set once (Streaks' gold page; "Enjoy your tomorrow!" in Amie's empty day) [obs].

## 8. Reorder and multi-select

- Reorder by long-press-and-drag on the row itself; no permanent handles. Nesting by dragging right (Todoist) or onto another item (Reminders) [doc].
- Multi-select: tap avatar or leading circle to select (Gmail), or Select in the nav bar; selected rows show filled circles; a bottom toolbar shows batch actions with the count on the button ("Update 25 Transactions", Copilot) [doc/obs].
- Bulk review queues: one "accept all" with the count, each row explaining the suggested change on its second line ("Restaurants → Health") (Copilot) [obs].

## 9. Databases and tables on a phone

- **Default to a list view.** Each record is the title plus one indented property line (Notion about 69pt; Obsidian's List layout indents properties); no horizontal scroll [meas/doc].
- **A database header is one row:** the view name as a pill with a chevron ("List ⌄"), search, filter (accent when active, count in the pill), sort, and a split "+ ⌄" for new record or new from template (Notion, Attio) [meas/obs].
- **When the table is the point, keep it a table:** frozen first column (checkbox, avatar, name), 46pt rows, horizontal scroll for the rest, an aggregate footer, column headers kept (Attio) [meas]. Open it full screen from inside a page (Craft zooms inline databases out to full screen) [doc].
- **Boards** show one column at about 85% width with the next peeking; drag cards between columns; column header has the count and a + (Notion, Attio) [know/obs].
- **Filters as removable chips** under the header ("Sep 2026 ×"), with the filtered totals right below them (Copilot's spent / income / net) [obs].
- Row height and summaries are per-view settings in power tools (Obsidian) [doc].

Expo: FlashList v2 for the list view; for a frozen-column table, a horizontal `ScrollView` of a `FlashList`, with the first column as a second list synced through a Reanimated shared scroll offset.

## 10. Pull to refresh and live updates

- The system refresh spinner sits above the large title [know]. Do not add a "Last updated" line while data is live; label staleness only when stale.
- Live rows update silently in place. Never reorder a list under the user's finger because background data changed.
