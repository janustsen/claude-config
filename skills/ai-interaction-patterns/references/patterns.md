# AI pattern library

Each pattern: anatomy (the best observed version), states, when to use it, and where it comes from. Values are measured unless tagged: **[obs]** live, **[src]** source code, **[doc]** vendor docs, **[know]** prior knowledge not re-verified.

## Input

### Morphing composer slot
- **Anatomy.** One 32-44px circular button at the composer's bottom-right. Its glyph and label change; its position never does.
- **States.** Idle (voice, or disabled at about 50% / fg 12%) → has text (send, accent fill, hover scale 1.05) → running with empty draft (stop, a red round square) → running with text (steer) → queued (queue icon) → paused (resume ▶) → editing a queued message (update ✓) → plan ready ("Implement" pill) → agent asked a question ("Submit answer").
- **Use.** Every AI input. For runs that last hours, give Stop its own fixed place instead, because a mis-click on a morphing button can destroy hours of work.
- **Seen in.** T3 Code [src], ChatGPT (44px, "never moves") [obs], Perplexity, v0, Claude.

### Composer pills
- **Anatomy.** Small pills inside the composer's bottom row: mode or autonomy, model, effort. Each opens a menu; each cycles from the keyboard (Shift+Tab mode, ⌘/ model). A non-default value is tinted in its mode's colour (Plan in amber). The effort word is muted next to the model name ("Opus 5.5 Medium"). A pill appears only when its value differs from the default.
- **Use.** Whenever users trade cost, speed or risk per turn. Label capability by outcome (Instant, Medium, High, Extra High, Auto) rather than model IDs, and offer Auto so most people never choose.
- **Seen in.** Cursor [doc], T3 Code [obs], Claude [doc], ChatGPT [doc].

### Attached tray ("chin")
- **Anatomy.** A menu that docks to the composer's top or bottom edge and squares the shared corners. A list on the left, a live preview or description pane on the right. One line per item: trigger word at 500, truncated muted description, bottom-edge fade. Opens with a 250ms reshape.
- **Use.** `/` commands, `@` references, `$` skills, sources, modes that need explanation.
- **Seen in.** Perplexity [obs], T3 Code [obs].

### Scoped composer
- **Anatomy.** The same composer on every object page, with a placeholder naming the object ("Ask anything about NVIDIA Corporation", "Ask about Acme Corp"). Navigating (entity search) sits at the top; asking docks at the bottom.
- **Use.** Every detail page in an AI product.
- **Seen in.** Perplexity [obs].

### Context chips and the send manifest
- **Anatomy.** The obvious context (current tab, selection, open file) attaches by default as a visible, removable chip. `@` picks become an inline token in the sentence and a chip in the manifest above the input. Each sent message keeps a compact, expandable stack of what it was based on ("SEE ALL ↖").
- **Use.** Any AI that reads context the user did not type. Keep the active constraint set visible and removable across turns, because multi-turn context drifts silently.
- **Seen in.** Dia, Comet, Atlas [obs]; Daydream silently dropped a constraint (negative) [obs].

### Composer as form
- **Anatomy.** When the AI needs structured data, the composer turns into a typed form for that one answer: fields, "Not sure" always offered, a "?" saying why it is asked. The answer is echoed back as a sentence under a "1 question answered" divider.
- **Use.** Intake, triage, configuration inside a conversation.
- **Seen in.** Doctronic [obs].

### Steer, queue, stop
- **Anatomy.** While a run is going, the input stays usable. Default follow-up is steer (delivered at the next safe boundary); ⌘Enter does the opposite (queue to send after). Queued messages are editable (⌥↑) and the first can be sent as a steer (⇧⌘Enter). Stop is separate. Say it in the placeholder: "you can keep typing", "⌥↵ to queue".
- **Seen in.** T3 Code [src], Cursor [doc], v0 [obs].

### Saved prompts that expand
- **Anatomy.** A `/` shortcut fills the input with its prompt, mode, model and source, and the user can edit before sending. It never executes blindly.
- **Seen in.** Comet, Dia skills [doc].

### Intent survives the gate
- **Anatomy.** Any action that hits sign-in or a limit carries the request through (`?next=`, `returnTo=`) and resumes it after; the typed prompt is preserved.
- **Seen in.** ChatGPT plugin links [obs], Krea's Generate wall keeps the prompt [obs].

