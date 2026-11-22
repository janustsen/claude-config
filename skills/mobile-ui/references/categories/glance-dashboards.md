# Glance dashboards and system health

Data-at-a-glance home screens and "is the system working" health views. The references are two weather apps, because weather is the best-made glance dashboard on the phone: the system's calm, fixed baseline (Apple Weather) and a dense, user-arranged one with a voice (CARROT Weather). Live status card rules come from the steal lists of Flighty and Uber. Users judge this category on one question: "Do I need to act?" The first screen must answer it with no scrolling: one number or verdict, its state, and what comes next. Detail is one tap away and built the same way everywhere.

Studied (no live app was driven):
- **Apple Weather** (iOS 26) v2.8: 3 framed renders cut to 402pt (±2%), the iPhone User Guide. Scroll motion and the lower tiles are prior knowledge, with tile sizes derived from the measured margins.
- **CARROT Weather** v6.9.3 (layout from the 6.0 redesign): raw full-bleed 393pt @3x press-kit screenshots (exact), App Store renders, the support FAQ, MacStories reviews of the layout editor. All measured screens use iOS 17-era chrome, so tab and nav bar numbers predate Liquid Glass.
- **Flighty** and **Uber**: only their steal lists and category note, for the status-card rules. Their full chapters are in live status and maps.

Tags: [meas] measured, [obs] seen in a capture, [doc] the maker's docs, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **An answer to "do I need to act?" on the first screen, without scrolling** (Apple Weather, CARROT category notes).
2. **One big number or verdict, a state symbol, and the next few hours.**
3. **Detail one tap away, identical in structure for every metric.**
4. **Alerts that appear only when something is wrong, ranked first, and leave when it clears.**
5. **Notifications only for thresholds**, so routine values never train them to ignore the app (Apple Weather).
6. **Stale data labelled where it sits**, and nothing said while it is live (Flighty).
7. **Status in words for the glance, numbers for the check** (CARROT's verdict word, Apple's word legends).

## The theses to choose from

### Apple Weather: one number, then everything else
Core bet: a single thin hero number over a background that is itself the state, then a scroll of uniform modules on a darker material.
- Hero temperature about 98pt thin, centred, in the top third; only the place above and the condition and "H:77° L:53°" below [meas].
- The whole screen is an animated sky for the condition and time; each list card previews its city's own sky [obs].
- Every module is the same panel: 20pt screen inset, about 11pt gap, 16pt padding, one continuous corner of about 12pt [meas].
- The 10-day list is a chart in disguise: each row's range bar sits on one shared scale, with a ringed dot for now on today [obs].
- Alert modules (severe weather, notable air quality, rain within the hour) are inserted only while the condition holds [doc].
- The hero shrinks into a pinned one-line header on scroll and module headers pin as they pass [know].

Choose this for a calm, read-only glance surface where nothing is configured.

### CARROT: one expressive band, plain data modules, a layout the user owns
Core bet: personality and state live in one band at the top; everything below is stock inset-grouped cards that the user arranges, with modules that show themselves when their condition holds.
- The top about 45% is a state-coloured sky with the hero number and one line of dialogue; data cards are white on #f2f2f7 with a 13pt grey caps header [obs, meas].
- Active modules are titled with the finding ("⚠ Tornado Warning", "Heavy Rain for Next Hour"), inserted first, and removed when the condition clears [obs].
- Show-rules are sentences with tappable tokens ("Show when **20 mph** or above over next **12 hrs**") [obs].
- Only the tile past its threshold is filled accent blue; the rest are outlined [obs].
- One metric chip row re-plots the hourly line and switches the daily card to the same metric [doc, obs].
- The Weather tab icon shows the current condition [obs].

Choose this for an operational dashboard whose users differ in what they watch: CARROT's conditional, finding-titled modules and editable thresholds map directly onto system health (CARROT category note).

## Comparison

