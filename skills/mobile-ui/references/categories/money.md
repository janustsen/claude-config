# Money

Phone money apps: a budget tracker built around a review queue (Copilot Money), a payments app whose home is a number pad (Cash App), a brokerage whose screen is a number and a line (Robinhood), a multi-currency transfer app (Wise) and a bank "super app" (Revolut). Users judge them on one question: "Can I trust this number, and is this commit safe?" All five answer it the same way: the number they care about at the top with how it changed and over what period, movements grouped by date with amounts right-aligned, the main act one tap from home, and a calm explicit commit followed by a receipt. None uses a confirm dialog.

Studied (no logged-in app was reached; all five have sign-up walls):
- **Copilot Money** v8.7.2: 9 App Store renders plus raw phone screens from its changelog ("Dispatch"), one at exactly 402pt @2x; help center.
- **Cash App** v5.78.0: 10 App Store renders and Cash App's own fall-2025 screen recording of a payment at 390x844pt, cut into frames at 30fps; press on the late-2025 redesign [3p].
- **Robinhood** v2026.46.1: 9 App Store renders (cut to 393pt at 2.496 px/pt) and the public stock page rendered at 393x852 @3x, its CSS read and its chart scrubbed with synthetic touches; newsroom and help center.
- **Wise** v9.128: 7 App Store renders and two frames of the 6s preview video measured at 2.254 px/pt; colour names from [3p] summaries because wise.design would not render to a fetcher.
- **Revolut** v10.156: 9 App Store renders at 2.295 px/pt (±5%); redesign coverage and a user forum thread [3p].

Tags: [meas] measured, [obs] seen in a capture, [doc] the maker's docs or App Store text, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **The number first, then how it changed and over what period**, directly under it [obs all five].
2. **Direction you cannot misread**: one up colour and one down colour, always with a sign or arrow, and nothing else coloured [meas Robinhood].
3. **Spending that does not shout**: expenses neutral, income green, red only for the one judgement that matters [obs Copilot, Wise, Revolut].
4. **The main act from home in one tap** (pay, send, trade, review) [obs].
5. **Cost, time and consequence stated before the button** [obs Wise, Cash App].
6. **A deliberate, calm commit and a receipt**, never confetti [obs Cash App, doc Robinhood].
7. **Privacy in public**: a way to hide balances [obs Wise].

## The theses to choose from

### Copilot Money: the work is a queue you clear, not a ledger you read
Core bet: the app guesses categories and the user approves. "You just approve." [doc]. The hero is a pace chart, not a number.
- The dashboard's hero card plots month-to-date spend (solid, yellow-to-green by pace) against an ideal pace (1pt dashed grey) with a word tag at today ("$268 under"); the number above it is only ≈21pt [meas].
- The second card is "To review": new transactions with guessed categories, closed by one "MARK AS REVIEWED" pill [obs].
- AI fixes arrive as a "Copilot briefing" card, each row's second line giving the reason ("Restaurants → Health"), with DISMISS / APPROVE ALL [obs].
- No tab bar: a scrolling pill strip of 8 sections at the top, reorderable in settings [obs, doc].

Choose this when the data arrives automatically and the user's job is to check and correct it.

### Cash App: the input is the hero
Core bet: the home tab is a full-screen brand-green number pad under a giant "$0", because "pay someone $X" is the dominant job [obs].
- The amount is ≈105pt (digit height ≈76pt), heavy and centred; the keypad has bare digits on a 66pt row pitch [meas].
- Who and why follow on a sheet that stops at 275pt of 844, so the amount stays visible above it [meas].
- The flow reads as a sentence that fills itself in: "Pay $65 to / Carissa T. for / Concert tixx", connectors grey, choices black; the sentence is the review screen [obs].
- Pool, Request and Pay are the brand green darkened 10%; black appears only on the final Pay and Done [meas, obs].

Choose this when one act dominates the app and should need zero taps to start.

### Robinhood: the number and its line are the screen
Core bet: title, a modest value, one change line, and a full-width chart with no axes; the chart is also an input [obs, meas].
- Price 32px / 500 in Capsule Sans Display; change line 13px / 700 in #FF5000 when down; chart 345x196pt [meas web].
- One reference only: the previous close as a 1px dotted #919FA6 line [meas].
- Scrubbing rewrites the value, the change line and a floating time label, and dims other sessions to 50% [meas].
- Colour means direction only; down is orange, never red. Dark-first on #000000 [meas].
- Orders commit with "Swipe up to place the order" on a review screen [doc].

