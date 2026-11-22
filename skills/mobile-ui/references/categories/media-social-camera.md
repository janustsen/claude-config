# Media, social and camera

Apps where the content owns the screen: music and podcasts (Spotify), a messenger (Telegram), a public text feed (Threads), a read-it-later reader (Readwise Reader) and a pro camera (Halide Mark III). Users judge them on one question: "Does the content own the screen, and do the controls fall under my thumb?" Every studied app keeps chrome neutral or floating, lets the content bring the colour, and puts the one constant action (play, send, post, triage, shutter) in the bottom third.

Studied (no logged-in app was driven):
- **Spotify** v9.2.2: 8 App Store renders cut to 393pt at 2.245 px/pt (±5%); Spotify Design articles on the now-playing bar and its buttons (Wayback copies). No motion was measured.
- **Telegram** v13.3: 7 App Store renders cut to 393pt at 1.855 px/pt; Telegram's own demo videos cut at 60fps (2021 reactions, 2026 Liquid Glass); the t.me channel preview measured as web CSS.
- **Threads** v456.0: 6 App Store renders cut at 2.405 px/pt; threads.com measured as web CSS behind its login modal.
- **Readwise Reader** v8.28: 8 App Store renders (Inbox cut at 2.504 px/pt), one raw @3x docs screenshot of the reading view, Reader's full docs.
- **Halide Mark III** v3.4.1: Lux's launch posts with raw @3x toolbar crops at 402pt; App Store renders are still from Mark II. No screen recording, so no timings.

Tags: [meas] measured, [obs] seen in a capture, [web] mobile web CSS, [doc] the maker's docs or App Store text, [3p] third party, [know] prior knowledge not re-verified.

## What users expect

1. **The constant action reachable from everywhere**: playback controls on every screen (Spotify), the composer pinned above the keyboard (Telegram), a big centred shutter (Halide) [obs, category notes].
2. **A full view that opens and closes with one swipe**: the full player, the media viewer [know Spotify, Telegram].
3. **Artwork-first or text-first lists with metadata as glyphs and numbers** [obs Spotify, Telegram, Threads].
4. **Long-press on an item for its actions, and the most frequent one as a gesture** (swipe to reply, double-tap to react) [doc, know Telegram].
5. **Instant-feeling motion that never blocks a tap** [meas Telegram].
6. **System media controls, Lock Screen and hardware entry points that work** [know Spotify, Halide].
7. **Remembered position, adjustable type and quick triage for saved reading** [doc Readwise].

## The theses to choose from

### Spotify: playback is ambient, artwork is the colour system
Core bet: a floating now-playing bar sits above a transparent tab bar on every screen, and colour comes from the content; the one brand colour is reserved for play and "now playing" [doc].
- The mini player is a floating card ≈54pt tall, inset ≈7-8pt, tinted from the artwork, with a 2pt progress line inside its bottom edge [meas].
- It became a floating tinted card because "It also wasn't clear to all listeners that when you tapped the NPB, it would lead to a more immersive 'now playing view'" [doc].
- Black play glyph on Spotify green for 10.9:1 contrast instead of darkening the green [doc].
- The playing track's title turns green in lists; no extra icon [obs].
- Dark only; chrome #121212, grey secondary [meas].

Choose this when the content plays over time and must stay controllable while the user browses.

### Telegram: the conversation is the interface; speed you can see
Core bet: every piece of chat chrome is a separate floating glass capsule over the wallpaper, and every state change is short and interruptible [obs, doc].
- Long-press lifts the bubble in place, blurs the rest, puts reactions above and actions below: the menu is done in ≈130ms, the whole reveal settled by ≈570ms [meas 60fps].
- Chat rows at 75-76pt with a ≈58-60pt avatar; metadata as glyphs (ticks, badges, pin, mute) [meas, obs].
- Search is a detached glass circle beside a 4-item tab pill; user folders with unread counts sit under the title [obs].
- One composer button morphs mic ↔ send; hold-to-record explains itself ("Slide to cancel", a lock target) [obs].
- Connection state lives in the title ("Connecting…"), never a banner [know].

Choose this when users send many short messages and speed is what they notice.