| Dimension | Apple Weather | CARROT |
|---|---|---|
| State field | whole screen, animated sky [obs] | top band only (about 45%); cards neutral [obs] |
| Hero | about 98pt thin, centred [meas] | about 46pt regular rounded, beside a 62pt icon, plus one dialogue line [meas] |
| Hero height | fixed block [meas] | follows its copy: cards start at y 374 or 353 [meas] |
| Modules | translucent panel darker than the sky (#3777bc on #4c87c3) [meas] | opaque white on #f2f2f7; #1c1c1e on #000 in dark [meas] |
| Grid | 20pt inset, about 11pt gap, 16pt padding [meas] | 16pt margin, 14pt gap, about 17pt padding [meas] |
| Corner | about 12pt continuous [meas] | about 12pt [meas] |
| Module header | title 16pt semibold + 13pt subtitle + segmented glass control (iOS 26) [obs] | 13pt glyph + 13pt semibold grey caps, hairline under [meas] |
| Data rows | 49pt with separators inset to the text [meas] | 44pt, no separators [meas] |
| On scroll | hero shrinks to a pinned one-line header [know] | hero scrolls away; nav becomes a solid 98pt bar in the sky colour [meas] |
| Alerts | inserted module at the top [doc] | inserted card titled with the finding, "Also: …" for the rest [obs] |
| Layout | fixed [know] | user list of sections, live gallery, Smart Layouts by context [obs] |
| Shell | pages per location, bottom glass toolbar [meas] | 5-tab bar, user-arrangeable, live tab icon [obs, 3p] |
| Voice | none; one plain verdict sentence per tile [know] | a character, after the fact, off in alerts and in "professional" mode [doc] |
| Non-content words | home 9, list 23 [obs] | home 11 in the reading lane [obs] |

## Category rules

### The top: verdict and state

1. **Pick the one number or verdict the user opens the screen for and make it at least 5x body size, alone in the top third**, because a glance takes about a second and only one thing gets read. Apple Weather [meas].
2. **Use a thin weight only for the hero and medium or semibold everywhere else**, because the weight contrast, not size alone, makes it the hero, and thin is illegible small. Apple Weather [meas].
3. **Encode overall state in one large colour field (calm, warning, incident, night) and keep data modules neutral**, because state is read before any text and neutral modules stay legible in every state. Apple Weather [obs], CARROT [obs, meas].
4. **Let the hero's height follow its content and start the first module right after it**, because a fixed hero box wastes the first screen on calm days; CARROT gains 21pt when its line is short. CARROT [meas].
5. **Overlap the first module onto the bottom of a decorative band and fade the art into the page colour**, so the home does not read as two screens. CARROT [meas].
6. **Keep the key number visible after scrolling**: shrink the hero into a pinned one-line header (Apple Weather [know]) or collapse the header into a solid bar in the state colour that keeps the title (CARROT [meas]).
7. **Let a root tab's icon show the worst live state**, because the tab bar is on every screen. CARROT [obs].

### Modules

8. **Build the home from one module component with fixed inset, gap, padding, radius and header**, because a uniform grid grows by adding modules and user-arranged layouts then look designed. Apple Weather 20 / 11 / 16pt, CARROT 16 / 14 / 16-17pt, both about 12pt corners [meas].
9. **Make the gap smaller than the padding**, so modules read as one grouped surface. Apple Weather [meas].
10. **Use one continuous corner for every module** (`borderCurve: 'continuous'`), because mixed radii look assembled. Apple Weather [meas].
11. **Size half-width tiles as (W − 2·inset − gap) / 2 and keep them square** (about 175pt on 402pt), so they reorder freely. Each tile: icon and caps label, a big value, a one-line visual, one plain sentence that interprets it. Apple Weather [know, derived].
12. **Set module headers smaller and greyer than the data (13pt caps grey against 17pt values)**, because the header is wayfinding. CARROT [meas], Apple Weather [obs].
13. **Put modules on a material darker than a coloured background, or on the system grouped pair (#f2f2f7 / white; #000 / #1c1c1e)**, never on opaque white over a colour field, so contrast stays fixed across states. Apple Weather [meas], CARROT [meas].
14. **Spend hue only on data (gradients, ramps, symbols) and keep all text one colour at 2-3 opacities**, so hue always means something. Apple Weather [obs]. Colour chart lines and bars by the value they show, one scale per metric, so the colour is the legend. CARROT [obs].
15. **Make every module tap through to a detail sheet with a day strip, one chart and a written summary**, because the chart shows shape and the sentence states the conclusion. Apple Weather [know, doc].
16. **Keep ambient motion slow, in the decorative band only, and frozen under Reduce Motion; keep data still.** Apple Weather [know], CARROT [obs].

### Alerts and conditional modules

17. **Insert attention modules at the top only while their condition holds, order them by urgency, and remove them after**, because a permanent "all clear" is chrome and a conditional module is news. Apple Weather [doc], CARROT [obs].
18. **Title an active module with its finding ("Heavy Rain for Next Hour", "⚠ Tornado Warning" in red), not its category**; calm modules keep small grey caps headers. CARROT [obs].
19. **Put concurrent secondary issues on the same card as "Also: …"**, because two stacked red cards halve each other's weight. CARROT [obs].
20. **Give expiry or age as a clock time plus a relative countdown ("Expires at 3:45 PM … (43 mins)")**, because people act on the countdown and verify against the clock. CARROT [obs].
21. **Fill only the tile that crossed its threshold and outline the rest**, so the grid is a status board. CARROT [obs].
22. **Omit modules with no data instead of showing them empty, and default multi-mode views to the mode the data makes relevant** (the map picks rain when rain is coming). Apple Weather [doc].

### Rows, charts and scales

23. **Draw per-row ranges as short capsule tracks (about 96x4.5pt) on one shared scale, numbers outside each end, and a ringed dot for now on the current row**, so rows compare without axes. Apple Weather [meas, obs].
24. **Dim the low or secondary value and keep the primary in full ink, labelled by a single letter or by weight alone** ("H:77° L:53°", or grey min and black max with no labels). Apple Weather [obs], CARROT [obs].
25. **Separate dense rows by rhythm (44pt) instead of hairlines, or inset separators to the text and drop the last one inside a module.** CARROT [meas], Apple Weather [meas].
26. **Print values on the line and drop the y-axis and gridlines; set AM/PM smaller than the digits.** CARROT [obs].
27. **Put events into the time axis at their exact time** (sunset "8:05" as its own column), because an even grid hides when the thing happened. CARROT [obs].
28. **Give every chart slot a faint track even at zero**, so zero and no data look different, and map probability or confidence to opacity. CARROT [obs].
29. **Write a status as number, bold one-word verdict, plain consequence sentence, scale with a marker** ("75 · **Moderate.** Unusually sensitive people should…"), serving glances of 1, 2 and 5 seconds. Use word scales in legends (Extreme / Heavy / Moderate / Light). CARROT [obs], Apple Weather [obs].

### Controls and customisation

30. **Put the metric switcher inside the chart's card as a scrolling chip row (30pt pills) clipped hard at the card edge, and let it drive every module that shares the axis.** The cut word is the "more" signal. CARROT [meas, doc].
31. **Swap a card's body between two views of the same data with a two-pill toggle** (Precip Chart / Mini Map), keeping its place on the home. CARROT [obs].
32. **Make customisation a plain list of sections with Edit and "Add Section +" last; add from a sheet gallery of modules rendered live with real data; preview changes on the real screen with Set / Cancel.** CARROT [obs, 3p].
33. **Write show-rules as sentences with tappable tokens, allow the same module type twice with priority order, and switch whole layouts by context (night, rain)**, because what you need during an incident is a different dashboard. CARROT [obs, 3p].
34. **Gate a complex editor's advanced options behind first use, with a visible skip.** CARROT [obs].
35. **For peer dashboards (locations, environments), make each a swipeable page with dots in a bottom glass capsule and keep the list one tap away; let each list card preview its item's state.** Apple Weather [doc, obs]; CARROT lets each row carry an optional mini chart chosen per site [3p].

### Live status cards (Flighty, Uber)

36. **Define the 5-10 phases of the live thing and swap the card's lead line by phase, not by user action.** Flighty [doc, obs].
37. **Order a live card identifier, big time or value, one status word, location badge; or rank facts P0 time, P1 identity, P2 progress.** Flighty [doc, obs], Uber [doc].
38. **Follow the status headline with one sentence of cause, and give problem states cause, probability and duration** ("grounded for the next 42m due to thunderstorms. Probability of extension is 30-60%"). Flighty [obs].
39. **Show a changed value big with the old value struck through beside it, and a prediction labelled next to the official value.** Flighty [obs, doc].
40. **Use a four-meaning status palette with light and dark pairs (green, amber, red, grey for not-yet), colour only what is live, and give one filled badge per block to the most actionable token.** Check contrast per background rather than trusting system defaults. Flighty [meas].
41. **Show the verdict on a faint tinted band (about 3% hue) instead of a bordered alert box.** Flighty [meas].
42. **Leave a slot empty while a value is unknown instead of faking one; shape progress so the last N% covers the last few minutes; switch a duration to a clock time when the question changes.** Uber [doc].
43. **Label stale data in place ("Offline Mode · Estimating all times") and say nothing while live; count down to the minute ("1h 42m").** Flighty [doc, obs].
44. **Use a Live Activity only for bounded processes (compact: countdown leading, capsule trailing; minimal: circular progress), with server-driven, debounced updates the server ends.** Flighty [doc], Uber [doc].

### Notifications and daily insights

45. **Notify only on threshold events, tiered by consequence (Critical, Time Sensitive, normal), written as fact plus distance or time ("Strike detected 0.8 mi to the south"), and let each source opt in.** Apple Weather [doc], CARROT [obs]. Flighty's grammar: "{object} • {event}" / "{new value} ({delta})" [doc].
46. **Drop any voice where stakes are real**: CARROT's critical alerts carry no persona, and its "professional" mode removes the jokes [obs, doc].
47. **Deliver a one-off daily insight ("7° warmer than yesterday") as a toast above the tab bar on first open, not as a module.** CARROT [meas, doc].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Hero | 98pt thin, y 175-245 on 402pt; condition and H/L 20pt medium; place 34pt regular | Apple Weather [meas] |
| Hero (band) | about 46pt regular rounded, 62pt icon; "Feels" about 15pt at 60%; dialogue about 17pt medium, 21pt pitch, inset about 48pt | CARROT [meas] |
| Hero → first module | about 24pt | Apple Weather [meas] |
| Module grid | 20pt inset, 362pt wide, about 11pt gap, 16pt padding, about 12pt continuous corner | Apple Weather [meas] |
| Module grid | 16pt margin, 361pt card, 14pt gap, about 17pt padding, about 12pt corner; header cap 19pt below the top, 13pt glyph, 8pt gap, hairline #e5e5ea | CARROT [meas] |
| Half-width tile | about 175pt square on 402pt | Apple Weather [derived] |
| Hourly strip | 7 columns at 51.5pt; "Now" 17pt semibold; symbol about 22pt; value 20pt medium | Apple Weather [meas] |
| Hourly chart | 46pt column pitch, 8 visible | CARROT [meas] |
| 10-day row | 49pt; day 20pt medium; range track 96x4.5pt | Apple Weather [meas] |
| Daily row | 44pt; bars 6pt on #e6e5eb | CARROT [meas] |
| Minutely chart | 30 bars, 6.7pt wide, 3.7pt gaps (11pt pitch), #007aff on faint tracks | CARROT [meas] |
| Chips and toggles | chips 30pt, 1pt outline, about 9pt gap; two-pill toggle 159pt each, 8.7pt gap | CARROT [meas] |
| Alert card | 93pt tall at y 353 | CARROT [meas] |
| Daily toast | 56pt, 11pt inset, about 12pt radius, shadow, floats 11pt above the tab bar | CARROT [meas] |
| Scrolled header | solid 98pt bar in the state colour | CARROT [meas] |
| Bottom toolbar | 46pt circles; page-dot capsule about 150x44pt; about 28pt above the bottom | Apple Weather [meas] |
| Location cards | 16pt inset, about 99pt tall, 11pt gaps, corner about 16pt; temperature about 52pt light | Apple Weather [meas] |
| State colours | day sky #4c87c3 with module #3777bc (Apple); CARROT day #0077f8, night #110150, storm #001986, sunset #ff5993→#fe1e73 | [meas] |
| Status palette | green #00A05A / #00FF8E, amber #FFC100 / #FFBB00, red #ED0001, grey not-yet; filled badge 72x31pt #FFC100; verdict band #F6FBFA | Flighty [meas] |
| Live detail sheet | opens at about 42% | Flighty [meas] |
| Commit | black, full width, 56pt, verb + object ("Confirm pickup") | Uber [meas] |
| Non-content words | Apple home 9, locations list 23, map about 12; CARROT home 11 (16 with tabs), layout settings about 20 | [obs] |

## Anti-patterns seen

- **A list of dashboards repeats its labels.** Apple Weather's locations list carries 23 non-content words, 14 of them "H" and "L" repeated across 7 cards [obs]. Fix: drop the letters once the order is learnt, as CARROT does with grey min and black max.
- **A helper sentence in settings.** CARROT's Layout screen opens with a 14-word sentence about Smart Layouts [obs]. Settings may talk, but this is the bulk of the screen's chrome.
- **Banner ads on a free tier** of a dashboard (CARROT) [3p]: noise in the one place built for calm.
- **No persistent number after scroll.** CARROT's hero scrolls away and leaves only the title on a coloured bar, unlike Apple's compact "61° | Mostly Sunny" [meas, know].

## Steal list

1. Make one number or verdict the hero, thin and at least 5x body, because a glance reads one thing.
2. Encode overall state in one colour field and keep modules neutral, because state reads before text.
3. Build every module from one component with fixed inset, gap, padding and corner, because the grid then grows without redesign.
4. Insert attention modules at the top only while their condition holds, titled with the finding, because order and headline should rank what matters now.
5. Fill only the tile past its threshold, because equal tiles carry no status.
6. Write status as number, verdict word, consequence, scale, because each layer serves a deeper glance.
7. Draw row ranges on one shared scale with a dot for now, because rows then compare without axes.
8. Let one chip row drive every chart on the screen, because the question is about a metric.
9. Give every chart slot a faint track and map confidence to opacity, because zero, no data and uncertain must differ.
10. Put events on the time axis at their exact time, because an even grid hides when it happened.
11. Write show-rules as sentences with tappable tokens, because the rule explains itself while edited.
12. Swap the live card's lead line by phase and follow it with one sentence of cause, because a verdict needs a why.
13. Strike through the old value next to the new one, because the change is the news.
14. Leave unknown slots empty and label stale data in place, because a fake or silent stale value is a lie.
15. Notify on thresholds only, tiered and written as fact plus time, because routine pushes train users to ignore you.

## For a business dashboard app (HQ)

The case files give concrete transfer rules for HQ's system health view. The top band is the overall verdict: one colour field (calm, degraded, incident), one hero number (open incidents, or "All clear") and one plain sentence naming the worst thing ("Gmail sync failing for 2 h") (CARROT H1; Apple Weather's hero is the same: "All systems normal" or the count of failing jobs over a background tinted by the worst state). Failing systems get inserted cards titled with the failure ("Email to-dos sync failed 3×", red with a glyph, "Also: 2 warnings" on the same card) with age as clock plus relative ("since 09:12 (2 h)"); healthy systems collapse into one calm module or a tile grid where only the tile past its threshold is filled, with thresholds as editable sentence rules (CARROT H2-H3). Each subsystem tile shows value, sparkline and a one-sentence verdict, and a per-job "last 10 runs" strip uses the 10-day row pattern (Apple Weather). Time-series cards put values on the line and deploys or outage starts in the axis, driven by one metric chip row (CARROT H4). The HQ tab icon shows the worst current state, and an incident preset switches the layout when anything is red (CARROT H5). Status lines read number, verdict word, consequence ("3 · **Degraded.** Notes pages load slowly; writes are queued.") (CARROT H6). For live jobs: a phase-driven card with verdict plus cause ("Sync healthy · last run 4m ago", then "Gmail token refreshed at 09:12; next run 10:00"), "Offline · showing 09:41 data" when stale (Flighty), and P0 "Next sync in 4 min", P1 "Gmail · inbox", P2 progress of the current run (Uber). Copy Apple's module grammar and alert insertion; borrow CARROT's editable layout only if more than one person's needs differ (Apple Weather category note).