Choose this when the user watches values move and the question is "how is it doing over this period".

### Wise: say the cost and time before the button
Core bet: sending is a two-sided calculator, and every fear (rate, fee, arrival) is answered in a row above the commit [obs].
- "You send 588.37" over "Recipient gets exactly 500", currency pills left, amounts right-aligned in a heavy display face that shrinks to fit [obs, meas].
- Fee, arrival and rate lock as rows: "Total fees 2.27 USD, Included in USD amount", "Arrives in seconds", "Guaranteed 24H" [obs].
- Home: one filled bright-green Send beside grey Add money and Request; a 4-item floating tab bar whose selected item is a grey capsule, not green [meas].
- Amounts carry the currency code after the number ("80.99 GBP"); outgoing items say "Spent" instead of a minus and red [obs].

Choose this when the commit carries cost and timing the user worries about, or several currencies coexist.

### Revolut: each account is a poster
Core bet: every account is a full-bleed background (a user photo or a product gradient) with a centred balance, an "Accounts" switcher pill and four round actions; everything else sits in dark cards below [obs].
- Balance ≈45-50pt bold white, pence at ≈45% on the baseline [meas].
- Four 50pt action circles on a ≈91pt pitch, product-specific, "More" always last [meas, obs].
- Swipe sideways between accounts with the neighbours' balances peeking at the edges [obs].
- Transaction amounts are white with a sign; green appears only on investment percentages in rows; the hero change line stays white [obs].
- Users complain the balance on imagery is hard to read [3p].

Choose this when the user holds several peer accounts or products and switches between them.

## Comparison

| Dimension | Copilot | Cash App | Robinhood | Wise | Revolut |
|---|---|---|---|---|---|
| Hero | Pace chart; number ≈21pt [meas] | The amount being typed, ≈105pt [meas] | Value 32px + full-width chart [meas web] | Balance card, ≈44pt display face [meas] | Centred balance ≈45-50pt on a photo [meas] |
| Shell | Scrolling top pill strip, no tabs [obs] | 3 unlabelled items, one is the balance "$789" [obs] | Icon-only bar [know] | 4-item floating bar, grey selected capsule [meas] | 5 tabs, customisable [know] |
| Colour on rows | Expenses ink, income green [obs] | Gains green with ↑ [obs] | Direction colour on sparklines [know] | Neutral, "Spent" word [obs] | Signed white; green only on investment % [obs] |
| Down colour | Red on over-budget rings only [obs] | None seen [obs] | Orange #FF5000 [meas] | None [obs] | Not seen on hero [obs] |
| Commit | Bulk "MARK AS REVIEWED", count-named apply [obs] | Tinted steps, one black Pay, mono note [obs] | Review screen + swipe up [doc] | Fee and arrival rows, green Continue [obs] | Not captured |
| After commit | Card reframed "So far today" [obs] | Receipt, then back to "$0" [obs] | Calm confirm; confetti removed [doc] | Not captured | Not captured |
| Mode | Light, dark available [obs] | Light [obs] | Dark-first [obs] | Light [obs] | Dark-first [obs] |
| Non-content words | Dashboard ≈22, with briefing ≈35 [obs] | Keypad 3, review 16, receipt 12 [obs] | Hero 2 [obs] | Home 9, calculator 19 [obs] | Savings ≈14, crypto 4 [obs] |

## Category rules

### Shell and navigation

1. **Make the one dominant act the home tab's whole screen and the centre tab**, because the most frequent job should need zero taps to start. Cash App [obs].
2. **Label a tab with the live value it leads to when that value is why users open it** ("$789"). Cash App [obs].
3. **Name tabs after the nouns the user manages (Home, Card, Recipients, Payments) and mark the selected one with a neutral capsule**, so the brand colour stays free for the primary act. Wise [obs, meas].
4. **For 6 or more equal sections, use a scrolling top pill strip that bleeds off both edges, reorderable in settings**, instead of forcing a More tab. Copilot [obs, doc].
5. **End every summary card in a "› destination" link**, because the card is a preview of a full list. Copilot [doc].
6. **Let one swipe move between peer accounts with their balances peeking at the edges**, because peeking proves there is more without a selector. Revolut [obs].
7. **Keep a fixed four-slot action row per object, the first three swapped by type and "More" last.** Revolut [obs].
8. **Put a hide-balances eye in the top bar of a money home.** Wise [obs].
9. **Keep the phone simple and put pro tools in a separate product.** Robinhood (Legend on desktop) [doc].

