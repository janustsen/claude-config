# Health

Consumer health apps where an AI triages symptoms or explains body data from wearables, logs and labs. Users judge them on one question: "Am I okay, and what should I do next?" They often arrive anxious, so the interface's first job is to lower arousal without becoming dishonest: calm colour, verbal uncertainty, evidence in the user's own words, and a clear path to a human when the AI has done what it can.

Studied:
- **Doctronic** (web): conversational AI triage. The full anonymous chat was driven live at a 390x844 phone viewport (DPR 2): consent, structured questions, live differential, report, doctor hand-off, and an emergency hard stop. Timings come from `document.getAnimations()` and computed styles [obs]. The paid doctor visit behind the email gate was not seen.
- **Bevel** (iOS): AI coach over wearable data, with photo food logging. Not run (iOS only, account required). Evidence is App Store screenshots and What's New, 22 help-center articles and official videos [doc]; onboarding comes from an older third-party capture [3p]. No Bevel motion was measured.

Tags: [obs] observed live, [doc] vendor docs, [3p] third-party write-up, [inf] inference from observed or documented facts.

## What users expect

1. **Reassurance before efficiency.** Warm neutrals, no red, gentle entrances and validating copy, because an anxious reader stops reading instructions.
2. **Honest uncertainty in words.** "Most likely / possible / less likely" and grey for non-significant change, because percentages imply precision the model does not have and invite fixation.
3. **The "why" one tap away, in their own terms.** Evidence quoted from what they said, or compared with "your usual", because they can verify it instantly.
4. **A way out to a human, and a hard stop when safety needs it.** The best answer is sometimes "see a doctor" or "call 911"; a chat that keeps chatting is a dead end.
5. **Control over memory and visibility.** Anonymous starts, ephemeral chats, readable and deletable memory, because health users fear judgment and leaks more than inconvenience.
6. **Their own baseline, not a population norm.** "Below your usual" is actionable; "out of range" without context alarms.
7. **Approval before anything is written to their record.** A wrong entry in a health log feels like a wrong entry in a medical chart.
8. **Value before identity.** Answers first, consent and account later (see L13), because the worried user will leave at a sign-up wall.

## The theses to choose from

### Doctronic: the quiet interview that ends at a portable report and a doctor

Core bet: an AI interview that dresses up its AI the least, walks the user from "I'm worried" to a two-audience report, and then hands off to a paid human, all without an account.

- The live composer is the landing-page hero, under a Fraunces 32px/400 H1 "Hi, I'm Doctronic" and the label "What brings you in?" [obs].
- The composer morphs into a typed form when the AI needs structured data: content fades over 120ms, radius 16→32px over 440ms, header rises 8px over 320ms with a 140ms delay, `cubic-bezier(.4,0,.2,1)`. Answers always include "Not sure" [obs].
- A hypothesis tray docks to the top of the composer ("Tension-type headache most likely…") and opens to evidence: wrapper 185→505px over 320ms [obs].
- Likelihood is ordinal pills, and the serious cause is named and labelled "Less likely" rather than hidden [obs].
- No red anywhere, including the emergency stop: a warm-butter sheet `rgb(254,249,231)`, 28px/600 heading, severity carried by bold phone numbers [obs].
- After the report, the fixed bottom slot becomes "Continue →" to a doctor with "● Licensed doctors available now" [obs].

Choose this when the user brings a question ("what is wrong with me?"), the flow is a linear intake, and escalation to a regulated human service is part of the product.

### Bevel: the score dashboard with a summonable coach

Core bet: a dashboard of scores is home, and the AI is an overlay that explains the numbers against the user's own baseline and stages every estimate for approval before it touches the log.

- Three rings with fixed identity hues (Strain orange, Recovery green, Sleep indigo), followed by one AI sentence that ends in an action: "Aim for 50-60% strain today" [doc].
- Values are compared with rolling personal baselines (60-day for HRV and RHR) and drawn with a 30-day normal band, e.g. "HRV is 31.3 ms, which is way below your usual 56.8 ms" [doc].
- Trends that are not statistically significant are grey, so colour encodes confidence [doc].
- AI food estimates land in an editable cart: "It won't be added automatically without your approval." Saying "I only ate a quarter of this" sets the item to 0.25 servings [doc].
- Memory is a browsable Files area (Memories, Plans, Artifacts, Notes, Logs, Core) of named, dated, deletable items [doc].
- AI cost is a published per-action credit table with weekly allowance and reset time; non-AI capture stays free [doc].

