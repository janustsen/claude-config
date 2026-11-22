# States, feedback and system surfaces

Every screen has more states than the happy one, and a phone app lives partly outside itself: on the Lock Screen, in notifications, in widgets and the Dynamic Island. Tags: [meas] [doc] [obs] [know]. Case files: firstmate `data/mobile-design-skill/evidence/cases/`.

## 1. The state set

Design each before styling: first run, permission primer, empty, loading, partial, error, offline, stale, gated (paywall or sign-in), success.

### First run and onboarding

- Land on the real home. If setup is needed, one question per screen, full-width options, one bottom capsule button (about 48pt, 16-20pt margins), skippable, never shown again (Opal) [obs].
- Postpone setup with good defaults; no licence text; no feature carousel [doc onboarding].
- Value before account: let the user do the core act before asking to sign in, where the product allows it [know].

### Permissions

- Ask at the moment of need, never at launch [doc privacy].
- A primer screen may explain first, and its only button triggers the system prompt: no "Not now", no fake buttons (HIG). Opal shows a picture of the dialog with an arrow at "Allow" before triggering the real one; Streaks explains Health access inside the task that needs it, in one sentence ("This task uses data from the Health app…") [obs/doc].
- Request the smallest scope the feature needs (only the HealthKit types used) [know].
- When denied, the feature shows a one-line explanation and a button to Settings, in place, and the rest of the app keeps working.

### Empty

- One short line plus the action, or a small reward when empty is good news: "Enjoy your tomorrow!" (Amie), Copilot's cleared review queue reframed as "So far today" with what was cleared [obs].
- Hide empty sections and features instead of showing placeholders (Fantastical hides empty days) [doc]. Never hide a tab because it is empty [doc].
- No illustration in a returning-user tool; a small illustration is fine on a first-run empty state.

### Loading

- Nothing for about 400ms, then a skeleton in the shape of the content or the live progress line; never show the empty state while the first load runs [know/doc expo skill].
- Pull to refresh uses the system spinner above the large title.
- Reserve the space the content will take so nothing jumps.
- AI and agent work: quiet grey step lines that collapse to a result card ("Worked for 2m 13s ›") [obs Claude, Perplexity].

### Error and offline

- Errors say what happened and the fix, with the semantic colour and a named action ("Reconnect Gmail"), in place where the failed thing is, not in a toast that disappears.
- Problem states carry cause, likelihood and duration when known: Flighty's "grounded for the next 42m due to thunderstorms. Probability of extension is 30-60%" [obs].
- Healthy sync is silent; only conflicts or failures surface, at the top of the list with an icon (Bear); sync state as a coloured glyph with a log behind it (Obsidian green / purple / red) [doc].
- Stale data is labelled in place: "Offline Mode · Estimating all times" (Flighty); "Offline · showing 09:41 data" [doc].
- Offline-capable apps fade what is unavailable offline with one sentence on how to get it back, and grey out online-only actions (Craft) [doc].
- Unknown values leave their slot empty; never a fake placeholder number (Uber) [doc].

### Gated

- A sign-in wall or paywall names what the user gets, shows the price and the trial terms plainly, and has a visible close.
- Upgrade prompts appear at the point of the limit, never on launch.

### Success and celebration

- Most success is the change itself: the row leaves, the tick fills, a success haptic plays. No toast for an action the user can see happen.
- A receipt for money and commitments: who, when, what for, amount, "✓ Complete", Done (Cash App); Robinhood removed its confetti and confirms with a calm summary [obs/doc].
- Celebrate the set, not the tap: Streaks turns the page gold once the whole day is done; Opal gives a collectible gem per milestone, revealed by a tap [obs/doc].
- Gentle copy at low points: "You'll be alright… cut yourself some slack today" (Oura); a status switch (Sick, On a Break) pauses nudges (Gentler Streak) [obs/doc].

### Undo instead of confirm

- Reversible actions (archive, done, delete to a recoverable bin, send with a delay) get a 5s undo snackbar above the tab bar or bottom toolbar; Apple Mail's undo send is configurable up to 30s [doc].
- Confirm only what cannot be undone, with an anchored action sheet naming the consequence ("Delete 3 projects and their 41 tasks").

## 2. Haptics

| Moment | Haptic |
|---|---|
| A task completes, a message sends, a payment succeeds | notification success |
| Something failed or was refused | notification warning or error |
| A value changes under the finger (scrubbing a chart, a picker, a slider you built) | selection |
| A dragged item snaps into a slot, a sheet hits a detent you drew | light or rigid impact |
| Press-and-hold progress | selection while filling, success at the end (Streaks) |
| Plain taps, navigation, opening sheets | none |

Native controls (switches, system pickers, date pickers) already play their own; do not add another [doc]. Haptics are silent in Low Power Mode and while the camera is active [doc]. Expo: `expo-haptics`; timing details in `animate-expo`.

## 3. Notifications

- A short title and one complete sentence in sentence case; no app name (the system shows the icon); no sensitive data in previews [doc].
- Say the outcome and the change: Flighty's "{object} • {event}" then "{new value} ({delta})"; Linear's notifications say who changed what [doc/obs].
- 1-3 action buttons that finish the job without opening the app: Done, Snooze, Reply, Approve (Reminders completes and reschedules from the notification; Todoist completes) [obs/doc]. Never "Open app".
- Time Sensitive only for genuinely time-bound events; let users set notification hours (Linear) [doc].
- Badge counts only unread notifications [doc].
- Expo: `expo-notifications` categories with actions; `interruptionLevel` set honestly.

## 4. Widgets

- One glanceable fact per widget, deep-linking each tap target to the exact screen: next item, today's count, time left in the current block (Amie), the day's suggestion with one action (Gentler Streak "Start Workout") [doc].
- Several shapes of the same data (Streaks: ring, streak number, dot calendar, bar chart) [obs].
- A + on list widgets for capture (Craft, Todoist); interactive rows that complete (Things) [obs/doc].
- An option to hide titles on Lock Screen widgets for privacy (Notion Calendar) [doc].
- Expo: `expo-widgets` (`createWidget`); widget code runs in an isolated runtime with no hooks or imports.

## 5. Live Activities and the Dynamic Island

- Only for a bounded process with a start and an end, at most 8 hours: a ride, a flight, a timer, a running sync or job, a recording (Granola, Streaks timers, Flighty, Uber) [doc/obs].
- Compact leading + trailing read as one sentence across the camera (countdown on one side, a capsule of status on the other); minimal is a circular progress [doc].
- Include the stop or end control when the process is the user's (Granola, Claude, Perplexity tasks) [obs].
- Drive updates from the server, debounced, and end them from the server the moment the process ends (Uber measured about 2% fewer pickup cancellations from its Live Activity) [doc].
- Animations at most 2s; heavier text weights; the Island background is always black [doc].
- Expo: `expo-widgets` `createLiveActivity`.

## 6. App icon and launch

- A layered Icon Composer icon of 1-2 bold flat shapes on a solid or gradient field; check default, dark, clear and tinted appearances; no text, photos or baked shadows [doc]. Expo: `ios.icon` pointing at the `.icon` directory.
- The launch screen is the empty shell of the first screen, no logo; restore the previous state on relaunch [doc]. Expo: `expo-splash-screen` with the background colour and a fade.

## 7. Privacy on a phone

- A hide-values eye toggle on screens of private numbers (Wise) [obs].
- Locked items stay findable as a title plus a lock or placeholder bars (Apple Notes, Bear) [obs/doc].
- Sensitive previews off by default in notifications and widgets.
