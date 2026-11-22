# The laws

Each law has the reason it works on a phone, the evidence from the apps studied, and the anti-pattern it replaces. The desktop laws in `product-ui/references/laws.md` still hold (chrome recedes, defaults are invisible, outcome first, every way in has a way out); these are the ones the phone changes or adds.

## Structure

### M1. One thing at a time
**Why:** a 393pt screen holds one list or one object; splitting it makes both unreadable. **Evidence:** every studied app is single-column; second panes arrive as pushes or sheets (Attio record facets as swipeable tab chips, Flighty's detail sheet over the map). **Anti-pattern:** a desktop two-pane layout squeezed onto the phone, or a dashboard of six equal tiles with no lead.

### M2. One hero, then uniform modules
**Why:** a glance reads one thing; the rest must be scannable by sameness. **Evidence:** Apple Weather (temperature ≥5x body, then one module component), Robinhood (value, change, chart), Oura (gauge plus a 3-4 word headline), Cash App (the amount at about 100pt), Streaks (the grid itself). **Anti-pattern:** a home of equally loud cards.

### M3. The phone has a job, and it is rarely authoring
**Why:** people pick up the phone to glance, capture, triage, approve and steer. **Evidence:** Linear iPhone is inbox and capture; ChatGPT Spaces are read-only on phones; Granola's phone app records and reads. **Anti-pattern:** porting every desktop editor to the phone with the same chrome.

### M4. Tabs are places; create is an action
**Why:** a tab bar that holds "Add" changes meaning by slot and breaks the floating bar's model. **Evidence:** Craft's split bar (destinations capsule plus +/AI capsule), Oura's separate + circle, Reminders' and Things' floating +, Apple's HIG. **Anti-pattern:** a centre "+" tab.

## Reach and placement

### M5. Act in the bottom third, read at the top
**Why:** the thumb rests low; the top is a stretch. **Evidence:** search moved to the bottom in iOS 26; Apple Mail's bottom row (filter, search, compose); bottom-right primary slots in ChatGPT, Claude, Reminders; sticky commit bars in Airbnb, Uber, Wise. **Anti-pattern:** a top-right "Save" as the only commit on a long form.

### M6. The commit shows its facts
**Why:** the last thing read before a commit should be what it costs and when it lands. **Evidence:** Wise (fee, arrival, guarantee rows above Continue), Airbnb (total + "Free cancellation" beside Reserve), Cash App (the sentence is the confirm screen, irreversibility in one small line). **Anti-pattern:** a confirm dialog repeating the form.

## Gestures and editing

### M7. Swipe is the verb, undo is the safety
**Why:** triage has two common outcomes, and fast actions need a cheap way back. **Evidence:** Superhuman (Done / Remind), Spark (Done + 5s undo), Gmail (archive both ways + undo), Things (schedule / select), Reminders and Notes (Recently Deleted instead of confirms). **Anti-pattern:** swipe-to-delete with an "Are you sure?" alert.

### M8. Long-press is a shortcut, never a secret
**Why:** hidden-only actions are never found; duplicated ones speed up experts. **Evidence:** ChatGPT (long-press Send, +, chats, messages), Apple Mail (schedule send), Craft (long-press a tab to create), HIG ("every item must also exist in the main UI"). **Anti-pattern:** an action reachable only by long-press.

### M9. Position decides; context pre-fills
**Why:** on a phone, where you put something is faster than a form field. **Evidence:** Things Magic Plus and Todoist Dynamic Add (drag + to the slot), Amie (drag a to-do into the time grid), Craft and Linear (destination chip from the current screen). **Anti-pattern:** a blank "New task" form that asks for the list and date the user is already looking at.

### M10. Parse one line, show what was understood
**Why:** typing fields one by one is the slowest thing on a phone. **Evidence:** Todoist (in-place highlights, tap to undo), Fantastical (bold tokens, title mirrored in the sheet title), Reminders ("Title: …" preview), TickTick (one sentence, several tasks). **Anti-pattern:** a date picker, a project picker and a priority picker for every task.

## Layers

### M11. Push to go deeper, sheet to step aside, full screen to change rooms
**Why:** the layer tells the user whether they will come back. **Evidence:** HIG modality, Things (inline edit), Superhuman (snooze sheet), Opal (full-screen focus), Apple Maps (persistent sheet over the canvas). **Anti-pattern:** a pushed screen for picking a date; a sheet on a sheet.

### M12. Glass is the control layer only
**Why:** glass marks what floats and can be touched; on content it muddies hierarchy and legibility. **Evidence:** Apple's WWDC25 sessions and HIG ("Don't use Liquid Glass in the content layer", "avoid glass on glass"). **Anti-pattern:** frosted cards stacked over a gradient.

## Information

### M13. Live things are phases with a verdict and a cause
**Why:** a live process has a different important fact at each moment. **Evidence:** Flighty (countdown → gate → progress → baggage; "Inbound aircraft is in air… enough time"), Uber (P0 time, P1 plate, P2 progress; empty slot when unknown; the last 20% of the bar covers the last 2 minutes), Apple Maps ("Opens 7:00 AM"). **Anti-pattern:** a static card listing every field with "Status: In progress".

### M14. Compare to the user's own normal
**Why:** a fixed goal shames on bad days; a baseline explains. **Evidence:** Gentler Streak ("Above typical", a shaded normal band), Oura (personal range bar), Opal ("Get back 1h23m" vs usual), Apple Health ("compared to your average"). **Anti-pattern:** a red "Goal missed" banner.

### M15. Show urgency only while it is true
**Why:** a permanent "all clear" panel is chrome; an inserted alert is news. **Evidence:** Apple Weather and Carrot insert alert modules at the top only while a threshold is crossed and title them with the finding ("Heavy rain next hour"); Carrot fills only the tile past its threshold. **Anti-pattern:** an "Alerts (0)" card.

### M16. Colour is identity, state or tap
**Why:** three jobs, never mixed, so colour can replace words. **Evidence:** Reminders (list colour tints title, + and tick), Todoist (priority stroke, date nearness), Flighty (four status meanings), Copilot and Wise (only income green). **Anti-pattern:** a brand gradient on every header plus coloured status pills plus a coloured primary.

## Feeling

### M17. Calm by default; celebrate the set
**Why:** per-tap celebration becomes noise; a rare, earned moment stays special. **Evidence:** Streaks (gold page once per day), Opal (gems per milestone), Robinhood (removed confetti). **Anti-pattern:** confetti on every completed task.

### M18. Haptics are words
**Why:** a haptic that fires on everything means nothing. **Evidence:** HIG (notification, impact, selection meanings), Streaks (selection while filling, success at the end), Robinhood (selection while scrubbing). **Anti-pattern:** a light impact on every button.

### M19. Native first
**Why:** users feel a non-native bar, sheet or switch immediately, and the system versions get Liquid Glass, haptics, accessibility and new OS behaviour for free. **Evidence:** Expo SDK 58 makes native tabs, toolbars and `@expo/ui` controls stable; the HIG's tab bar minimize, search tab and accessory slot exist only natively. **Anti-pattern:** a JS tab bar, a JS bottom sheet for a simple picker, Ionicons, hard-coded #007AFF.

### M20. The app reaches past itself
**Why:** most phone interactions with an app happen outside it. **Evidence:** Reminders and Todoist complete from notifications; Flighty and Uber live in the Dynamic Island; Gentler Streak's widget starts the suggested workout; Things ships completable Lock Screen widgets. **Anti-pattern:** a notification that only says "Open the app to see what changed".
