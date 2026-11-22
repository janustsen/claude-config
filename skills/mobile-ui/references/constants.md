# Measured constants (iPhone, iOS 26/27)

Every number here was measured on App Store screenshots in points, read from mobile web CSS, measured on Apple HIG illustrations, or taken from Apple's documentation. Tags: [meas] measured, [doc] Apple or the maker's docs, [web] the product's mobile web in iPhone emulation, [know] prior knowledge not re-verified. App Store renders are ±5-10%; raw screenshots and web values are exact. Evidence files are in firstmate `data/mobile-design-skill/evidence/cases/`.

## Devices and safe areas

| Thing | Value |
|---|---|
| Phone widths (pt) | 375 (SE, mini), 390 (12-14, 16e), 393 (15, 16), 402 (16 Pro, 17, 17 Pro), 420 (Air), 430 (Plus, 15 Pro Max), 440 (16/17 Pro Max) [know] |
| Design at | 393 or 402; test the smallest (375) and largest (440) [doc] |
| Top safe area | 59pt (393/430), 62pt (402/440) on Dynamic Island phones; 47pt notch; 20pt SE [know] |
| Bottom safe area | 34pt; home indicator about 134x5pt [know] |
| Dynamic Island | about 126x37pt; compact Live Activity slots 52x37pt each side at 393 wide [doc] |
| iOS 27 | iPhone apps are resizable (iPhone Mirroring, iPad); iPhone Duo moves bars to a side strip on its outer display. Use size classes and insets, never model checks [doc] |

## Margins and grid

| Thing | Value |
|---|---|
| System layout margin | 16pt up to 402pt wide, 20pt at 414pt and wider [know]; Apple's own iOS 26 apps measure 20pt for content insets even at 402pt (Weather) and 430pt (Reminders) [meas]. Use 20pt for module and card layouts, 16pt in dense edge-to-edge lists |
| Reading text margins | 16-30pt: Readwise Reader 16pt, Apple Notes 30pt on 430, Bear about 30pt, Craft and Notion 21-24pt, Obsidian 20-24pt [meas] |
| Module grid | Apple Weather: 20pt inset, 11pt gap, 16pt padding [meas]; Carrot: 16pt margin, 14pt gap, 16-17pt padding [meas]; health cards: 16-20pt margins, 8-11pt gaps [meas] |
| Half-width tile | (W − 2·margin − gap) / 2, e.g. about 175pt on 402 [derived] |
| Smart-list tiles | Reminders: 2 per row, 80pt tall, 8pt gaps [meas] |
| Big-target grid | Streaks: 2 columns of 159pt circles with about 40pt margins and gutters [meas] |
| Horizontal rows | last card cut off at the edge to say "scrolls" (Notion Jump back in about 132pt squares; Fantastical 5.4 day columns) [meas] |

## Bars

