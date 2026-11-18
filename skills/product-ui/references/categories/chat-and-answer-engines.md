# Chat assistants and answer engines

A chat assistant or answer engine is one composer, one thread and a sidebar of the user's own objects: the user types, the model writes back, and everything else (models, modes, files, agents, verticals) hangs off those two surfaces. Chat assistants are judged on one question: "can I get a good answer, read it comfortably, and steer the next one without hunting?" Answer engines add a second: "can I verify it?" Every decision in this chapter serves the read-and-steer loop and, for answer engines, the proof attached to each claim.

Studied (all observed 2026-11-18, clean logged-out profiles, 1440x813 desktop and 390x844 mobile, light and dark):
- ChatGPT (chatgpt.com): full logged-out chat, six prompts streamed, menus, gates, settings, mobile. Logged-in features from OpenAI help center [doc] or prior knowledge [know].
- Claude (claude.ai): hard login wall, so no live chat. Studied the login page, a public shared chat (uses the real thread renderer) and a public artifact page [obs], plus CSS tokens [obs]; logged-in app from Anthropic help center [doc] and [know].
- Perplexity (perplexity.ai): two full cited answers in one thread, command menus, citation hover cards, Sources pane, Links and Images tabs, Finance and Discover verticals, the gating ladder, mobile [obs].

## What users expect

1. Type immediately on arrival, because the first answer is the product demo. ChatGPT and Perplexity allow it logged out; Claude does not and must sell through its login page and share pages instead.
2. Send, stop and copy work on every answer, at every tier, because their absence reads as broken, not premium.
3. The answer is readable as a document (one measure, no avatar chrome), because people read answers, they do not watch a chat.
4. A visible way to try again (regenerate, edit, fork, rewrite with another model), because the first answer is often not the one they keep.
5. Visible progress within ~2s and first text within ~2.5s, because anything slower without feedback looks stuck (ChatGPT first text 1.45-2.4s; Perplexity "Finished 2s" plus first text at +2.3s on a fresh thread) [obs].
6. History they can come back to, and a warning before anything is lost, because silent loss is the one thing a free tier is not forgiven for.
7. Model choice for power users, close to where they commit or judge a message, because quality and cost are traded per message.
8. Answer engines only: a link to every claim and a way to see "the real results", because verification is the reason to use one over a chatbot.
9. A clear privacy story (what is saved, what trains the model, incognito), stated where the choice is made.

## The theses to choose from

### ChatGPT: the composer is the product, every other feature is a visible locked door

Core bet: disappear into one composer and one calm column, show the whole feature surface logged out, and convert after value.
- One 44px slot morphs Voice → Send → Stop; the blue disc never moves, only glyph and label change (Stop appeared 554-2006ms after send) [obs].
- Pill composer (768x52, radius 28) that becomes a card with a bottom toolbar when text wraps; textarea 17px/24px, one pixel above body text [obs].
- One saturated accent, blue `oklch(0.5609 0.2145 265)`, spent only on Send, Voice, switches and the mobile new-chat button; the user bubble is tinted with the same hue [obs].
- Streamed words fade in per SPAN over 700ms linear with ~4ms stagger; no caret [obs].
- New question pins near the top; the page does not auto-follow the stream [obs].
- Gated items stay visible: a grey "Log in to use..." group in the `+` menu, blur walls with two real rows visible, one upsell popover template for every gate [obs].

Choose this when the product is mass-market, interactions are short, the first session must happen before sign-up, the audience is international (system font), or a free tier needs upsell or ad surfaces.

### Claude: two voices, and the work shown as a quiet ledger

