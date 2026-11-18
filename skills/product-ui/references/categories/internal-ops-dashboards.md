# Internal operations dashboards

Internal tools that a small team opens many times a day: a CRM, an agent command center, a reporting page, an approvals queue. They are not read for pleasure; they are checked. The center of gravity is one question: "What needs me, and is the system working?" Everything on the page either answers that question, explains a number behind it, or gets out of the way.

Built from: the dashboard anatomy of a live finance research surface (freshness strip, KPI tiles, generated "what changed" prose, event timeline, tables, provenance footer, scoped ask bar), measured in the Finance chapter [obs]; the proactive-home and event-timed nudge patterns of a consumer money assistant [doc]; and cross-product principles for agent operations tools [know]. No internal tool was driven for this chapter, so values marked [obs] are carried over from the finance measurements and should be treated as starting points.

## What users expect

1. **What needs me, first.** The top of the page is the short list of items only a human can unblock, because that is why they opened it. See L17.
2. **Needs-you kept apart from FYI.** Mixing "approve this" with "agent finished that" buries the one item that matters under ten that do not.
3. **What happened since I last looked.** New items marked as new (a dot) and counts on their sections, not a greeting and not a sentence restating those counts.
4. **Is the data fresh?** Period and as-of on reporting numbers; on a live queue, nothing while it is live and a plain warning when it is stale or offline, because a stale number is a silent wrong decision and a "Live" label on every visit is noise.
5. **Each fact said once.** A number in a tile, again in the prose and again in a table reads as three facts and invites "which one is right?".
6. **Agents visible as teammates.** Who is working on what, who is waiting on me, who is stuck, and a receipt for what each one did.
7. **Approvals that name the consequence.** "Send to <name>" tells the reviewer what the click does; "Approve" does not.
8. **A stop where the work is.** Pause or stop on the agent's own row and progress line, not in settings.
9. **Calm.** One accent, red only for real failure, nothing moving on its own, because the page is glanced at dozens of times a day.

## The theses to choose from

### Inbox first: the page is a queue

Core bet: the home is the list of things that need a human, ranked by consequence; metrics and history are one level down.

- Needs-you section at the top, each item an actionable card (approve, reply, decide) [know].
- FYI collapsed below as a dated feed with no badges [know].
- New items since the last visit get a dot; the needs-you count sits on its section, done items on a counted shelf. No summary sentence restating those counts [know].
- Empty queue written as good news: "Nothing needs you." [doc pattern: "No more bills this week"].

Choose this when most visits end in a decision: CRM follow-ups, support, approval-heavy workflows.

### Report first: the page explains the numbers

Core bet: freshness strip, KPI row, a generated "what changed" paragraph, then the timeline and tables that back it, with provenance at the end.

- Freshness strip at the right of the tab row, 12px: period, "as of 09:40 CET", state word [obs].
- Four equal KPI tiles with a dashed reference line (target or previous period) [obs].
- Serif "what changed" block with inline entity chips and bold figures, "N sources · Updated 4 min ago" [obs].
- Dated event timeline explaining each notable jump, linked to source records [obs].

Choose this when visits are reviews: weekly reporting, finance and growth pages, leadership dashboards.

### Command center: agents are the staff

Core bet: the page is a roster of agents with state pills and receipts, plus the approval cards they raise.

- Roster rows: agent name, current task in one line, state pill, last receipt, stop and pause on the row [know].
- Live progress as one line per running agent, collapsing to a receipt (see L5) [know].
- Drafts arrive as approval cards whose primary button names the consequence ("Send to <name>") [know].

Choose this when agents do most of the work and the human's job is to unblock, review and correct them.

Most real tools combine them in this order: needs-you, agents, KPIs, what changed, timeline and tables. Freshness and provenance appear where a number is reported, not as permanent strips over a queue.

## Comparison

| Dimension | Inbox first | Report first | Command center |
|---|---|---|---|
| Top of page | Needs-you queue | Freshness strip + KPI row | Agents waiting on you, then running agents |
| Unit of content | Actionable card | KPI tile, sentence, row | Roster row, receipt, approval card |
| Generated text | One-line item summaries | "What changed" paragraph | Receipts and drafts |
| Badges | Needs-you count only | None | Waiting-on-you count only |
| Primary action | Decide the item | Drill into a number | Approve, stop, pause |
| Freshness signal | None while live; a warning when stale | As-of time in the header | Per-agent last activity on hover |
| Failure display | Item flagged "Failed" with cause | Source marked stale in strip and footer | State pill "Failed" with cause and retry |
| Live updates | New items appended silently | Values swapped silently in batches | Pills and progress lines swapped silently |
| Typical visit | 30 seconds, ends in a click | Minutes, ends in understanding | Seconds, ends in "all fine" or an unblock |