Choose this when the user brings data ("what is my data telling me?"), returns daily, and logs things that the AI can estimate.

## Comparison

| Dimension | Doctronic | Bevel |
|---|---|---|
| Home | Live composer plus 4 job chips [obs] | Score rings plus one AI sentence [doc] |
| Where the AI lives | It is the product: one chat [obs] | Overlay summoned from a bottom "Ask" pill, the "+" button or the dashboard; can read screen context [doc] |
| Account | None needed; asked at "Don't lose this chat" [obs] | Required [doc] |
| Uncertainty | Ordinal pills, "fits / doesn't fit" evidence [obs] | Personal baseline band, grey for non-significant [doc] |
| Severity colour | None; weight, position, modal interruption [obs] | Soft orange for unfavourable deltas, no red seen [doc] |
| Structured input | Composer morphs into a form [obs] | Photo, voice, files, screen context, "+" sheet catalogue [doc] |
| Correcting the AI | None: no edit, no regenerate [obs] | Editable cart plus natural-language correction [doc] |
| Progress | EKG trace plus rotating verb plus "what I'm doing with your input" subline [obs] | Named, collapsible thinking steps; "Thought for 24 seconds" [doc] |
| Interrupt | Input disabled, no stop [obs] | Send becomes a stop square [doc] |
| Per-message actions | Share only; one rating on the report [obs] | Copy, thumbs up, thumbs down; up to 3 follow-ups [doc] |
| Memory | Tied to account creation [doc] | Files you can read and delete; Ghost Mode with expiry [doc] |
| Cost | AI free and unlimited; the human costs $39 [obs] | Per-action credits, weekly allowance with reset [doc] |

## Category rules

### Layout and entry

1. **When the core job is one question, put the live input on the landing page instead of a "Get started" button**, because every step between worry and saying it out loud loses the most motivated users. Doctronic [obs].
2. **Use 3-5 starter chips to name the product's jobs, and make each chip send a full first-person message** ("Check my symptoms", "Understand my lab results"), because a nervous user needs to know what this thing is for. Doctronic [obs]. Extends L20.
3. **Re-assign the fixed bottom slot when the job changes stage**: composer while gathering facts, "Continue →" to a human once the AI has done what it can, with chat demoted inline ("Continue your chat…"). The thumb zone should always hold the next best action. Doctronic [obs].
4. **In data products, keep the dashboard as home and make the AI an overlay summonable from anywhere that can ingest the current screen as context**, because the user's question is usually about what they were just looking at. Bevel [doc]. See L11.
5. **Pair every score cluster with one generated sentence that ends in an action, stamp live metrics "Last updated at 9:32 AM", and put an ⓘ on every score screen** that explains its contributors. The deeper "View insights ›" is a deliberate tap below the short explanation, because numbers answer "how much" and only a sentence answers "so what". Bevel [doc].

### Composer and input

6. **When the AI needs structured data, swap the composer for a typed mini-form in the same slot, always offer "Not sure", and render the submitted answer as a plain user sentence** ("I'm a 30-year-old male") followed by a centred divider ("1 question answered"). Forms give parseable data; the echo keeps the transcript a conversation. Doctronic [obs]. Refines L12.
7. **Prefix every AI question with what the answer changes, and give every sensitive field an inline "Why do we ask for this?" sheet with the clinical reason in one sentence**, because people share personal data when they know its purpose. When a value is invalid, say what is wrong with it, never a "connection dropped" style error (see L16). Doctronic [obs, doc].
8. **Put the privacy state inside the composer as a tappable chip, and layer the explanation chip → one-screen sheet → policy.** The fear peaks while typing a symptom. Name the stigma directly ("our AI will never judge you"). Doctronic [obs].
9. **For photo estimation, teach the photo**: one clear shot at about 45 degrees, a fork, glass or hand in frame for scale. Put it in help and the empty state, because input quality caps estimate quality. Bevel [doc].

### Output and uncertainty

