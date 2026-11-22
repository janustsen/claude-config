# AI assistants

Phone AI apps: a chat-and-agent app (Claude), an answer engine with sources (Perplexity), an AI meeting notepad (Granola), a search browser whose AI writes web pages (Arc Search) and ChatGPT from an earlier study. The phone is held in one hand, the keyboard covers half the screen, and much of the work now runs somewhere else while the phone supervises it. Users judge the category on one question: "Can I ask, read and steer with one thumb, in the mode I meant?" Every studied app answers with a thread or a list, a composer floating at the bottom, and a primary slot bottom-right that changes with state.

Studied (no native app was driven; claude.ai and perplexity.ai sat behind a Cloudflare bot check in iPhone emulation):
- **Claude** v1.261116.19: 14 framed App Store renders measured at an assumed 393pt (±10%), help center articles on dictation, voice, widgets, Lock Screen controls and Cowork.
- **Perplexity** v26.46.0: 6 current and 8 older framed renders (older ones labelled), one raw help-center screenshot of the voice settings sheet, measured at ±5%.
- **Granola** v1.16.4: 10 renders, raw help-center screenshots (home measured at ±2%), eight help articles.
- **Arc Search** v1.49.0: 15 renders and a 39.5s real screen recording at 393x852pt, 30fps. Arc's AI features (Browse for Me, pinch to summarize) turn off on 23 November 2026 [doc]; use it as a pattern reference, not a live product.
- **ChatGPT**: the earlier study's ten top findings (firstmate `data/design-apps-b/evidence/chatgpt-mobile.md`, section 0; its full write-up is product-ui's `mobile-ai-apps.md`) plus a delta measured on chatgpt.com at 393x852 with an iOS user agent: streaming, scroll, composer growth, thread layout. Web values are exact but are web, not native.

Tags: [meas] measured, [obs] seen in a capture, [doc] the maker's docs or App Store text, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **The app opens on the conversation or the list it serves.** Claude, ChatGPT and Perplexity open on a thread; Granola, whose object is the note, opens on a list of meetings with the AI as a pill in the bottom bar [obs].
2. **The main action bottom-right, in the same place every time**, morphing with state (voice when empty, send when typed, stop while streaming) [obs ChatGPT, Claude].
3. **Two speech contracts that look different before the tap**: dictation gives text you review and send; voice is a live conversation. All five apps keep them apart [doc].
4. **Long-press goes faster, never somewhere hidden.** Every ChatGPT long-press duplicates a visible path [doc ChatGPT].
5. **Evidence one tap away**: a chip, a header tab or a disclosure per section, depending on how much the product is about sources [obs].
6. **A page that holds still while text streams**, because a moving page cannot be read [meas ChatGPT].
7. **Agent work reported, not watched**: a quiet log, a result card, a notification when done or blocked [obs Claude, Perplexity].
8. **Entry from outside the app**: widget, Action button, Control Center, Lock Screen, Siri and the Share sheet, each opening straight into one mode [doc ChatGPT, Claude, Perplexity].
9. **Honest device roles**: read, approve and steer on the phone; author on the big screen, and the app says which is which [doc ChatGPT, Granola].

## The theses to choose from