### Mode marks the frame
- **Anatomy.** Agent, research, incognito and temporary modes change the composer frame itself (a border, a label, a glow), and the placeholder changes ("Temporary chat"), so the mode is visible at the moment of typing, not only inside a closed menu.
- **Seen in.** Claude incognito [obs], ChatGPT temporary chat [doc].

## Progress

### Status line with timer
- **Anatomy.** A verb plus an elapsed counter on one line: "Working for 7s", ticking on a shared wall-clock second. The verb shimmers. Labels change tense on completion ("Running → Ran", "Thinking → Thought", "Working 5s → Finished 5s"). Under reduced motion, static text at 70% ink.
- **States.** Working / finished (collapsible) / error (by cause) / stopped.
- **Use.** Any wait over about 1s.
- **Seen in.** T3 Code [obs], Perplexity [obs], Beautiful UI ("Thought for 4 seconds") [obs].

### Synced shimmer
- **Anatomy.** A gradient sweep across the label text (`background-clip: text`), 0.65-2.4s linear (or `steps(30)`), one clock for every working label on screen, paused off-screen, in hidden tabs and under reduced motion.
- **Seen in.** Cursor 1.6s, Perplexity 1.2s, v0 650ms, Linear 2.4s, T3 Code 2.2s [obs].

### Work ledger
- **Anatomy.** Three levels. One counted summary line per burst ("Ran 3 commands, created a file", hammer icon) → typed one-line rows with one icon per kind (brain: reasoning excerpt; `>_`: command; eye: read; pencil: file edit; speech bubble: approval) in two tones (verb at 60% ink, object at 40%) → detail cards on expand (the syntax-highlighted command and its output, or "No output." in italic mono; the edited path with "Open diff"). Reasoning stays in the UI sans even when answers are serif.
- **Use.** Agents and tool use.
- **Seen in.** T3 Code [obs], Claude [obs], Cursor [obs], Dia (a rail: 16px marker, 6px dot, 2px line at 9% alpha) [obs].

### Turn receipt
- **Anatomy.** When a turn ends, everything collapses into one disclosure with a divider: "Worked for 18m 3s ›". Expanded: the summary sentence with counts, the steps, time and cost ("used 0.224 credits"). The answer and a files-changed card ("Edited 2 files +23 −24", Undo / Review) stay outside it. Failed or stopped turns never fold. A closing status line can carry the lifecycle ("◷ Settled 13m ago · Un-settle").
- **Seen in.** T3 Code [obs], v0 [obs], Cursor [obs], ChatGPT Codex [doc].

### Reserved output card
- **Anatomy.** A placeholder of the final size with a diagonal sweep (1500ms) and two lines: "Creating artifact… / Your artifact will appear here." Media: blurry-to-sharp in the final tile slot with a percentage. Text: the new turn scrolled to the top with empty space below; min-height on streaming answers.
- **Seen in.** v0 [obs], Midjourney [doc], Perplexity [obs].

### Agent state pill
- **Anatomy.** A closed vocabulary: Working (shimmer) / Waiting on you / Error (by cause) / Done. Show it as an icon and colour on the row; spell the word only where the list is not already sectioned by state, and never again in the detail header. Done means a completion the user has not seen yet. Priority: approval > input > request > ready. A failure that needs a human counts as needs-you; within needs-you, sort by consequence: failures that block other work, then approvals, then questions, then reviews. Working rows recede to 70% opacity; needs-you rows never fade. The agent sits under a human owner ("Sam └ Agent").
- **Seen in.** T3 Code [src], Linear [obs].

### Motion signature per agent state
- **Anatomy.** Each state gets its own low-amplitude motion: a looping trace while working (Dia: violet conic trace, 2.03s), a one-shot pop on arrival (0.75s), a stroke-draw on completion (0.42s) with overshoot only here. Finished items never loop.
- **Seen in.** Dia [obs].

### Tasks surface
- **Anatomy.** Background agents get a list grouped Running (Watching), Needs you, Done, Failed. Each row shows its current value and since when ("Now $640 · since today", "12 found · since Tue"). The empty state lists example asks labelled with what they will touch. Tasks that need input pause rather than fail.
- **Seen in.** Daydream My tasks [obs], ChatGPT tasks [doc], Dia [obs].

## Output

