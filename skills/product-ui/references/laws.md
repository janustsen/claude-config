# The laws

The thesis, then 24 laws. Each law held in at least four of the studied products, usually with measured values. Each gives the rule, the reason, the evidence and the anti-pattern. An agent that obeys these on a blank page already produces something that reads as designed.

Law IDs are stable (other files cite them), so they are grouped by theme rather than numbered in order.

Provenance tags: **[obs]** observed live in the running product, **[src]** read from the product's source code, **[doc]** vendor docs or changelog, **[know]** prior product knowledge not re-verified.

## The thesis behind them

T3 Code states its intent in its own repository, and those sentences explain almost every pixel. They generalise to any tool people use all day.

| Stated intent | What it produces |
|---|---|
| "A minimal GUI for coding agents" | A chat-first shell. Everything else sits in collapsible sidecars. |
| "Software that feels obvious … the smallest model that makes the correct behavior unsurprising" | Few modes. Defaults hidden. One noun per concept. |
| "Reverse states. If you added a way in, add the way out and the way to see it." | Every lifecycle verb has an inverse, plus a 5s ⌘Z undo. |
| "Our users … notice a dropped frame, a lying spinner, and a stale label. No continuously repainting animations." | Stepped, duty-cycled indicators. Status written as text with a timer. Layout animation off. |
| "UI primitives own their look: pick a variant or size, never restyle." | Perfectly consistent controls, enforced by a lint rule. |
| "Action names agree across label, tooltip, menu and accessible name." | "Copy prompt link", not "Copy". Each label names its real target. |

Four tests follow, and every element must pass them: is it needed now, does it differ from the default, is this where the decision is made, does it need a human.

---

## Colour, ink and type

### L1. Chrome recedes; colour means state
- **Rule.** Build all chrome from one neutral ink. Spend saturated colour only on meaning: state, live, error, links and trust, the active mode, the one primary action. The user's content must be the most colourful thing on screen.
- **Why.** Colour is the fastest pre-attentive channel, and it stays an alarm only if it never decorates. When the content is the payoff (a generated app, an image, a document), chrome that competes with it lowers perceived quality.
- **Evidence.** T3 Code puts its one accent on about 1 in 6 buttons, checked controls, sliders and focus, never on selection [src]. Linear dimmed its sidebar "a few notches so main content takes precedence" [doc]. v0 is monochrome and turns blue only when Design mode is on [obs]. Perplexity keeps its teal off primary buttons, which are near-black [obs]. Cursor's orange appears only on text links [obs].
- **Anti-pattern.** Brand colour on every button, coloured section headers, gradient chrome.

### L2. Every neutral is an alpha of one tinted ink
- **Rule.** Define one ink (a warm, cool or brand-tinted near-black) and one paper. Text roles are ink at fixed alphas. Borders are ink at 2.5-10%. Draw a border as a 1px alpha ring inside the shadow stack, so border and shadow never double up.
- **Why.** Alpha neutrals harmonise on any surface (cards, previews, images) and give dark-mode parity for free. A single tinted ink is what makes a palette feel authored rather than default grey.
- **Evidence.** Cursor: ink `#26251e` on `#f7f7f4`, text at 100/92/60/50/40%, border 2.5% [obs]. Perplexity: every grey is an alpha of teal ink `#0b2833` [obs]. Notion: neutrals on `rgba(42,28,0,x)` [obs]. Dia: `color-mix(in srgb, CanvasText 60%, page)` [obs]. v0: `--shadow-sm: 0 0 0 1px alpha-300, 0 2px 1px #0000000a` [obs].
- **Anti-pattern.** Hand-picked hex greys per component; `border: 1px solid #ddd` next to a separate box-shadow; pure black text on pure white.

### L3. Four text roles, and body text is never pure black or white
- **Rule.** Exactly four text roles: primary (titles), secondary (body, labels), tertiary (meta, descriptions), quaternary (timestamps, placeholders, icons). Icons sit one tier below their label. In-app body text sits at about 85-90% contrast, not 100%.
- **Why.** A predictable ladder keeps dense screens readable for hours and gives hierarchy without adding size or weight.
- **Evidence.** Linear dark: `#f7f8f8` / `#d0d6e0` / `#8a8f98` / `#62666d`, with the brightest reserved for marketing [obs]. v0: `#171717` / `rgb(77,77,77)` / `#8f8f8f` / `#c9c9c9` [obs]. T3 Code sets assistant prose at 90% ink [src].
- **Anti-pattern.** Five ad-hoc greys, or one grey for everything secondary.

