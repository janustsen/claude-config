# Health and habit

Apps that read the body or track a behaviour: a workout and wellbeing tracker that judges you against yourself (Gentler Streak), a smart-ring companion built around one score (Oura), a daily habit grid (Streaks), Apple's own Health and Fitness, and a screen-time blocker (Opal). Users open them for one answer ("how am I today", "did I do it") in under five seconds, usually in the morning or right after an act, and come back for trends weekly. Users judge them on one question: "Am I okay today, and did I do it?" Every app answers with one hero element (Oura's gauge, Gentler's headline and path, Streaks' grid of rings, Apple's rings, Opal's gem) and pushes detail one tap down.

Studied (no app was run; most need a device, an account or a permission):
- **Gentler Streak** v6.0.1: 10 App Store renders and raw 390pt and 402pt @3x screenshots from the maker's site (exact); blog, help centre, Apple "Behind the Design", a Sketch interview.
- **Oura** v7.32.0 (the late-2025 redesign by Instrument): 9 App Store renders cut to 393pt at 2.4326 px/pt, the agency's case study and stills, Oura's blog.
- **Streaks** v11.6.0: 10 raw full-bleed 440pt @3x App Store screenshots (exact) and the maker's 25.7s demo video at 30fps.
- **Apple Health** (v2.9 listing) and **Fitness** (v8.5): 5 framed renders each; Health calibrated to a 440pt phone at 2.132 px/pt from the Dynamic Island and large title; Fitness values are relative.
- **Opal** v4.24: 8 App Store renders (proportions only), Opal's design blog, and a third-party onboarding teardown whose screens are blurred previews (layout and colour readable, text not).

Tags: [meas] measured, [obs] seen in a capture, [doc] the maker's docs or App Store text, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **One answer on open**, with detail one tap down [obs all five].
2. **A sentence that says what the number means**, then the number [obs Gentler, Oura, Apple Health].
3. **Comparison to themselves**: "Above typical", "LESS THAN USUAL", "31 minutes earlier than your average bedtime" [obs Gentler, Opal, Apple Health].
4. **Kindness at low values**, never a grade: "You'll be alright" [obs Oura].
5. **Completion that feels deliberate and earned**, with celebration reserved for the set or the milestone [obs Streaks, Opal].
6. **Permissions asked in context with a reason** [obs Streaks, Opal].
7. **A clear streak rule**, because ambiguity about what breaks a streak is the main source of anger in habit apps [doc Streaks].

## The theses to choose from

### Gentler Streak: the sentence first, your own baseline, rest is valid
Core bet: translate the number into a sentence about you, compare it to your own baseline instead of a goal, and make rest a valid outcome. "Statistics are just numbers. Without knowing how to interpret them, they are meaningless" [doc].
- Today leads with a mascot illustration, a greeting, a 26-28pt SF Pro Rounded Bold state headline ("Great Effort Today") and a 3-4 line explanation, then the full-bleed Activity Path chart [meas].
- Metrics carry baseline words ("Normal", "Above typical", "As Usual"); there is no progress-to-goal ring anywhere [obs].
- A status switch (Active, On a Break, Sick, Injured) pauses suggestion and reminder notifications [doc].
- Vitals cards name no metric: a glyph and a unit identify it, and the sparkline sits on a pale band that is the normal range [obs].
- Each metric's detail screen owns a full-bleed colour field (Steps orange glow, Sleep purple) [obs].

Choose this when the metric varies day to day and a missed fixed goal would shame the user.

### Oura: one big thing, three levels of detail
Core bet: Today is built around the single most important score or insight for this moment; everything else is a shortcut above it. Detail comes in three levels with one semantic colour language [doc].
- Hero: a 180° gauge labelled only 0 and 100, the score ≈50pt light, "READINESS" tracked caps, a serif ≈40-44pt headline ("Go get 'em!"), a 17pt paragraph and a "Learn more" glass capsule [meas].
- A scrolling row of ≈69pt score chips above the hero is the navigation to details; the last chip is cut to say "scrolls" [meas, doc].
- The background photo changes with the score band (snow peak at 88, dusk dunes at 56) [obs].
- Three tabs in a dark glass capsule plus a separate 60pt + circle [meas].
- Status words sit above values in the semantic colour (blue Optimal, teal Good, amber Needs care) [obs, doc].
- Instrument reports Today tab CTR 42% (+7 pts) and D5 stickiness 80% after the relaunch [doc].