### Threads: text first, chrome last
Core bet: a post is an avatar column and a text column with no cards, borders or labels; posting must feel as light as reading [obs].
- Avatar ≈44pt native (36px web), text column at x≈68pt native (60px web); body 15/21 [meas].
- Four bare 20pt action icons with 13px counts in fixed slots; everything else behind ⋯ [meas web].
- No accent: black on white, black primary buttons, colour only for state (liked red, verified blue) [obs].
- An inline "What's new?" composer at the top of the feed and a pinned "Add your reply…" bar on threads [obs].
- Feed: 2 non-content words [obs].

Choose this when the content is short text and the feed is scrolled for long stretches.

### Readwise Reader: triage first, reading second
Core bet: everything lands in an Inbox processed like email ("deleting, archiving, or moving them to Later"), modelled on Superhuman's game-like triage; the reading view protects selection [doc].
- Rows ≈162pt: favicon and caps domain, 2-line title, 2-line summary, author and minutes, ≈80pt thumbnail, a reading-progress line [meas].
- Swipes are user-configurable; right-to-left reveals Later on #5a48d7 [doc, meas].
- Selection is the highlight, with no confirm step; one highlight colour, categories in tags [doc].
- Pages scroll vertically and turn by margin taps, because horizontal flips break cross-page selection and swipe panels [doc].
- Reading progress and last location are tracked separately; a "Return to 31%" pill appears only when they diverge [doc, meas].

Choose this when users save more than they consume and must decide quickly what to keep.

### Halide: hierarchy over completeness
Core bet: "When tool has equal visual importance, nothing has importance"; the default layout exposes the key tools within thumb reach and pushes the rest into a "…" menu, and tools appear only while used [doc].
- Read-outs in the "ears" beside the Dynamic Island; viewfinder 402x536pt; control rows ordered by frequency toward the bottom; shutter ≈72pt in a ≈85pt ring [meas].
- One engaged colour, yellow #ffd72c, on black chrome [meas].
- A setting moved off its default adds its icon to the toolbar as a reminder until reset [doc].
- Dragging the focus dial turns on the loupe and peaking; release turns them off ("Intelligent Activation") [doc].
- The Mark II layout stays reachable from the "…" menu because "people don't like their habits disrupted" [doc].

Choose this pattern for any one-screen tool used one-handed under time pressure.

## Comparison

| Dimension | Spotify | Telegram | Threads | Readwise Reader | Halide |
|---|---|---|---|---|---|
| Shell | Home, Search, Library (+ Create/Premium) with floating mini player [know, obs] | 4-item glass pill + detached search circle [obs] | 5 unlabelled icons, centre Create pill [obs] | Home, Library, Feed, Search, Account [doc] | One screen, no tabs; ears, corners, "…" [obs] |
| Constant action | Play/pause in the mini player [obs] | Mic ↔ send in the composer [obs] | Inline composer + Create tab [obs] | Swipe to triage [obs] | Shutter ≈72pt [meas] |
| Colour source | Artwork tints; green for play [doc] | Wallpaper; blue for selection, unread, links [obs] | None; state only [obs] | Indigo accent; yellow for highlights [meas] | Yellow for "engaged" [meas] |
| Glass | Transparent tab bar over a gradient [doc] | Every floating control [doc] | 85% white + blur bars [web] | Floating circles over text [obs] | None; opaque black chrome [obs] |
| Row | Tracks 64-68pt, library ≈87pt [meas] | 75-76pt chats [meas] | Post, no separators [obs] | ≈162pt documents [meas] | No lists |
| Long-press | Preview + menu [know] | Lifted bubble, reactions, menu [obs] | Avatar preview [know] | Summary preview without opening [doc] | Not used |
| Non-content words | Playlist 1-2, library ≈14, player ≈4 [obs] | Chat list 11, chat 6, menu 8 [obs] | Feed 2, thread ≈12, search ≈14 [obs] | Inbox 5, reading 2 [obs] | Camera 3, exposure menu 6 [obs] |

## Category rules

### Shell and navigation