10. **Show AI likelihood as ordinal verbal buckets (Most likely / Possible / Less likely) and list the serious possibility, ranked honestly**, because naming the scary option and showing why it is unlikely reassures more than hiding it. Doctronic [obs].
11. **Justify each conclusion with "Fits what you described / Doesn't quite fit" bullets quoted from the user's own inputs**, so the user can catch a misunderstanding in one read. Doctronic [obs].
12. **Expose the AI's working conclusion as a collapsible tray anchored to the input**: one line collapsed, evidence expanded, transcript blurred behind it. It ties "what I think" to "what I need from you next" without interrupting the interview. Doctronic [obs].
13. **Compare metrics with a rolling personal baseline, draw the normal band on the chart, and say "your usual X" in the sentence.** Variation inside the band is visibly normal. **Grey out trends that are not statistically significant and print "correlation does not imply causation" wherever correlations appear**, so colour encodes confidence and users stop chasing noise. Bevel [doc].
14. **Withhold a score until there is enough data, and show a "Calibrating" or locked state with the unlock condition** (Nutrition Score unlocks at about one-third of the calorie goal logged), because a confident wrong number does more damage than a wait. Bevel [doc].
15. **Let users declare context that changes the maths**: Activity Status (Active, Sick, Injured, On a Break), lowered heart-rate zones for medication such as beta blockers, up to four excluded food contributors. A score that ignores your situation reads as judgment. Bevel [doc].
16. **Ground every pattern claim in the user's numbers with the statistic shown, and render a small chart when you claim a pattern** ("almost zero linear correlation (-0.09)"; "next-day recovery is 7.2% higher"). Save charts to the user's files. Bevel [doc].
17. **When output will reach a professional, generate a second, professional-format rendering of the same facts and label who each is for** ("SOAP Note (for Physicians)"), because the patient and the doctor scan differently. Doctronic [obs].

### Colour and severity

18. **Signal severity with interruption, position and weight, not saturated red**; use warm neutrals for "less likely / caution". Red narrows attention exactly when instructions must be read. Doctronic, Bevel [obs, doc]. Extends L1.
19. **Give each metric a constant identity hue, keep direction (▲▼) separate from valence, and use one soft caution hue for every unfavourable delta**, so a bad day never turns the screen red. **Give the AI one brand hue distinct from every status hue** (purple and periwinkle), so "the AI is talking" never reads as "something is wrong". Bevel [doc].
20. **Use two quiet, permanent disclaimer layers**: an action line pinned first in every chat ("If this is an emergency, call 911…", 16/600 ink, not red) and an identity line at the input (10px at 60% alpha). Never use a modal for the routine disclaimer. Doctronic [obs].

### Progress

21. **Make progress copy say what the system is doing with the user's input**, beside a domain-native glyph (an EKG trace), inside `role=status aria-live=polite`: "Reassessing symptoms with your latest answers". Waiting then feels like being listened to. Doctronic [obs]. Refines L5 and L6.
22. **For data-analysis answers, show what was read as named, collapsible steps** ("Analyzing Sleep Data", "Reconciling Cart Discrepancies"), expanded by default only if the user opts in, **and swap send for stop while running.** If you must disable input during a turn, keep turns to 3-8s. Bevel [doc], Doctronic [obs].
23. **Let long AI jobs survive the user leaving**: finish in the background, show an in-app preview banner that deep-links back, and notify "Responses ready". Bevel [doc].

### Trust, safety and escalation

24. **Fire emergency escalation on the first message that contains red-flag phrases, before demographics; make every number a one-tap `tel:` button; leave the conversation visibly ended with the instruction unobstructed.** In an emergency every extra tap or covered line is a failure. Doctronic got the stop but missed all three [obs].
25. **Gate the second turn, not the first: put consent inline where the reply would go, dim the composer until it is checked, then collapse it into a receipt divider ("Terms accepted").** The user has already seen value, and the divider is an audit trail that does not nag. Doctronic [obs]. See L13.
26. **Frame paid human escalation around the emotional outcome ("personalized guidance and peace of mind"), list concrete deliverables, and show price and refund in the same view** ("$39 self-pay or insurance accepted", "Full refund if you're not 100% satisfied"). Show the price only at the escalation point, never mid-chat. Doctronic [obs].
27. **Make sensitive data categories separately opt-in for the AI (reproductive health), explain the data flow with a test the user can run (airplane mode: the AI stops, biometrics still sync), and publish where each data source is less precise. Publish a "will not do" list and a "can't yet do" list, and tell users to trust their body over the data.** Boundaries stated up front prevent the worst misuse. Bevel [doc].

### Records, memory and recovery