### L4. The primary output is a document; only the human's input is boxed
- **Rule.** Render long output (the AI's answer, the document, the record body) as plain, left-aligned, reading-tuned prose in a 680-768px measure with no bubble and no avatar. Box only the user's input (a soft grey bubble or a bordered card). When output is generated, give it its own typographic voice: a reading serif or distinct style for generated narrative, a sans for UI and data, mono for codes and IDs.
- **Why.** The answer is the artifact and the question is its label. Bubbles around long text cut the measure and frame a document as chat. A distinct voice lets readers tell "the model wrote this" from "this was measured" without a label.
- **Evidence.** T3 Code: 14px prose at 90% ink, user bubble `#ebebed` radius 16 at 80% max width [src]. ChatGPT: answer unboxed in a 768px column at 16/26 [obs]. Claude: answers in `--font-voice` serif in a 720px column [obs]. Perplexity: serif answers 16/26 on 720px, sans UI, mono tickers [obs]. Daydream: Plantin serif for the AI's voice, sans for product data [obs].
- **Anti-pattern.** Symmetric left and right bubbles (SMS style) in a tool whose answers are long. A serif on buttons or labels.

## Attention and structure

### L17. "Needs me" is the top-level grouping, and the order is stable
- **Rule.** Once more than one thing is in flight, make "needs your input / ready for review" the first section, the loudest badge and the default view. Sort the rest by attention state (in progress, then done). Never reorder rows on background activity; move an item only when it needs the user. When a returning user lands, answer "what changed since last time, and what needs me" with section counts and new-item dots, needs-action kept apart from FYI, not with a sentence restating those counts. Badge only where action is pending.
- **Why.** In an agent product compute is cheap and human review is the bottleneck. A list organised by what needs the user becomes a clearable queue. Stable order protects spatial memory.
- **Evidence.** T3 Code's sidebar is one cross-project inbox with Pinned / Active / Working / Snoozed / Settled shelves; "They return to the top of the inbox when they need you" [obs, src]. Cursor's Agents Window opens on "READY FOR REVIEW 5" [obs]. Linear's inbox badges only pending action [doc]. checklist.design's dashboard rule: the first screen is what changed since the last visit [doc].
- **Anti-pattern.** A project tree as the main navigation of an agent tool. A greeting headline ("Good morning, Sam"), or a summary sentence ("Since yesterday: 4 need you, 11 done") restating the section counts below it. Counts on every nav item.

### L21. Controls live at the point of decision
- **Rule.** Every control that configures the next action sits on the input that triggers it (model, effort, mode, permission, attach on the composer). Context choices (workspace, branch, target, recipient) sit in a strip directly under the input and disappear once the choice is locked. Inline actions sit next to the content they act on. Rare global destinations go to the bottom-left corner as icon buttons with tooltips; transient status goes bottom-right and appears only when relevant.
- **Why.** The user never travels to configure the next action. A choice that can no longer change leaves the screen instead of sitting there disabled.
- **Evidence.** T3 Code's context strip shows only before the first turn; once a run starts it disappears and the permission chip moves into the composer row [obs]. "Open diff" sits on the edited file row; Approve sits on the exact action row [obs]. The project switcher is inside the empty-state question: "What should we build in **project**?" [obs].
- **Anti-pattern.** A settings page for per-message options. A toolbar of actions far from the item they affect.

### L22. Density follows urgency
- **Rule.** Make row height a function of urgency: a rich three-line card for items that need action, a one-line row for done items, a collapsed shelf with a count for archives. Background work recedes (about 70% opacity); needs-you items never recede.
- **Why.** A power tool shows a lot, so information is compressed by relevance rather than uniformly.
- **Evidence.** T3 Code: active cards 78px (badge, name, status / title / branch, provider, PR), settled rows 36px with a greyscale badge at 40%, "Settled 100 ⌄" shelf with 10 rows and "Show 25 more" [obs, src].
- **Anti-pattern.** Every row the same height regardless of whether it needs anything.

### L23. Defaults are invisible, and one control morphs instead of multiplying
- **Rule.** Show a control only when its value differs from the user's default. Keep one primary action in one fixed position and change its glyph and label with state. Use split buttons for one frequent action plus alternatives; choosing an alternative makes it the new default. A split button's label follows the object's state.
- **Why.** The eye never moves to find the primary action, and the screen shows only decisions the user actually made.
- **Evidence.** T3 Code's send button is disabled, then send, then stop, steer, queue, resume, update and "Implement" in one 32px slot [src]. Its permission chip appears only when it differs from the default [obs]. "Commit & push" becomes "Publish repository" with no remote, or "Commit" with only local changes [obs]. ChatGPT's one 44px slot goes Voice, Send, Stop and "never moves" [obs].
- **Exception.** For runs that last hours, give Stop its own place: a mis-click on a morphing button can destroy hours of work (Cursor) [doc].
- **Anti-pattern.** A row of five buttons where one would do; a disabled control for a choice the user can no longer make.

### L24. Every way in has a way out; undo beats confirm
- **Rule.** Every lifecycle verb has an inverse (pin/unpin, settle/un-settle, snooze/wake, archive/unarchive). Every reversible action gets a 5s inline undo bound to ⌘Z, and no confirmation. Confirm only what is irreversible: destructive items come last, in red, behind a separator; the dialog title is a question naming the object, the body states the consequence, and focus starts on Cancel. Remote irreversible actions (merge, close, publish) get an in-place arm-then-confirm that disarms after 3s.
- **Why.** People experiment only when going back is free. Confirmation on everything trains rubber-stamping; confirmation on nothing destroys trust in one incident.
- **Evidence.** T3 Code: "Archived 1 thread, ⌘Z to undo" inline for 5s; delete confirms by default, archive and unpin do not; "Close terminal "Terminal 1"?" / "This stops the running process and clears its history." with Cancel focused [obs, src]. Linear: undo over confirm, 30-day archive [doc].
- **Anti-pattern.** "Are you sure?" on archive. Enter on a destructive dialog that destroys.

### L11. New capability lives on existing objects, at the scale of the task
- **Rule.** Attach every AI or power-feature entry point to an object the user already has (a selection, row, page, record, meeting, issue). Offer it at three distances: at the cursor or selection for line-level work, at the object as a corner button or side panel, at the workspace as a destination or command. Output lands as the app's native objects.
- **Why.** A free-floating "AI tab" competes with the work and forces the user to carry context. Native output can be edited, moved and owned with tools the user already knows.
- **Evidence.** Notion's cursor / page / workspace distances [doc]. Linear puts agents in the assignee menu and the activity feed [obs]. Dia: selection verbs, Ask on Page (⌘E), chats as sidebar items [obs]. Perplexity's page-scoped composer "Ask anything about NVIDIA Corporation" [obs].

## Output, progress and trust

### L5. Progress is one live line, then a receipt
- **Rule.** While working, show one status line: a verb plus an elapsed counter ("Working 3s"). Finished steps freeze into one-line, past-tense rows ("Read about.md", "Ran 3 commands"). When the turn ends, collapse everything into one disclosure ("Worked for 1m 8s ›") with steps, counts and cost inside. Keep the result outside the collapse.
- **Why.** Users want proof of work, not the work. One moving thing says exactly where the system is; a rising number says it is not stuck.
- **Evidence.** T3 Code "Worked for 18m 3s ›" then "Ran 2 commands, changed 2 files, and performed 3 other actions" [obs]. Cursor "Worked for 14m 22s" [obs]. v0 "Worked for 1m 8s" with "used 0.224 credits" inside [obs]. Perplexity "Working 1s, 2s…" then "Finished 5s ⌄" [obs]. Claude: one counted line per burst, then a step timeline, then the raw command [obs].
- **Anti-pattern.** A bare spinner; a wall of streaming logs; a fake progress bar. Looking busy without progress is a bug (Linear) [doc].

### L6. Shimmer the words, not the box; motion means live
- **Rule.** Animate in-progress status as a sweep across the label text (`background-clip: text`), 0.65-2.4s, synced to one clock across the screen. Everything else is still. Under reduced motion the label becomes static text at about 70% ink.
- **Why.** The label stays readable while the motion says "alive". Motion anywhere else would destroy the signal, and out-of-phase shimmers read as noise.
- **Evidence.** Cursor `shimmer-synced` 1.6s; Perplexity 1.2s; v0 650ms; Linear 2.4s; T3 Code 2.2s `steps(30)` paused off-screen [obs, src].

### L7. Provenance is one gesture away from every generated claim
- **Rule.** Every generated claim carries a quiet source marker (a mono host chip, a numbered circle, a hover magnifier). It opens a card after about 250-300ms hover, or on click, naming the source, why it is trusted, and linking to the exact passage.
- **Why.** Users act only on output they can verify. A readable host name builds more trust than a superscript number.
- **Evidence.** Perplexity: mono 10px chip, 7% fill, 6px radius, hover card at about 280ms with the trust class and reason [obs]. Notion: 18px numbered circle, click jumps to the transcript line [obs]. Granola: hover a bullet, a magnifier opens the reasoning and a quote [doc].

### L8. Proposals look different from accepted truth
- **Rule.** One visual grammar for "proposed, not yet yours": a dashed outline, a grey ink or a pending state, consistent across the app. Accepting makes it solid and ordinary.
- **Why.** Trust needs the user to know at a glance what they decided versus what the machine suggested.
- **Evidence.** Linear: dashed chip suggested, solid applied [obs]. Granola: human ink `#292929`, AI ink `#72726E`, same font and size [obs]. v0 Design mode holds edits as pending until Apply [obs].

### L9. Approval is proportional to rollback cost
- **Rule.** If undo is cheap (local edits, versions, checkpoints), apply first and review after, with undo per item, per file and per turn. If undo is expensive or impossible (send, pay, post, deploy, write to another system), require an explicit confirmation whose button names the consequence ("Send to Alex", "Buy all · 3 items, $345").
- **Why.** Pre-approving cheap steps makes users rubber-stamp; auto-running irreversible ones destroys trust in a single incident.
- **Evidence.** Cursor Keep/Undo per hunk, file and checkpoint [doc]. Notion "Write actions (like sending) will ask you to confirm" [doc]. Daydream's purchase approval is single-use, lasts 30 minutes and is voided by any change to the total [doc].

### L10. Never destroy the original or the history
- **Rule.** Restore appends a new version. Generated changes never overwrite the human's raw input; keep both behind a two-state toggle. Separate "restore the files" from "rewrite the conversation". Log generated edits under a named author.
- **Why.** People experiment only when nothing is lost, and "who changed this?" must have an answer for agents as much as for people.
- **Evidence.** v0 "Restoring an old version creates a new, most recent version" [doc]. Granola "My notes / Enhanced" toggle [obs]. T3 Code "Edit from here" offers "Revert files too" or "Revert and keep changes" [src].

### L14. Reserve the output's space before it exists
- **Rule.** As soon as output is coming, render a placeholder with its final footprint (a shimmering card, a blur-to-sharp tile in its slot, the new turn scrolled to the top with space below).
- **Why.** Layout stability reads as competence; jumps read as bugs and lose the reader's place.
- **Evidence.** v0's "Creating artifact… / Your artifact will appear here." card with a 1500ms sweep [obs]; Midjourney blur-to-sharp [doc]; Perplexity anchors the new turn to the top [obs].

### L15. Cost, limits and context are ambient meters, never surprises
- **Rule.** Show cost at the moment of choice in the plan's own unit, and per-run cost in that run's receipt. Show usage as a small persistent meter with a click-through breakdown. At a limit, disable only the costly control, explain it on that control, and offer a cheaper path next to "buy more".
- **Why.** Hidden meters produce bill shock and "it forgot". A visible ceiling sells upgrades without nagging.
- **Evidence.** Krea: a unit price on every model card [obs]. Cursor: a context ring and a cheaper-model escape [doc]. T3 Code: usage bars with a pace marker and a reset countdown, kept out of the chat [obs].

### L16. Every blocked or failed state names the cause and the next action
- **Rule.** Say what happened, why, and what to do: "Approval required · Approve", "Sign in to share", "Codex CLI is not authenticated. Run `codex login` and try again." Never a bare "Unauthorized" or "Something went wrong". Fail per item, with one Retry where the failure happened.
- **Why.** The next action depends on the cause, and a raw error makes the product look broken exactly when trust is decided.
- **Evidence.** T3 Code [obs]; Cursor changed "Couldn't start" to "Approval required / Approval denied" [doc]; v0's bare "Unauthorized" is the counter-example [obs].

## Input and keyboard

### L12. One composer, with a morphing primary slot and small pills for expensive choices
- **Rule.** The primary input is a large rounded container (outer radius = inner radius + padding). Its primary slot morphs: idle, send when there is text, stop while running. Mode or autonomy and model sit as small pills inside it, cyclable from the keyboard. Attachments sit behind one control. While a run is going the input stays usable: queue, steer and stop are separate intents. The placeholder teaches syntax and names the current scope.
- **Why.** The hand learns one place. Autonomy and model decide cost, speed and risk, so they must be visible and cheap to change.
- **Evidence.** T3 Code: "Ask anything. @ files, $ skills, / commands" [obs]. Perplexity: 26px frame around a 20px field with 6px padding [obs]. ChatGPT: 768x52 pill, radius 28, turning into a card when text wraps [obs]. Cursor: mode pill on Shift+Tab, model pill on ⌘/ [doc].

### L18. Every verb has a key; ⌘K does everything; menus teach the keys
- **Rule.** Ship a command palette that runs every action, scoped to the current selection, with type prefixes. Show each shortcut right-aligned in every menu row and tooltip. Store shortcuts as data and render every label from that table. Give the main objects one-key verbs on hover or selection.
- **Why.** A keyboard-first surface lets the visible UI stay quiet, and menus that show shortcuts turn every use into a lesson.
- **Evidence.** T3 Code: 86 default rules in one table driving matching, tooltips, menus, palette rows and the settings page [src]. Linear: C, A, I, S, L, P, ⌘K with prefixes, G-chords [doc].

## Motion and onboarding

### L19. Motion: instant for frequent, short for occasional, nothing loops
- **Rule.** Hover backgrounds instant on, 100-150ms off. Menus, selects and keyboard-driven highlights instant. Popovers, hover cards and tooltips 100-180ms opacity plus scale from .95-.98. Dialogs and sheets 200ms. Structural reshapes (panels, the composer's attached tray) 200-250ms, or off by default. Press `scale(.97)`. Animate in, cut out (or exit in about half the entrance). No continuous animation except stepped, duty-cycled status indicators paused off-screen.
- **Why.** Tools used all day must feel instant without teleporting. Layout animation costs frames in lists that constantly re-render; opacity and scale cost only compositing. Motion exists to show where something came from.
- **Evidence.** T3 Code ships layout animation at 0ms ("Zero avoids per-frame layout work") [src]. Linear `--speed-highlightFadeIn: 0s`, `FadeOut: .15s` [obs]. Perplexity pops 150ms `cubic-bezier(.16,1,.3,1)` from .95 [obs]. Claude press `scale(.975)` in 60ms with a spring release [obs].

### L13. Reach the "aha" before the wall
- **Rule.** Let new users run the real thing at least once. Put the wall at the moment of spending real compute or persisting or sharing. Preserve whatever they typed through the wall. Escalate gently, keep locked value visible behind a blur, never re-wall content already received. Onboard over the real product (blurred behind a dialog), detect and pre-select instead of asking, and end in a working state rather than a tour.
- **Why.** The result is the pitch, and typed work is the strongest reason to sign up.
- **Evidence.** v0 runs real logged-out generations [obs]. Krea's Realtime needs no account and its wall keeps the prompt [obs]. T3 Code's onboarding is a glass dialog over the real app with the most recent project pre-checked and "Import 1 project" [obs]. Doctronic asks for consent after the first answer [obs].

### L20. Empty states teach by being minimal
- **Rule.** For a tool people return to, the empty state is a question plus the primary input ("What should we build in **project**?") or one muted line for a list ("No archived threads"). For a first-run consumer or creative product, show real outputs as one-click examples that fill the input (never auto-send). An empty property is a verb ("Set priority"). Put the fix inside the empty state ("Edit filters").
- **Why.** Blank canvases paralyse, but fake suggestions and illustrations add noise for experts. Filling instead of sending keeps control with the user.
- **Evidence.** T3 Code has no suggestion chips or templates [obs]. ChatGPT "Where should we begin?" with one chip [obs]. v0 chips fill the composer [obs]. Linear "Set priority" [doc].