1. **Keep a persistent mini player (or any running task) above the tab bar on every screen**, because playback outlives navigation and the user must be able to pause from anywhere. Spotify [doc, obs].
2. **Promote search to a detached button beside the tab bar**, because it is used from every tab and is a verb, not a place. Telegram [obs].
3. **Use filter chips at the top of a mixed-content screen (All · Music · Podcasts) instead of extra tabs**, because the types share one surface. Spotify [obs].
4. **Put user folders as a horizontal strip under the title with unread counts as the only number**, because the count is the reason to switch. Telegram [obs].
5. **Carry the "unread elsewhere" count on the back button**, so it answers "should I go back?" from inside a chat. Telegram [obs].
6. **Put the account avatar top-left of root screens as the door to settings**, because settings are rare. Spotify [obs].
7. **Use a label-free tab bar only when every icon is universal (home, heart, person, plus, plane).** Threads [obs].
8. **In a single-purpose tool, put every secondary surface one tap from the main screen (corners, ears beside the Dynamic Island, a "…" menu) instead of tabs.** Halide [obs, doc].
9. **Model a "things to process" list as Inbox → Later → Archive with one-gesture moves between them, and give pushed content (feeds) different states (Unseen / Seen).** Readwise Reader [doc].

### Players and full views

10. **Make the mini player a floating card inset about 8pt, about 54-56pt tall, tinted from the current artwork, with a 2pt progress line inside its bottom edge**, so it reads as a separate object that expands. Spotify [meas].
11. **Grow the full player out of the mini player as a full-screen cover and collapse it back on swipe down**, so the user feels it is the same object. Spotify [know].
12. **Title the full player with the source context ("playing from X"), and make play/pause the largest control (≈64pt) in the middle of the transport row.** Spotify [obs].
13. **Swap the action toolbar for a quiet progress footer in long-form reading.** Readwise Reader [doc].

### Rows and feeds

14. **Express per-row metadata as glyphs and numbers (ticks, badges, pin, mute), never words**, because a list of 50 rows multiplies every label by 50; grey out muted badges. Telegram [obs].
15. **Keep chat rows at about 76pt with a 60pt avatar and two lines (three in groups) at the same height.** Telegram [meas].
16. **Build a text post as a two-column grid (avatar column, 12pt gap, one text column everything aligns to) and skip separators or keep them under 4% black.** Threads [meas web, obs].
17. **Put post actions as four bare 20pt icons with counts in fixed slots, even at zero; push mute, report and save behind ⋯.** Threads [meas web, obs].
18. **Use relative-time units (1m, 2h) and bare counts as the only social metadata.** Threads [obs].
19. **Put follow as a small badge on the avatar, not a button per post.** Threads [obs].
20. **Mark the playing row by recolouring its title in the accent, not with an icon.** Spotify [obs].
21. **Put ⋯ at the end of every media row for the long action list, and keep one swipe for the most frequent act (add to queue).** Spotify [know].
22. **Make rows for long-form content tall and rich (source, 2-line title, 2-line summary, minutes, thumbnail)**, with cost in minutes ("16 mins"), because the decision is "read this or not". Readwise Reader [meas].
23. **Grey out, don't hide, items unavailable offline**, so the library keeps its shape. Spotify [know].

### Gestures, menus and swipes

24. **Build the long-press menu around the pressed item: lift it in place, blur the rest, reactions above, actions below**, so the eye stays on what was pressed. Telegram [obs].
25. **Finish the functional layer in ≤150ms and let decoration follow** (Telegram: blur ≈100ms, menu ≈85-130ms, reaction bar ≈150ms, emoji staggered ≈180ms, settled ≈570ms). Telegram [meas].
26. **Grow overlays from the point of touch and stagger small items 10-20ms apart left to right.** Telegram [meas, obs].
27. **Order menus by frequency, Delete in red near the end, and the mode switch (Select) in its own last group.** Telegram [obs].
28. **Give the most common response a zero-menu gesture (double-tap to react), configurable.** Telegram [doc].
29. **Offer swipe-to-reply with a threshold haptic.** Telegram [know].
30. **Make swipe actions user-configurable in a triage app**, because each user's two most common dispositions differ; draw the revealed panel with rounded leading corners. Readwise Reader [doc, meas].
31. **Offer a bulk "mark everything above as seen" for feeds**, because skimming is scroll-then-clear. Readwise Reader [doc].
32. **Let long-press preview a document's summary without opening it**, because opening changes its state. Readwise Reader [doc].

### Composing and input

33. **Let one composer button morph by state (mic ↔ send) instead of showing both.** Telegram [obs].
34. **Make hold-to-record self-explaining with inline copy ("Slide to cancel") and a visible lock target.** Telegram [obs].
35. **Swap the keyboard for media pickers at the same height**, so the layout does not jump. Telegram [obs].
36. **Offer a one-line inline composer where people read, with an expand control to the full composer.** Threads [obs].
37. **Keep Post disabled until there is content and put the audience setting as a quiet footer beside it; confirm a draft dismiss with "Save draft" first.** Threads [know].