Core bet: the assistant writes in a serif, the interface speaks in a sans; agent process collapses into a ledger and deliverables move beside the chat.
- Font token literally named `--font-voice: anthropic-serif` for assistant prose at 15px/21px; UI, user turns and tool lines in anthropic-sans [obs].
- Tool bursts collapse into one grey counted line ("Ran 3 commands, created a file", sans 14px/20px, `rgba(0,0,0,.6)`), expanding to an icon timeline, then to the raw command [obs].
- Composer is a card from line one; model and effort read as one phrase next to the clay Send ("Opus High ⌄"), and the effort menu warns that higher effort reaches limits faster [obs demo; doc].
- Deliverables (docs, slides, designs) open as artifacts in a panel beside the chat; connectors choose inline card, side panel or full screen by how long the user stays [doc].
- Warm grays (`#f9f9f7` to `#0b0b0b`), clay `#d97757` for brand and Send only, blue `#2a78d6` for focus and links only [obs].

Choose this when outputs are documents, code or analyses, transcripts would otherwise drown in tool calls, or the product is paid and trust, readability and controllable cost matter more than first-session conversion.

### Perplexity: answer first, proof always attached

Core bet: the moat is trust, so the richest components go to provenance, and the answer reads as an article.
- Every paragraph ends in a mono 10px source chip with the host name and a class icon; a ~280ms hover card names the class ("Trusted", "Government") and why [obs].
- One source set, four presentations: inline chips, a favicon stack with "10 sources" in the action row, a 336px Sources pane, a full SERP-style Links tab [obs].
- Answers in pplxSerif 16px/26px on a 720px measure; the question is the only bubble; reasoning text stays sans [obs].
- Streaming in labelled phases: "Working" shimmer, then "Working 1s, 2s…", images before text, "Finished 5s", then text at ~150-180 chars/s, then actions and related questions fade in [obs].
- Command "chin" attached under the composer with a live preview pane per item; `/` modes, `@` connectors, typing gives completions [obs].
- A context-scoped composer on every page ("Ask anything about NVIDIA Corporation") [obs].

Choose this when answers are retrieved from sources, users must verify before acting (research, finance, health, academic), or the product mixes generated prose with live structured data.

## Comparison

| Dimension | ChatGPT | Claude | Perplexity |
|---|---|---|---|
| Logged-out access | Full chat, one thread at a time [obs] | None; login is the homepage [obs] | Two answers, then a blur wall [obs] |
| Answer type | System sans 16/26, 768px | Serif 15/21, 720px | Serif 16/26, 720px |
| User turn | Blue-tinted bubble, blue text, radius 22 | Neutral grey bubble, sans, radius ~16 | Grey bubble, sans, right-aligned |
| Composer | Pill → card on wrap, radius 28 | Card from line one | Frame 26 + field 20 + 6px padding |
| Primary slot | Voice → Send → Stop, blue 44px | Clay Send → Stop [know] | Voice → Submit → Stop, `#252525` 32px |
| Model choice | Header "ChatGPT ⌄" [know] | "Model Effort ⌄" next to Send [doc] | Composer "Model ⌄" and Rewrite submenu [obs] |
| Process display | "Thought for Ns" collapsible [know] | Counted ledger, 3 disclosure levels [obs] | "Finished Ns ⌄" status with steps [obs] |
| Provenance | Source chips and panel logged in [know] | Share-page provenance card [obs] | Class-coded chips, hover card, pane, SERP tab [obs] |
| Per-answer actions | Copy, Share (logged out); +thumbs, Regenerate [doc] | Last turn visible, older on hover [obs] | Latest turn only, after streaming [obs] |
| Regenerate | Icon in row [doc] | Retry with model dropdown [know] | Rewrite › mode or named model [obs] |
| Accent use | Blue for "go" | Clay for brand + Send, blue for focus | Teal for links, trust, active mode; buttons near-black |
| Monetization surface | Labelled ads under answers [obs] | Plans under login, usage windows [obs] | Locked rows, plan badges, pricing sheet [obs] |

## Category rules

### Layout

