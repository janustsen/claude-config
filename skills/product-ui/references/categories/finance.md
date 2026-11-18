# Finance

AI-forward money apps: research and markets surfaces that put generated prose next to live numbers, and personal-money assistants that coach behaviour on small budgets. Users judge them on one question: "Can I trust this number, and what does it mean for my money?" A stale or unlabelled number is a nuisance elsewhere; here it causes losses.

Studied:
- **Perplexity Finance** (web): market, ticker, financials, watchlist and portfolio pages plus real AI asks, driven live while logged out. Values come from DOM and computed-style reads, `document.getAnimations()` and MutationObserver timings [obs]. Narrow layout captured at 500px (the headless minimum); dark-mode colours read from computed styles; Screener and Computer were gated.
- **Cleo** (iOS/Android): chat-first money assistant with a persona. Not run (account plus bank link required). Evidence is 10 full-resolution App Store screenshots (v3.90.0), the official "Introducing Cleo 3.0" post and App Store legal text [doc]; roast, hype and nudge behaviour from third-party write-ups [3p]. No Cleo timings.

Tags: [obs] observed live, [doc] vendor docs, [3p] third-party write-up, [inf] inference.

## What users expect

1. **State before value.** Every number says what kind it is: live or closed, estimate or actual, snapshot or calculation, which session, which timezone, as of when. Users act on numbers.
2. **Direction encoded twice.** Colour plus arrow or sign, so up and down survive colour blindness, glare and greyscale screenshots.
3. **Provenance they can check.** A named vendor per data type, trust-tiered citations, a source count on every AI block.
4. **Arithmetic shown, not asserted.** Formula rows, "Here's the math", inputs listed under projections, and maths done by code.
5. **Calm motion.** Money pages are watched for long stretches; a page that twitches reads as panic.
6. **Personal units.** Per-day allowance, debt-free date, "$10,000 would become", every % paired with money.
7. **Permission language at the moment of linking.** Read-only, credentials never stored, processor named.
8. **Tone split by audience.** Research readers want a neutral wire-service register; stressed consumers respond to a persona, but only around the numbers, never inside them.

## The theses to choose from

### Perplexity Finance: generated prose next to live data, never blurred

Core bet: AI is on every page, and each block is narrow, counted, dated and sourced, while live data keeps its own typography, timestamps and motion rules.

- Three type families with three jobs: serif for AI prose (16/26), sans for UI and data, mono for tickers, exchanges and citation domains [obs].
- KPI tile: label plus coloured % on line 1, value plus absolute change on line 2, sparkline with a dashed previous-close baseline [obs].
- Dual quote: "At close: Nov 17, 4:00:00 PM EST" beside "Pre-market: Nov 18, 5:14:07 AM EST", the second ticking to the second [obs].
- Live updates land in one silent batch (4 KPI cards, all crypto rows and "Updated 2 minutes ago" rewritten within 73ms); only one hero price rolls (900ms) [obs].
- Answers stream sources first (count at 1.6s), stop at 2.2s, prose at 6.3s, and never auto-scroll [obs].
- Citations carry a trust tier: a shield chip plus "cnbc.com is trusted for edited business and financial-market journalism" [obs].

Choose this when the reader is professional or semi-professional, the page is dense with live data, and the tone should be neutral.

### Cleo: a persona that turns balances into days and dates

Core bet: a chat-first assistant with a loud voice opens on one personal observation, translates money into time, explains every recommendation with the user's own maths, and leaves the actual maths to deterministic code.

- Home is a sentence, not tiles: "We made a budget last week / Which, based on your spending, you've already forgotten about…" plus one CTA [doc].
- Money typography: small "$", huge integer, small ".00"; "used of limit" as a small "/200" denominator [doc].
- Budgets as "Left of $600", "12 days to go", "$16.67 per day"; payoff as a huge "May 2028" debt-free date plus time saved [doc].
- "Fits your budget ⓘ" opens "Here's the math: $5,000 comes in each payday, and around $4,500 goes out…" [doc].
- Deterministic tools do sums and filters; the LLM interprets and narrates. Cleo published 81% accuracy on 129 real transactions [doc].
- No red: ✗ marks in dark ink, lime status chips, colour identifies product area [doc].

Choose this when the goal is consumer behaviour change, users are anxious and on small budgets, and the product is mobile-first.

## Comparison