Choose this when one daily score drives the product and users dig into trends only sometimes.

### Streaks: the habits are the screen; completing is a physical act
Core bet: six big circles in a 2×3 grid, the user's task names under them, two corner buttons and page dots: zero non-content words [obs]. You press and hold to complete; the ring fills in ≈0.5s, flashes a check, then the count ticks [meas].
- 159pt circles, ≈40pt margins and gutters, ≈256pt row pitch on a 440pt phone [meas].
- Completed = inverted (solid white disc, black icon); all done for the day = the page turns gold [obs, doc].
- The whole screen is one of 78 theme colours or gradients; there is no fixed accent [doc].
- The streak rule is strict ("Miss a day and your streak goes back to zero"); softness comes from scheduled days off and a 2-Day Rule for negative tasks [doc].

Choose this when the user tracks a small fixed set of daily items and wants to tick them off one-handed.

### Apple Health and Fitness: identical cards, category colour as the label
Core bet: Health is a feed of identical cards, one per metric, each labelled only by its category colour and icon; Fitness is three coloured rings [obs].
- Health card: icon and category name in the category colour, timestamp and chevron right, a ≈28pt rounded number with a smaller grey unit on the baseline, a mini chart whose latest bar is coloured [meas, obs].
- Fitness: Move, Exercise and Stand rings with their values written in the ring colours, so no legend is needed [obs].
- Insights are sentences comparing to your own average; score bands are words first ("High") [obs].
- Charts annotate extremes in place ("MAX 74", "MIN 49") [obs].

Choose this as the baseline users compare every third-party health app against, or when the app aggregates many metrics.

### Opal: an object worth caring for, time won back
Core bet: no guilt. The home hero is a 3D opal gem, not a chart, and time is framed as gained ("Get back 1h23m every day", "1h 23m LESS THAN USUAL") [obs]. "Guilt-tripping or scary screen time stats are counter productive" [doc].
- A three-stat row under the hero: tracked caps captions over values ("SCORE 94▲", "SCREEN TIME 2h 56m", "CULPRITS" + app icons) [obs].
- Block screen copy in the user's favour: "You set this rule yesterday. Past you was right." [obs].
- Permission primers show a mock of the system dialog with an arrow at the button to tap, then trigger the real prompt [obs blurred].
- Milestones are collectible gems revealed by a tap; the streak is a small flame and number in the header [doc, obs].

Choose this when the product asks users to do less of something and guilt would drive them away.

## Comparison

| Dimension | Gentler Streak | Oura | Streaks | Apple Health / Fitness | Opal |
|---|---|---|---|---|---|
| Hero | Headline + explanation, then path chart [obs] | Gauge + score + serif headline [meas] | Grid of six 159pt rings [meas] | Pinned cards / three rings [obs] | 3D gem + three-stat row [obs] |
| Judges against | Own baseline band [doc] | Own baseline bar [obs] | Daily target; strict reset [doc] | Fixed ring goals; own average in insights [obs] | Own usual [obs] |
| Low-value copy | "taking a break never means starting over" [doc] | "You'll be alright" [obs] | None; streak resets [doc] | Neutral, factual [obs] | "Past you was right" [obs] |
| Completion | Not a tap; logged from Health [doc] | Confirm detected activity inline [obs] | Press and hold ≈500ms, check ≈400ms [meas] | Ring closes [know] | Gem reveal per milestone [3p] |
| Celebration | "cute surprises", mascot pose [doc] | Gold crown on top scores [obs] | Page turns gold once a day [obs] | Awards, ring animation [know] | Gems, day-streak screen [obs] |
| Shell | 4 tabs, avatar top-right [obs] | 3 tabs + separate + circle [meas] | No bars; 4 pages of 6, corner buttons [obs] | Health 3 tabs, Fitness 4 [obs] | Not verified [know] |
| Numbers | SF Pro Rounded [obs] | Light geometric sans [obs] | Bold condensed [obs] | SF Pro Rounded [obs] | SF Pro, tracked caps captions [obs] |
| Mode | Light; Sleep dark [obs] | Dark only [obs] | Theme colour [obs] | Health light, Fitness dark [obs] | Dark [obs] |
| Non-content words | Today 17 + a 25-word paragraph; vitals ≈13 [obs] | Today ≈19 + 26-word paragraph; vitals ≈17 [obs] | Grid 0; statistics 9 [obs] | Health ≈24; Fitness ≈26 [obs] | Home ≈8; block screen 10 [obs] |