1. Use one reading column for every output type (prose, code, tables) and size the composer to it: 720px (Claude, Perplexity) to 768px (ChatGPT) [obs]. Do this because aligned left edges make a long thread scan as one document and the composer reads as part of the page.
2. Put retrieval material in a fixed 320-336px right pane beside the 720px column, never between paragraphs, because sources must stay one glance away without interrupting the text (Perplexity `--context-pane-width: 336px`) [obs].
3. Keep the sidebar for the user's own objects (new, history, projects, agents) and move product verticals to one secondary menu, because the sidebar reads as "my stuff" (Perplexity "Apps and more") [obs].
4. Give threads of 3+ turns a turn navigator: one 8x1.5px dash per turn at the left edge (opacity .25, current .6) with a hover card of question, 3-line snippet and time, because it costs ~10px and replaces scrolling (Perplexity) [obs]. Keep in-thread view switches (Answer / Links / Images) in a URL query param (`?sm=r`), because they are lenses on one object.
5. Set `scrollbar-gutter: stable` on the thread scroller and fade content under the sticky composer, because streaming growth otherwise shifts layout sideways and a hard cut makes the composer look pasted on (Perplexity, ChatGPT) [obs]. Reserving the last line's space is L14.

### Composer

6. Build the composer as an outer frame plus an inner field with concentric radii (outer = inner + padding, e.g. 26 = 20 + 6), with elevation on an `::after` layer, because attached menus and mode states can restyle the frame and animate depth without touching the text (Perplexity) [obs].
7. Choose the shape by prompt length: a pill at one line that becomes a card with a bottom toolbar on wrap for quick questions (ChatGPT), a card with a fixed bottom toolbar from line one for long work prompts (Claude). Cap growth at 40-45vh and scroll inside (Perplexity). Do this because controls must not move under a long draft and the answer above must stay visible [obs].
8. Attach composer menus as a "chin" that squares the composer's bottom corners and extends the same recessed surface (radius animated 250ms `cubic-bezier(.22,1,.36,1)`), with a preview pane that explains the highlighted item in one sentence plus its own CTA ("Use" or "Sign in"), because the menu reads as part of the input and each capability is explained before commitment (Perplexity) [obs].
9. Map one trigger character per intent: `/` for modes and tools, `@` for connectors and sources, plain typing for completions (typed prefix regular, predicted suffix bold), because the character tells the system which menu the user means (Perplexity) [obs].
10. Rotate the placeholder through hidden power features ("Ask anything…" → "Type @ for connectors" → "Type / for search modes", ~1.5s each) and scope it to the page ("Ask anything about NVIDIA Corporation", "Ask a follow-up"), because the placeholder is free onboarding at the exact spot of use (Perplexity) [obs].
11. Mark modes that change how the message runs or what is saved on the composer frame itself: accent border and glow for agent mode (Perplexity Computer), black border plus "Incognito chat" label (Claude), a blue indicator for Research (Claude), because the state must be visible where the user types, not only in a closed menu [obs; doc].
12. Show model and effort as one short text phrase next to Send ("Opus High ⌄") with the cost warning inside that menu ("Higher effort ... you'll reach your usage limits faster"), and express plan limits as time windows and multipliers ("every 5 hours and every week", "5x Pro"), because quality and quota are chosen at the commit point and users plan around time, not tokens (Claude) [doc; obs]. Sharpens L12 and L15.

### Output

