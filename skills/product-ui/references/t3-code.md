# Case study: T3 Code

T3 Code (desktop app 0.1.7, open source at `github.com/pingdotgg/t3code`, tag `v0.1.7`) is a GUI for coding agents. It was driven screen by screen at 1440x900, 1100, 840 (its minimum width), 390px phone emulation and dark mode, and read alongside its source for exact values. It is the reference product for this skill because it does one hard thing well: it stays calm while running ten agents in parallel.

**In one line:** a quiet, dense, monochrome workbench where the agent's output is the document, the human's attention is the scarce resource, and each control sits where its decision is made, shows itself only when it matters, and morphs in place instead of multiplying.

## Screen inventory (what was opened)

| Area | Screens and states |
|---|---|
| First run | Welcome, agent detection, project import with the most recent pre-checked, importing, landing in a thread |
| Shell | Main at 1440, thread details card, settled shelf, row hover, tooltips |
| New thread | Empty hero question, composer, context strip |
| Add project | Palette "Sources" page, keyboard highlight, new project page with inline Create, created toast |
| Composer pickers | Model and reasoning, permissions slider with hover preview, workspace, branch, `/` commands, `@` files, `$` skills |
| Running turn | Turn start, progress, inline approval and its More menu, provider status banner, stop |
| Finished turn | Folded receipt, expanded work log, file-edit row with Open diff, command row with output |
| Right panel | Diff (skeleton, loaded, file expanded), file viewer and tree, "+" launcher, terminal, destructive confirm |
| Global | ⌘K palette, Usage sheet, Pull requests (skeleton), project filter, focus ring |
| Settings | 26 routes, legacy aliases redirect |
| Responsive | 1100, 840 overlay mode, 390 phone (thread, sidebar sheet, new thread, settings rail, usage) |
| Boot | Splash is the centred app icon only |

## Teardown by category

Each line is an observation; the rules they produce live in the files named.

**IA** ([shell-and-navigation.md](shell-and-navigation.md) §1)
- No home screen: launch lands on a draft thread in the most recent project.
- Sidebar 256px is a cross-project inbox: Pinned / Active / Working / Snoozed / Settled. "Boring sidebar" (group by project) is an opt-in Labs toggle.
- Activity never reorders rows. Settings copy: "They return to the top of the inbox when they need you."
- Settle is a first-class verb ("done for now"), distinct from archive; settled threads collapse into "Settled 100 ⌄", 10 rows then "Show 25 more". Auto-settle on merged PRs and inactivity.
- The project is metadata: an initials badge with an auto colour ("DS" red, "FE" blue) and a filter in the sidebar header.
- Top bar: project badge, "project / Thread title" breadcrumb (title auto-derived from the first prompt, doubles as the thread menu), three 28px panel toggles at the far right.
- Back and forward arrows sit next to the wordmark, mirrored by ⌘[ ⌘].
- Settings and Usage open as large sheets over the thread; closing restores scroll and state.

**Placement** ([shell-and-navigation.md](shell-and-navigation.md) §2)
- Composer bottom row: paperclip far left, then model chip ("✳ Opus 5.5 Medium", effort word muted), permission chip only when non-default, 32px round send far right.
- Send button states: disabled grey (fg 12%), blue with text (hover scale 1.05), red round stop while running with an empty draft, steer arrow while running with text ("Click to steer, ⌘-click or ⌘↵ to queue"), queue, resume, update ✓, compact-and-send, "Submit answer", "Implement".
- Context strip under the composer (12px, fg 70%, 24px controls): "Current checkout" or new worktree, branch, permissions. Shown only before the first turn.
- Empty state: "What should we build in **project**?" with the project name as a combobox, and a muted "or start without a project".
- Sidebar search row: Search, then 28px project filter, add project and new thread. New-thread tooltip "New thread (⇧⌘O)" plus "New thread in current project: Shift+click".
- Footer bottom-left: Settings, Pull requests, Usage as 32px icons. Bottom-right: a status button only when relevant ("Update 1 provider").
- Row hover: the relative time fades out over 150ms and "Un-settle" takes its spot; the greyscale badge regains colour. Active cards swap status for snooze and "✓ Settle".
- Approvals show only Decline and Approve; Cancel and "Always allow this session" sit in More. The composer placeholder flips to "Send feedback to decline this request".
- Destructive dialog: "Close terminal "Terminal 1"?" / "This stops the running process and clears its history." Cancel (outline) then red Confirm, Cancel focused.
- New project name field carries an inline "Create ⏎" and a live "Goes in <path>" preview.

