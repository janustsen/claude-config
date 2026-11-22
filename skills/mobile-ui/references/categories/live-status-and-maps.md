# Live status and maps

Apps whose screen shows something happening in the world right now: a flight tracker (Flighty), the system's maps app (Apple Maps), a ride in progress (Uber) and a travel booking app with a trip timeline (Airbnb). Users judge them on one question: "What is happening, and what do I do next?", often answered from the Lock Screen without opening the app. All four put a live canvas (a map) under a persistent bottom sheet when location matters, open that sheet at about 35-45% of the screen (Flighty 42%, Airbnb trip 35%, Apple Maps open detent 320pt ≈ 38%) and never hide the canvas fully (Apple Maps leaves 24pt) [meas].

Studied (no app was installed or signed into):
- **Flighty** v4.12.1: 10 App Store renders, one screen cut to 393pt at 2.234 px/pt; help centre; Apple's "Behind the Design" and "Spotlight on: The Dynamic Island" quoting its designer. A third-party guide's hex palette is the Tailwind palette and is not used. No video, so no Flighty timings.
- **Apple Maps** v5.12: 6 App Store renders cut to 402pt at 2.49 px/pt, plus maps.apple.com in iPhone emulation, whose tray constants were read from Apple's `shell.js` (exact, but the web port, not the native app).
- **Uber** v3.748: 8 App Store renders that are old (pre-2023 styling, 375pt): flow and anatomy only. Uber Engineering's 2024 Live Activity post with its figures and measured outcomes.
- **Airbnb** v26.47: 7 App Store renders at 430pt (2.595 px/pt) and airbnb.com in iPhone emulation, logged out (exact CSS, but web).

Tags: [meas] measured, [obs] seen in a capture, [web] mobile web in iPhone emulation, [doc] the maker's or Apple's docs and code, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **One glance answers "on time, late or broken, and what next"** [doc Flighty].
2. **The live object stays visible while they read about it**: the map above the sheet [meas all four].
3. **The cause, not only the state**: "Inbound aircraft is in air from New York, with enough time for 10:20 AM departure" [obs Flighty].
4. **The Lock Screen and Dynamic Island do the job while the app is closed** [doc Flighty, Uber].
5. **Live data they can tell from scheduled data** [obs Apple Maps, Flighty].
6. **Calm when fine, loud when not**: "We want Flighty to work so well that it feels almost boringly obvious" and "We really have to shine when things go awry" [doc Flighty].
7. **Honesty when data is stale or estimated**, in the place the live value sits [doc Flighty].

## The theses to choose from