13. Give the assistant's prose a role-named typeface distinct from the UI (a text serif as `--font-voice`, sans for controls and the user, mono for metadata), and keep reasoning text in the UI sans, because type alone then tells the reader who is speaking and thinking is not the answer (Claude, Perplexity `.thought .prose`) [obs]. Use the system sans instead when coverage of every script matters more (ChatGPT) [obs].
14. Pin the new question to the top of the viewport with empty space below, do not auto-follow the stream, and fade text in by word (ChatGPT: 700ms linear opacity, ~4ms stagger) or by chunk, never with a typewriter caret, because readers start at the first line and bursty 200ms chunks then arrive as a calm wave (ChatGPT, Perplexity) [obs].
15. Render tables at or below prose size with hairline row dividers, no vertical rules and no outer frame; Claude uses zero horizontal cell padding so columns align with the text edge, and has the model bold the winning value per row. Give code a language label, a top-right Copy and three syntax roles (keyword, function, builtin). Do this because tables are scanned and should carry their own conclusion, and code is the most-copied output [obs].
16. Disclose agent work in three levels: one counted past-tense summary line per burst ("Ran 3 commands, created a file"), then a step timeline with type icons and plain-English titles, then the raw command in a card, because each level answers a different question: what, in what order, exactly how (Claude) [obs]. This is the category's concrete form of L5.
17. Open a deliverable in a panel beside the chat when it is self-contained, over ~15 lines, and likely to be edited or reused; pick the container by dwell time (inline card for a confirmation, side panel for something watched, full screen for something edited, composer still available), because a document has a different lifecycle from a reply (Claude) [doc].
18. End the latest answer with 5 full-width related-question rows (↳ glyph, ~49px pitch, no heading) that send as follow-ups in the same thread, because the follow-up is the habit loop of an answer engine (Perplexity) [obs].

### Progress

19. Stream in labelled phases: status with a rising elapsed counter ("Working 3s"), then media or source cards, then "Finished Ns", then text, then actions, and collapse the status into a disclosure afterwards ("Finished 2s ⌄", "Thought for Ns"), because a verb plus a number proves the system is not stuck, images fill the 3-5s research gap, and the finished answer should not carry its wait (Perplexity [obs], Claude [doc], ChatGPT [know]). Shimmer the status label per L6.

### Trust and provenance (answer engines)

20. Put a source chip after each sentence or claim cluster, not a superscript number: mono 10px, tabular-nums, 7% ink fill, radius 6, 20px tall, host label ("jpl.nasa"), "+N" overflow, because a readable host builds trust at a glance and mono reads as metadata (Perplexity) [obs].
21. Encode source class in the chip icon (shield = Trusted, building = Government) and explain it in the hover card with a one-sentence reason and "Rate this source", because "who says so" matters more than "where" (Perplexity) [obs].
22. Present one source set at four depths (chip, favicon stack + count, side pane grouped by the query that produced it, full SERP tab), because readers verify at different depths (Perplexity) [obs]. L7 sets the one-gesture minimum; this is the full ladder.
23. Keep the accent for meaning (links, trust classes, active mode) and make the primary button near-black, because a coloured primary competes with the coloured citations the product depends on (Perplexity `#252525` buttons, teal `#016a71` links) [obs].
24. On public copies of a chat, render with the real thread renderer, state who shared it, that it is a snapshot and may be incomplete, put Report inside that notice, end with one centered CTA ("Ask Claude your own question"), and serve user-generated artifacts from a separate origin in a sandboxed iframe, because readers need provenance first and an invitation last, and shared code must never touch the logged-in app (Claude) [obs].

### Recovery

25. Put model switching inside regenerate ("Rewrite ›" lists modes and named models, sticky "Rewrite" footer) and state that a mid-thread change "applies starting with the next response", because "try again" and "try with a better model" are one intent, best offered where the user judges the result (Perplexity [obs], Claude [doc]).
26. Offer Fork beside edit, and make editing a user turn create a branch with "‹ 1/2 ›" arrows, because exploring must keep the cited original intact (Perplexity [obs], ChatGPT and Claude [know]). This is L10 applied to threads.
27. Mark a stopped answer as stopped and offer Continue, because ChatGPT's silent mid-sentence end ("...and I'll help") looks like a crash [obs].

### Actions

28. Show per-answer actions only after streaming ends, visible on the latest turn (Perplexity: latest only; Claude: last visible, older on hover, toolbar opacities 0,1,0,0,0,1) and always visible on touch. Use icon-only 32-44px ghost buttons for frequent verbs (Copy, thumbs, Fork) and words in an overflow for rare or consequential ones (Rewrite, Download, Export as PDF, red Delete under a divider). Do this because actions on a half-written answer invite mistakes, repeated toolbars clutter a thread, and words prevent slips [obs].

### Cost and gating

