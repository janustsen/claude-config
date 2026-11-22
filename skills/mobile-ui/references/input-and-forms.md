# Input, keyboards and forms

Typing on a phone is slow, so the best apps type less: they parse one line, pre-fill from context, offer chips and pickers, and keep the keyboard from ever hiding the commit. Tags: [meas] [doc] [obs] [web] [know]. Case files: firstmate `data/mobile-design-skill/evidence/cases/`.

## 1. Quick capture: parse, don't form

- **One line that understands.** Todoist parses "Call Dana tomorrow 3pm #Sales p1" as you type and highlights each understood phrase in place (peach #FDE7D8), echoing the values as chips below; tapping a highlight undoes that parse [meas/doc]. Fantastical bolds each recognised token and mirrors the parsed title in the sheet's nav title [obs]. Reminders previews what it will save ("Title: Water the plants") [obs]. TickTick turns one spoken sentence into several parsed task cards before saving [doc].
- **Keep the title literal where parsing would eat words:** Things parses dates only in its date field, never in the title [doc]. Pick one model per app and say which by what highlights.
- **The full form is one tap away** ("Show More" in Fantastical; property chips in Linear's composer) [obs].
- **The capture sheet opens with the keyboard up**, at the medium detent or as a bar docked above the keyboard, with the destination shown as a chip (Linear's scope chip in the composer header; Craft's destination on the capture sheet) [obs].
- **Property chips docked above the keyboard** for structured items: status, assignee, priority, date, each a chip that opens a picker (Linear) [obs]. Expo: `KeyboardStickyView` with a horizontal `ScrollView` of chips.
- **Capture from everywhere:** a widget with a +, a Control Center control, the Action button, a Lock Screen widget, the share sheet, Siri (Todoist, Things, ChatGPT) [doc].

## 2. Keyboard configuration (every field)

- Set the **keyboard type** (email, number pad, decimal pad, URL, phone), the **return key** ("next" through a form, the verb on the last field: send, search, done, go) and **autofill** (`autoComplete` / `textContentType`: email, username, password, newPassword, oneTimeCode) on every field [doc].
- Dismiss by dragging the scroll view (`keyboardDismissMode="interactive"`) and by return on single-line fields; `keyboardShouldPersistTaps="handled"` so the first tap on a button works [doc/know].
- The focused field and the primary button stay visible above the keyboard, always [doc]. Expo: `KeyboardProvider` at the root; `KeyboardAwareScrollView` for forms; `KeyboardStickyView` for bars.
- Inputs are 17pt (body); never below 16pt [know].

## 3. The keyboard accessory bar

- **Context-aware tools:** in a list, indent, outdent, move up, move down; in plain text, insert and media (Notion) [doc/obs]. User-reorderable in power tools (Obsidian, TickTick quick-add toolbar) [doc].
- **The dismiss-keyboard key is pinned at the right edge, outside the scrolling tools** (Notion) [obs].
- **Undo and redo first** on a formatting surface, because a phone has no ⌘Z (Bear) [doc].
- **When the tools outgrow one bar, swap the keyboard for a same-height tool panel:** Notion's 2-column block grid on +, Bear's 6x4 formatting keyboard, Apple Notes' format panel with styles first [doc].
- **The same tools in the same order** above the keyboard as in the bottom toolbar when the keyboard is down (Apple Notes) [know/doc].
- Toolbar taps must never blur the editor (Obsidian) [3p].
- Expo: `KeyboardToolbar` (keyboard-controller) or `InputAccessoryView`.

## 4. Composers (messages, AI prompts, comments)

- **One bottom-right slot that changes with state:** voice when empty, send when text exists, stop while a reply streams, end in a voice call. Only the send state is accent-filled (Claude keeps voice black, send coral) [obs]. Stop appears within 0.5s of send (ChatGPT web) [obs].
- **Attach far left, send far right**, so occasional and frequent actions never collide [obs].
- **Return inserts a newline; only the button sends** on a phone (ChatGPT, Claude) [obs/know].
- **Dictation and live voice are two controls with two glyphs:** mic = speech to text you review (X cancel, ✓/arrow send); waveform = a live conversation [doc]. When one mic could mean "ask" or "record a meeting", put them on different controls and say which records (Granola) [doc].
- **The placeholder names the mode** ("Temporary chat", "Describe or edit this image", "Who did I meet with?") and is the only label [doc/obs].
- **The model or mode picker sits in the composer** when users change it per message (Claude's "Opus" pill, Granola's "Auto ⌄"), and at the top when they rarely do (ChatGPT) [obs].
- Long-press Send for the power variant (schedule send with concrete times; pick a model for one message) [obs/doc].
- Grow the composer to about 5 lines, then scroll inside it.
- Expo: `KeyboardStickyView` for the bar; `KeyboardChatScrollView` or an inverted Legend List for the thread.

## 5. Pickers and choosing

- **Show the resolved value beside each preset:** snooze rows read "tomorrow · Mon 8:00 AM" right-aligned (Superhuman); schedule-send presets name the time ("Send 8:00 AM Tomorrow", Apple Mail) [obs].
- **Preset amounts plus Custom** for small numeric inputs (Uber tips) [obs].
- **Date picker:** Today, Tomorrow, This Weekend, Someday shortcuts above a calendar; show existing load per day inside the picker (Todoist) [doc]. Use the native compact or inline date picker; never a custom wheel.
- **Anchored pickers open fast** (about 130ms, Things) [meas].
- **Segmented control** for 2-5 closely related views; a pull-down menu for more, or for rarely changed choices (Gentler Streak's range capsule beside the headline; Attio's All / Mine from the nav title) [doc/obs].
- **Chips, sliders and tappable day circles instead of text fields** for logging moods, symptoms and ratings (Apple Health, Oura) [obs].
- **One question per screen** with full-width options in onboarding and clarifying steps; offer Skip whenever the user can proceed without answering (Opal, Perplexity) [obs].

## 6. Forms

- Prefer a sentence over a form for short flows: Cash App builds "Pay $65 to Carissa for Concert tixx" as the steps complete and the sentence becomes the confirm screen [obs]. Carrot writes rules as sentences with tappable tokens ("Show when **20 mph** or above over next **12 hrs**") [obs].
- **Editable defaults as rows with a "Change" chip**, not as fields (Wise) [obs].
- **Prefill what is known, focus what is unknown** in two-field entry (Uber pickup and destination) [obs].
- **One page, finished steps collapse** into summary cards, and the next picker jumps to the first available option (Amie booking) [web].
- Visible labels on forms with several fields; a placeholder alone only where the field's job is obvious from its place (composer, search, title line).
- The Continue button enables only when the required input exists, changing its fill in place (Cash App) [obs]; no validation errors before the user leaves a field.
- **Commit facts sit right above the commit button:** cost, arrival time, guarantees (Wise "No hidden fees, ever"), the total with a breakdown link (Airbnb) [obs/web]. Irreversibility is stated once, small, under the button; no confirm dialog (Cash App) [obs].
- Hold or swipe to commit only for irreversible money or safety actions (Robinhood swipe up on review, with a setting to skip) [doc].
- Guard swipe-to-dismiss on a dirty form with Save / Discard (`usePreventRemove`).

## 7. Search

- At the bottom (tab or toolbar field) unless a sheet owns the bottom; see navigation-and-gestures.md.
- Focused state: recent searches (removable, with Clear in the header), suggested filter chips, then live results grouped by kind (Gmail filter chips under the field) [obs/doc].
- Results highlight the matched words; no-results repeats the query and offers to broaden.
- Find-in-document docks at the bottom with n / N and arrows (Bear) [obs].
- One "create or find" field can serve both (Obsidian's quick switcher) [doc].