## Category rules

### Page structure

1. **Order the page to answer "what needs me, and is the system working?" before anything else**: needs-you, then running work, then KPIs, narrative, timeline and tables. Anything that does neither waits below the fold. "Is it working" is answered by the absence of failures, not by a status sentence. [know]. See L17.
2. **Keep needs-you and FYI in separate sections, and never interleave them in one feed.** Needs-you items leave the list only when a human resolves them; FYI items age out. One "approve" hidden among ten "done" lines is a missed approval. [know].
3. **Replace the greeting with nothing.** The section counts and new-item dots answer "what changed"; a summary sentence above them says it a second time. Use a since-last-visit line only on a screen that has no counted sections. [know].
4. **On a reporting page, show the reporting frame once, in a 12px strip at the right of the tab row: period and "as of HH:MM TZ"; add a state word only when it is not final (Provisional, Stale).** Every number below inherits this frame instead of repeating it. A queue or inbox has no strip. [obs].
5. **On a reporting page, a reference rail of about 300px (saved views, connected sources) may sit beside the narrative.** On a queue, the detail view is one column; sources and history open on demand. [obs].
6. **Say each fact once.** Give every fact one home (a tile, a row, an item); everywhere else it appears as a chip that links to that home, never as a restated sentence. A detail view does not repeat the selected row; a summary line does not repeat the section counts. [know].

### KPI tiles and numbers

7. **Build KPI tiles as label plus change on line 1, current value plus absolute change on line 2, then a sparkline with a dashed reference line (target or previous period, labelled in place).** Use four equal tiles. Make the comparison the most salient element, because the delta drives the decision and the reference answers "versus what". [obs].
8. **Label the state of every number that is not final (Provisional, Estimate, Forecast), and when an official and a provisional value both exist, show both side by side with a label and time each.** Estimates and forecasts go in lighter ink (75%). [obs].
9. **Encode direction with arrow or sign in ink, add a muted caution hue for unfavourable deltas, and never use the failure red for a falling KPI.** A down week is information, not an incident. [obs, know].
10. **Use `font-variant-numeric: tabular-nums` for every number that updates or aligns**, because proportional digits jitter on refresh and rag in columns. [obs, inf].

### "What changed" narrative

11. **Put one generated "what changed" block above the tables, set in a prose typeface distinct from data (serif 16/26), with inline entity chips carrying live values ("Region North ↘ 4.1%"), every figure bolded, and a footer "N sources · Updated 4 min ago".** It turns tiles into a story and stays auditable. [obs]. Extends L4.
12. **Compute every figure in the narrative with queries, have the model only narrate, and label each quoted figure with its period** ("week to Sunday, excluding refunds"). The model is the hallucination source; the query is checkable. [doc, obs].
13. **Regenerate the narrative on data refresh, mark the paragraph when it changed ("Updated 09:40, was 09:10"), and never rewrite it while someone is reading.** A silent rewrite mid-sentence was observed on the finance surface and is a trust failure. [obs, inf].

### Event timeline and upcoming items

14. **Explain each notable KPI jump in a vertical timeline: date and time on the left, a one-paragraph explanation, a link to the source records and a source count.** Use a fixed-height card with internal scroll and a bottom fade. Mark only the latest entry as current, in words, not with a pulse. [obs].
15. **For each scheduled item (renewal, payroll run, launch, contract end), show three bullets: what is expected, the track record, and what to watch.** It prepares the decision before the date. [obs].

### Tables

16. **Show 3-5 horizons as columns (Today / 7D / 30D / QTD), tint the sorted column and mark it with a caret, right-align tabular numbers, round to the precision the decision needs, and print the rounding rule.** Several horizons answer "blip or trend" in one glance. [obs].
17. **Show the components of any computed total as signed rows above it, render derived ratios as italic rows indented 32px at 80% opacity, use a plain minus for negatives and "-" for missing values, and put export at the top right of the table toolbar.** Skeptics can rebuild the number without leaving the table. [obs].