29. Escalate logged-out nudges with delivered value: passive sidebar card, then a dismissible bar above the composer after answer 1, then a non-modal popover after answer 2, then a wall (Perplexity on query 3; ChatGPT auto-modal ~8s after answer 5), because the first steps can be ignored at no cost [obs]. Never re-wall answers already received, which Perplexity does [obs]. Refines L13.
30. Keep gated features visible: a grey "Log in to use..." group label with the reason in each item's accessible name ("Create image. Log in to use."), greyed model rows with a lock and plan badge, and one upsell template (image, title, one benefit sentence, filled primary + outline secondary) for every gate, because the ceiling is the pitch, screen readers need the reason too, and a consistent gate reads as policy, not nagging (ChatGPT, Perplexity) [obs].
31. Carry intent through login (`?next=` on ChatGPT plugin installs, `returnTo=` on every Claude route), because a second click after sign-up loses people [obs].
32. Fence ads below the answer with a hairline, a lead-in sentence ("This might also interest you."), an "Ad" pill and a one-click "About this ad", never inside the answer body, because mixing paid content into the model's voice destroys trust in every later answer (ChatGPT) [obs; doc].

### Mobile

33. Dock the composer to the bottom edge on every page (Perplexity, 16px gutters) or center it vertically on an empty home (ChatGPT, 12px gutters); turn the side pane into a draggable bottom sheet (24px handle, content `calc(100dvh - 24px)`); collapse toolbar labels to icons before dropping any control. Do this because the thumb zone is the bottom third, a 336px pane has no room beside a 390px column, and feature parity matters more than labels [obs; obs CSS].
34. Tell the user when a mobile feature silently degrades, because Claude's mobile research skips connectors "without an error or other sign" and that looks like a wrong answer [doc].

### Copy

35. Phrase the empty state as a question ("Where should we begin?", "What do you want to know?") and swap it by mode or entry ("What should we work on?" for agent mode, "You've been invited to an artifact" for invitees); write status as a verb plus a measured number ("Finished 5s", "10 sources", "Ran 7 commands"); keep the disclaimer one grey line under the composer, shortened inside a thread ("ChatGPT is AI and can make mistakes."). Do this because a question invites typing, numbers are the trust language of an AI answer, and later visits need only the caution [obs].

## Answer-engine pattern library

Compact anatomy of Perplexity's components, all [obs] unless tagged. Format: anatomy · states · use.