| Dimension | Perplexity Finance | Cleo |
|---|---|---|
| Register | Neutral wire-service headlines ("Bitcoin Pinned Below $65,000") [obs] | Persona "she", roast and hype modes; plain language for numbers [doc, 3p] |
| Home | Narrative column plus ~300px reference rail [obs] | One proactive sentence plus one CTA [doc] |
| Where the AI lives | Generated block on every page; docked ask bar; answers open their own session [obs] | Its own tab with the persona avatar, plus an "Ask me anything…" pill on Home [doc] |
| Number state | Session word, date, timezone in header; dual quote; estimates in lighter ink [obs] | Inputs listed under projections; rounding rule printed [doc] |
| Down colour | Muted red `#A23544`, always paired with arrow or sign [obs] | None; ✗ in dark ink [doc] |
| Who does the maths | Model states method and exclusions in prose [obs] | Deterministic tools, model narrates [doc] |
| Provenance | Per-data-type vendor footer, trust-tiered citations, "N sources" per block [obs] | Asterisked fine print under each claim; referral conflict disclosed [doc] |
| Live motion | Silent batches; one rolling hero number; one ping dot [obs] | Voice orb that reacts to listening and speaking [doc] |
| Memory | Not observed (logged out) | Summarised takeaways (goals, stress points); no visible editor found [doc] |
| Gating | Pro/Max tags in menus; gated modals at Screener and Computer; sign-in after first answer [obs] | All 3.0 AI (reasoning, memory, voice) Pro-only; free tier keeps classic chat and budgeting [doc] |
| Mobile | Drops precision first; composer stays docked [obs] | Native; segmented controls, four range pills [doc] |

## Category rules

### Layout and navigation

1. **Nest at most three levels (global shell, section bar, entity bar), put the entity's name in the H1 and its parent in a breadcrumb, and never show section tabs and entity tabs at once**, so the user never wonders which market or company they are in. Perplexity [obs].
2. **Show the reporting state once, at the right of the tab row, in 12px: one state word plus date and timezone** ("Pre-market · Nov 18, 2026, EST"), because every number below means something different pre-market, in session or after close. Perplexity [obs].
3. **Split dashboards into a narrative column (what changed and why) and a reference rail of about 300px (stable lists, your items, prompts), and end the rail with provenance and legal text.** Users learn the rail is lookup, not news. Perplexity [obs].
4. **Use separate controls for navigate and ask**: an entity typeahead at top centre (logo, name, mono `NVDA · NASDAQ`, mono price, delta pill) and an ask composer docked at the bottom with a placeholder naming the current scope ("Ask anything about NVIDIA Corporation financials"). Navigation then never fires an expensive query. When an answer outgrows its page, give it its own address and a one-click way back to the entity ("Deep dive on Perplexity Finance ›"). Perplexity [obs].
5. **Give each entity page one primary non-destructive verb at the top right of its header (☆ Follow), repeated as a trailing icon on every list row of that type. Put chart controls inside the chart frame in the order scope, form, layers, output** (range, line/candle, indicators and compare, screenshot, expand, more), 32-34px tall with 4px gaps, and watermark anything exportable so shared charts keep their brand and timestamp. **More than 5 ranges go in a dropdown labelled with the current range; 4 or fewer stay visible as pills.** Perplexity [obs], Cleo [doc].
6. **For consumer coaching, open on one personalised observation plus one CTA, and keep each top-level page to two sub-views in a segmented control** (Overview | Budget). A sentence about you creates the urge to check. Cleo [doc].

### Numbers, charts and tables