**Menus** ([shell-and-navigation.md](shell-and-navigation.md) §3)
- ⌘K: 576px, radius 16, glass, 200ms enter, height morphs between pages. 27 actions then 12 recent threads. Footer legend changes per page. `>` filters to actions; Backspace on empty pops a level.
- Model picker: provider rail, list with search and ⌘1-4 chips, reasoning column (Low / Medium / High / Extra High / Max / Ultracode), "Standard | ⚡ Fast" footer.
- Permissions: 4-step slider (lock / pencil / sparkle / crossed shield) with the selected mode's consequence below and hover preview of other steps.
- `/`, `$`, `@`, `#` menus dock to the composer top as an attached tray.
- Right panel "+" menu: Browser B › · Terminal T · Files F · Diff D · Pull request P · Linked pull requests L · Device M · Side chat S, with single-letter accelerators.
- Menus and selects open instantly; popovers and tooltips fade and scale.
- PR merge, close and revert: two-click confirm in the menu, disarms after 3s.

**Layout and density** ([constants.md](constants.md))
- Sidebar 256 (min 208), top bar 52, gutter 12 (wide 20), lane 46rem, details card 280, palette 576.
- Active cards 78px (3 lines); settled rows 36px with a greyscale badge at 40%.
- Opening the right panel splits the main area; at 840px it overlays and tabs get scroll arrows.
- Text: 12px dominant chrome (859 uses), 14px body (413), 11 and 10px counters.

**Type and colour**
- SF first, then Inter Variable. Weights 500 and 600, never bold except the wordmark ("**T3** Code"). Hero light 400 at 30/36, -0.75px.
- Assistant prose 14px, line height 1.625, 90% ink, no bubble. User bubble `#ebebed` / `#1e1e1e`, radius 16, padding 12, max 80% width.
- One accent at hue 264. Selection is foreground 6-9%. Button mix: outline 33%, ghost 38%, filled primary about 17%.
- Light mode is "paper on a rail": canvas `#fcfcfc`, sidebar `#fafafa`, hover `#f4f4f5`, white cards; the current sidebar row is the white one.
- Dark mode is true black with `#111` raised surfaces and white-alpha borders (8%).
- A contrast slider (50-200%) scales inks without touching surfaces; generated themes solve text to 7:1.
- Lint bans em dashes in UI copy and native `title` tooltips.

**Motion** ([constants.md](constants.md) Motion)
- Layout animation ships at 0ms ("Zero avoids per-frame layout work"), tunable 0-400ms.
- Popovers 150ms, dialogs 200ms `cubic-bezier(.4,0,.2,1)`, press .97, hover backgrounds instant, menus instant.
- "Departing content cuts." Where both directions animate: exit 100ms, enter 150ms after 50ms. Fading content is frozen first.
- Indicators stepped and duty-cycled (skeleton 2.4s, pulse 2s `steps(6)`, shimmer 2.2s `steps(30)`), paused off-screen and in hidden tabs.
- Toasts, completion sound and OS notifications are off by default; thread-scoped toasts render only while their thread is open.
- Wait ladder: 400ms, 2s, 15s, 20s.

**AI patterns** (`ai-interaction-patterns`)
- Turn anatomy: user bubble, "Worked for 18m 3s ›" receipt, a summary sentence with counts, typed one-line rows (brain for reasoning, `>_` for commands with "No output." in italic mono, eye for reads, pencil for edits with Open diff, speech bubble for approvals), assistant prose, end line "◷ Settled 13m ago · Un-settle".
- Running: "Working for 7s" on a shared wall-clock second; a "Thinking" row with one shimmer band; labels change tense on completion; failed or stopped turns never fold; text streams in finished blocks (600ms fade per block).
- Permission modes as plain consequences: Supervised "Ask before commands and file changes." / Auto-accept edits / Auto "Supported providers approve routine actions; others still ask." / Full access "Allow commands and edits without prompts." Default is Full access: trust from inspectability, not friction.
- Steer is the default follow-up; ⌘Enter queues. Queued messages are editable (⌥↑).
- Undo is turn plus git checkpoint: "Edit from here" with "Revert files too" or "Revert and keep changes". Any response can be forked. No regenerate, no per-hunk accept.
- Diff is first class: scoped by "Tool call ▾" (this call / turn / thread), stacked or split, wrap, whitespace, file tree, a "Changes +3 −1" row in the details card.
- Status vocabulary: Working, Waiting, Approval, Input, Request, Limited, Failed, Woke, Done. Priority approval > input > request > ready. Working rows recede to 70%.
- Usage: bars with a pace marker, hatched remaining portion, reset countdown "↻ 1d 1h"; cost and tokens kept out of the chat.
- Agent tools (terminal, browser, files) are the human's tools too, in the same panel.
- Prompt aids: ↑ recalls, ⌘S stashes, pastes of 32 KiB or more become an attachment.