### Reading

38. **Make selection itself the highlight, with handles to adjust and no confirm step; one highlight colour, categories in tags.** Readwise Reader [doc].
39. **Render highlights as a per-line tinted fill plus a 2px saturated underline**, so they stay visible on any theme. Readwise Reader [meas].
40. **Keep the UI accent separate from the "kept" colour** (indigo vs highlight yellow). Readwise Reader [meas].
41. **Show reading progress as a 2pt line and a "Return to X%" pill only when position and progress diverge; track furthest-read separately from current location.** Readwise Reader [meas, doc].
42. **Stop auto-follow (text-to-speech scroll) the moment the user scrolls and offer a return control.** Readwise Reader [doc].
43. **Use margin taps for page turns when horizontal swipes are taken, and let a swipe across the bottom toolbar move to the next document.** Readwise Reader [doc].
44. **Let the reader choose face, size, spacing and theme, including accessibility faces (Atkinson Hyperlegible, OpenDyslexic).** Readwise Reader [doc].

### Camera and one-screen tools

45. **Stack a tool screen as read-outs at the top, content in the middle, control rows ordered by frequency toward the bottom, the primary action centred in the lowest row.** Halide [meas, doc].
46. **Size controls by importance: primary ≥72pt, frequent toggles 44-46pt, chips in a group about 29pt with the selected one larger (35pt) and ringed.** Halide [meas].
47. **When a setting leaves its default, surface it on the main screen until it is reset**, because forgotten manual settings ruin the next result. Halide [doc].
48. **Turn aids on only during the adjustment (loupe, peaking) and off on release; show the precise number only while dragging.** Halide [doc].
49. **Bind continuous values to swipe axes (vertical = brightness, horizontal = focus) and give dials detent haptics.** Halide [know, 3p].
50. **Keep chrome around a photo or preview neutral and opaque**, because tint or translucency changes how the image is judged. Halide [obs].
51. **Explain a control with a brief tooltip on its first toggles instead of a permanent label.** Halide [doc].
52. **Keep the old layout reachable after a redesign of a muscle-memory tool.** Halide [doc].

### Colour, type and materials

53. **Let content supply the colour (artwork tints, wallpapers) and keep chrome neutral.** Spotify [doc], Telegram [obs].
54. **Give one accent one job set and reserve red for destructive and live.** Telegram [obs]; Halide's yellow means only "engaged" [meas]; Threads uses black as primary and colour only for state [obs].
55. **Put a dark glyph on a bright brand colour when white fails contrast, rather than darkening the brand colour.** Spotify [doc].
56. **Use glass only on floating controls, never content, and offer a "reduce effects" switch.** Telegram [obs, doc].

### Messages and states

57. **Make a one-line bubble about 33pt tall with full-round ends, the time and ticks inside it, the tail only on the last of a run, about 80-85% max width and about 10pt outer margin.** Telegram [meas].
58. **Show delivery as a glyph progression inside the bubble meta (clock, one tick, two ticks).** Telegram [obs, know].
59. **Put connectivity state in the title, not a banner.** Telegram [know].
60. **When a confirm guards a destructive action, make the safe option the filled default.** Telegram [obs].

### System surfaces

