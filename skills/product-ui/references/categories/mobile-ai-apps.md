# Mobile AI apps

A phone-first AI app: one hand, one thumb, no hover, a keyboard that covers half the screen, and an operating system full of entry points (widgets, Lock Screen, Siri, CarPlay) that can open the app straight into a mode. The phone is also where the user is often walking, driving or holding something, so speech and the camera are first-class inputs, and long-running work tends to run somewhere else while the phone supervises it. Users judge the category on one question: can I get from "I want to ask" to "it's answering" with one thumb, in the mode I meant, without hunting for anything?

Studied: the ChatGPT iPhone/iPad app, version 1.2026.307 (Nov 10, 2026), studied 2026-11-18. The native app was not run. Native details come from App Store renders, official screenshots and videos, help center and release notes; exact pixel values come from chatgpt.com in iPhone emulation (393×852 @3x, iOS Safari user agent), used as a proxy. ChatGPT web and desktop are used only as a contrast.

Tags: [obs] observed in a capture (App Store render, official video frame, mobile web); [doc] OpenAI help center, release notes, posts or App Store listing; [3p] press or reviews, used only where OpenAI documents nothing; [inf] reasoning, not verified. Pixel numbers from App Store renders are approximate (≈); mobile web numbers are exact.

## What users expect

1. **The app opens into the conversation.** Asking is the one main job; every other destination can cost one swipe.
2. **The main action is under the right thumb, in the same place every time.** Muscle memory is the phone's shortcut system.
3. **Speech that does what the glyph promised.** Dictate-to-text and talk-live are different contracts and must look different before the tap.
4. **Long-press goes faster, never somewhere hidden.** iOS users try long-press on everything, but nothing may live only there.
5. **Actions visible without hover.** There is no hover on touch, so per-message actions must be on screen.
6. **Native behaviour.** System font with Dynamic Type, native context menus and text selection, 16 px inputs that do not zoom, biometrics instead of passwords.
7. **Permissions asked at the moment of need.** Mic on first voice use, photos on first photo, notifications on first task.
8. **Entry from outside the app.** Widget, Action button, Control Center, Siri and Lock Screen open straight into a mode.
9. **Honest device roles.** Read, approve and steer on the phone; author on the big screen, and the app says which is which.

## The theses to choose from

### ChatGPT iPhone: the thread is the app, the phone is an outbound surface
Core bet: one thread with a bottom composer is the whole app; voice, images, tasks, shopping and widgets render inside the thread as sheets, chips and cards, and the operating system is the shortcut layer.
- No tab bar, no home dashboard: hamburger top-left, a capsule with compose and ••• top-right, composer pinned at the bottom (all 8 App Store screenshots) [obs].
- One morphing primary slot bottom-right: Voice (accent circle, waveform) when empty, Send (accent up-arrow) when text exists, black X to end during voice; dictation mic stays still to its left [obs].
- Voice is a layer on the thread, not a separate mode (since Nov 2025); Live is full-duplex, so you interrupt by talking, and slow reasoning is delegated "behind the scenes" while the voice keeps talking [doc].
- Long-press duplicates visible paths: Send → one-off model, + → recent photos, chat row → Pin, user message → Copy/Edit [doc].
- Every primary mode is a system entry point: widget buttons for camera, photos, voice and dictation, Control Center, Shortcuts and Action button, Live Activities, CarPlay [doc][3p].
- Mobile supervises: Space pages are read-only on mobile; the Remote tab approves and redirects Codex running on a paired desktop [doc].
Choose this when one conversational job dominates and the product has several input modes (text, voice, camera) worth exposing at the OS level.

### Contrast: the same product on web and desktop
Core bet: a pointer and a wide screen let controls live in the composer and on hover.
- Model picker inside the composer instead of at the top of the conversation [doc].
- Per-message extras (for example "Branch in new chat") behind a hover ⋯ [doc].
- Full editing of Space pages and full Codex [doc].
Choose this split when the phone's job is quick asking and steering, and authoring needs a keyboard.

## Comparison