**States** ([states-copy-safety.md](states-copy-safety.md))
- Empty: a question plus the composer, no chips; lists get one muted line.
- Skeletons shaped like the final rows with a label. Busy buttons say "Importing…" without a spinner.
- Errors carry the fix in code style; disabled items say how to enable them.

**Onboarding** ([shell-and-navigation.md](shell-and-navigation.md) §6)
- Glass dialog over the blurred real app, three steps, filled checks, height morph.
- Agents detected; projects scanned from existing history with the most recent pre-checked; rows show name, muted mono path, provider icons, conversation count and age. "Import 1 project"; Skip is a muted ghost.

**Settings** ([shell-and-navigation.md](shell-and-navigation.md) §5)
- Large sheet, searchable nav, grouped. Row = title + consequence sentence + control. Visual pickers for scheme, theme and font. "10 of 12 on" summaries. Labs and "(legacy)" labels. Icon rail and stacked rows on phones.

## Keyboard map (core defaults)

| Chord | Command |
|---|---|
| ⌘K | Command palette (not in terminal) |
| ⌘P / ⇧⌘F | Go to file / search contents |
| ⌘N, ⇧⌘O | New thread (⌘N is new terminal inside a terminal) |
| ⇧⌘N / ⌥⌘N | New thread in current project / without a project |
| ⌘B | Toggle sidebar (yields to Bold when text is selected in an editor) |
| ⌥⌘B / ⇧⌘B | Toggle right panel / thread details |
| ⌘J | Toggle terminal drawer |
| ⌘T / ⌘W / ⇧⌘T | Panel tab new / close / reopen; ⌘W never closes the window |
| ⌘D | Toggle diff (split terminal when the terminal has focus) |
| ⌘[ / ⌘] and ⇧⌘[ / ⇧⌘] | Back / forward; previous / next thread |
| ⌘1-9 | Jump to Nth thread (Nth model when the picker is open) |
| ⇧⌘S / ⇧⌘P | Settle and advance / pin |
| ⌘Z | Undo the last list action |
| ⇧⌘M / ⇧⌘E / ⇧⌘A | Model / effort / permissions pickers |
| Enter / ⇧Enter / ⌘Enter | Send / newline / opposite follow-up (queue vs steer) |
| ↑ / ⌘S | Recall previous prompt / stash prompt |
| ⌘U | Usage (then C/T/L for metric) |
| F6 / ⇧F6 | Cycle workspace areas |
| ⌘Q | Quit: hold 1.2s or double-press within 500ms |
| Esc | Innermost layer first; does not stop the agent |

## Its website applies the same thesis

The marketing site reuses the app's tokens (true black, white-alpha borders, the hue-264 accent, the same font stack and radii). The hero is a balanced three-line headline (`clamp(38px, 5.6vw, 76px)`, max 20ch), one sentence, one primary CTA that detects the platform ("Download for macOS"), one quiet text link ("Steal our code (legally) ↗"), then a full product screenshot framed only by a 1px ring at radius 12. Entrance is one staggered rise (0.7s `cubic-bezier(.2,.7,.2,1)` from 16px, delays 0 / 90 / 180 / 300 / 400 / 520ms). Ambient motion (logo parallax for fine pointers only, testimonial marquees at 76s per loop) plays only when visible and stops under reduced motion. The app's voice is literal; the site's is cheeky. See `website-design`.

## Do not copy

- Mixed tooltip formats ("Label (⌘B)" and "Label · ⇧⌘H"). Pick one.
- Copy drift: "…" vs "...", "Could not" vs "Failed to", "12.3k" vs "12.3K", Title Case stragglers ("Recent Threads"), one concept named environment, machine or computer depending on the screen.
- No default stop chord, and Esc does not interrupt the agent. Bind Esc or ⌘. to stop when the input is empty.
- Native context menus cannot show shortcuts, so pin, settle and find are never taught there.
- No cheat sheet; keybinding conflicts warn but never block.
- Esc from a directly opened sub-palette returns to the root instead of closing.
- Provider-generated banner strings slip past the no-em-dash rule.
- Approvals gave no per-click pending feedback while a provider check was slow, so Approve looked stuck. Show a pending state on the clicked decision.