- **AE1 Citation chip.** Inline after the sentence; 20px pill, mono 10px, 7% ink, radius 6, padding 3/4.8px, optional 12px class icon, host label, "+N". · Idle, hover (150ms colour), hover card after ~280ms, keyboard focus. · Every factual paragraph drawing on retrieval; one chip per claim cluster.
- **AE2 Source hover card.** 320px, radius 12, ring + soft shadow; favicon + host, 1-line title, 3-line snippet, divider, trust class + reason, "Rate this source · Learn more". · Opens scale .95→1 in 150ms, side=bottom. · Any inline reference where leaving the page to check is costly.
- **AE3 Favicon stack + count.** 2-3 overlapping 16px favicons + "N sources" (12-14px secondary). · Static; click opens the Sources pane. · Wherever a generated block needs one-glance proof of breadth.
- **AE4 Sources context pane.** 320px card in a 336px column; collapsed "Sources [stack] N ›"; expanded list grouped by query; rows favicon, host, trust icon, 2-line title, 3-line snippet; "»" hides it. · Collapsed, expanded, hidden, empty ("Cited sources from search will appear here."), mobile bottom sheet [obs CSS]. · Threads with retrieval.
- **AE5 SERP tab (Links).** "Search results for: <q>", rows with 28px favicon, host + badge, URL 12px, accent title, 2-line snippet, 80px thumbnail. · Per-tab URL param. · Classic results without leaving the thread.
- **AE6 Media tab (Images).** Justified rows 160px tall, 24px gaps, favicon + host caption. · Tab, not inline. · Visual queries; keeps answers text-first.
- **AE7 Status line.** 14px sans secondary "Working" with 1.2s text shimmer + seconds counter → "Finished Ns ⌄"; expands to a left-ruled step list with icons. · Working, finished, expanded. · Any AI task over ~1s.
- **AE8 Phased streaming.** Bubble + status at once → media → text in ~150-180 chars/s chunks with chips at sentence ends → actions and related questions fade in (150ms). · Pin the new turn to the top. · Any long-form generated answer.
- **AE9 Answer action row.** 32px ghost icons (Copy, Helpful, Not helpful, Fork) + source stack + far-right "…" (Download, Rewrite ›). · Hidden while streaming, latest turn only, dark tooltip radius 8. · Per-answer verbs, rare ones in overflow.
- **AE10 Rewrite-with-model menu.** Modes (✓ current), tinted upsell row, named models with New/Max badges and locks, sticky "Rewrite" footer. · Locked rows greyed. · Rerun with another engine where the result is judged.
- **AE11 Related questions.** 5 full-width rows, "↳", 16px sans, ~49px pitch, rounded hover fill, no heading. · Latest turn only; click = follow-up. · End of every answer.
- **AE12 Sticky follow-up composer.** 720px, docked to the column bottom, "Ask a follow-up", 130px reserve; sign-in bar may stack above; 32px ↓ button floats above when content is below. · Any thread UI.
- **AE13 Command chin (`/`, `+`).** Recessed container under the composer sharing the 26px outer radius; 320px list (36px rows, radius 8, separators, plan badges, › submenus) + preview pane (image, title, one sentence, "Powered by …", CTA). · Frame radius animates 250ms; arrow keys drive the preview; `+` becomes ×. · Tools, modes, attachments.
- **AE14 Mention popover (`@`).** Caret-anchored card, section label ("Connectors"), rows with logo + name + status ("Monthly query limit reached"). · Picking a source or connector inline.
- **AE15 Query typeahead.** Rows in the chin with a search glyph, typed prefix regular, completion bold, hidden "Fill query" button. · Search-like composers with short factual queries.
- **AE16 Data page with AI narrative.** Price strip with semantic colour and arrows · chart with toolbar and dot-grid backdrop · 3x3 hairline stats grid · AI timeline (date, dot rail, price, paragraph, "N sources" pill) · AI summary accordion ("Updated 1 minute ago", "99 sources") · right rail · entity-scoped composer. · Lead with numbers, let generated text explain the move, always with a sources pill. In-answer variants not observed (walled).
- **AE17 Turn navigator.** Column of 8x1.5px dashes at the thread's left edge, opacity .25 / .6 current; hover card with question, 3-line snippet, time. · Threads with 3+ turns.
- **AE18 Context-scoped composer.** Same component, placeholder naming the page's entity. · Every content or data page.
- **AE19 Gating ladder.** Dismissible bar above the composer → non-modal bottom-right auth popover (300x469, no backdrop) → `blur(4px)` wall with serif headline and "Back home", answer streaming behind. · Space steps by delivered value; unlike Perplexity, leave delivered answers readable.
- **AE20 Trust badge vocabulary.** Tiny icon (shield, building) in chips, pane rows and SERP rows; named class + one-sentence reason in the hover card. · Any UI mixing sources of different reliability.

## Measured constants

