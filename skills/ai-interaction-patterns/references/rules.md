# AI interaction rules

Imperative rules, each with the reason it exists. Anatomy and measured values for the patterns named here are in [patterns.md](patterns.md). These held across unrelated products (chat, coding, notes, browsers, health, finance, shopping), which is why they are trusted.

## Input and context

1. **Put the AI inside the input people already use**, then add a dedicated surface. Users already know where to type, and routing on the server removes "where is the AI?".
2. **Separate navigating from asking.** Entity search at the top, the AI composer docked at the bottom with a scoped placeholder. One control per intent stops wasted queries and keeps answers grounded in what is on screen.
3. **Offer AI at three radii sized to the context it needs:** an inline verb on a selection, a side panel about the current object, and a navigable item (a chat, a task, a report) for multi-source work. Small asks stay small.
4. **Dock AI beside the object, never over it.** The object stays live on the leading side; AI sits on the trailing edge (side panels measured at about 28-40% of the window). The user needs source and answer visible together.
5. **Attach the obvious context by default as a visible, removable chip.** Zero setup, and the user can audit it.
6. **Keep the active constraint set visible and removable** across turns. Multi-turn context drifts silently.
7. **Teach syntax and scope in the placeholder.** It costs no space and replaces an onboarding tip.
8. **Separate input contracts by control, not by setting.** Dictate-to-text and talk-live are two adjacent buttons with distinct icons, so the user knows the outcome before tapping.
9. **When the AI needs structured data, turn the composer into a typed form** with "Not sure" and a reason for each question, then echo the answer as a sentence.
10. **Explain every sensitive question before asking it**, with one reason.
11. **Label capability by outcome** (Instant, Medium, High, Auto), not internals.
12. **Never lock the input while the AI works**, and say so ("you can keep typing"). Queue, steer and stop are three intents with three gestures.
13. **Keep the fast loop separate from slow work.** Acknowledge immediately, work in the background, insert results when ready.

## Streaming and progress

14. **One thing moves.** While working, one status line with a verb and a timer; the verb shimmers; nothing else loops. Motion is attention, so a page where everything moves has no signal.
15. **Stream evidence before claims:** sources, then structured data, then prose. Users judge the basis before the claim.
16. **Stream in finished blocks or fading words; never jitter, never replay finished text.**
17. **Never yank the scroll.** Follow the bottom only while the user is within about 24-40px of it; once they scroll up, stop and offer "Jump to latest".
18. **Reserve the output's final space** as soon as output is coming. Layout shift during streaming makes working UI feel broken.
19. **Progress copy describes what the system is doing with the user's input** ("Reassessing symptoms with your latest answers", "Searching 10,000+ brands…"), with `aria-live`. Waiting then feels like being listened to.
20. **Present tense while running, past tense with counts when done.** "Searching" becomes "Searched 3 sources · 4 new people".
21. **Collapse finished work into a receipt; keep the result outside it; never fold failures.** Users want proof of work, not the work.
22. **Deliver ranked visual results all at once** behind a status line that names the scope. Streaming a grid card by card reorders under the pointer.
23. **For tasks over about 10s, signal "done" and "needs your input" with two different, short, optional cues** (a sound, a notification). Never grab audio focus.

## Stop, retry, correct, undo

24. **Stop where the agent acts and where you typed.** A floating Pause / Stop on the acted surface plus a square stop in the input; the key in its label. Attention is on the action.
25. **Offer Stop for any batch that can exceed 5s.**
26. **A stopped run names what stopped** and offers Continue. Silent truncation reads as a bug.
27. **Fail per item, with one Retry exactly where it failed.** Treat "offline or waiting" as its own state; retry transient failures once automatically.
28. **Rank recoveries by cause** (retry without the attachment, edit, start new), details collapsed.
29. **Never auto-commit an AI estimate.** Stage it in an editable cart with quantity chips, Remove and Edit, accept natural-language corrections ("I only ate a quarter"), commit with one button. The user owns the record.
30. **Explanation leads straight to correction.** Every source or memory used offers "Not relevant" and "Make a correction".
31. **Show self-correction as an event, never a silent rewrite.**
32. **Real undo where it exists; stage and confirm where it cannot exist.** Merge edits within 500ms into one undo step, keep about 100 steps. Restore appends a version.
33. **Regenerate derived output when its source is deleted**, so the AI layer never leaks what the user removed.
34. **Separate "restore the files" from "rewrite the conversation".** Offer rewind-with-checkpoint and fork rather than a bare regenerate.

## Evidence and uncertainty