| Thing | Value |
|---|---|
| Large title | 34pt bold (Large Title style, leading 41), left-aligned at the margin; collapses to 17pt semibold inline on scroll [doc/know] |
| Object title on a pushed screen | 26-28pt bold with its glyph (Things Today about 28pt with ★; Apple Notes first line 28pt; Notion page 25-26pt; Obsidian 30pt) [meas] |
| Nav subtitle | one line under the title for a live count or sync state (Apple Mail "Updated Just Now"; Notes "112 Notes" at 15pt grey) [doc/meas] |
| Nav buttons | 44pt glass circles, 16pt from the edges; grouped symbols share one capsule; at most 3 groups [meas/doc] |
| Tab bar | floating glass capsule about 62pt tall, inset about 26pt from the sides (Gentler Streak's custom bar about 16pt), bottom edge about 27pt above the screen bottom; selected tab is a lighter pill about 88pt wide with the tint on icon and label; labels 10-11pt; icons about 24pt [meas HIG] |
| Tab bar accessory | capsule about 48pt tall, 8pt above the bar [meas HIG]; Spotify's mini player about 56pt, 8pt side inset, tinted from the artwork, a 2pt progress line inside [meas] |
| Tab count | 3-5 including Search; iPhone shows 5 before More [doc/know] |
| Bottom toolbar row | Apple Mail: filter circle · search pill · create circle, 48pt tall, 12pt gaps [meas] |
| Floating + | Reminders 48pt, 28pt from the right and bottom edges of the content area [meas]; Things about 56pt resting, 74pt lifted while dragging [meas]; Gmail extended "Compose" 56pt, collapses on scroll [meas] |
| Search pill at top (search-first apps) | Gmail and Airbnb about 56pt, full radius [meas/web] |

## Type (Dynamic Type at the default size)

| Style | Size / leading | Weight | Used for |
|---|---|---|---|
| Large Title | 34 / 41 | Regular (bars render bold) | tab-root titles |
| Title 1 | 28 / 34 | Regular, emphasized Bold | object titles, first-line note titles |
| Title 2 | 22 / 28 | Regular / Bold | section heroes, sheet titles |
| Title 3 | 20 / 25 | Regular / Semibold | card titles |
| Headline | 17 / 22 | Semibold | row titles that need weight, inline nav title |
| Body | 17 / 22 | Regular | row titles, reading text |
| Callout | 16 / 21 | Regular | reading text in dense apps (Craft 16/24, Obsidian 16 at 1.5) |
| Subhead | 15 / 20 | Regular | secondary lines, counts |
| Footnote | 13 / 18 | Regular | meta lines, context under a row (Things 13pt grey) |
| Caption 1 | 12 / 16 | Regular | timestamps, chart labels |
| Caption 2 | 11 / 13 | Regular | the floor; module caps headers (Carrot 13pt semibold caps), tab labels 10-11 |

- Minimum 11pt. Body 17pt. Reading line height 1.5-1.7 for long text (Bear about 1.7, Obsidian 1.5) [doc/meas].
- SF Pro tracking is automatic: never set letter-spacing on system text (Apple's table is +0.40pt at 34pt, −0.43pt at 17pt) [doc].
- Dynamic Type grows Body to 53pt at AX5 but Large Title only to 60pt: scaling is per style, not linear [doc].
- Hero numbers: Cash App amount about 100-105pt; Apple Weather temperature at least 5x body in a thin weight; Robinhood price 32px (web), Revolut and Wise about 44pt, Copilot about 21pt (its hero is the chart) [meas]. Decimals at about 45% size (Revolut); a shrunken raised currency symbol (Copilot); shrink-to-fit on long numbers (Wise) [meas].

## Colour (iOS 26 values, light / dark)

| Role | Value |
|---|---|
| System blue | #0088FF / #0091FF (was #007AFF before iOS 26) [doc] |
| Red, orange, yellow, green | #FF383C / #FF4245, #FF8D28 / #FF9230, #FFCC00 / #FFD600, #34C759 / #30D158 [doc] |
| label | #000000 / #FFFFFF [know] |
| secondaryLabel | rgba(60,60,67,.6) (about #8A8A8E on white) / rgba(235,235,245,.6) [know/meas] |
| tertiaryLabel | rgba(60,60,67,.3) (chevrons about #C9C9CB) / rgba(235,235,245,.3) [know/meas] |
| systemGroupedBackground | #F2F2F7 / #000000; grouped cell #FFFFFF / #1C1C1E [meas/know] |
| separator | rgba(60,60,67,.29) / rgba(84,84,88,.6) [know] |
| Product inks seen | Airbnb #222222 / #6C6C6C two-tier ink [web]; Robinhood dark #000 with #919FA6 secondary [meas]; Todoist warm page #F8F5F2 with white cards [meas]; Amie #F5F5F5 page, white cards [meas]; Things dark #1D2229 (blue-tinted charcoal) [meas] |
| Status palette (Flighty) | green #00A05A / #00FF8E, amber #FFC100 / #FFBB00, red #ED0001, grey for not-yet [meas] |
| Money down on dark | orange #FF5000 with sign and arrow (Robinhood) [meas] |
| Parse highlight | Todoist peach #FDE7D8 behind the understood phrase [meas] |
| Priority stroke | Todoist p2 #EB8909 on the tick circle [meas] |

## Rows and lists

| List | Row | Notes |
|---|---|---|
| Inset grouped (Settings, forms) | 52pt, card radius about 26pt, text 20pt from the card edge, chevron 7x12pt tertiary | iOS 26 [meas HIG] |
| Things to-do | 44pt pitch for two lines (17pt title + 13pt project), no separators, 15pt tick box | [meas] |
| Reminders | 42pt one line, 67pt two lines | [meas] |
| Notion database list | about 69pt title + one indented property line; 36pt single line | [meas] |
| Notion page tree | about 47pt rows with chevron, emoji, title, + | [meas] |
| Apple Notes list | about 59pt with a 36pt thumbnail | [meas] |
| Mail (3-4 lines) | Gmail 85pt, 40pt avatar, 16/14/14pt text; Spark 79pt, 38pt avatar; Apple Mail about 102pt, 44pt avatar; Superhuman 135pt with a chip row | [meas] |
| Attio table | 46pt rows, frozen first column, horizontal scroll, totals footer | [meas] |
| Attio task | 64pt: circle, title, meta line (due coloured by urgency, assignee, linked count) | [meas] |
| Apple Maps place rows | 44pt; 66pt with a subtitle; live values right-aligned | [web] |
| Unread dot | 6-7pt, left gutter | [meas] |
| Swipe reveal | Spark Done about 132pt (one third of the row) on a short swipe; full swipe commits past about 60% | [meas/doc] |

## Cards, radii and depth

| Thing | Value |
|---|---|
| Inset grouped list | 26pt (half the 52pt row: capsule-concentric) [meas HIG] |
| Weather and Carrot modules | about 12pt continuous [meas] |
| Health metric cards | about 25-26pt continuous (Gentler Streak, Apple Health) [meas] |
| Amie | 20pt list cards, 12pt form cards, 10pt event blocks; shadow `0 1px 2px rgba(0,0,0,.04), 0 2px 6px rgba(0,0,0,.08)` on a #F5F5F5 page [meas] |
| Airbnb | listing card radius about 20, about 80% image; detail sheet overlaps the hero photo by 24pt with a 24pt top radius [web/meas] |
| Calendar event blocks | about 6pt radius, 15-20% tint fill, 3-4pt full-colour left stripe, 2-3pt gaps (Fantastical, Notion Calendar); Amie uses fill only, no stripe [meas] |
| Chips | filter chips 33pt (web) / about 40pt (native) tall, radius half the height; selected = filled (Apple Maps); category icon chips 40pt (Airbnb) [meas] |
| Concentric rule | inner radius = outer radius − padding; capsules near the screen edge [doc] |

## Sheets

| Thing | Value |
|---|---|
| Medium detent | about 52% of the screen height (top at y≈403 of 852) [meas HIG] |
| Partial sheet | floats about 6pt from the screen sides and bottom on glass; top radius about 35pt, bottom radius concentric with the display (about 52pt); opaque and edge-anchored at full height [meas/doc] |
| Grabber | about 36-38 x 5pt, about 4-6pt below the top edge, tappable [meas] |
| Close / Done | 44pt glass circle X at 16pt from leading and top edges; tinted ✓ trailing [meas/doc] |
| Persistent map sheet | peek about 120-124pt (title + search), open about 320pt (35-45% of screen), full = screen − 24pt [web Apple Maps]; Flighty detail opens at about 42% [meas] |
| Custom detent to keep context visible | Cash App about 67% so the amount stays visible above [meas] |

## Targets and spacing

| Thing | Value |
|---|---|
| Hit area | 44x44pt default, 28x28pt absolute minimum [doc] |
| Spacing | about 12pt around bezeled controls, 24pt between borderless icon buttons [doc] |
| Commit capsule | 48pt (Airbnb Reserve, 148pt wide beside the total) to 56pt full width (Uber "Confirm pickup"), full radius, inside the safe area [web/meas] |
| Sticky commit bar | 96pt tall including the safe area: total and context left, 48pt button right (Airbnb) [web] |
| Segmented control | at most 5 segments; nouns [doc] |

## Motion and timing

| Thing | Value |
|---|---|
| Anchored pickers | about 130ms open and close (Things When) [meas, video frames] |
| Insert / edit expand | about 300ms (Things) [meas] |
| Context menu | the menu itself in about 130ms, the full reveal (lift, blur, reactions) settled by about 570ms (Telegram, 60fps frames) [meas] |
| Sheet in | system spring; a custom sheet in Cash App measured about 650ms damped spring with the backdrop starting 1-2 frames earlier [meas] |
| Press-and-hold complete | Streaks ring fills in about 500ms (starting about 230ms after touch-down), ✓ shows about 400ms, then the count ticks [meas] |
| Completion linger | the row stays a beat (about 1s; Things about 1-2s [know]) before leaving, so a second tap undoes [doc/know] |
| Map sheet snap | about 300ms ease-in-out (web), system spring natively, about 12pt hysteresis [web] |
| Springs | critically damped by default (SwiftUI `.smooth`: 0.5s, bounce 0); `.snappy` bounce 0.15 after a flick [know] |
| Live Activity animations | 2s maximum [doc] |
| Undo snackbar | 5s (Spark Done); Apple Mail undo send up to 30s [doc] |

## Widgets and system surfaces

| Thing | Value |
|---|---|
| Widget sizes at 390-393 wide | small 158x158, medium 338x158, large 338x354; Lock Screen circular 72x72, rectangular 160x72, inline 234x26 [doc] |
| Widget margin | 16pt; text at least 11pt [doc] |
| Live Activity Lock Screen | 84-160pt tall, 14pt margin; 8 hours maximum [doc] |
| Notification actions | 1-3 short verbs with symbols; never "Open app" [doc] |