28. **Never auto-commit an AI estimate to the user's record: stage it in an editable list with per-item quantity chips, Remove and Edit, accept spoken corrections ("only half"), and commit with one explicit button ("Add to log").** Estimates are wrong at the margin and the user owns the record. Bevel [doc]. Refines L8 and L9.
29. **In high-stakes answers drop regenerate, offer Share, and ask for one 3-point rating on the finished artifact** ("Not helpful / So-so / Helpful", neutral faces), because "ask until it says what I want" undermines trust. **Still let users edit a submitted fact**; Doctronic does not, and that is a gap. Doctronic [obs].
30. **Store AI memory as named, dated, deletable items, deletable both by asking the AI and by direct manipulation, and offer an ephemeral mode with explicit expiry (30 min, 1h, 6h, 24h) plus a separate toggle for whether it may read stored memory.** Trust in memory tracks its visibility. Bevel [doc].
31. **Ask for an account at the moment of loss ("Don't lose this chat"), after the report, and name exactly what memory buys.** Keep account actions and trust badges in the menu footer, available but never in the way, and colour only the one menu action you want repeated (New chat). Doctronic [obs]. See L13.
32. **Price AI per action in a published table, show used, remaining and reset time, and keep the non-AI path to the same outcome free** (photo, describe and scan capture are free). Bevel [doc]. See L15.

### Proactive, mobile and onboarding

33. **Let users schedule the AI to come to them ("Send me a daily recovery summary every morning at 8am") and treat each schedule as an editable, pausable object pinned in history; let them choose the coaching tone** (Friend, Commander, Guardian, Data Nerd), because the same advice motivates one person and shames another. Bevel [doc].
34. **Put the fastest input outside the app** (widget that logs water, hardware Camera Control opening food capture), **and notify on completed AI work and positive milestones, not on scary thresholds.** Bevel deliberately sends no real-time stress alerts [doc]. **Earn each OS permission with a branded pre-permission screen, build a graceful "no data found" branch, and ask for goals before body metrics**, so metrics feel like they serve the goal [3p].

### Copy

35. **Acknowledge, then ask one question per turn; hedge the diagnosis but be concrete about actions, with numbers and time windows** ("every 20 minutes, look at something distant for 20 seconds"; "book a video visit if it does not resolve in 1-2 weeks"), **and always state what would change the plan.** Frame low states as an invitation to rest ("Time to take it easy"). Doctronic [obs], Bevel [doc].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Background / ink | cream `rgb(253,253,247)` / `rgb(27,27,24)`; secondary = ink at 60-73% alpha | Doctronic [obs] |
| Single accent | `#2463EB` (CTA, links, selected only) | Doctronic [obs] |
| Type | Fraunces display (H1 32px/400); Geist body 16/22.4, labels 12/500, legal 10px at 60% alpha | Doctronic [obs] |
| User bubble | `#F0F6FF`, radius `16 0 16 16`, 16px padding; AI unboxed | Doctronic [obs] |
| Send button | 32px round; ready `#2463EB` + `0 4px 7px rgba(36,99,235,.39)`; empty `rgb(228,228,220)`; state 150ms ease-in; press `transform 0.1s ease-in` | Doctronic [obs] |
| Privacy chip | 32px tall, dashed 1px at 8% alpha, 600ms infinite dash animation | Doctronic [obs] |
| Likelihood pills | 12px/500. Most likely bg `rgb(219,230,220)` text `rgb(25,62,30)`; Possible bg `rgb(245,245,240)` ink 73%; Less likely bg `rgb(228,225,216)` text `rgb(89,65,13)` | Doctronic [obs] |
| Emergency sheet | bg `rgb(254,249,231)`, heading 28px/600, ink text, bold numbers | Doctronic [obs] |
| Bottom sheet | open 300ms `cubic-bezier(.16,1,.3,1)`; close 150ms ease-in; top radius 24px | Doctronic [obs] |
| Scrim | cream at 40% + `backdrop-filter: blur(4.5px)`, 200ms ease; never black | Doctronic [obs] |
| Sidebar | translateX −100%→0, inner view −5% + fade, 300ms | Doctronic [obs] |
| Two-phase collapse | fade 0-50%, then grid-rows 1fr→0fr 50-100%, 600ms ease-in-out (consent); 300ms (status lines) | Doctronic [obs] |
| Bubble entrance | translateY 8→0, 500ms `cubic-bezier(.34,1.56,.64,1)` | Doctronic [obs] |
| Thinking words | each word translateY 5px + fade 420ms `cubic-bezier(.2,0,0,1)`; 1000ms linear shimmer, infinite | Doctronic [obs] |
| Answer arrival | chunk opacity 0→1, 1000ms `cubic-bezier(.2,0,0,1)` (chunks, not tokens) | Doctronic [obs] |
| Composer→form morph | content fade 120ms; radius 16→32px 440ms; header rise 8px 320ms, delay 140ms, `cubic-bezier(.4,0,.2,1)` | Doctronic [obs] |
| Segmented select | bg + colour 200ms ease; 800ms label shimmer, 120ms delay | Doctronic [obs] |
| Hypothesis tray | 185→505px, 320ms `cubic-bezier(.4,0,.2,1)`; expand icon in 240ms (delay 160ms, scale .85→1), out 150ms no delay | Doctronic [obs] |
| Accordion | differential card 280ms `cubic-bezier(.4,0,.2,1)`; report section 400ms ease-out, chevron 200ms | Doctronic [obs] |
| Availability pulse | two rings scale 1→2.8 / 3.4, opacity .55→0, 2200ms infinite, second ring delayed 1100ms | Doctronic [obs] |
| Animation pause | 40px floating button; persisted; decorative durations collapse to ~1ms | Doctronic [obs] |
| Turn latency | first reply ~3s; typical turn 3-8s | Doctronic [obs] |
| Baselines | HRV and RHR rolling 60-day average; strain band rolling 30-day variability | Bevel [doc] |
| Chart timeframes | 1M/3M/6M/1Y, each point = 1 day / 3 days / 6 days / 1 month | Bevel [doc] |
| Credit costs (Standard model) | message ~1, reminder check-in ~3, food log ~5, impact analysis ~8, data check-in ~10, plan reconciliation ~20; Upgraded model ~3x | Bevel [doc] |
| Credit packs | 350 / 700+50 / 1,400+150 / 3,500+700; purchased credits never expire; Pro allowance resets every 7 days | Bevel [doc] |
| Ghost Mode expiry | 30 min, 1h, 6h, 24h | Bevel [doc] |
| Follow-ups | up to 3, user can turn off | Bevel [doc] |