### Answer as document
- **Anatomy.** Assistant output unboxed, left-aligned, 15-16px at line height 1.6-1.75 in a 680-768px column (T3: 14px, 1.625, 90% ink in 736px). The user's turn is a soft bubble (radius 16-22, max 80% width) or a bordered card. Headings compressed (h1 at most 1.5x body).
- **Seen in.** ChatGPT, Claude, Perplexity, T3 Code, Dia [obs].

### Typed voice per speaker
- **Anatomy.** A role-named font token (`--font-voice`) for model prose, the UI sans for controls and the user's text, mono for metadata, IDs and codes. The assistant's text can be one size larger than the user's (Dia 15 vs 14).
- **Seen in.** Claude, Perplexity, Daydream, Dia [obs].

### Native components, not prose about them
- **Anatomy.** In shopping, the answer is a product grid with at most two sentences above it. In finance, a live quote or comparison widget inside the answer, rendered before any prose. In a work tool, rows and cards. Box only output that has a next step (a draft, code, a chart) as a typed card with its export actions top-right; leave conversational text unboxed. Documents get a near-square radius (about 3px) so they read as paper.
- **Seen in.** Daydream, Perplexity Finance, ChatGPT, Dia [obs].

### Follow-up chips from the result set
- **Anatomy.** Each answer ends with the trade-off it noticed and 5-8 chips for the attribute that would narrow the results most, drawn from the actual results. "Like this, but…" refinement on any result (two presets plus free text), with the anchor item shown inside the user's next turn. Chips fill the composer; they do not auto-send.
- **Seen in.** Daydream [obs], v0 [obs].

### Stream order
- **Anatomy.** Sources first, then structured data, then prose (Perplexity: sources at 1.6s, widget at 1.4s, prose at 6.3s). Text in finished blocks fading in over 600ms, or words at about 60ms each with a steady caret. Never replay finished text on reopen. Never auto-scroll: stick to the bottom only while the user is within 24-40px of it; once they scroll up, stop following and show "Jump to latest" naming what waits below.
- **Seen in.** Perplexity [obs], T3 Code [src], vercel-labs/ui [src], ChatGPT [obs].

## Trust

### Citation chip and hover card
- **Anatomy.** A trailing mono 10px host chip (7% fill, 6px radius, "+N" for more) with a source-class icon. Hover after about 280ms (150ms scale-fade) opens a card: favicon and host, title, snippet, trust class with its reason ("Trusted · Government"), "Rate this source". The same sources appear three ways: inline chips, a sources pane (336px), a Links tab. On mobile, collapse provenance into one Sources chip that opens a sheet.
- **Seen in.** Perplexity [obs], ChatGPT [obs], Notion (18px numbered circles) [obs].

### Provenance magnifier
- **Anatomy.** Hover a generated line, a magnifier appears, click opens a popover with a small-caps label, one sentence of reasoning and a quoted excerpt from the source (a transcript, an email, a record). Click through jumps to the exact line.
- **Use.** Summaries of private sources (meetings, docs, CRM).
- **Seen in.** Granola [doc], Notion [obs].

### Evidence drill-down
- **Anatomy.** A summary paragraph → aspect chips with a sentiment icon and mention count → "30 positive / 24 negative" → verbatim quotes with the matched words in bold. Each level has a plain label saying where it came from. Evidence from people outranks the model's opinion.
- **Seen in.** Amazon review summaries [doc].

### Verbal uncertainty
- **Anatomy.** Ordered words instead of false-precision percentages: "Most likely", "Possible", "Less likely", with the serious possibility named honestly where it ranks. Evidence phrased in the user's own words under "Fits what you described" and "Doesn't quite fit".
- **Seen in.** Doctronic [obs].

### Number state and arithmetic
- **Anatomy.** Every number that is not live and final says what it is (closed, estimate, calculated) and "as of" when; a page-level frame says it once for all numbers below. Sums, filters and projections are computed by deterministic code; the model states the method and what it left out. Recommendations show the user's own maths behind an ⓘ ("Why 3%? Here's the math…"). Constraint failures are stated plainly with the nearest feasible value as a chip ("These aren't all under $15 · Under $500").
- **Seen in.** Perplexity Finance [obs], Cleo [doc], Daydream [obs].

### Honest limits of verification
- **Anatomy.** The AI states what it did not check ("I haven't tested it in a browser").
- **Seen in.** v0 [obs].

## Proposals and recovery