7. **Label the state of every number, and when a metric has an official and a live provisional value, show both side by side with a state label and timestamp each.** Make the headline delta describe the visible range and print the range under it ("Oct 19 to Nov 17, 2026" becomes the subtitle when the range is 1M). Perplexity [obs].
8. **Build KPI tiles as label plus coloured % change (line 1), value plus absolute change (line 2), then a sparkline with a dashed reference line**, and make the comparison metric the most salient, because % is what you compare across tiles and the baseline answers "versus what". Perplexity [obs].
9. **Colour a time series by its sign relative to the period's reference value, label the reference line in place ("Prev close: $155.46"), and mark lower-confidence periods with texture (dotted extended hours), not colour.** Perplexity [obs].
10. **Encode direction twice, and change the delta grammar with density**: arrow plus unsigned % on stand-alone values; the same inside a 9%-alpha tint pill in rail lists; signed text in dense rows; colour only in tables. Transition live colour flips over 200ms. Perplexity [obs].
11. **Lead chart tooltips with time, timezone and session before values, then an aligned two-column list; show secondary stats as a label-value grid (label left, value right when wide; stacked when narrow) and abbreviate to 3-4 significant digits with T/B/M.** Perplexity [obs].
12. **In data tables, render estimates in lighter ink (75%) under an italic header with an "Estimate" ⓘ, derived ratios as italic rows indented 32px at 80% opacity, and the components of any computed total as signed rows above it.** Use a plain minus for negatives, "-" for missing, and red/green only for change, never for accounting sign. Perplexity [obs].
13. **In comparison tables, show 3-5 time horizons as columns, tint the sorted column, round to the precision the decision needs ($258, not $257.89), and print the rounding rule** ("Rounded to whole numbers"). Perplexity [obs], Cleo [doc].
14. **Use `font-variant-numeric: tabular-nums` (or mono) for any number that updates live or aligns in a column**, because proportional digits jitter and rag. Perplexity gets away without it only by right-aligning and batching. [obs, inf].
15. **Clamp heatmaps to a symmetric legend (±3%) with 3 perceptual steps per side and a timestamp in the legend row; show distributions as counts plus a proportional bar, ranges as current against low/average/high on one line, and estimate versus actual as hollow versus filled marks.** Perplexity [obs].
16. **Set hero money with the currency symbol and decimals at 40-50% of the integer's size, cap-height aligned; list stacked-bar segments as dot rows with dotted leaders to right-aligned amounts; show N-of-M goals as one mark per period (hit, miss, future).** Cleo [doc, inf for sizes].
17. **Translate money into time and money into money**: budgets as remaining, days to go and per day; payoffs as a target date plus time saved; every % paired with a currency amount ("$10,000 would become $7,260"). **List the user's inputs under every projection** so it can be checked. Cleo [doc], Perplexity [obs].

### Typography and colour

18. **Give generated prose a different typeface from data and chrome (serif 16/26, answer H2 18/600), set codes and IDs in mono at secondary ink, and keep section headings at body size and medium weight (14/20, 500) on dense pages**, so the reader instantly knows what was written and what was measured, and the numbers stay loudest. Perplexity [obs]. Extends L4.
19. **Define up, down and warn as hue tokens with an alpha ladder (fg 100%, fg-secondary 65%, bg-soft 9%, bg-subtle 5.5%, border 5.5%), using muted mid-dark greens and reds, lifted in dark mode; never pure #00FF00/#FF0000.** Perplexity [obs]. Extends L2.
20. **In stress-prone consumer money apps, encode good and bad with marks (✓/✗), chips and words rather than red, and use colour to identify product areas** (budget sage, advance blue). Cleo [doc, inf].

### Motion and live data

21. **Batch live updates on a 15-60s cadence, swap text silently, refresh "Updated N ago" in the same batch, and animate at most one hero number per view; use one pulsing marker per screen, on the latest entry only.** Motion is attention; when everything moves nothing signals. **Never silently rewrite AI prose someone may be reading**: the market summary regenerated three times in ~45 minutes with changed headlines and no cue, so mark the changed paragraph or regenerate only on user action. Perplexity [obs, inf]. Extends L19.

### AI output

22. **Give every generated block its source count, its generation time and live delta chips for every entity it names ("Microsoft ↘ 2.27%"), and bold every figure in generated prose** so skimmers can read only the numbers. For upcoming events, generate "consensus / track record / what to watch" triplets. Perplexity [obs].
23. **Stream sources first, then live data widgets, then prose; show elapsed time ("Working 5s", then "Finished 5s"); put the shortcut in the stop label ("Stop response (Esc)"); never auto-scroll, and offer a jump-to-latest button that shows stream status.** Users judge the basis before the claim and can read from the top. Perplexity [obs]. Extends L5.
24. **Embed live data widgets above generated prose and initialise their parameters (range, entities) from the question; if widget and prose cover different periods, label both.** Perplexity's widget defaulted to 1D while the prose discussed the month [obs].
25. **Make the model label every number it quotes as live, snapshot or calculated, with period and exclusions** ("excluding dividends, fees and taxes"), **and correct earlier turns explicitly at the top of the new turn** ("One correction to my earlier answer…"). Perplexity [obs].
26. **Never let the language model compute money: route sums, filters and projections to code, have the model narrate the results, and publish accuracy on real data.** This removes the main source of numeric hallucination. Cleo [doc].
27. **Attach a trust tier to each citation (shield icon plus a one-line reason on hover), group several sources per claim behind a pager (‹ 1/2 ›), and let users rate sources**, because in money "where from" is not enough without "should I believe it". Perplexity [obs]. Extends L7.
28. **Back every AI recommendation with a verdict chip and an ⓘ that opens "Here's the math": inputs in and out, the margin left, and the annualised result.** People act on advice they can verify in one read. Cleo [doc].
29. **Seed the ask three ways (scoped placeholder, live headline-based suggestions while typing, 4-6 named presets with one-line descriptions) and offer about 5 entity-specific follow-ups after each answer.** Perplexity [obs]. Extends L20.