35. **Every AI block shows its source count and generation time**, with live chips for entities it mentions.
36. **Every claim drills down to raw evidence** with counts and highlighted excerpts and a plain label of where it came from. Trust moves to the source.
37. **Rate sources and say why** (trusted publishers marked, a one-line reason on hover, "Rate this source").
38. **Express uncertainty in words and order**, not false-precision percentages.
39. **Phrase evidence in the user's own words** ("Fits what you described" / "Doesn't quite fit").
40. **Label every number's state** (live, closed, estimate, calculated) and when, including numbers the AI quotes. An unlabelled stale number is a silent error.
41. **Compute in code, narrate with the model.** Deterministic tools do sums, filters and projections; the AI states the method and what it left out. This removes the main source of numeric hallucination.
42. **Explain recommendations with the user's own maths** behind a verdict chip and ⓘ; pair a percentage with currency.
43. **State constraint failures plainly** and offer the nearest feasible value as a chip. A silent relaxation destroys trust.
44. **Evidence from people outranks the model's opinion.** Aggregate with counts and quotes.
45. **Say what was not verified.**

## Proposals and authorship

46. **Decide whether AI text is a draft or a contribution before choosing its mark.** A draft the user must verify (summaries, notes about other people) gets a persistent quiet mark (grey ink). A contribution that becomes the user's own (rewrites, generated docs) gets an accept step, then becomes ordinary text with authorship kept in history. A suggestion about structured data gets a dashed chip that turns solid.
47. **Show the proposal where the user's judgment lives:** a diff for people who own the code, a rendered preview for people who own the outcome, the draft for writers.
48. **Give each AI-filled field a trust dial** (show / auto-apply / hide) and dry-run bulk AI on the visible rows before running it on everything.
49. **Never overwrite the human's original.** Keep both behind a two-state toggle.
50. **Agents appear as named authors** in history and activity feeds, acting "on behalf of" a human owner.

## Agency, approval and permissions

51. **Agents stage, humans commit.** End every run with side effects on the prepared state and one yes/no commit whose button names the consequence and updates live. Real-world undo rarely exists, and the button replaces helper text.
52. **Match the gate to rollback cost.** Apply-then-review for cheap undo; stage-and-confirm for irreversible effects. Rubber-stamping and single incidents are the two failure modes.
53. **Money approvals are single-use, time-boxed (30 minutes at most) and void on any change**, and name who handles after-care. These are the guarantees that make delegation safe.
54. **State five things on any purchase or send screen:** amount and recipients in the button, what voids the approval, how long it lasts, who handles returns or replies, where the result will be listed.
55. **Echo rules set in a sentence back as a structured card with Cancel** before they go live ("Buy when 30% off").
56. **Approvals are on screen, even mid-voice.** While waiting, pause; do not fail.
57. **Put the approval on the action row**, quote the exact command, keep Decline next to Approve, make the input the decline channel, and hold prompts while the user is typing.
58. **Describe autonomy levels as plain consequences** on a stepped control, about four per action type. The default can be high autonomy when every action stays inspectable after the fact: trust comes from legibility, not friction.
59. **Separate read, write and spend permissions**, scoped per app or site, granted once / always / never, and log every decision in the conversation.
60. **Use a closed, tiny vocabulary for "your turn" states**, shown on the object, its row and the notification. Learn it once, recognise it everywhere.
61. **Reserve one hue for "the AI is acting"** and put it on the frame of the controlled surface. Agent control must be obvious from anywhere on screen; keep red only for ending a run.
62. **Make safety calls visible and contestable.**
63. **Mark the confirming control for agents too** (`data-agent-confirm`) and give every action a unique verb-plus-object accessible label ("Actions for Jane Doe"). The same labels serve screen readers and automation.
64. **Let the agent's tools be the human's tools** (terminal, browser, files in the same panel), so the human can take over in place.

## Trust, cost, memory and access

65. **Show a privacy mode in three places** (toggle, empty-state explanation, placeholder) and lock it after the first message.
66. **Make memory inspectable and deletable as named, dated items**, or have none. Hidden memory is the one wrong answer.
67. **Publish cost per action, the remaining allowance and the reset time**, and keep a free non-AI path to the same outcome. Hidden metering makes every tap anxious.
68. **At a limit, degrade rather than dead-end**: keep the conversation, drop the expensive part, offer the cheapest way to continue before the upsell.
69. **Put the trust line where the fear is** (under the commit button), and the legal "not advice" line in the footer, never inside answers.
70. **Name the data provider per data type** in a quiet footer.
71. **Reach the result before the wall.** Gate saving and sharing, not the first answer; keep the typed prompt through sign-up; never re-wall content already received.
72. **Run generated artifacts on a separate origin** in a sandbox.
73. **Proactive AI is bounded and steerable**: a finite set of cards on a schedule, feedback on each, a visible pause.