### Provenance and connections

18. **End a reporting page (not a queue) with a quiet provenance footer naming the source of each data class with its last sync time** ("Orders from <store platform>, synced 09:38 · Ad spend from <ad platform>, synced 06:00 · Payroll from <payroll provider>, synced Mon"), in 12px secondary ink with linked names, plus "Updated N ago" on each block. A skeptic can trace one number's origin. [obs].
19. **Directly under any connect-a-source button, state access scope (read-only or write), what is stored (never credentials) and the processor; under any query tool, state coverage, data vintage and result cap in one line.** The doubt peaks at the click. [obs].

### Ask bar

20. **Dock one ask bar at the bottom of the content column with a placeholder scoped to the current page ("Ask about Q4 margins"), kept separate from navigation search (see L18).** Navigating never fires an expensive query, and the question stays grounded in what is on screen. [obs].
21. **Stream answers as sources first, then tables or charts with parameters taken from the question, then prose; never auto-scroll; numbers come from queries, each labelled with its period.** [obs]. Extends L5.

### Agents as teammates

22. **List agents like colleagues: avatar, name, current task in one line, and a state shown by icon and position (Working rows recede, Failed is red, Waiting on you is in needs-you).** Last activity and last receipt on hover or in the detail. The roster answers "is the system working?" in one scan. [know].
23. **Leave a receipt for every finished agent run: one line of what it did with counts and duration, links to every object it touched, and undo where the action allows it.** A spinner that just disappears gives no evidence it worked. [know]. See L5, L10.
24. **Review drafts as the recipient will see them: the recipient as an avatar chip, the subject as the first line, the body, and a primary button that names the consequence ("Send to <name>", "Post to #channel", "Charge $420").** No "To" or "Subject" labels, no "drafted for you" line, no helper text under the button. Pair it with Edit and Discard. Batch approval only for identical consequences, with the count in the button ("Send 4 replies"). [know]. See L9.
25. **Put stop and pause wherever an agent's work shows: its roster row, its live progress line, and its detail view.** Pause keeps state; stop leaves a receipt of the partial work. A stop buried in settings is a stop nobody reaches in time. [know].
26. **A waiting agent's request lives in needs-you; its roster pill reads "Waiting on you" and links there**, so the fact has one home (rule 6). [know].

### Badges, colour and motion

27. **Badge only what needs a human: count badges appear on needs-you and nowhere else, and the badge number always equals the length of that list.** A badge on every tab trains users to ignore badges. [know].
28. **Use one accent for the primary action and selection only, and reserve red for real failure: a failed run, a broken sync, data or money at risk.** Warnings use amber, unfavourable deltas use a muted caution hue. When red means failure, a red pill gets read. [know]. Extends L1.
29. **Nothing animates on live data: swap values silently in batches every 15-60s and use no rolling digits, flashes or pulsing rows.** Say nothing about liveness while it is live; say "Offline" or "Stale since 09:40" when it is not. Motion belongs to the user's own actions (see L19). This is stricter than the finance surface, which rolls one hero number. [obs, know].

### Mobile and copy

30. **On narrow screens keep needs-you first, drop precision before data (absolute change, seconds and timezone go first, the % stays), render approval cards full width with the named button intact, and keep the ask bar docked.** [obs, know].
31. **Write headlines as subject, verb, number ("Refunds rose 18% this week"), body as claim, evidence, caveat, and empty states as good news** ("Nothing needs you."). Errors name the cause and the next action (see L16). [obs, doc].

## Measured constants

Carried over from the finance dashboard measurements [obs] unless marked otherwise.