| What | Value | App, tag |
|---|---|---|
| Reading column | 768px | ChatGPT [obs] |
| Reading column | 720px (thread container 1100px) | Claude, Perplexity [obs] |
| Context pane | 336px column, 320px card, 16px gutter | Perplexity [obs] |
| Sidebar | 260px; collapsed rail 55px | ChatGPT [obs] |
| Sidebar | 240px default, resizable 200-400, rail 56px | Perplexity [obs] |
| Sidebar item | 247x36, 14px/20px, -0.15px tracking, radius 10 | ChatGPT [obs] |
| Answer type | 16px/26px system sans, `rgb(13,13,13)` | ChatGPT [obs] |
| Answer type | anthropic-serif 15px/21px, `rgba(0,0,0,.9)` | Claude [obs] |
| Answer type | pplxSerif 16px/26px, `#0b2833`; h2 18/28 600 | Perplexity [obs] |
| Composer text | 17px/24px | ChatGPT [obs] |
| Composer | 768x52, radius 28, halo `0 4px 80px 8px rgba(0,0,0,.024)` | ChatGPT [obs] |
| Composer | frame 652 radius 26, field 640 radius 20, padding 6 | Perplexity [obs] |
| Composer max height | 45vh (40vh lg, 25vh sm) | Perplexity [obs] |
| Follow-up composer reserve | 130px | Perplexity [obs] |
| Primary slot | 44px circle, blue `oklch(0.5609 0.2145 265)` | ChatGPT [obs] |
| Primary slot | 32px circle, `#252525` | Perplexity [obs] |
| User bubble | bg `oklch(0.9627 0.0179 265)`, text `oklch(0.497 0.215 265)`, radius 22, padding 10px 16px | ChatGPT [obs] |
| Stream fade | 700ms linear opacity per word, ~4ms stagger | ChatGPT [obs] |
| Stream rate | ~150-180 chars/s in chunks | Perplexity [obs] |
| First text after send | 1.45-2.4s | ChatGPT [obs] |
| Stop appears after send | 554-2006ms | ChatGPT [obs] |
| Citation chip | mono 10px, 20px tall, radius 6, padding 3px 4.8px, bg `rgb(28 28 28 / .07)` | Perplexity [obs] |
| Hover card | ~280ms open delay, 150ms `cubic-bezier(0.16,1,0.3,1)` scale .95→1, 319px, radius 12 | Perplexity [obs] |
| Working shimmer | 1.2s linear text sweep, band 38-62%, size 300% | Perplexity [obs] |
| Jump-to highlight | 3s ease-out, accent 15% fill + 2px ring | Perplexity [obs CSS] |
| Chin attach | 250ms `cubic-bezier(.22,1,.36,1)` on radius and bg | Perplexity [obs] |
| Menus | 150ms expo-out scale+fade, 36px rows, radius 8 | Perplexity [obs] |
| Menu | radius 16, items 44px radius 10 inset 6px | ChatGPT [obs] |
| Tool summary line | sans 14px/20px, `rgba(0,0,0,.6)`, radius 8, transition .2s `cubic-bezier(0.4,0,0.2,1)` | Claude [obs] |
| Button press | scale .975 in 60ms, 450ms spring release (`linear()`) | Claude [obs CSS] |
| Attachment enter | from opacity 0, scale .92, translateY 4px; 0.18s `cubic-bezier(.215,.61,.355,1)` | Claude [obs CSS] |
| Agent rail shimmer | 1.6s ease-in-out at opacity .75 | Claude [obs CSS] |
| Turn navigator dash | 8x1.5px, opacity .25 / .6 current | Perplexity [obs] |
| Related question row | ~49px pitch | Perplexity [obs] |
| Code block | radius 24, bg `oklch(0.964)`, 44px Copy circle | ChatGPT [obs] |
| Code block | radius 8, 0.5px `rgba(0,0,0,.08)`, mono 14px/22.75px | Claude [obs] |
| Table cells | 14px/20px, padding 8px 8px 8px 0, dividers `rgba(13,13,13,.05)` | ChatGPT [obs] |
| Table cells | serif 15px/21px, padding 7.5625px 0, TH rule `rgba(0,0,0,.1)` | Claude [obs] |
| Ink | teal-ink `#0b2833`, greys as 75/50/20% alpha | Perplexity [obs] |
| Accent | teal `#016a71` (dark `#4e99a3`) | Perplexity [obs] |
| Brand / functional accent | clay `#d97757` / blue `#2a78d6` | Claude [obs] |
| Dark page / text | `#000` / white | ChatGPT [obs] |
| Dark page / text | `rgb(21,21,21)` / `rgb(240,239,236)` | Claude [obs] |
| Dark page / text | `#15171b` / `#dbdee3` | Perplexity [obs] |
| Blur wall | `backdrop-filter: blur(4px)`, serif 30/39 headline | Perplexity [obs] |
| Login modal | 448x504, radius 20, backdrop `rgba(0,0,0,.5)` | ChatGPT [obs] |