### Trust, gating and copy

30. **Name the source of each data class in a quiet persistent footer ("<data type> provided by <vendor>", 12px secondary ink, vendor names linked), keep "not advice" there and repeat it only at action points; inside AI answers, prefer specific trust signals (tier, as-of, method) over boilerplate.** Perplexity [obs].
31. **Directly under any connect button, state access scope, what is stored and the processor** ("Read-only and encrypted. Perplexity never stores your login credentials."), list covered account types before it, and print coverage, data vintage and result cap under every query tool ("Maximum of 1000 equities returned per query"). The fear peaks at the click. Perplexity [obs].
32. **Put fine print directly under each money promise, disclose paid referrals next to the product recommended, keep one source of truth for limits across marketing and product, and keep research surfaces free of money-moving buttons.** Cleo [doc], Perplexity [obs, inf].
33. **Place upsells only where the free path ends, after one real result, with a "Hide" on every persistent promo; tag cost tier in menus (`Max`) and show no quota counter until a limit is near; if AI is the product's identity, gate depth (memory, reasoning, voice), not access.** Perplexity [obs], Cleo [doc]. See L13, L15.
34. **Use personality only in hooks, nudges and empty states; switch to plain declarative copy for every number, fee and legal line; let users choose the tone (roast or hype) as a chat command and mark a flagged transaction as intentional; time nudges to money events (payday, bill due, renewal), not the calendar.** Cleo [doc, 3p].
35. **On narrow screens, drop precision before data**: absolute change, seconds and timezone go first, the % stays; iconify secondary verbs; keep the ask bar docked. Perplexity [obs].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Sidebar | 240px, resizable 200-400px | Perplexity [obs] |
| Reference rail | ~300px | Perplexity [obs] |
| Header state line | 12px; warning/sentiment `rgb(151,67,26)`; 10-segment meter | Perplexity [obs] |
| Ink | primary `rgb(11,40,51)`; secondary 75% alpha; tertiary 50% | Perplexity [obs] |
| Up / down, light | `#016B1D` / `#A23544` | Perplexity [obs] |
| Up / down, dark | `rgb(83,158,85)` / `rgb(220,105,115)`; background ~`#15171B` | Perplexity [obs] |
| Semantic alpha ladder | fg 100%, fg-secondary 65%, bg-strong 100%, bg-soft 9%, bg-subtle 5.5%, border-subtle 5.5% | Perplexity [obs] |
| Tonal button | idle 5.5%, hover 12.5%, active 20% | Perplexity [obs] |
| Type | AI prose serif 16/26, answer H2 18/600; section titles 14/20 500; meta 12/16; KPI name 14/20 500, KPI price 12/16 at 75% | Perplexity [obs] |
| Digit widths (proportional) | ten "1"s 68.3px vs ten "0"s 107.5px | Perplexity [obs] |
| Table | estimates 75% ink, italic header; derived rows italic, indent 32px, 80% opacity; numbers 14px right-aligned | Perplexity [obs] |
| Chart toolbar | controls 32-34px, gaps 4px | Perplexity [obs] |
| Heatmap | 3 OKLCH steps per side, e.g. `--heatmap-positive-1: 0.9566 0.0528 133.18`; negatives hue ~9-12; legend ±3% in six swatches | Perplexity [obs] |
| Motion tokens | quick 75ms (row hover), normal 150ms; ease-out `cubic-bezier(0,0,0.2,1)`; press `cubic-bezier(0.16,1,0.3,1)` | Perplexity [obs] |
| Extra curves | out-quint `(.22,1,.36,1)`, out-soft `(.36,1.3,.64,1)`, in-out-cubic `(.65,0,.35,1)` | Perplexity [obs] |
| Entrance | fadeIn 150ms outExpo; slide offset 5px | Perplexity [obs] |
| Dropdown | in 150ms scale .95→1 + fade `cubic-bezier(0.16,1,0.3,1)` from trigger origin; out 150ms `cubic-bezier(0.7,0,0.84,0)` | Perplexity [obs] |
| Delta colour flip | `color 200ms ease-in-out` | Perplexity [obs] |
| Live batch | all KPI, crypto rows and "Updated" label rewritten within 73ms, no animation | Perplexity [obs] |
| Hero roll | NumberFlow transform 900ms spring-like `linear(…)`, opacity 450ms ease-out | Perplexity [obs] |
| Live ping | `animate-ping` 1s infinite, scale→2 with fade | Perplexity [obs] |
| Answer timeline | route change 516ms / 584ms; shimmer 584ms; sources 1.6s; stop 2.2s; first prose 6.3s; ~300 chars per 1.5s; action row fades in 150ms at end | Perplexity [obs] |
| Widget-first answer | live widget at 1.4s, before prose | Perplexity [obs] |
| Follow-ups | 5 per answer; 6 screener presets | Perplexity [obs] |
| Ranges | dropdown of 9 (1D…MAX, Custom); Cleo 4 pills (1W 1M 6M 1Y) | Perplexity [obs], Cleo [doc] |
| Hero money | currency and cents at 40-50% of integer | Cleo [doc, inf] |
| Savings setup | 5-step segmented progress bar, back and close | Cleo [doc] |
| AI accuracy | 81% on 129 real transactions | Cleo [doc] |