61. **Publish now-playing metadata and remote commands to the system**, because the Lock Screen and Dynamic Island are where users pause. Spotify [know].
62. **Expose the primary action to every system entry point (Lock Screen, Control Center, hardware button).** Halide [know, doc].
63. **Make the share extension a first-class capture surface with one-tap disposition (Inbox, Later, note), recent targets first.** Readwise Reader [doc], Telegram [know].

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Mini player | ≈54pt tall, inset ≈7-8pt, radius ≈6-8pt, art ≈40pt, title 14-15pt, 2pt progress inside the bottom edge | Spotify [meas ±5%] |
| Playlist | hero ≈300pt, title ≈40pt heavy; play circle ≈48pt; track rows 64-68pt, art 48-51pt | Spotify [meas] |
| Library | header ≈56pt, avatar 32pt, title ≈24pt; chips ≈32pt; rows ≈87pt, art ≈69pt; 16pt margins | Spotify [meas] |
| Player | play/pause ≈64pt white circle | Spotify [obs] |
| Contrast | black on green 10.9:1; green on grey 9.7:1 | Spotify [doc] |
| Chat list | nav row ≈44pt; stories ≈51pt avatars, row ≈90pt; chat rows 75-76pt, avatar ≈58-60pt at x=15, text at x≈84 | Telegram [meas] |
| Tab pill | ≈62pt tall, inset ≈16pt | Telegram [meas approx.] |
| Chat | back circle 44pt; avatar ≈40pt; bubble ≈33pt one line, radius ≈16-17pt, 10-11pt outer margin; composer circles ≈40pt, field ≈250pt, ≈6pt gaps | Telegram [meas] |
| Web bubble | radius 0 15px 15px, padding 4px 9px, 14/21, meta 12px #7d7f81, 3px gap, max 84% width | Telegram [web] |
| Context menu | blur ≈100ms; menu ≈85-130ms; reaction bar ≈150ms; emoji ≈180ms; total ≈570ms; rows ≈44pt, group gap ≈8pt | Telegram [meas 60fps] |
| Feed post | avatar ≈44pt at x≈13, text at x≈68; name and body 15pt, 21pt pitch; tab icons ≈26pt, Create pill ≈48x36pt | Threads [meas] |
| Web post | avatar 36px, text at x=60; time #999; counts 13px #424242; icons 20px at ≈72-77px pitch; bars rgba(255,255,255,.85) + blur 28.5px; separators rgba(0,0,0,.04) | Threads [web] |
| Inbox | title ≈34pt; rows ≈162pt; domain 12pt caps; title 17pt semibold; summary 15pt; thumbnail ≈80pt, radius ≈6pt; 16pt margins | Readwise Reader [meas] |
| Swipe panel | #5a48d7, leading radius ≈10-12pt, label 15pt, icon ≈24pt | Readwise Reader [meas] |
| Reading view | text #2a313a on #f7f8f9, 16pt margins, 22pt line pitch; default 20px at 1.4, range 14-80px | Readwise Reader [meas, doc] |
| Progress | 2pt, #4e46dd on #e1e3e6; "Return to" pill ≈41pt; footer ≈35pt, title 13pt | Readwise Reader [meas] |
| Highlight (dark) | fill #454115 per line + 2px underline #ffd300 on #131d24 | Readwise Reader [meas] |
| Camera | viewfinder 402x536pt; composition circles 46pt; AF 37pt; lens pill ≈198x47pt, chips 29pt, selected 35pt; shutter ≈72pt in ≈85pt ring; thumbnails ≈68pt | Halide [meas] |
| Camera colours | #000, #101010 band, #181818 chips; yellow #ffd72c; active AF fill #4c4914 | Halide [meas] |

## Anti-patterns seen

- **An expand that users did not discover.** Spotify found that not all listeners knew tapping the old now-playing bar opened the full player, which led to the floating tinted card [doc].
- **Type words repeated on every row of a mixed list.** Spotify's library spends most of its ≈14 non-content words on "Playlist / Podcast" per row; the case calls it the price of a mixed list [obs].

## Steal list

1. Keep the constant action (player, running job) as a floating bar above the tab bar on every screen.
2. Grow the full view out of the bar and collapse it back with a swipe down.
3. Let content bring the colour and keep chrome neutral; one accent with one job set.
4. Lift the pressed item in place for its menu and finish the menu in ≤150ms.
5. Write row metadata as glyphs and numbers; grey what is muted.
6. Morph one composer button between record and send.
7. Align every part of a post to one text column and drop separators.
8. Keep four fixed action slots with bare counts; the rest behind ⋯.
9. Triage saved items Inbox → Later → Archive with configurable swipes.
10. Make selection the highlight and keep the highlight colour apart from the accent.
11. Track furthest-read separately from current position and offer a return pill only when they differ.
12. Order tool controls by frequency toward the bottom edge and size them by importance.
13. Surface any non-default setting on the main screen until it is reset, and show aids only while the finger is adjusting.

## For a business dashboard app (HQ)

The case files name three transfers. A long-running job (sync, upload, timer) can live in a mini bar above the tab bar, exactly like Spotify's now-playing bar. Email to-dos can take Readwise Reader's triage model: Inbox → Later → Archive with configurable swipes, and one accent for "act" kept separate from the colour for "kept" or "flagged". An active filter or non-default sort shows as a chip on the list header until it is reset, Halide's reminder for non-default settings; any one-screen tool in HQ (quick capture, a timer) takes Halide's hierarchy by size and position with one active colour.