### Dashed suggestion chip
- **Anatomy.** A dashed-outline chip carrying the proposed value in the field it would fill (owner, label, project, linked record). Click or a number key accepts (it turns solid); another key declines; hover shows why ("same email domain as 3 earlier calls"). Per-field policy: show / auto-apply / hide. Bulk accept on a selection.
- **Seen in.** Linear Triage Intelligence [obs, doc].

### Two-ink authorship
- **Anatomy.** Human text in near-black (`#292929`), AI text in mid-grey (`#72726E`), same font, size and weight. Editing AI text makes it the user's. During generation a coloured write-head rides the frontier and settles to grey.
- **Use.** Documents where AI elaborates human input and the user must verify it.
- **Seen in.** Granola [obs].

### Proposal bar
- **Anatomy.** Under inline AI output: Keep / Discard / Try again, plus a follow-up instruction field. For multi-change passes, a "Suggest edits" step-through that walks proposals top to bottom; for code, Keep / Undo per hunk (⌘Return accept all, ⌘⇧Backspace reject all).
- **Seen in.** Notion [doc], Cursor [doc].

### Original / AI toggle
- **Anatomy.** A two-state segmented control ("My notes / Enhanced") top-right of the document. The raw input is never modified.
- **Seen in.** Granola [doc, obs].

### Append-only versions
- **Anatomy.** Each change is a version; restoring an old one creates a new latest version; staged edits wait for Apply; a before/after toggle.
- **Seen in.** v0 [doc, obs].

### Checkpoint rewind and fork
- **Anatomy.** "Edit from here" rewinds the conversation and offers "Revert files too" or "Revert and keep changes". Any response can be forked. Restoring files is separate from rewriting the conversation. Model or effort changes apply from the next response, and the UI says so; "Try again" and "try with a better model" are one intent at the answer.
- **Seen in.** T3 Code [src], Cursor [doc], Claude [know].

### Visible self-correction
- **Anatomy.** When the AI revises an earlier claim, it says so as an event in the next answer. Summaries that regenerate in place show that they changed (a "Updated just now" stamp, a diff toggle), never a silent rewrite while someone reads.
- **Seen in.** Perplexity corrected itself (good) but regenerated a market summary three times silently (bad) [obs].

### Explanation leads to correction
- **Anatomy.** Each source or memory used has "Relevant / Not relevant / Why this memory? / Make a correction". Each item card's ⋯ menu leads with feedback verbs ("Suggest less").
- **Seen in.** ChatGPT sources sheet [doc], Daydream [obs].

## Agency

### Inline approval at the action
- **Anatomy.** On the exact work-log row: "src/cart.js · ⚠ Waiting for approval · Decline · **Approve** · More". Only Decline and Approve visible; "Always allow this session" and Cancel in More. Approve is the one default-toned button. The composer placeholder becomes "Send feedback to decline this request". Approvals are held while the user typed in the last 1.5s. The clicked decision shows a pending state.
- **Seen in.** T3 Code [obs, src].

### Permission modes as consequences
- **Anatomy.** A stepped control (lock / pencil / sparkle / crossed shield) whose selected step shows its name and one sentence: "Ask before commands and file changes." / "Auto-approve edits, ask before other actions." / "Supported providers approve routine actions; others still ask." / "Allow commands and edits without prompts." Hover previews another step's sentence. About four named levels per action type: act without asking, act if pre-approved, ask first, hand off to you.
- **Seen in.** T3 Code [src], Cursor run modes [doc], ChatGPT [doc].

### Consequence-named commit
- **Anatomy.** The commit button names the effect and updates live: "Apply 3 changes" → "Apply 2 changes", "Send to Alex", "Schedule for Thu 9:00", "✦ Buy for me · $345". Yes and no get equal width in consent dialogs. Scope copy sits under the button only when the scope is not the default and the button cannot say it (a different sender, a wider audience, write access); never restate the button ("1 recipient").
- **Seen in.** Beautiful UI, Daydream, Atlas, Perplexity [obs].

### Single-use money approval
- **Anatomy.** An approval to spend covers one order, expires (30 minutes at most), and is voided by any change to the total. The screen states five things: the amount and recipients in the button, what voids the approval, how long it lasts, who handles returns, and where the result will be listed. Price drift tolerance is explicit (auto-OK up to +$15, asked again above). Rules set in a sentence ("buy when 30% off") are echoed back as a structured card with Cancel before going live. "Prepare" stays separate from "submit".
- **Seen in.** Daydream, Amazon Buy for Me, Google agentic checkout [doc].