| What | Value | Source |
|---|---|---|
| Freshness strip (reporting pages only) | 12px, right of the tab row; period + as-of; a state word only when not final | [obs] |
| Reference rail | ~300px; sidebar 240px, resizable 200-400px | [obs] |
| KPI row | 4 equal tiles; name 14/20 weight 500; secondary value 12/16 at 75% ink | [obs] |
| Ink roles | secondary 75% alpha, tertiary 50% | [obs] |
| Estimates and forecasts | 75% ink, italic header with ⓘ | [obs] |
| Derived rows | italic, indent 32px, 80% opacity | [obs] |
| Table numbers | 14px, right-aligned, tabular | [obs, inf] |
| Narrative prose | serif 16/26; section titles 14/20 weight 500 | [obs] |
| Semantic tint ladder | fg 100%, fg-secondary 65%, bg-soft 9%, bg-subtle 5.5%, border 5.5% | [obs] |
| Tonal button | idle 5.5%, hover 12.5%, active 20% | [obs] |
| Muted up / down (light) | `#016B1D` / `#A23544`; keep the down hue distinct from the failure red | [obs, know] |
| Row hover | 75ms | [obs] |
| Menus and popovers | 150ms in, strong ease-out `cubic-bezier(0.16,1,0.3,1)`, from trigger origin; 150ms out ease-in | [obs] |
| Entrance offset | ≤ 5px | [obs] |
| Live batch cadence | 15-60s; all values and "Updated N ago" rewritten together (observed batch: 73ms) | [obs] |
| Toolbar controls | 32-34px tall, 4px gaps | [obs] |
| Comparison horizons | 3-5 columns | [obs] |
| Upcoming-item bullets | 3: expected, track record, what to watch | [obs] |

## Anti-patterns seen

- **Greeting as the hero.** "Good morning!" in 32px with nothing about what changed. Fix: the queue itself, with its counts on its sections.
- **A summary sentence restating the counts.** "Since yesterday: 4 need you, 11 done, 1 failed" above a badged needs-you section and a "Done 11" shelf. Fix: delete it.
- **The detail repeats the row.** Type, agent, client and age on the row, then again under the detail title. Fix: the title alone.
- **Needs-you mixed into the activity feed.** The one approval scrolls away under agent chatter. Fix: two sections, needs-you first.
- **Badges everywhere.** Every tab carries a count, so none means anything. Fix: badge only needs-you.
- **The same number three times.** A KPI in a tile, restated in the narrative and again in a summary table, each rounded differently. Fix: one home per fact, chips elsewhere, rounding rule printed.
- **Red for a down week.** A falling KPI in the same red as a failed sync. Fix: muted caution hue for deltas, red for failure only.
- **Rolling counters and flashing cells on refresh.** The page twitches every few seconds. Fix: silent batched swaps and a visible "Updated N ago".
- **AI summary rewritten under the reader.** Observed on the finance surface [obs]. Fix: mark changes or regenerate on demand.
- **"Approve" with no consequence.** The reviewer cannot tell whether it sends, posts or charges. Fix: name it ("Send to <name>").
- **Stop control in settings.** By the time the user finds it, the agent has finished. Fix: stop and pause on the row and progress line.
- **Agent status as an endless spinner.** No receipt, no last-activity time. Fix: state pill plus receipt.
- **KPI without a reference line.** "$48,200" with no target or prior period. Fix: dashed reference, labelled.

## Steal list

1. Answer "what needs me, and is the system working?" at the top, because that is why the page was opened.
2. Keep needs-you and FYI in separate sections, because one approval in a feed of ten updates gets missed.
3. Replace the greeting with nothing; counts live on their sections and new items carry a dot, because a sentence restating them is the same news twice.
4. On reporting pages put period and as-of in one header strip, because every number inherits its frame; on queues say nothing until data is stale.
5. Give every fact one home and link to it elsewhere, because repeated facts drift and invite doubt.
6. Build KPI tiles as delta first, value second, sparkline with a labelled dashed reference, because the comparison drives the decision.
7. Write one "what changed" paragraph with live chips and bold figures, computed by queries and narrated by the model, because it is readable and checkable.
8. Explain each KPI jump in a dated, sourced timeline, because "why did it move" is the next question.
9. Show formula rows above totals and estimates in lighter ink, because skeptics rebuild numbers in place.
10. On reporting pages, name each data source and its last sync in the footer, because one stale source can poison a page.
11. Scope the ask bar to the page and keep it apart from navigation, because questions stay grounded and navigation stays cheap.
12. Show agents as teammates with avatars, a state icon and receipts on demand, because "is it working?" needs evidence, not a spinner or a pill on every row.
13. Name the consequence on every approval button ("Send to <name>"), because the reviewer must know what the click does.
14. Put stop and pause where the agent's work shows, because a stop must be reachable in time.
15. Badge only what needs a human, one accent, red only for failure, because scarce signals get read.
16. Let nothing animate on live data, because a page checked dozens of times a day must not twitch.