| Dimension | ChatGPT iPhone | ChatGPT web / desktop | Why it differs |
|---|---|---|---|
| Root screen | One thread, drawer for everything else | Thread plus persistent sidebar | Reach and width |
| Model choice | Top of the conversation; long-press Send for one message | Inside the composer | The commit button doubles as override under the thumb |
| Speech | Dictation and Voice both always in the composer; background voice, Live Activities, CarPlay, Action button | Voice exists, no system surfaces | Hands and eyes are busy on a phone |
| Photo input | Long-press + for recent photos, Scan → PDF, Sketch, full-screen image edit | Upload or drag | The camera is the phone's best input |
| Per-message actions | Always-visible row; native long-press menus | Hover ⋯ | No hover on touch |
| New chat | Compose top-right; mobile-web drawer has an accent "Chat" button bottom-left | Sidebar top item | Thumb reach |
| Authoring | Space pages read and share only | Create and edit | Long-form editing is poor on a phone |
| Long-running agents | Remote tab: approve and steer a paired host | Full Codex | Phone as supervisor |
| Locked chats | PIN or Face ID / Touch ID | PIN | Biometrics are the cheapest unlock on a phone |
| Event-triggered tasks | Create and edit | Desktop app can only display them | Triggers get set up on the go |
| Haptics | Toggle, auto-off at low battery | n/a | Device budget |

## Category rules

### Layout and navigation
1. **Make the most frequent job the root screen and put other destinations in a drawer, not a tab bar**, unless two or more destinations are used about as often as the main one. A drawer costs one swipe for rare trips and gives the thread the full screen. ChatGPT [obs].
2. **Keep the top bar to at most three controls: left for "go elsewhere", right for actions on this object grouped in one capsule, swapped per mode instead of added.** The right side becomes voice settings during voice and a temporary-chat toggle in that mode, so the bar never grows. ChatGPT [obs].
3. **In the drawer, give product areas one compact horizontal strip and give the user's own chats and projects the scrolling list.** Features grew faster than the list could absorb; the user scrolls their own content far more. ChatGPT, Mar 2026 [doc].
4. **Put the drawer's create action bottom-left as a labelled, accent-filled button and settings bottom-right.** That is where the thumb rests while the drawer is open. Mobile web "Chat" button 102×48 [obs].
5. **On a first visit where cookie, login or install banners will cover the bottom edge, put the first input in the vertical middle, and move it to the bottom once the user is in a thread.** Centering keeps the input visible; logged-out composer sits at y=394 of 852 [obs][doc].
6. **Keep the corner-control frame identical from phone to tablet**, so muscle memory carries over; a single-column chat on iPad is acceptable for a v1. ChatGPT iPad [obs][inf].

### Composer and the thumb-zone slot (extends L12)
7. **Lay out the bottom composer left to right as [add] [input] [secondary input mode] [primary], with exactly one accent-filled control.** Attach is occasional and sits far from Send to avoid mis-taps; the primary sits under the right thumb. ChatGPT [obs].
8. **Cycle the primary slot through speak → send → stop → end, and keep the secondary control (dictation) still while it changes.** The hand learns one place for "the main thing" and the icon says what it is now. ChatGPT [obs]; Stop while streaming [inf].
9. **Give every composer control at least a 44×44 hit area even when the glyph is 20-24 pt, and set input text at 16 px or more.** Smaller hit areas cause mis-taps; iOS zooms on focus below 16 px. Mobile web [obs].
10. **Let the placeholder describe the current mode and attachments** ("Temporary chat", "Describe or edit this image", "Describe a new image"). The placeholder is the one label the user reads while typing. ChatGPT [doc].

### Speech
11. **Give dictation (speak to type) and voice (speak to converse) two adjacent controls with distinct glyphs, and make the more committal one visually primary.** One modality, two contracts; the user must know the outcome before tapping. Mic is dictation, waveform is Voice; help docs tell users when to use each [doc].
12. **Build the dictation bar as live transcript on top, cancel X on the left, scrolling waveform and elapsed timer in the middle, commit on the right (spinner while transcribing), with auto-submit off by default.** A visible transcript builds trust; review-before-send prevents mis-transcriptions going out. ChatGPT [doc]. **Retry a failed dictation once silently before showing an error, and keep dictation available after text exists so the user can keep building the message.** Transient failures are common on mobile networks. iOS Aug 2026, Android [doc].
13. **Make live voice a layer on the thread, not a separate screen, and show lists, maps and weather as cards in the thread while it talks.** Voice alone is bad at lists and code; the screen shows what speech cannot. ChatGPT since Nov 2025 [doc].
14. **Acknowledge instantly, delegate slow work to the background, and insert the result when ready; never block the live surface on a tool call.** Dead air reads as broken. GPT-Live delegation [doc].
15. **Scale the ambient voice indicator to the space: large and centered (≈44% of width) when it is the only content, small and docked above the composer (≈56 pt) when content exists; animate the interior at idle and enter in ≈250-300 ms.** Presence without taking the screen from content. Voice orb [obs].