### Handoff vocabulary
- **Anatomy.** A closed set of verb-first "your turn" labels (Dia: Sign In, Verify, Enter Information, Take Over), shown in the same words on the object (address bar), its list row (tab) and the notification. Tasks waiting on a human pause; they do not fail.
- **Seen in.** Dia [obs], ChatGPT tasks [doc].

### Stop on the acted surface
- **Anatomy.** A floating bar at the bottom centre of the page or document being driven ("Pause / Stop", "Take control / Stop"), mirrored as a square stop in the composer. Prefer Pause or "Take control" to Stop; red only for ending the run. The key is in the label. Any batch over about 5s gets a stop.
- **Seen in.** Comet, Atlas [doc], Perplexity [obs].

### Control hue on the driven frame
- **Anatomy.** One reserved hue means "the AI is in control" and nothing else, applied to the frame of the controlled surface (Comet's teal edge glow, Dia's violet `#5a4de6` while acting, amber `#fcbf49` for intent routed to chat).
- **Seen in.** Comet, Dia [obs].

### Read, write and spend permissions
- **Anatomy.** Permissions separate read, write and spend; scope per app or site; choices "Allow this time only / Always allow / Don't allow"; every decision logged in the conversation (Allowed, Always allowed, Denied). Sensitive modes explained in the mode ("works only while you watch this tab"); a logged-out mode for risky work. Per-object AI visibility toggles in the object's header, sensitive categories off by default.
- **Seen in.** Comet, Atlas, Dia [doc, obs].

### Contestable safety call
- **Anatomy.** "Hid part of the page" with "Wrong call?"; the confirmation says the report becomes an evaluation case.
- **Seen in.** Dia [obs].

### Spoken approval is not approval
- **Anatomy.** Consequential actions need on-screen approve or decline even during a voice session.
- **Seen in.** ChatGPT [doc].

## Cost and access

### Context and usage meters
- **Anatomy.** A small ring near the composer; click for the token breakdown; a cheaper-model escape at the limit. Usage pages: bars with a pace marker (a vertical line where you "should" be by elapsed time), a hatched remaining portion, a reset countdown ("↻ 1d 1h"), limit banners with actions ("Resume at reset", "Snooze until reset"). Keep cost and tokens out of the conversation itself.
- **Seen in.** Cursor [doc], T3 Code [obs].

### Unit price at choice
- **Anatomy.** Each model card shows its unit price (with "~" when it varies) and speed / quality / cost meters as glyphs out of 3; pricing pages translate units into outputs ("64 images"). Effort menus warn that higher effort reaches limits faster.
- **Seen in.** Krea [obs], Claude [obs].

### Locked door
- **Anatomy.** The premium or signed-in feature rendered in place, greyed, with a lock and a plan badge or "Log in to use…"; the description states the unlock condition ("Add a reference image to use Ultra"); the click carries `next=`.
- **Seen in.** ChatGPT, Perplexity, Krea [obs].

### Limit that degrades
- **Anatomy.** At a limit, keep the conversation, drop the expensive part, disable only the costly control and explain it on that control, offer the cheapest way to continue before the upsell. A trial ends with a receipt of value delivered ("messages, sources read, artifacts generated, $0.00, this one's on us") rather than a paywall.
- **Seen in.** ChatGPT [doc], Dia [obs].

### Fenced sponsored unit
- **Anatomy.** If a free tier must carry ads: below the answer, past a hairline, a lead-in sentence, an "Ad" pill, and "Why you're seeing this ad", so paid content is never mistaken for the model's voice.
- **Seen in.** ChatGPT [obs].

## Memory and privacy

### Privacy mode in three places
- **Anatomy.** A top-bar toggle, an explanation in the empty state, and the placeholder. The sub-choice is made in a sheet before the first message and then locks.
- **Seen in.** ChatGPT temporary chat [doc].

### Inspectable memory
- **Anatomy.** Memory as named, dated, deletable items; an ephemeral mode with an explicit expiry. Hidden memory is the one wrong answer (removing memory entirely is also honest).
- **Seen in.** Bevel [doc]; Dia removing memory [doc].

### Separate origin for generated artifacts
- **Anatomy.** User-generated or shared output (code, HTML artifacts) runs on a separate origin in a sandboxed iframe, so it never touches the logged-in app. Shared copies say who shared them, that they are snapshots, and offer Report.
- **Seen in.** Claude [obs].