## Anti-patterns seen

- **Emergency numbers were plain text.** Doctronic's stop sheet had zero anchors. Fix: every number is a `tel:` button.
- **The red-flag message was answered with a demographics form first.** Doctronic escalated only after age and sex. Fix: scan the first message and escalate before any intake.
- **A live form covered the safety instruction.** After the stop sheet closed, the three-question red-flag form stayed interactive and hid the AI's emergency text. Fix: end the conversation visibly and freeze or remove pending forms.
- **No way to interrupt or correct.** Doctronic disables input during the turn, has no stop, and submitted answers are immutable. Fix: a stop control, and "edit answer" on the echoed bubble.
- **Empty submit does nothing.** No feedback at all on Doctronic's empty send. Fix: the disabled send state should look disabled and explain on tap, or not be tappable.
- **Ambient infinite motion on a worry page.** Doctronic's marching-ants chip and pulse rings run forever; its own fix is a persistent pause button, which every infinite animation should have alongside `prefers-reduced-motion`.

## Steal list

1. Put the live input on the front door, because the user arrives mid-worry.
2. Morph the composer into a typed form with "Not sure", then echo the answer as a sentence, because you get clean data without leaving the conversation.
3. Say why before every question, because people answer when they know what it changes.
4. Show likelihood in ordinal words and name the serious option as "Less likely", because honesty reassures more than omission.
5. Back every conclusion with "fits / doesn't fit" bullets in the user's own words, because the user can audit it instantly.
6. Dock the AI's current belief to the composer as a collapsible tray, because the conclusion stays one tap away without interrupting.
7. Compare to the user's rolling baseline and draw the normal band, because "below your usual" is actionable.
8. Grey out non-significant trends, because colour should encode confidence.
9. Lock a score until there is enough data and say what unlocks it, because a wrong confident number does the most harm.
10. Keep red out of severity; use interruption, position and weight, because panic stops reading.
11. Re-assign the bottom slot when the stage changes (composer → doctor), because the thumb zone holds the next best action.
12. Stage every AI estimate in an editable cart and commit with one button, because the user owns the record.
13. Make progress copy describe what is being done with the user's input, because waiting then feels like being heard.
14. Fire safety stops on the first red-flag message with `tel:` buttons and an unobstructed instruction, because seconds and taps matter.
15. Make memory named, dated, deletable files and offer an ephemeral mode with expiry, because trust in memory tracks control.
16. Publish what the AI will not do and cannot yet do, because boundaries set expectations before misuse.
17. Close sheets in half the open time (300ms in, 150ms out) and fade before collapsing, because dismissal is already decided and reflow under visible text reads as a glitch.
18. Generate a professional-format copy of the same facts when a doctor will read it, because each audience scans differently.