### Long-press and menus
16. **Make long-press a faster route to something already visible, never the only route.** Long-press Send → one-off model without changing the default; long-press + → recent photos (the most common phone attachment). Experts gain speed, novices lose nothing. ChatGPT [doc].
17. **Use the OS context menu (lifted preview, blur) with 2-4 iconned actions, and add domain actions to native text selection instead of building custom selection.** Long-press then does what iOS users expect; "Make a correction" appears in the native selection bubble on the memory page. ChatGPT [doc].
18. **Use bottom sheets with a grabber for choices tied to the composer or an answer.** + sheet, Sources, temporary-chat settings all use them [doc]. In an add/tools sheet, put the 3 most common inputs on top as large tiles (Camera · Photos · Files) and the rest as rows with an outcome subtitle ("Get an in-depth guide", "Visualize anything"), mirrored as @-mentions for typing.
19. **Separate "set my default" (top of conversation, or a setting) from "just this once" (long-press the commit button), label options by effort (Instant / Medium / High / Extra High) and offer Auto switch.** Most users then never choose; brand-name models go one submenu deeper. ChatGPT Jun 2026 [doc].

### Output on a small screen
20. **Show per-message actions persistently but quietly: a row of ≈16 pt line icons at ≈32 pt spacing in a tertiary colour, left-aligned under each answer.** Hover-only actions do not exist on touch; ChatGPT moved actions to "always visible" in Feb 2025 and moving Read aloud into overflow drew complaints from accessibility users [doc][3p].
21. **Box output that leaves the chat (email draft, code, chart) as a card labelled by type, with its next-step actions (edit, copy, send, run) top-right.** Separates "read this" from "take this somewhere". Writing block "Email" with pencil, copy and accent send [obs]. Extends L4. **Put tap-to-expand detail behind highlighted entities (people, places, products) in a side panel, and show structured answers (weather, maps, fixtures) as native cards in the stream.** The main answer stays short at phone width. ChatGPT Jan and Jun 2026 [doc].
22. **Collect provenance into one tappable "Sources" chip per answer that opens a sheet, and give each source "Why this memory?" and "Make a correction" (plus Relevant / Not relevant).** Inline footnotes are untappable at thumb scale, and explanation should lead to correction. ChatGPT [doc]. Extends L7.
23. **Stream with a word-level opacity ramp over the trailing words, and never replay a finished answer when the user returns to it.** The soft edge reads as "being written" without a cursor; replaying is fake latency. ChatGPT Aug 2026 [doc]. Extends L6.
24. **Put anything sponsored after the answer's own action row, separated by a hairline, labelled "Sponsored" in words, with a one-line trust statement linking to controls.** The answer and its actions must stay one unit. ChatGPT ads test [doc].

### Trust, approval and modes
25. **Show a data-handling mode in three places: a top-bar toggle, an empty-state explanation, and the placeholder. Make the sub-choice in a sheet of two described option cards before the first message, then lock it and offer "save" to promote instead of edit.** Privacy choices must happen before data flows, and the user must see the mode while typing. Temporary chat [doc].
26. **Require on-screen approve/decline for consequential agent actions, even mid-voice ("spoken approval is not supported"), and pause the flow while waiting instead of failing it.** Speech is easy to mishear and say by accident; a tap is deliberate and leaves a record. ChatGPT Voice, tasks [doc]. Specific case of L9. **Hand credential entry to the user on a surfaced login screen; the agent never sees it.** ChatGPT Work browser [doc].
27. **Offer autonomy as about four named levels per type of action** (dots: "Take action without asking", "Take action if pre-approved", "Ask before taking action", "Hand off to you"; plugins: always ask / ask before changes / only important changes). A small named ladder is learnable on a phone. ChatGPT [doc].
28. **When the AI creates a persistent object, confirm cadence and trigger in one sentence and attach a typed chip that opens an editable sheet with pause at the top level** ("Done. I'll check your Gmail hourly and notify you only when a new package is confirmed delivered." + "Monitoring · Package Delivery Watch"). ChatGPT tasks [doc].
29. **Use device biometrics for privacy features and state a protection's limits next to it.** Locked chats unlock with Face ID / Touch ID and say they are not end-to-end encryption; "Resetting your account PIN permanently deletes all locked chats." ChatGPT [doc].