### Claude: one composer, results decide their own form
Core bet: no mode switch on the phone. "Describe your task in any conversation, and Claude takes it from there" [doc]; text, files, interactive apps and agent tasks all arrive in the thread as cards, and the phone is the remote for work running elsewhere.
- No tab bar: a hamburger circle top-left opens the history drawer; one capsule top-right holds new chat and ••• [obs].
- Two-row composer: text on top; + , a model pill ("Opus"), mic and the primary on the row below, every control a ≈37pt filled circle [meas].
- The primary slot is an ink voice circle when empty and a coral (#D97757) Send when text exists; coral appears only on Send and new task [obs, meas].
- AI prose is unboxed serif; only things you take away (file, draft, app) get a card [obs].
- Agent work lives in a task list with count chips ("Blocked 12") and approve-inside-the-row [obs].

Choose this when one assistant does both chat and long-running agent work, and the phone's job is to start, steer and approve it.

### Perplexity: every answer is a document with its evidence beside it
Core bet: a thread is one research question, so sources get their own view and a new topic gets a fresh page.
- A centred segmented capsule in the header switches views of the same thread: answer, sources and (for Computer threads) output, icons only [obs].
- Sources is a full view grouped by origin with counts: "Connectors 2", "Web 4", "Files 1"; web rows lead with publisher name and logo [obs].
- Bottom: a follow-up pill ("Ask a follow up…") with the mic inside it, and a separate ≈54pt new-thread circle outside it [meas].
- Key phrases in the answer are accent-blue inline links instead of numbered footnotes (the older design used numbered bubbles) [obs].
- Agent steps print as one grey ≈12pt line each with a chevron, then a preview card of what was built [obs].

Choose this when the answer's credibility is the product, or when users start fresh topics often.

### Granola: the note is the product; AI is a pass you trigger by ending
Core bet: capture starts from the thing that already names it (a calendar event, a call), runs in the pocket, and AI output appears only after End, with a notification when ready [doc].
- Home is "My notes" (serif ≈33-34pt) with "Coming up" calendar rows above today's notes [meas].
- One floating bottom pill holds call · "Ask anything" · an ink ≈70x51pt compose pill, the only filled control on home [meas].
- An active recording is a bottom sheet with pause, timer, live green level bars and an ink End, mirrored to a Live Activity, the Dynamic Island and the Watch [obs, doc].
- Authorship by ink: user text black, AI text grey #4E4D4B [meas, know].

Choose this when AI processes something the user captures (a meeting, a call, a document) and the user should not watch it work.

### Arc Search: AI as a second verb on every query (pattern reference)
Core bet: search is the launch state, and each suggestion row offers both "search" (tap the row) and "Browse for Me" (tap the button), so the user picks links or an answer per query [obs, doc].
- Opens with the keyboard up; the search field rides on the keyboard [doc, obs].
- The AI answer is a web page in the normal browser frame, so back, share and tabs need no new UI [obs].
- While it works, the loading screen lists the six domains being read: progress and provenance at once [obs].
- Pinch-in on any page summarizes it: ≈267ms collapse, ≈170ms pause, ≈300ms settle into a tilted card [meas].
- Chrome is three bottom buttons (tabs · + · ^) tinted from the page and collapsing on scroll [obs, doc].

Choose this pattern when AI is an alternative way to do the app's main job rather than a separate place.

### ChatGPT: the conversation is the app; the phone is an outbound surface
Core bet: one thread with a bottom composer, and everything else (voice, images, tasks, apps) renders inside it or on a sheet, drawer or chip on top of it [obs, doc].
- The bottom-right slot is Voice (accent-filled) when empty, Send when typed, a black X in voice; dictation sits left of it as an unfilled glyph [obs].
- The model picker sits at the top of the conversation on phones, named by effort (Instant / Medium / High / Extra High) with an "Auto switch" toggle [doc].
- A fixed, always-visible action row under each answer: Copy, Read aloud, Good, Bad, Regenerate, Share, plus contextual chips such as Sources [obs, doc].
- Widgets, Action button, Control Center, Lock Screen, Siri, Live Activities and CarPlay each launch straight into a mode [doc, 3p].

Choose this when the product is a general assistant and chat is the main loop.

## Comparison

| Dimension | Claude | Perplexity | Granola | Arc Search | ChatGPT |
|---|---|---|---|---|---|
| Root | Thread; drawer for history [obs] | Thread (home not captured) [obs] | List of notes and upcoming meetings [meas] | Search field over the keyboard [doc] | Thread; drawer [obs] |
| New conversation | Top-right capsule with ••• [obs] | Bottom-right circle beside the follow-up pill [meas] | Ink compose pill in the bottom bar [meas] | Centre + in the bottom bar [obs] | Top-right [obs] |
| Primary slot when empty | Ink voice circle [obs] | Mic inside the follow-up pill [meas] | Mic (dictation) [meas] | Browse for Me per row [obs] | Accent voice circle [obs] |
| Model choice | Pill in the composer ("Opus") [meas] | Not on the thread screen [obs] | Pill in the composer ("Auto ⌄") [meas] | None | Top of the conversation, effort names [doc] |
| Sources | Not captured | Header tab, grouped full view [obs] | Transcript behind ••• [doc] | "▸ From nps.gov" per section [obs] | One chip that opens a sheet [doc] |
| Agent work | Task list, count chips, approve in the row [obs] | Grey step log, then a preview card [obs] | Named stages, then a notification [doc] | Domains being read [obs] | Cards in the thread [doc] |
| Voice | Hands-free and push-to-talk [doc] | Hands-free, push-to-talk, subtitles [doc] | Meeting transcription, not conversation [doc] | Hold + to speak; raise to ear [doc] | Separate Voice and Dictation buttons [doc] |
| Accent | Coral, Send and new task only [meas] | Blue inline links; teal toggles [meas] | Ink; green level bars [doc] | Indigo #3B35E4 titles and links [meas] | Accent voice and send [obs] |

## Category rules

### Shell and navigation

1. **Use a drawer plus floating corner controls instead of a tab bar when the app has one primary job**, because every other destination is visited rarely and can cost one swipe. Claude [obs], ChatGPT [obs], Perplexity [obs].
2. **Open on the user's object when the AI serves it** (meetings, pages), and put the AI in a bottom pill, because the object is what the user came for. Granola [obs].
3. **Put view switches for one object (answer, sources, output) in a centred icon capsule in the header**, because they are views of the same thing, not destinations. Perplexity [obs].
4. **Group the thread-level actions in one top-right capsule and leave the drawer button alone on the left**, because the grouping says "these act on this thread". Claude [obs].
5. **Put new conversation at the bottom when starting fresh is frequent (search, notes) and top-right when follow-ups dominate (chat)**, because the more frequent act gets the thumb. Perplexity, Granola, Arc vs Claude, ChatGPT [obs, chatgpt-ios-delta judgement].
6. **Separate "follow up" from "new topic" as two controls at the bottom of a thread**, because the common phone mistake is asking an unrelated question inside old context. Perplexity [meas].
7. **Make back a full-width swipe on reading screens**, because a one-handed thumb cannot reach the left edge on a 6-inch phone; Arc later tuned it to reduce accidental backs. Arc Search [doc].

### Composer and the primary slot

8. **Keep one composer that accepts any size of request and let the result pick its presentation** (text, card, sheet), because a mode switch costs a tap and a decision on every message. Claude [doc].
9. **Morph the bottom-right slot with state: voice when empty, Send when typed, Stop while streaming**, because the one place the thumb returns to should always hold the next action. ChatGPT [obs, meas], Claude [obs].
10. **Spend the accent only on the control that sends text; keep the empty-state voice button ink**, because colour then means "this will commit". Claude [obs]; ChatGPT fills voice with the accent instead [obs].
11. **Put the model choice where the decision is made**: a pill in the composer when users switch per message, the top of the conversation when it is a rare default; default to "Auto", not a model name. Claude, Granola [meas], ChatGPT [doc].
12. **Give every composer control the same filled circle hit shape (≈37pt)**, because equal shapes read as one toolbar. Claude [meas].
13. **Start the composer as one 48pt row and switch to two rows once text wraps** (text on top, controls below; 90, 124, then 148pt for 1-3 lines), because the text then gets the full width. ChatGPT [meas].
14. **Make Return a newline and send only with the button**, because a soft keyboard has no Shift+Return. ChatGPT [meas].
15. **Float the composer 12-16pt above the keyboard, not flush**, so it still reads as a card. Granola [meas].
16. **Suggest with the placeholder ("Who did I meet with?") and greet with one short line**, not a suggestion grid, because the composer is the call to action. Granola, Claude [obs].
17. **Open a single-job app straight into its input with the keyboard up, with a setting to turn that off.** Arc Search [doc].

### Speech

18. **Keep dictation and voice conversation on different controls with different glyphs**, and say which one records, because accidental recording is a privacy failure. ChatGPT [doc], Claude [doc], Granola [doc].
19. **Give dictation exactly two exits: X cancels, arrow or ✓ sends**, because it is a short modal state. Claude [doc], Granola [doc].
20. **Offer push-to-talk beside hands-free in every voice mode**, because turn detection fails in noisy places; let speaking again interrupt the AI. Claude, Perplexity [doc].
21. **Open voice settings from inside voice mode as a sheet with grouped, subtitled options** (Hands free, Push to talk, Subtitles, named voices), because users change them while listening. Perplexity [meas].
22. **Hide a secondary input mode on long-press of the primary button** (hold + to speak), because it costs no space. Arc Search [doc].
23. **Ask for approval on screen, never by voice, even during a voice call.** ChatGPT [doc].

### Streaming and reading on a small screen

24. **On send, scroll once so the new question sits at the top, then never move the viewport while text streams; reserve blank space after the last turn so short answers can still pin**, because a phone shows about 30 lines and a moving page cannot be read. ChatGPT [meas].
25. **Show a pending dot within 0.5s and switch the primary to Stop at once**, because the first words may take 1-2s (ChatGPT: dot at +0.5s, first words at ≈1.5s, ≈500-600 characters per second, done at ≈5s). ChatGPT [meas].
26. **Offer a 44pt scroll-to-bottom circle centred 4pt above the composer**, because that is where the thumb already is. ChatGPT [meas].
27. **Stream only when the user is watching; batch and notify when they are not.** A summary that streams during a meeting competes with the meeting. Granola [doc], chatgpt-ios-delta judgement.
28. **Set tables one step below body (14 vs 16) and let them scroll sideways**, because the body must not shrink. ChatGPT [meas].
29. **Give AI prose its own face (Claude's serif) or ink (Granola's grey), and keep UI in the sans**, so the reader knows who is speaking without a label. Claude [obs], Granola [meas].
30. **Keep the answer's action row always visible with a fixed set of icons, its first glyph aligned with the text edge.** Moving Read aloud into overflow drew angry reviews from accessibility users. ChatGPT [obs, meas, 3p].
31. **End an answer with a quiet completion mark, not a toast.** Perplexity [obs].

### Sources and provenance

32. **Use one chip for a few sources and a full grouped view when sources are the product**, grouping by origin (your apps, the web, your files) with a count per group, because "which of my data did it use" is a different question from "which websites". Perplexity [obs], ChatGPT [doc].
33. **Lead a web source with publisher name and logo, headline second**, because the publisher is what the user trusts. Perplexity [obs].
34. **Mark 2-4 key phrases per screen as inline accent links instead of footnote numbers**, because those are the taps that deepen the answer. Perplexity [obs].
35. **Show the sources being read as the loading state**, because it is progress and provenance at once. Arc Search [obs].
36. **When replacing content with an AI version, keep a thumbnail of the original on top** ("Summarized for you"). Arc Search [obs].

### Agent work: logs, queues and approvals

37. **Design the phone side of agent work as review and steer: a list, approval in place, notifications**, because the work runs elsewhere and the phone is where the human is. Claude [doc, obs], ChatGPT [doc].
38. **Print agent steps as single grey lines below prose size, each with a chevron to expand, ending in a loud result card.** Log quietly, result loudly. Perplexity [obs].
39. **Give a queue of many agent tasks its own list, filtered by chips that carry counts ("Blocked 12")**, because the count is the reason to tap. Claude [obs].
40. **Show task state with a glyph tile (spinner, raised hand, branch) plus an unread dot, and relative times without "ago" ("2m")**, because the state word already lives in the filter chip. Claude [obs].
41. **Put the agent's question and the Approve button inside the blocked row**, because approving from the list skips a push and a back. Claude uses an outlined button inside a highlighted card; use filled when the row is not highlighted. Claude [obs], chatgpt-ios-delta judgement.
42. **Let users choose how often an agent asks (always, before changes, only important changes).** ChatGPT [doc].
43. **When the AI needs one answer before working, ask with option chips, an "other" field and equal-width Skip and Continue**, so the user can proceed without answering. Perplexity [obs, older].
44. **Split long processing into named stages ("Uploading", "Generating notes") and notify at the end**, because "processing…" with no stage looks stuck. Granola [doc].

### Results and artifacts

45. **Box only what the user takes away (file, draft, app) as a card with a type subtitle ("Presentation · PPTX"); leave prose unboxed.** Claude [obs].
46. **Open anything the user will use (an app, a quiz, a deck) as a large sheet over the thread with X top-left and ••• top-right**, so the thread stays one swipe away. Claude [obs].
47. **Show alternatives as lettered chips on one card, before the fields** ("A Warm and gracious", "B Confident and concise"), because the user is picking a voice, not reading twice. Claude [obs].
48. **Put attachments as ≈94pt square tiles above the message they belong to**, file tiles with a type chip and the source app icon. Claude [meas].
49. **Render an AI answer inside the frame the app already has** (a web page in a browser), so back, share and tabs work unchanged. Arc Search [obs].
50. **Keep read-only on the phone what is authored on desktop, and route what the phone cannot do** ("Sign in on desktop", templates on desktop) instead of a cramped version. ChatGPT [doc], Granola [doc].

### Capture that outlives the screen

51. **Start capture from the event that names it** (a calendar row expanding to "Start notes", a Lock Screen "Start Granola"), because nobody names a recording afterwards. Granola [obs, doc].
52. **Keep an active capture as a bottom sheet with pause, timer, live level bars and one filled End; drive the bars from the real mic input**, because the bars are the only proof a phone in a pocket is hearing. Granola [obs, doc].
53. **Mirror a long capture to the Live Activity, Dynamic Island and Watch, with End reachable from each.** Granola [obs, doc].
54. **Never auto-record; allow pause; generate only on End.** Granola [doc].

### System entry points and privacy

55. **Make each input mode a separate system entry point** (widget buttons for new chat, dictation and camera; a Share-sheet intent on selected text; Action button shortcuts for ask, new chat and voice), because the fastest path skips the home screen. Claude, Perplexity, ChatGPT [doc].
56. **Let a Shortcuts intent use the default model**, so it never asks for one. Claude [doc].
57. **Show a privacy mode in three places: a top-bar toggle, an empty-state explanation and a changed placeholder ("Temporary chat")**, and lock the personalization choice after the first message. ChatGPT [doc].
58. **Delete voice audio after transcription by default; make sharing recordings opt-in.** Claude [doc].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Top controls | ≈43pt circles, ≈20pt inset; capsule ≈100x43pt (new chat + •••) | Claude [meas ±10%] |
| Header | 42pt circles at 16pt inset; segmented capsule ≈112x42pt | Perplexity [meas] |
| Header (web) | 44pt circle at x=16, no bar background | ChatGPT [meas web] |
| Composer | two rows, radius ≈24pt; controls ≈37pt circles; model pill ≈56x37pt | Claude [meas] |
| Composer (web) | 48pt single row, radius 28, 16pt side insets, 24pt from the bottom; two rows 90, 124, 148pt | ChatGPT [meas web] |
| Composer with keyboard | inset 16pt, ≈102pt tall, ≈14pt above the suggestion bar, mic ≈38pt | Granola [meas] |
| Follow-up pill | x 16 to ≈310pt, ≈52-56pt tall, mic ≈32pt inside; new-thread circle ≈54pt; bottom ≈20pt above the edge | Perplexity [meas] |
| Scroll to bottom | 44pt circle, centred, 4pt above the composer, rgba(252,252,252,.78), shadow 0 4px 24px rgba(0,0,0,.1) | ChatGPT [meas web] |
| Streaming | pending dot ≈12pt at +0.5s; first words ≈1.5s with a 2-3 word trailing fade; ≈500-600 chars/s | ChatGPT [meas web] |
| User bubble | max ≈253pt (64%), radius 22, padding 10/16, #EDF3FE / #2451DA, 16/24 | ChatGPT [meas web] |
| User bubble | #F0EEE6, radius ≈18pt, ≈16pt | Claude [meas] |
| Answer text | 16/26 #0D0D0D, 16pt margins, 16pt paragraph gap; tables 14/20 | ChatGPT [meas web] |
| Action row | 44pt hit areas, 20pt glyphs #5D5D5D, 36pt pitch, first glyph at x=18 | ChatGPT [meas web] |
| Attachment tiles | ≈94x94pt, radius ≈12pt | Claude [meas] |
| Claude colours | page #FAF9F5, composer #FFFFFF, controls #131313, accent #D97757 | Claude [meas] |
| Perplexity colours | page #FAF8F5; teal #1FBCD2; dark sheet #191A1A, card #222423 | Perplexity [meas] |
| Voice settings sheet | 16pt inset, two-line rows ≈77pt, one-line ≈54pt | Perplexity [meas] |
| Home (notes) | circles 44pt; serif title ≈33-34pt at x 25; row cards inset 17pt, ≈78pt tall, ≈14pt gap, radius ≈18pt; date tile ≈36pt | Granola [meas ±2%] |
| Bottom pill | inset ≈17pt, 48pt tall, ≈50pt above the screen edge; compose pill ≈70x51pt | Granola [meas] |
| Note | serif title ≈34-35pt, line pitch ≈38pt; chip capsule ≈143x32pt; 32pt icon circles; hanging # in #B0B1AC; AI text #4E4D4B on #EAEBE5 | Granola [meas] |
| Search field | 361x45pt, full radius; suggestion rows ≈56pt; Browse for Me pill ≈100x30pt, 13pt semibold | Arc Search [meas] |
| Tools sheet | top at ≈584pt; URL pill 48pt; four 78x78pt tiles, 16pt gaps and insets; half pills 38pt | Arc Search [meas] |
| Pinch summary | collapse ≈267ms, pause ≈170ms, settle ≈300ms | Arc Search [meas 30fps] |
| Non-content words | Claude chat 5, empty 8, task list 14; Perplexity thread 4, sources 10, Computer thread 22; Granola home 12, note 0-1, recording sheet 7; Arc search sheet 13, result page 2 | [obs] |

## Anti-patterns seen

- **A step log louder than the answer.** Perplexity's Computer thread carries about 22 non-content words, most of them step status [obs]. Fix: keep steps smaller and lower in contrast than prose so the eye skips them, as Perplexity's own rows do.
- **A per-row verb that repeats its label.** Arc's "Browse for Me" on four rows costs 12 of the search sheet's 13 non-content words [obs]. That is the price of a per-row verb; pay it only when the per-query choice is the product.
- **A metadata word on every row.** Granola repeats "attendees" on each meeting row, its one wordy spot [obs]. Its notes themselves carry 0-1 such words, which shows where the budget went.
- **Moving an accessibility action into overflow.** ChatGPT moved Read aloud and drew angry reviews [3p]. Fix: keep the fixed action set visible.
- **Gestures that fire by accident.** Arc had to ship "Reduced Accidental Call Arc Activation" for raise-to-ear and tune its full-width back swipe [doc]. Gestures with no visible control need tuning after launch.

## Steal list

1. Morph one bottom-right slot through voice, Send and Stop, because the thumb always returns there.
2. Keep voice ink and Send accent, because colour then means "this commits text".
3. Pin the new question to the top, hold the page still while streaming and reserve space below, because a phone cannot be read while it scrolls.
4. Make Return a newline and grow the composer to two rows when text wraps, because the soft keyboard has no Shift+Return.
5. Put the model pill in the composer when users switch per message, default "Auto", because the control belongs where the decision is made.
6. Separate follow-up from new topic at the bottom of a thread, because old context poisons new questions.
7. Give sources a grouped view with counts when they are the product, a chip when they are not.
8. Show the sources being read as the loading state, because it doubles as citations.
9. Log agent steps as grey one-liners and end with a loud result card.
10. Put the agent's question and Approve inside the blocked row, and filter queues with count chips.
11. Box only artifacts; open usable ones as a large sheet over the thread.
12. Start capture from the event that names it and show AI output only after End, with named stages and a ready notification.
13. Mirror any long capture to the Live Activity, Dynamic Island and Watch, each with End.
14. Keep dictation and voice on different controls, each with push-to-talk and a clear cancel.
15. Make every input mode its own widget, Action button and Share-sheet entry.
16. Offer AI as a second verb beside the normal one (Browse for Me) instead of a global mode.