## Anti-patterns seen

- **Proportional digits on live numbers.** Perplexity's `font-variant-numeric` is `normal` everywhere. Fix: `tabular-nums` or mono.
- **AI prose rewritten under the reader.** Perplexity's market summary changed headlines three times in ~45 minutes with no cue. Fix: mark changed text or regenerate on demand.
- **Widget and prose disagreed on the period.** The user asked for "past month"; the widget showed 1D while the prose discussed the month and drew an ASCII bar chart in a code block. Fix: take widget parameters from the question; render the chart as a chart.
- **Dead-end 404.** An unknown ticker showed only "404 Page Not Found / Return home". Fix: keep the search box focused and suggest nearest matches.
- **Mismatched money claims.** Cleo's screenshot says "Up to $250*" while its description says "up to a $500 cash advance". Fix: one source of truth for every limit.
- **Tone misjudging intent.** A reviewer reports Cleo flagged "overspending" on an intentional extra mortgage payment [3p]. Fix: let users mark a transaction intentional so roast and alert logic stops repeating it.
- **Silent memory.** Cleo stores goals and "financial stress points" with no documented editor. Fix: a visible "what I know about you" list with delete.
- **No AI changelog.** Cleo's last 25 release notes all read "Bug fixes & minor improvements". [inf] When AI behaviour changes, say what changed.

## Steal list

1. Label every number live, closed, estimate, snapshot or calculated with an as-of, because an unlabelled stale number is a silent error.
2. Show the reporting frame once in the header (state word, date, timezone), because it frames every card without repeating.
3. Build KPI tiles as % first, value second, sparkline with a dashed reference, because the comparison drives the decision.
4. Colour series by sign against the reference and encode direction twice, because it reads without the axis and survives colour blindness.
5. Batch live updates silently every 15-60s and animate one hero number at most, because a page where everything moves has no signal.
6. Use tabular figures for updating or aligned numbers, because proportional digits jitter.
7. Set generated prose in its own typeface, because readers must tell written from measured at a glance.
8. Give every AI block a source count, a generation time and live entity chips, because that makes AI text auditable and keeps quoted numbers fresh.
9. Stream sources, then data widgets, then prose, without auto-scroll, because users judge the basis before the claim.
10. Compute money in code and let the model narrate, because the model is the hallucination source.
11. Explain every recommendation with "Here's the math" from the user's own inputs, because verifiable advice gets acted on.
12. Show formula rows above totals and estimates in lighter ink, because skeptics need to rebuild a number in place.
13. Separate navigate from ask and scope the ask placeholder to the page, because one control per intent prevents wasted queries.
14. Put scope and storage promises directly under the connect button, because the fear peaks at the click.
15. Translate money into days, dates and per-day amounts, because a date is easier to act on than a balance.
16. Keep personality around numbers, never inside them, because money facts must read the same to everyone.
17. Rate citation sources with a one-line reason, because "where from" needs "should I believe it".
18. Drop precision before data on narrow screens, because the % is the decision and seconds are not.