### System entry points and device roles
30. **Expose each primary mode as its own system entry point (widget button, Control Center control, Shortcut / Action button action) that opens straight into that mode, configurable per surface, with distinct icons for modes that share a verb.** The fastest interaction skips the app's home; Control Center's "Voice" and "Remote voice" sharing one icon drew a "Voice or Voice?" complaint [doc][3p]. **Show long-running live sessions on the Lock Screen and Dynamic Island through Live Activities, and end background sessions on inactivity only after a "still there?" check.** The user has left the app but the session is still running. ChatGPT Aug 2026 [doc].
31. **Choose capability per device on purpose and say so in the UI** ("Mobile does not support editing pages"); design the phone view of remote work for status, approval and redirection, mirroring the same objects (threads, approvals, diffs). A cramped editor is worse than an honest read-only view. Space, Codex Remote [doc].

### Errors, limits and onboarding
32. **Mark a failed send under the user's own bubble ("Something went wrong. ⓘ", small gray) and a failed reply inside the answer slot with one outlined "↻ Retry" pill, and give "waiting for an internet connection" its own state.** The failure stays at the turn it belongs to, and offline is not an error. ChatGPT [doc]. Specific case of L16.
33. **At a limit, name the limit and drop only the expensive part, offering the cheapest way on (continue in text, or a new chat "with a summary") before the upsell.** "Context window full" with a summary option keeps momentum. ChatGPT [doc]. Extends L15.
34. **Let the core action work before sign-in, ask for each permission only when its feature is first triggered (mic on first voice, photos on recent photos, push on first task), and teach features with an in-thread card that states its cost** ("Research the best Wi-Fi routers >" / "Spend a few minutes for better results"). The benefit is obvious at that moment, and a tour is not. ChatGPT [obs][doc]. Extends L13, L20.

## Measured constants

| Element | Value | Tag |
|---|---|---|
| Emulated viewport | 393×852 @3x | [obs] |
| Composer pill | 369×48, radius 28, white, `0.5px rgba(0,0,0,.1)` hairline, shadow `0 4px 16px rgba(0,0,0,.05)` | [obs] |
| Composer hit areas (+, mic, Voice) | 44×44 each | [obs] |
| Input text | 16 px (no iOS focus zoom) | [obs] |
| Voice button glyph | ≈32 pt (≈8% of width) | [obs, render] |
| Top bar hamburger chip | ≈44 pt circle, soft shadow | [obs, render] |
| Drawer width | 310 of 393 px (79%), dark scrim over the rest | [obs] |
| Drawer rows | 44 px tall at 48 px pitch, 17 px semibold, radius 12 | [obs] |
| Drawer Search | 44 px circle, top-right | [obs] |
| Drawer "Chat" create button | 102×48, `rgb(53,102,240)` / `#3566F0`, bottom-left | [obs] |
| Drawer Settings | 48 px circle, bottom-right | [obs] |
| Drawer recents | up to 8 recent conversations (Android) | [doc] |
| Empty-state headline | 24/28, weight 400 | [obs] |
| Secondary buttons | 14 px medium | [obs] |
| Logged-out layout | heading at y=342, composer at y=394 of 852, one starter chip, legal footer pinned bottom | [obs] |
| Assistant body | ≈16-17 pt regular; headings bold at body size | [obs, render] |
| User bubble | right-aligned, ≤≈75% width, pale accent tint | [obs, render] |
| Answer side margins | ≈20 pt, no container | [obs, render] |
| Generated image | ≈60% width, ≈16 pt radius (Android moved to full width) | [obs][doc] |
| Action row | 6 icons (Copy, Read aloud, Good, Bad, Regenerate, Share), ≈16 pt glyphs at ≈32 pt spacing | [obs, render] |
| Light colours | page `#FCFCFC`, text `#0D0D0D`, composer `#FFFFFF` | [obs] |
| Dark colours | page `#000000` (true black for OLED), text white, composer `#212121` | [obs] |
| Accent | `#3566F0`, user-selectable (Blue, Green, Yellow, Pink, Orange, Purple, Black/White, custom hex per appearance); applies to bubbles, Voice button, highlighted text | [obs][doc] |
| Terminal actions | black, not red (end-voice X, "Done" pill) | [obs] |
| Font | `-apple-system-body, ui-sans-serif, -apple-system, system-ui` (SF with Dynamic Type) | [obs] |
| Voice orb, empty chat | ≈44% of screen width, centered | [obs, video] |
| Voice orb, docked | ≈56 pt above the composer | [obs, render] |
| Orb entrance | ≈15% → full in 8 frames at 30 fps (≈270 ms) | [obs, video, may be composited] |
| Orb idle | diameter constant, interior band cycle ≈1.7 s | [obs, video] |
| Dictation timer | elapsed "0:02" format; auto-submit default off | [doc] |
| Haptics auto-off | Low Power Mode or battery below 20% | [doc] |
| Temporary chat retention | up to 30 days | [doc] |
| Audio clip retention | 30 days with transcript | [doc] |
| Locked chats | 4-digit PIN or Face ID / Touch ID | [doc] |
| Accounts | up to 2 per app | [doc] |
| Voice limits | rolling 24 hours | [doc] |