## Category rules

### The hero and its sentence

1. **Lead a score screen with a headline that interprets it, then the chart, then the number's detail**, because users act on meaning, not values. Gentler Streak [obs, doc], Oura [obs].
2. **Explain a score with a 3-4 word headline, one paragraph and a "Learn more", and pick the copy from the score band.** Oura [obs].
3. **Give each typeface one role: a display serif only for the interpretation sentence, a sans for data.** Oura [obs].
4. **Explain a score by its components as coloured lines matching the chart segments ("Duration: 44/50") plus one sentence of cause.** Apple Health [obs].
5. **Use a 180° gauge with only the endpoints labelled and 4 tick dots for a 0-100 score**, because the arc already says "out of 100" and precision is not the point. Oura [obs].
6. **Put the other scores as a scrolling chip row above the hero that doubles as navigation, and cut the last chip at the edge.** Oura [obs, doc].
7. **Put secondary numbers in a three-stat row of tiny tracked caps captions over values under the hero.** Opal [obs].
8. **Change the background with the state** (Oura's photo per score band, Gentler's full-bleed colour field per metric), so the mood or the metric registers before the number. Oura, Gentler Streak [obs].

### Judging the user

9. **Compare to the user's own baseline ("Above typical", "As usual", "LESS THAN USUAL") instead of a fixed goal when the metric varies day to day**, because a missed arbitrary goal shames and a baseline explains. Gentler Streak [obs, doc], Opal [obs], Apple Health [obs].
10. **Show "normal for you" as a pale band behind the sparkline or a thin bar with range ends and a dot for today**, so the eye judges every point at once. Gentler Streak [obs], Oura [obs].
11. **Frame a usage metric as what the user gained** ("Get back 1h23m"), because the same fact as loss creates guilt and churn. Opal [obs, doc].
12. **Write low-value copy as reassurance with a next step** ("We've all had bad nights… cut yourself some slack today"). Oura [obs].
13. **Use a gentle status scale ("Pay attention / Needs care / Good / Optimal / Thriving") and put the status word above the value in the semantic colour.** Oura [obs].
14. **Give users a status switch (Active, On a Break, Sick, Injured) that pauses nudges and resets expectations**, with first-person one-liners ("Injured / My body needs to heal."). Gentler Streak [doc, obs].
15. **Let the user's own rating override the computed estimate, and keep the check-in optional.** Gentler Streak [doc].
16. **State the streak rule explicitly and give legitimate days off through scheduling.** Streaks [doc].
17. **Show a streak as a small flame and number in the header, not the hero, when the product's goal is calm.** Opal [obs].
18. **Write refusals in the user's favour** ("Past you was right"). Opal [obs].
19. **Say when a baseline is still forming** ("stabilises within 10 to 14 days"), and suggest an easier day when sleep or body metrics are off. Gentler Streak [doc].

### Completion and celebration