## Anti-patterns seen

- ChatGPT logged out stops mid-sentence with no "stopped" marker and no Continue [obs]. Fix: mark it stopped and offer Continue on the same turn.
- Perplexity walls every earlier thread once the third query hits the limit [obs]. Fix: gate new answers, leave delivered ones readable.
- Perplexity disables Share logged out and gates even viewing the model list [obs]. Fix: let people see the ceiling (it is the pitch) and share what they already have.
- Claude's mobile research silently skips connectors [doc]. Fix: a one-line notice in the answer naming what was skipped.
- ChatGPT logged out swallows Cmd+K and Cmd+/ with no response [obs]. Fix: disable or hide shortcuts until they have something to act on, or show the sheet.
- ChatGPT's "About this ad" says targeting uses "general location, context, and device type" while the ad matched the chat topic [obs]. Fix: name the chat topic as the signal when it is the signal.
- ChatGPT ships all four data toggles on by default logged out, including two marketing toggles [obs]. Fix: default marketing off, and explain each toggle's trade in one sentence (ChatGPT does the sentence well).
- Claude offers no logged-out trial at all [obs]. Fix if the business allows: one free answer before the wall; otherwise invest in share pages and a login page that carries the pitch.

## Steal list

1. Do morph one fixed slot through Voice → Send → Stop, because the hand never moves during the send-and-interrupt loop.
2. Do pin the new question to the top and let the answer grow below without auto-scrolling, because people read from the start.
3. Do fade streamed words in (700ms, ~4ms stagger) instead of showing a caret, because it hides bursty delivery.
4. Do set the assistant's prose in a role-named reading font (`--font-voice`) and everything else in the UI sans, because the typeface tells the reader who is speaking.
5. Do collapse agent tool bursts into one counted line that expands to a step timeline and then to raw commands, because process must be auditable but quieter than the answer.
6. Do stream in labelled phases with an elapsed counter ("Working 3s" → "Finished 5s"), because a verb plus a rising number makes waiting legible.
7. Do end each claim with a mono 10px host chip whose icon encodes source class, opening a ~280ms-delay hover card with the reason, because "who says so" is the real question.
8. Do present one source set as chip, count, side pane and SERP tab, because readers verify at different depths.
9. Do attach composer menus as a chin with a live preview pane, and map `/`, `@` and typing to three menus, because the input becomes the feature directory.
10. Do rotate and scope the placeholder ("Type / for search modes", "Ask anything about NVIDIA Corporation"), because the placeholder teaches at the point of use.
11. Do mark agent, research and incognito modes on the composer frame (border, glow, label), because the mode must be visible where the user types.
12. Do put model and effort next to Send as one phrase, with the cost warning in its menu, because quality and quota are chosen at commit time.
13. Do put model choice inside regenerate ("Rewrite ›") and offer Fork, because retrying with a better model is one intent and forks keep the original.
14. Do show per-answer actions only after the answer finishes, on the latest turn, always visible on touch, because half-written answers and repeated toolbars invite mistakes.
15. Do keep the accent off primary buttons when the accent marks links and trust, because coloured citations need the colour to themselves.
16. Do escalate gates with value (bar → popover → wall), keep locked value visible behind a blur, carry intent through login (`next=`, `returnTo=`), and never re-wall delivered answers, because value first makes the ask fair.
17. Do end public share pages with one centered CTA and open them with a provenance notice plus Report, served from the real renderer, because the shared link is the best demo the product has.
18. Do run user-generated artifacts on a separate origin in an iframe, because shared code must never touch the logged-in app.