## Anti-patterns seen

- **Hiding an accessibility action in overflow.** Moving Read aloud out of the always-visible row produced angry reviews from accessibility users [3p]. Fix: keep actions that some users depend on in the visible row.
- **Two modes with one icon.** Control Center "Voice" and "Remote voice" shared an icon ("Voice or Voice?") [3p]. Fix: one glyph per mode, even when they share a verb.
- **Store notes that say nothing.** Every App Store version said "Bug fixes and small improvements." on a weekly cadence (25 versions, Jun to Nov 2026) while real notes lived in the help center [doc]. Fix: put at least the headline change in the store notes.
- **Silent behaviour change.** Haptics turn off below 20% battery and this is explained only in a help article [doc]. Fix: say it once in the setting itself.
- **Replaying finished answers.** Until Aug 2026, returning to a chat replayed completed answers as if they were still streaming [doc]. Fix: animate only content that is actually arriving.
- **Pilots that complicate the core loop.** Group chats launched Nov 2025 and stopped creation Jul 2026 "to simplify" [doc]. When retiring, keep history readable and publish the dates, as ChatGPT did.
- **A gray box after sending an image.** Fixed Jun 2026 with an immediate optimistic preview [doc].

## Steal list

1. Open into the conversation and put everything else in a drawer, sheets and inline cards, because modes should not cost a navigation step.
2. Give the primary action one fixed bottom-right slot that cycles speak → send → stop → end, with one accent-filled control at a time, because the thumb learns one place.
3. Use 44×44 hit areas and 16 px input text everywhere, because mis-taps and focus zoom are the cheapest bugs to avoid.
4. Put dictation and voice side by side with distinct glyphs, because the user must know which contract they are starting.
5. Default dictation to review-then-send with a live transcript and timer, and retry once silently, because mis-transcriptions are embarrassing and mobile networks flake.
6. Keep voice inside the thread and delegate slow work while it keeps talking, because the screen shows what speech cannot and dead air reads as broken.
7. Make long-press a shortcut to something visible (one-off model on Send, recent photos on +), because experts get speed and novices lose nothing.
8. Use native context menus and text selection, adding your actions into them, because iOS users already know how they behave.
9. Show the per-message action row always, in tertiary line icons, because there is no hover on touch.
10. Collect sources into one chip and sheet with "Why this?" and "Make a correction", because footnotes are untappable and explanations should lead to fixes.
11. Show a privacy mode in the top bar, the empty state and the placeholder, and lock it after the first message, because users must see the mode as they type.
12. Approve consequential agent actions on screen only, never by voice, and pause while waiting, because a tap is deliberate and leaves a record.
13. Confirm persistent AI objects in one sentence with cadence and trigger, plus a typed chip that opens an editable sheet with pause, because the user needs a handle on what now runs without them.
14. Label model options by effort with an Auto switch, and keep the per-message override on long-press, because users can judge speed but not codenames.
15. Ship every primary mode as a widget button, Control Center control and Shortcut action that opens straight into the mode, because the fastest interaction skips the home screen.
16. Show live background sessions on the Lock Screen through Live Activities, because the user has left the app but the session has not ended.
17. Make the phone the place to read, approve and steer, and say plainly when editing is desktop-only, because an honest read-only view beats a cramped editor.
18. Use black for End and Done and keep red for real danger, with true black in dark mode, because the accent and red then keep their meaning.
19. Scale the live-state indicator to the free space (≈44% of width alone, ≈56 pt docked) with a ≈270 ms entrance, because presence should not take the screen from content.
20. Ask for each permission only when its feature is first used, and let the core action work before sign-in, because the benefit is obvious at that moment.