### Flighty: an airport departures board that changes with the phase
Core bet: one line per flight in board order (code, time, status, gate), and the card's lead changes with the phase of the trip, not with the user's navigation [doc].
- Full-bleed live map behind a persistent sheet; the list's large title is a menu ("Friends' Flights ⌄") [obs].
- Flight sheet opens at 42% (top at 359 of 852pt), inset ≈6.5pt each side, ✕ in a grey circle at the trailing end of the header [meas].
- A faint status band (#F6FBFA, ≈3% green) holds the verdict ("Gate Departure in 1h 42m") and a one-sentence cause [meas, obs].
- Big times ≈33pt semibold in status green; a changed time shows the old one struck through, small and grey; the gate is the one filled badge (black on #FFC100) [meas].
- A four-meaning palette with light and dark values; colour only on live, confirmed values; future flights are grey and ink [meas, obs].

Choose this when the live object passes through named phases and each phase needs a different lead fact.

### Apple Maps: the map is the screen and one sheet is the whole stack
Core bet: no tab bar, no nav bar; one persistent tray holds search, results, a place, transit and directions, and its height is the user's zoom on detail [obs, web].
- Three detents: peek 124pt (grabber, title, search), open 320pt, full = screen minus 24pt [web, doc].
- Search lives in the sheet at the bottom, in the thumb zone [obs].
- Live values carry a small green glyph (#34C759) and are right-aligned in 44pt rows (66pt with a subtitle) [meas].
- Status is written as the next change: "Opens 7:00 AM", "Closed till 8:00 AM" [meas web].
- In navigation, the bottom tray collapses to three numbers: "9:54 arrival / 13 min / 10 mi" [obs].

Choose this when the user explores a canvas and goes from overview to detail and back many times.

### Uber: one question per phase, answered by one number
Core bet: the Live Activity's P0 is the time to pickup or destination; identity is P1, progress P2; the progress bar is shaped for anxiety [doc].
- Each ride step replaces the sheet's content over one map; the sheet title is the instruction ("Confirm your pickup spot") [obs].
- The plate is the largest text on the en-route sheet; the identity line leads with it ("3XFH2C • Silver Honda Civic") [obs, doc].
- "The last 20% of the progress bar represents the last 2 min" [doc].
- Unknown slots stay empty (dispatch shows no ETA); on trip the duration becomes a clock time ("3:42 PM dropoff") [doc].
- Outcome: −2.26% driver and −2.13% rider cancellations at pickup [doc].

Choose this when a bounded process runs for minutes and the user is waiting to act at its end.

### Airbnb: the booked thing first, photos as the product
Core bet: the least "live" of the four and the most emotional; warmth from animated 3D objects used as icons, everything else plain [3p, obs].
- The upcoming trip is the first card on Explore, with a 3D tear-off calendar "STARTS IN 7 DAYS" [obs].
- The trip is a map plus a sheet at 35% and a day timeline (weekday over day number on a rail, event cards) [obs].
- Listing cards are ≈80% photo with a ≈20pt radius and two short lines [web].
- A sticky reserve bar keeps the total (underlined, opens the breakdown), a reassurance chip and the 48pt Reserve button on screen [web].

Choose this when the user plans toward a future commitment and the live phase is the trip itself.

## Comparison

| Dimension | Flighty | Apple Maps | Uber | Airbnb |
|---|---|---|---|---|
| Shell | Map + persistent sheet; tab bar with trailing search [obs, know] | Map + one tray, no tabs [obs] | Home, Services, Activity, Account; ride is one modal flow [doc] | 5 tabs; Explore, Wishlists, Trips, Messages, Profile [know, doc] |
| Detail opens at | 42% [meas] | 320pt open detent [web] | fit to content, ≈30-60% [obs] | trip sheet 35% [obs] |
| Lead fact | Verdict + countdown, then cause [obs] | Next change ("Opens 7:00 AM") [meas] | Time to pickup (P0) [doc] | Countdown card "Starts in 7 days" [obs] |
| Live marker | Status colour on live values only [obs] | Green live glyph [meas] | Moving car icon on map and bar [doc] | None |
| Changed value | New big, old struck through [obs] | Not seen | Same layout, only the number changes [doc] | Not seen |
| Primary button | Blue "Share" pill 110x46pt [meas] | Blue "Download" beside grey Cancel [obs] | Black, 56-58pt full width [meas] | Pink gradient Reserve 148x48pt [web] |
| Close | ✕ trailing in a ≈36pt grey circle [meas] | ✕ trailing, 44pt glass circle [meas] | ← circle on the map [obs] | ← 44pt circle [obs] |
| Lock Screen | Live Activity by phase; Island countdown + gate [obs] | Navigation Live Activity [know] | Live Activity P0/P1/P2; Island by phase [doc] | Check-in Live Activity [know] |
| Non-content words | Island 0, Live Activity 6, list row 5, flight sheet ≈34 [obs] | Navigation 5, transit sheet ≈14, peek 2 [obs] | Island 0-1, Live Activity 3, confirm sheet ≈9 [obs] | Home ≈14, listing ≈25 [obs] |

## Category rules

### Canvas and persistent sheet

1. **Make the live canvas the screen and put the list and details in a persistent sheet above it**, because the user's real question ("where is it now?") is answered by the canvas. Flighty [obs], Apple Maps [obs], Uber [obs].
2. **Use one persistent sheet as the whole navigation stack instead of tabs plus pushes**, each level replacing the sheet's content and adding ✕ or ‹, because the canvas must stay visible at every level. Apple Maps [web, obs].
3. **Give a persistent sheet three detents: peek ≈120pt (grabber, title, search), open ≈320pt, full = screen minus ≈24pt**, because each height answers a different intent and the sliver keeps the canvas present. Apple Maps [web, doc].
4. **Show the search field at peek, not a list fragment**, because at peek the next act is to search. Apple Maps [obs].
5. **Open a detail sheet at a middle detent of about 40-50% with the live object visible above.** Flighty (42%) [meas].
6. **Size each step's sheet to its content**, so a short confirmation leaves most of the map visible for checking the pin. Uber [obs].
7. **Raise the sheet to full height when its search field is focused**, because the keyboard would cover the results. Apple Maps [know].
8. **Float canvas controls as a small glass stack top-right (44pt buttons, 10pt from the edge) and hide them when the sheet is full.** Apple Maps [meas web].
9. **Make the grabber tappable as well as draggable (tap cycles detents) and snap on release with about 12pt of hysteresis**, because some users never discover dragging, VoiceOver needs an action, and a tray left between detents flickers. Apple Maps [doc shell.js].
10. **Go full screen only when the canvas is the input** (select a region, drop a pin), with one bottom panel stating the consequence ("Size of selected map: 286.1 MB") and two buttons. Apple Maps [obs].
11. **Turn the large title into a menu when it switches between two or three peer datasets** (Mine / Friends'), because that is cheaper than a segmented control. Flighty [obs].

### The live status card

12. **Model the live object as a sequence of named phases and decide what the card leads with in each**, because one static layout shows the wrong thing most of the time. Flighty lists days out, check-in, morning of, pre-departure, delay predicted, taxi, in flight, offline, landed, bags, changed, airport problem [obs, doc]; Uber dispatch, enroute, arriving, arrived, on trip, completed [doc].
13. **Lay the card out like a departures board: identifier, big time or value, one status word, location in a high-contrast badge**, because users scan for the same four facts in the same order. Flighty [doc, obs].
14. **Rank the card's facts P0 / P1 / P2 and size them in that order (time, identity of the thing to find, progress)**, because a glance reads only the biggest line. Uber [doc].
15. **Lead the identity line with the most matchable token (the licence plate before make and model)**, because the user matches it against the real world. Uber [doc].
16. **Write the verdict as a headline and the cause as one sentence under it**, and spend words only on the cause, because a symbol cannot say why. Flighty [obs].
17. **Give every problem state a cause, a duration and a likelihood** ("No flights can takeoff for the next 42m due to thunderstorms. Probability of extension is 30-60%."). Flighty [obs].
18. **Show a changed value big with the old value struck through beside it, smaller and grey**, because the change is the news. Flighty [obs].
19. **Show predicted and official values side by side and label the prediction** ("35m Delay Predicted"). Flighty [doc, obs].
20. **Give the most actionable token its own filled badge (the gate) and keep everything else as text**, because the eye finds one filled shape per block. Flighty [meas].
21. **Write status as the next change ("Opens 7:00 AM", "Closed till 8:00 AM"), not the current state**, because "Closed" alone makes the user work out when it opens. Apple Maps [meas web].
22. **Leave a slot empty while its value is unknown**; a placeholder or "--" reads as a broken number. Uber [doc].
23. **Switch from a duration to a clock time when the question changes from "how long" to "when"**, and make it impossible to mistake for the system clock. Uber [doc].
24. **Show "your turn" as an image or gesture (👋 + the driver's face), not a number**, because the meaning flips from wait to act. Uber [doc].
25. **When data is stale or estimated, say so in the status line itself** ("Offline Mode · Estimating all times"), because a banner gets ignored while the numbers keep looking authoritative. Flighty [doc].
26. **Put a relationship between two items (a gap, a dependency) on its own thin row between them, coloured by risk** ("55m at JFK · 🏃 Tight ›"). Flighty [obs].
27. **For a list of systems, give each item a name and one metric chip, and a body line with a one- or two-word verdict in status colour.** Flighty's airport cards ("📶 5m delay", "Normal Operations") [obs].

### Colour and type

28. **Use exactly four status meanings (good, caution, bad, not-yet) plus one action blue, each with a light-background and a dark-background value**: green #00A05A / #00FF8E, amber #FFC100 / #FFBB00, red #ED0001, grey; action #008CFF. Flighty [meas].
29. **Colour only live, confirmed values; keep scheduled and unknown values grey and ink**, so colour means "real and current". Flighty [obs].
30. **Tint the verdict band faintly (≈3% of the status hue) instead of drawing a coloured box.** Flighty [meas].
31. **Use red as a filled badge only for the one headline problem (RUNNING LATE); elsewhere as text.** Flighty [obs].
32. **Mark real-time values with a small live glyph in system green next to the number.** Apple Maps [meas].
33. **Make the primary button solid ink and keep blue for the canvas (route, pin, location)**, because a coloured canvas and a coloured button compete. Uber [obs].
34. **Use a connector word in a lighter weight instead of an arrow ("London to Miami") and small caps for units ("790KM/H")**, so the data dominates. Flighty [obs].
35. **Label a glanceable number with a one-word unit under it ("13 / min")**, not a phrase. Apple Maps [obs].
36. **Use two text inks, near-black and mid grey (#222222 / #6C6C6C), and spend the brand colour on the selected tab and the one commitment button only.** Airbnb [web].
37. **Use illustrative 3D objects only as icons with one meaning each (calendar = upcoming, door = check-in), and animate only the selected one.** Airbnb [obs, web].

### Rows and lists

38. **Right-align the live value and keep the label left; 44pt rows, 66pt with a subtitle; separators inset to the text.** Apple Maps [meas].
39. **Make a whole result card one tap target**, because a sheet over a map has no room for precision. Apple Maps [meas web].
40. **Put the distance or time cost of a choice beside it ("🚶 2 min") and give several next departures one unit ("3, 17 min").** Apple Maps [obs].
41. **Mark the selected row in a choose-one list with a light grey fill and repeat its name in the confirm button ("Choose UberX").** Uber [meas, obs].
42. **Cut the last card of a horizontal row (show 20-30% of it) and put a "→" circle at the row title's end for the full list.** Airbnb [web, obs].

### Flows and commits

43. **Run a multi-step task as one canvas and one sheet whose title is the instruction** ("Meet at your pickup spot", "Rate your trip"). Uber [obs].
44. **Prefill what you know and focus the field the user must type**; offer 3 preset amounts plus custom for small payments. Uber [obs].
45. **Keep the total and the primary action in a sticky bottom bar on any detail page that ends in a commitment, underline the total to open its breakdown, and answer the top fear beside the button ("$0 today · Free cancellation").** Airbnb [web].
46. **Break a multi-field search into stacked steps where only the current one is expanded.** Airbnb [know].
47. **Let import do the typing (calendar, email forwarding) and keep manual entry to one search field**, and show optional fields as "Tap to Edit" tiles where their value will appear. Flighty [doc, obs].

### Home and system surfaces

48. **Put an upcoming commitment first on the home screen as a countdown card**, because what the user owns beats anything recommended. Airbnb [obs].
49. **Use a Live Activity for a bounded live process and switch its content by phase (countdown, then progress, then result).** Flighty [doc], Uber [doc].
50. **In the compact Dynamic Island, put the countdown leading and the place or next action trailing as a coloured capsule, with no words** (Flighty "↗ 45m" + "🚶A10"). Flighty [obs].
51. **Draw progress as a non-linear bar that gives the final minutes a fixed share (Uber: last 2 min = last 20%), with the map's glyph grammar (dot start, square end) and a moving icon as the thumb.** Uber [doc].
52. **Drive live surfaces from the server: push, debounce, throttle, and end the activity from the server**, because Uber's first app-driven version kept updating late or never ended. Uber [doc].
53. **Pre-cache Live Activity images in a shared App Group**, because the extension cannot fetch them. Uber [doc].
54. **Write notifications as "{object} • {event}" in the title and "{new value} ({delta})" in the body** ("AUS ✈ JFK • Flight changed / New Departure: 8:28pm (was 11:30pm)"), naming the object as people think of it (the route, not the flight number). Flighty [doc, obs].
55. **Tick countdowns at minute resolution ("1h 42m") unless the user acts on seconds.** Flighty [obs, know].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Flight sheet | top at 359/852pt (42%); inset ≈6.5pt; top radius ≈40pt; content 16pt inside | Flighty [meas] |
| Sheet header | 73pt; logo ≈32pt; eyebrow ≈13pt grey; title ≈20pt semibold; ✕ ≈36pt #EFEFEF | Flighty [meas] |
| Status band | 81pt, #F6FBFA; headline ≈17pt bold; cause ≈16pt | Flighty [meas] |
| Big time | ≈33pt semibold #00A05A; gate badge 72x31pt #FFC100, ≈22pt bold, radius ≈6pt | Flighty [meas] |
| Share pill | 110x46pt #008CFF | Flighty [meas] |
| Status colours | #00A05A / #00FF8E; #FFC100 / #FFBB00; badge #ED0001, text #F03935 | Flighty [meas] |
| Live Activity | ≈343x147pt, radius ≈22pt; 2pt progress arc; countdown ≈24pt semibold | Flighty [meas] |
| List row | ≈92pt, 44pt avatar | Flighty [obs ±6pt] |
| Tray detents | peek 124pt (top y 728), open 320pt (225pt on small screens), full = viewport − 24pt | Apple Maps [web, doc] |
| Snap | nearest detent, 12pt hysteresis; transform 0.3s ease-in-out | Apple Maps [doc, meas web] |
| Grabber | 38x5pt, radius 5, #CCCCCC, 6pt from the top | Apple Maps [meas web] |
| Tray parts | sheet #F2F2F2; header 46pt; ✕ 30pt web / 44pt native; search ≈45pt; chips 33pt web / ≈40pt native, radius half; cards inset 16pt, radius 16 web / ≈24pt native | Apple Maps [meas] |
| Map controls | 44x44 glass, 44x89 stacked, radius 12, rgba(255,255,255,.8) blur 15px, 10pt from the right, 20pt from the top | Apple Maps [meas web] |
| Rows | 44-45pt, 66pt with subtitle; live glyph #34C759 | Apple Maps [meas] |
| Navigation | maneuver card inset 8pt, radius ≈32; side buttons 60pt glass, 10pt gaps; ETA numbers ≈26pt bold, labels ≈17pt | Apple Maps [obs, meas] |
| Primary button | "Confirm pickup" 56pt, "Choose UberX" ≈58pt, black; separators #E2E2E2; selected row #F4F4F4 | Uber [meas, old renders] |
| Progress | last 20% of the bar = last 2 min | Uber [doc] |
| Search pill | native ≈60pt; web 345x56pt, shadow 0 6px 20px rgba(0,0,0,.1) | Airbnb [obs, web] |
| Category chips | 40pt, radius 40, padding 10x14, icon 28pt; press 0.22s cubic-bezier(0.1,0.9,0.2,1) | Airbnb [web] |
| Cards | 167pt wide, image 167x158, radius ≈20; text 13px/500 #222222, meta 12px #6C6C6C | Airbnb [web] |
| Listing | photo 393x373; sheet overlaps by 24pt with ≈24pt top radius; title 26px/500 | Airbnb [web, meas] |
| Reserve bar | 96pt incl. safe area (12 top / 16 bottom); total 16px/700 underlined; Reserve 148x48pt, gradient #E61E4D → #E31C5F → #D70466 | Airbnb [web] |
| Tab bar | 24pt outline icons, 10px labels, selected #DA1249 weight 500; hides on scroll in 0.2s | Airbnb [web] |
| Trip sheet | top at ≈327/932 (35%); grabber ≈36x4; radius ≈32; home pin 52pt | Airbnb [obs] |

## Anti-patterns seen

- **A live surface that outlives its event.** Uber's first Live Activity, driven by the app in the background, "stopped updating or it was not dismissed after trip completion" [doc]. Fixed by server-driven updates and ends.
- **A clock-like time on a live card.** Uber had to redesign the drop-off time so it was not mistaken for the system clock [doc].
- **A detail sheet over the word budget.** Flighty's flight sheet carries about 34 non-content words against this skill's 15 for a detail screen; about a third is the cause sentence, which is the product's point, and the rest is labels such as "Departs in", "Arrives in" and "Tap to Edit" ×2 [obs].
- **A listing page heavy with reassurance.** Airbnb's listing carries about 25 non-content words above the fold, much of it trust copy ("Top 5% of homes", "Prices include all fees") [obs].

## Steal list

1. Define the phases of the live thing and swap the card's lead by phase, because what matters now keeps changing.
2. Write a verdict headline plus one cause sentence, because "why" is the one thing a glyph cannot carry.
3. Rank the card P0 time, P1 identity, P2 progress, and lead identity with the matchable token.
4. Show a changed value big with the old one struck through.
5. Use a four-meaning status palette with light and dark values, coloured only when live.
6. Label stale or estimated data in the status line, not a banner.
7. Write status as the next change ("Closed till 8:00 AM").
8. Keep the canvas visible: a persistent sheet with peek ≈120, open ≈320, full = screen − 24pt, search at peek.
9. Give the final minutes a fixed share of the progress bar, because attention peaks at the end.
10. Leave unknown slots empty and switch duration to clock time when "when" becomes the question.
11. Drive Live Activities from the server and end them there.
12. Put the countdown leading and the next action trailing in the compact Island, with no words.
13. Write notifications as object • event / new value (delta).
14. Put the upcoming commitment first on home as a countdown card.
15. Keep the total, the reassurance and the commit in a sticky bottom bar on detail pages that end in a commitment.

## For a business dashboard app (HQ)

The case files give HQ's system-health view a kit. Build the status card from Flighty: a verdict plus one cause line ("Sync healthy · last run 4m ago", then "Gmail token refreshed at 09:12; next run 10:00"), phases instead of a static layout, and stale data labelled in place ("Offline · showing 09:41 data"). Rank it like Uber's Live Activity: P0 the number ("Next sync in 4 min"), P1 the identity ("Gmail · inbox"), P2 the progress of the current run. Mark live values with Apple Maps' green glyph and write state as the next change. Put the next deadline or the next scheduled run first on home, as Airbnb puts the upcoming trip (Flighty, Uber, Airbnb category notes).