20. **Complete a big target with press-and-hold (Streaks: the ring starts ≈230ms after touch-down and fills in ≈500-530ms)**, because a tap is too easy on a grid of huge targets and the fill makes the act deliberate. Streaks [meas].
21. **Show completion by inverting the element (filled disc, dark icon), flash a check for ≈400ms, then return to the icon with the counter incremented.** Streaks [meas, obs].
22. **Reserve celebration for the whole set (Streaks' gold page, once a day) or a milestone (Opal's gems, Apple's awards), never the single tap.** Streaks [obs, doc], Opal [doc], Apple Fitness [know].
23. **Reveal a milestone object with a tap the user makes**, because a self-triggered reveal feels earned. Opal [doc, 3p].
24. **Ask to confirm auto-detected data inline (Confirm / Edit / ×) instead of logging silently or opening a modal.** Oura [obs].

### Cards and metrics

25. **Give every metric card the same anatomy: coloured icon and name header, timestamp and chevron right, a big rounded number with a small grey unit on the baseline, a mini chart right.** Apple Health [obs, meas].
26. **Assign each category one colour and use it only for its header, its latest data point and its value**, so colour becomes the label. Apple Health [obs].
27. **On repeated cards, identify the metric by glyph and unit and drop the name.** Gentler Streak [obs].
28. **Anchor the value at the bottom of each card**, so a row of cards aligns its numbers on one baseline regardless of title length. Oura [obs].
29. **Write ring or score values in the ring's own colour beside it**, so no legend is needed. Apple Fitness [obs].
30. **Use rounded numerals and set units smaller (about 60%) and grey on the number's baseline.** Apple Health, Gentler Streak [obs].
31. **Make the home of a data-heavy app a pinned, user-editable Summary.** Apple Health [obs]; Oura's Vitals has a pencil to choose and order metrics [obs].

### Charts

32. **Run charts full-bleed while text and cards keep the 16pt margin**, because the x-axis is time and wants every point of width. Gentler Streak [meas].
33. **Label the y-axis with min and max only, on the right, and the x-axis with about 4 ticks or start and end.** Oura, Apple Health [obs].
34. **Annotate extremes and key values in place (MAX, MIN, the latest point) and colour only the latest bar.** Apple Health [obs].
35. **Use polar words ("Below / Above") instead of numbers on axes whose units mean nothing to users.** Oura [obs].
36. **Encode each day's outcome as a thin coloured strip under a trend chart** (8pt: green in path, yellow above, blue rest). Gentler Streak [obs].
37. **Put a rarely changed time range in a small menu capsule beside the headline, not a segmented control.** Gentler Streak [obs]. Streaks uses one big capsule that cycles ranges [obs].

### Grids, logging and navigation

38. **For a small fixed set of daily items, use big circular targets in a 2-column grid with about 40pt margins and gutters, a faint full ring track, progress clockwise from 12 o'clock with round caps, and tick marks for multi-count goals.** Streaks [meas, obs].
39. **Log feelings and symptoms with sliders, chips and tappable day circles, not text fields.** Apple Health [obs], Gentler Streak [doc].
40. **In detail views, swap the tab bar for a sideways switcher between sibling metrics and support swipe between them.** Oura [obs, doc].
41. **Make the date the detail screen's subtitle with a chevron, so the title is the date picker.** Gentler Streak [obs].
42. **Put Create (+) outside the tab capsule as its own circle.** Oura [meas].
43. **Make a focus or timer mode visually distinct (full screen, skeuomorphic LCD)** so entering it feels like changing rooms; set duration with a − / + stepper. Opal [obs].
44. **Use dashed outlines for optional alternatives next to a solid primary chip.** Gentler Streak [obs].
45. **Let a theme colour carry the brand and tint list cards and separators from it instead of mixing in system greys.** Streaks [meas].

### Permissions and onboarding

46. **Ask for Health access inside the step that needs it, with one sentence of why** ("This task uses data from the Health app. Please grant Streaks permission if prompted."), and request only the types that feature needs. Streaks [obs], Apple Health [know].
47. **Prime every system permission with a screen that says why and shows the dialog with an arrow at the right button, and trigger the real prompt from that screen's button.** Opal [obs blurred].
48. **Ask one question per onboarding screen with full-width options and one bottom capsule (≈48pt).** Opal [obs blurred].
49. **Put the primary button and a quieter "Skip" stacked at the bottom of a selection step, and show selection limits as a counter on the tile ("4 of 5 selected").** Apple Fitness [obs].

### System surfaces

50. **Give an interactive widget one action, the day's next step** ("Start Workout"). Gentler Streak [doc].
51. **Offer widgets in several shapes of the same data (ring, streak number, dot calendar, bar chart).** Streaks [obs].
52. **Put a running timer on the Lock Screen as a Live Activity with a pause button.** Streaks [obs].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Today tab | 16pt margins; headline 26-28pt Rounded Bold; explanation 17pt; chart full-bleed; day strip 8pt; axis 15pt; range capsule ≈87x33pt | Gentler Streak [meas] |
| Tab bar | floating glass ≈62pt tall, inset ≈16pt; selected pill #e3e3e4 ≈87x51pt | Gentler Streak [meas] |
| Vitals cards | page #f3f3f7, card #fff, 16pt margin, 93pt tall, ≈9pt gap, ≈25pt radius; glyph 26pt; value ≈22pt bold rounded, unit ≈15pt | Gentler Streak [meas] |
| Steps detail | hero ≈60pt Rounded Heavy; stat grid values ≈28pt, labels 15pt, ≈68pt row pitch | Gentler Streak [meas] |
| Colours | orange #f47538; status green #29c986; path #21b879 → #2ad28d; mood #628fe7 | Gentler Streak [meas] |
| Today hero | top circles 43pt at 20pt inset; chips ≈69pt (icon 11pt, number 22pt, label 15pt); gauge ≈294pt wide; score ≈50pt light #f6ede8; headline serif ≈40-44pt; body 17/24; button ≈121x43pt | Oura [meas] |
| Tab bar | dark glass capsule x 20 → 300pt; + circle 60pt | Oura [meas] |
| Vitals cards | ≈190x206pt, ≈8pt gutter, ≈28pt radius; value ≈38pt light; page #1b1c20 | Oura [meas approx.] |
| Insight card | radius ≈25pt, padding ≈19pt, icon 36pt, value ≈27pt light, action capsule ≈40pt | Oura [meas, scale assumed] |
| Task grid | 159pt circles, ≈40pt margins and gutters, ≈256pt row pitch; ring ≈12pt at ≈35% white; label ≈20pt bold condensed caps; timer disc 48pt; corner buttons 48pt | Streaks [meas, 440pt] |
| Hold to complete | fill starts ≈230ms after touch-down, ≈500-530ms to full; check ≈400ms; count +≈100ms | Streaks [meas 30fps] |
| All done | discs gold in ≤100ms; background to gold over ≈1.5s | Streaks [meas] |
| Add Task rows | 60pt; separators a darker theme shade (#cf5b3d on #e66544) | Streaks [meas] |
| Statistics | range capsule 228x53pt #fa114f | Streaks [meas] |
| Summary cards | 18-20pt margins, ≈133pt tall, ≈11pt gap, ≈26-28pt radius, ≈18pt padding; value ≈28pt rounded, unit ≈17pt grey | Apple Health [meas, 440pt] |
| Tab bar | ≈277pt wide, ≈70pt tall, 3 tabs | Apple Health [meas] |
| Fitness tiles | ≈20pt radius on black; value ≈34pt rounded in the metric colour | Apple Fitness [meas relative] |
| Onboarding button | white capsule ≈48pt, ≈16-20pt margins | Opal [obs blurred] |

## Anti-patterns seen

- **A rating prompt before any value.** Opal asks for an App Store rating right after a personalised "report" in onboarding, before the product has done anything; the case calls it ethically borderline [3p].
- **Summary screens heavy with labels.** Apple Health's Summary carries about 24 non-content words and Fitness about 26, while Streaks' grid carries 0 [obs].

## Steal list

1. Put the sentence that interprets the number above the number, chosen by score band.
2. Compare to the user's own baseline, drawn as a band or a bar with a dot for today.
3. Write low values as reassurance with a next step; never grade.
4. Offer Active / On a Break / Sick / Injured, and pause nudges when not Active.
5. Complete big targets with a ≈500ms press-and-hold, invert on done, flash the check, then tick the count.
6. Celebrate the whole set or a milestone, never a single tap.
7. Give every metric the same card, labelled by category colour and glyph.
8. Use rounded numerals with small grey units on the baseline.
9. Run charts full-bleed with min/max axes on the right and extremes annotated in place.
10. Put the status word above the value in the semantic colour and anchor values at the card's bottom.
11. Put Create outside the tab capsule.
12. Ask for each permission inside the step that needs it, after a primer that shows the dialog.
13. Frame usage as time won back and colour only the improving value.
14. Make the streak rule explicit and let scheduled days off protect it.