### The hero number

10. **Size the hero by what shares the screen**: the typed amount alone at 90-110pt (Cash App), a value over a 200pt chart at 30-32pt (Robinhood), a balance card at about 44pt (Wise, Revolut), a small number when the chart is the hero (Copilot ≈21pt) [meas].
11. **Put the change line directly under the value: signed amount, signed percent in parentheses, then the period word in plain ink** ("-$6.46 (-1.85%) Today"). Robinhood [meas].
12. **Shrink everything that is not the digits**: decimals at ≈45% on the baseline (Revolut), a raised currency symbol at ≈60% (Copilot), auto-shrink long amounts to one line (Wise), because the whole-unit digits are what the user reads [meas].
13. **Write the currency code after the number when several currencies coexist** ("80.99 GBP"), because symbols collide. Wise [obs].
14. **Roll changing digits like an odometer**, each digit a 9-0 column, so the eye sees which digit moved. Robinhood [meas DOM].
15. **Show estimates as estimates** ("Est. daily interest +£0.56"). Revolut [obs].
16. **Centre the hero, its label and its switcher on a poster screen, and left-align the lists below.** Revolut [obs].

### Colour and direction

17. **Use exactly one up and one down colour, on the chart line and the change text only; keep titles, values, buttons and icons neutral**, so direction is never confused with brand. Robinhood [meas].
18. **Use orange (#FF5000) for down on black and pair it with a sign and arrow**, because it reads well and alarms less than red. Robinhood [meas].
19. **Leave expenses neutral and colour only income green**, because nearly every row in a spending app is an expense. Spend red on the one aggregate that is over (a budget ring). Copilot [obs], Wise [obs].
20. **Sign transaction amounts but do not colour them; colour only investment performance.** Revolut [obs]. Or replace the sign with a status word ("Spent"). Wise [obs].
21. **Ship a colour-blind switch for every good/bad pair** (Copilot swaps red/green for green/magenta). Copilot [obs, doc].
22. **Derive every control on a brand-colour field from that hue plus black**, because a second hue fights the field. Cash App [meas].
23. **Make the brand colours mean something: light green fills the one primary act, dark green inks money.** Wise [meas].
24. **On imagery, keep hero text white over a dark gradient and test contrast**, because users complained. Revolut [obs, 3p].

### Charts

25. **Draw the chart full width with no axes, gridlines or labels and one dotted grey reference line** (previous close, ideal pace). Robinhood [meas], Copilot [obs].
26. **Plot pace for budgets and targets: actual to date solid, the ideal dashed and continued to the period's end, a word tag at today ("$268 under")**, because "am I on track" is the question and the empty right side shows the runway. Copilot [obs, doc].
27. **Make every chart a scrubber that rewrites the hero value, the change line and a floating time label, and restores them on release.** The change line recolours by its own sign while the chart keeps the day's colour. Robinhood [meas].
28. **Dim everything outside the inspected segment to 50% instead of drawing crosshairs or a tooltip box.** Robinhood [meas].
29. **Put range chips under the chart (1D 1W 1M 3M YTD 1Y ALL) with a "• LIVE" chip, the selected one filled.** Robinhood [obs].
30. **Put status colour on the aggregate (ring, pace line), never on each row.** Copilot [obs].

### Rows and lists

31. **Group rows by day under small grey caps headers and by month under a large header that carries the month total on the right.** Copilot [obs].
32. **Align category chips in a fixed column**, because chips after variable-length names zigzag. Copilot [obs].
33. **Write transaction subtitles as "time · person".** Revolut [obs].
34. **List upcoming items above posted ones with a relative due time ("Due in 2 days").** Revolut [obs].
35. **Lead transaction rows with a 40-48pt round merchant logo (Wise) or category icon (Revolut)**, so the kind reads before the name. Wise [meas], Revolut [obs].
36. **Put filters as removable chips in the list header with a spent / income / net triplet under them**, so filtered totals need no extra screen. Copilot [obs].

### Review queues and bulk edits

37. **Make "accept all as is" the one big button and editing the exception, and cap the batch** (Copilot's Mac card stops at 25), because most guesses are right and a mis-tap must not accept hundreds. Copilot [obs, doc].
38. **Give every suggested change its reason in the row's second line with an arrow**, because the user approves a change, not a row. Copilot [obs].
39. **When one edit implies many, list the affected rows and name the count on the button ("Update 25 Transactions"), with a text "No thanks" under it.** Copilot [obs].
40. **Reframe an empty queue as progress ("So far today" over what was cleared).** Copilot [obs].

### Entry and commit

41. **For amount entry, use your own keypad with bare digits and the amount at 90-110pt**, because the system keyboard would cover the context. Cash App [obs, meas].
42. **Build multi-step flows as a sentence that fills in, grey connectors and black choices, and let the sentence be the confirm screen.** Cash App [obs].
43. **Keep the first step's result visible while later steps run: a sheet with a custom detent that stops under it.** Cash App [meas].
44. **For a two-sided amount, stack "You send" and "They get" with currency pills left and numbers right-aligned, and recalculate the other side live.** Wise [obs].
45. **Show every assumption (funding source, arrival, fee) as a one-line row with a small "Change" chip**, so defaults are visible and editable without a form. Wise [obs].
46. **State cost, time and guarantees in rows directly above the commit, plus a one-line promise ("No hidden fees, ever").** Wise [obs].
47. **Reserve the filled black (or brand) button for the single irreversible commit; tinted pills before it.** Cash App [obs], Wise [meas].
48. **State irreversibility once, small, under the commit, in a different face** (Cash App's grey monospace "Payments can't be canceled once they're sent."), instead of a dialog. Cash App [obs].
49. **Commit an irreversible trade with a deliberate gesture (swipe up) on a separate review screen, with an expert setting to skip it.** Robinhood [doc].
50. **Keep a Continue grey until required input exists, then fill it in place without moving it.** Cash App [obs].
51. **Let the commit follow the user into any detour** (Cash App's "Style it" screen keeps Pay in its top capsule). Cash App [obs].

### After the commit

52. **Confirm with a receipt (who, when, what for, amount, a ✓ "Complete" row, Done)**, because it doubles as the record the user screenshots. Cash App [obs].
53. **Celebrate nothing.** Robinhood removed its first-trade confetti in 2021 [doc]; Cash App's success is a receipt [obs].
54. **Reset the creation screen to its zero state after commit** ("$0"). Cash App [obs].
55. **Keep notifications informational, opt-in, and not for engagement.** Robinhood [doc].

### Motion and haptics

56. **Dim the background before the sheet moves (Cash App: dim starts ≈330ms earlier), then bring the sheet in on a damped spring of ≈650ms with no overshoot.** Cash App [meas].
57. **Play selection haptics while scrubbing a chart, a light tick per keypad press and a success haptic on payment sent.** Robinhood, Cash App [know].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Dashboard | title row 54-110pt; pills 31pt; hero card 16pt margin, ≈20pt radius; "$2,272 left" ≈21pt with "$" at ≈60% | Copilot [meas] |
| Pace chart | 4pt line, gradient by pace; 1pt dashed ideal; ≈9pt endpoint ring | Copilot [meas] |
| Transaction rows | 30pt apart within a day; day block 67pt; day headers ≈12pt caps; no separators | Copilot [meas] |
| Amount | ≈105pt font (digit height ≈76pt), centred | Cash App [meas] |
| Keypad | 66pt row pitch; columns at x ≈72 / 195 / 313; digits ≈24pt semibold | Cash App [meas] |
| Action pills | Pool / Request 172x53pt, 9pt gap, 16pt margin; Pay 54pt full width; fill #00C80F on #00DE12 | Cash App [meas] |
| Pay sheet | rests at y=275 of 844pt; radius ≈32pt; grabber 40x4pt; 16pt margins; backdrop dims to ≈50% | Cash App [meas] |
| Sheet motion | dim leads by ≈330ms; travel ≈667ms, fast start, long ease-out, no overshoot | Cash App [meas 30fps] |
| Review / receipt | sentence title ≈32pt bold; Pay 52pt black; disclaimer ≈12pt mono; receipt avatar 64pt, amount ≈64pt | Cash App [meas, obs] |
| Recipient rows | 48pt avatar, ≈64pt pitch | Cash App [obs] |
| Stock page | margin 24pt; price 32px/500; change 13px/700; chart 345x196pt, 2px line; reference 1px dotted #919FA6 | Robinhood [meas web] |
| Scrub | 10pt dot with 2px black ring; time label 13px #919FA6 above the chart; other sessions at 50% (#FF5000 → #802800) | Robinhood [meas web] |
| Direction colours | web up #00C805, down #FF5000; app up #CCFF00 (Robin Neon) | Robinhood [meas] |
| Native hero | value ≈31pt regular; change ≈15pt semibold | Robinhood [meas] |
| Related chips | 44pt tall, 40px radius | Robinhood [meas web] |
| Home actions | three 40pt pills ≈112pt wide, ≈12pt gap, 16pt margin; Send #9DE56E, others #E8EBE8 | Wise [meas] |
| Balance card | radius ≈24pt, #F2F4F7; total ≈44pt #133100; currency rows 46pt pitch with 32pt flags | Wise [meas] |
| Transaction row | 48pt logo, 17pt name, 15pt grey status | Wise [meas] |
| Tab bar | 4 items, inset ≈24pt, icons ≈22pt, labels 11pt, selected #E4E4E4 | Wise [meas] |
| Poster | balance ≈45-50pt bold white; Accounts pill 100x41pt; four 50pt circles, ≈91pt pitch; cards radius ≈20pt, inset ≈17pt | Revolut [meas ±5%] |
| Crypto hero | ≈44pt bold, decimals ≈45%; change ≈15pt white; 3pt white chart line; card #161618 on #000; secondary #A1A1A3 | Revolut [meas] |
| Row pitch | ≈64-80pt with 40pt icons | Revolut [meas] |

## Anti-patterns seen

- **A dashboard heavy with words.** Copilot's dashboard carries about 22 non-content words above the fold and about 35 with a briefing card, heavier than the reference apps; the case judges that the reason lines earn their place [obs].
- **Text on photos that users cannot read.** Revolut's poster balances drew forum complaints [3p].
- **One meaning, two colours.** Robinhood's up colour is #CCFF00 in the app but #00C805 on the web page: the brand moved and the web lagged [meas].
- **Confetti on a money commit.** Robinhood shipped it after a first trade, then removed it [doc].
- **Rows below the touch target.** Copilot's same-day transaction rows sit 30pt apart, well under 44pt; the case accepts it only because editing a row is rare [meas].

## Steal list

1. Lead a money or KPI screen with one hero and its change line directly under it, because the change is the meaning.
2. Plot pace against an ideal with a word tag at today, because a line answers "on track?" faster than a number.
3. Make the chart a scrubber that rewrites the hero and restores on release, and dim instead of drawing crosshairs.
4. Use one up and one down colour on the line and change text only, orange for down on black, always with a sign.
5. Keep expense rows neutral, income green, red only on the aggregate that is over.
6. Shrink decimals and currency symbols and auto-fit long amounts, because digits are the content.
7. Treat incoming items as a review queue with one bulk accept, a batch cap and the reason on each row.
8. Name the count on bulk buttons and list the affected rows above them.
9. Put the dominant act on the home tab as a full screen with the input as the hero.
10. Keep the amount visible above a custom-detent sheet while who and why are filled in as a sentence.
11. Show fees, arrival and defaults as rows with "Change" chips directly above the commit.
12. Reserve the filled button for the one irreversible commit, state irreversibility once under it, and skip the dialog.
13. Confirm with a receipt and reset to zero; celebrate nothing.
14. Swipe between peer accounts with the neighbours peeking.
15. Offer a hide-values eye and a colour-blind palette.

## For a business dashboard app (HQ)

The case files name three transfers. Lead a KPI dashboard with Copilot's pace chart (actual against an ideal-to-date line, a word tag at today), because "on track?" is the question. Build each KPI's detail screen as Robinhood's stack: title, value at about 30pt, change line at 13-15pt, a full-width chart of about 200pt, range chips, nothing between. If HQ has several peer dashboards, let one swipe move between them with the neighbours peeking (Revolut).
