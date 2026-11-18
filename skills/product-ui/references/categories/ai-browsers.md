# AI browsers and agents on pages

An AI that reads, and then acts on, content that belongs to someone else: a web page, a third-party app, a document the product did not author. The AI is a guest on the page. It can see what the page shows and click what the page offers, but it cannot redesign it, and the page's own controls must keep working underneath it. Users judge the category on one question: at every moment, do I know what the AI can see, what it is about to do, and how to stop it?

Studied (read-only, 2026-11-18, no app was run):
- Dia 1.57.1 (The Browser Company): official app bundle (native strings, bundled chat web app CSS and copy, asset catalogs, agent prompts, two in-app demo videos), the site and changelog. Deepest source: measured tokens are [obs].
- Comet (Perplexity): help center, official site, launch video. No bundle (the download is bot-gated), so no tokens or string table.
- ChatGPT Atlas (OpenAI): official app bundle strings and asset catalogs, launch video. Atlas is retired (no longer updated as of late 2026); treat it as a well-built reference, not a living product.

Tags: [obs] observed in a bundle, frame or screenshot; [doc] vendor docs or changelog; [inf] reasoning from evidence; [3p] third-party source, used only where nothing official exists.

## What users expect

1. **The page stays primary and interactive.** The AI docks beside it, never over it, because the answer is about the page and both must be visible at once.
2. **One box for URL, search and chat.** Users will not think about where to type, so the product must route, and make a wrong route cheap to reverse.
3. **The current page is already attached.** "Ask about what I'm looking at" is the default case and should need zero setup, but the attachment must be visible.
4. **A visible answer to "what can the AI see right now".** Per site, per profile, per message, because privacy is per site in people's heads ("not my bank").
5. **Unmistakable "the AI is driving" state.** When an agent clicks and types, the user must see it from anywhere on screen, because unseen automation on a logged-in page is the category's main fear.
6. **A stop control where the action is.** The eyes are on the page while the agent works, not on the panel.
7. **The agent stops before money, sends and sign-ins.** Real-world actions rarely have undo, so the human commits.
8. **Keep working while it works.** The input is never locked during a run.
9. **Proof of work, not the work.** A short receipt of steps, expandable, with sources one click away.

## The theses to choose from

### Dia: the AI is part of the browser's vocabulary
Core bet: every browser object (tab, tab group, profile, address bar) is also an AI context, and AI commands sit in the same menus and keys as browser verbs.
- Command bar routes between Chat and Google with an on-device model, previews the route in the caret colour (amber `#fcbf49` for chat, blue `#6395fc` for search, gray `#787d86` for URL), and offers a post-hoc "Not the answer you wanted? Click to toggle between Chat and Google" [obs][doc].
- @-mention menu anchored at the caret, max 5 tabs plus "View more" plus group scopes ("All open tabs (8)", "All open <domain> tabs"), inserting an inline token and a removable chip [obs].
- Context bundle saved above each sent user message, fanned like papers, with "SEE ALL" [obs].
- Fixed handoff vocabulary: exactly one of Sign In / Verify / Enter Information / Take Over, shown in nav bar, tab and notification [obs].
- Violet reserved for "agent acting": running tab card border `#5a4de638`, conic trace `#9288ff → #d3ceff`, cursor glow `#635bff` [obs].
- Long chats become sidebar items next to ordinary tabs, with a "•••" working indicator [obs].
Choose this when the AI must work across many of the user's objects at once and power users will drive it from the keyboard.

### Comet: the assistant is a sidecar that also drives
Core bet: a wide right sidecar plus a selection button cover most needs, and when the agent drives, the page itself shows it.
- Assistant sidecar at about 40% of window width (≈360/910 px), toggled by a labelled "Assistant" button that becomes "× Assistant" when open, ⌥A [obs].
- Teal glow around the controlled page while the agent works, plus a floating bottom-center pill "■ Stop Comet Assistant", later "❚❚ Pause Comet Assistant" [obs].
- Inline selection button whose verbs change with object state: reading (Summarize, Fact check, Define, Translate, Ask anything), editable (Rephrase, Translate, Edit anything), empty field (Help me draft) [doc].
- "/" shortcuts that expand into the full prompt on submit instead of running, storing prompt, mode, model and source [doc].
- First agent run asks "Allow this time only / Always allow / Don't allow" [doc].
Choose this when most requests are about one page at a time and the brand can carry a strong "agent working" colour.

### Atlas: ask first, then work with the user watching
Core bet: agent mode is a deliberate, risk-labelled choice, asked as a question, with the user able to take control at any point.
- Pre-flight consent in the assistant's voice: "Would you like me to use your browser to work on this?", with full-width "Continue" and equally full-width "No thanks" [obs].
- Black agent cursor with an "-ing" label pill ("Adding sunscreen to cart") on the page [obs].
- Floating page bar: [favicon] task title | "Take control" | "Stop" (red) [obs].
- Identity scope as a mode: logged-in vs logged-out; "Sensitive mode allows ChatGPT to work only while you are actively viewing this tab" [obs].
- Permission tiers "Allow read actions / Allow low-risk actions / Allow all actions" plus "Allow for this chat" [obs].
- Side chat at about 28% of window width (≈278/998 px), chrome `#fcfcfc` against content `#fff` [obs].
Choose this when actions carry real risk (purchases, logged-in accounts) and trust matters more than speed.

## Comparison

| Dimension | Dia | Comet | Atlas (retired) |
|---|---|---|---|
| Panel width | ≈50% (demo) | ≈40% | ≈28% |
| Entry radii | Command bar, ⌘E panel, tab hover card, chats as sidebar items, Morning Brief | Omnibox, new-tab prompt, ⌥A sidecar, selection button | New-tab composer, side chat, cursor chat in text fields |
| Routing | On-device model, caret colour preview, ⌃⌘↩ / ⇧⌘↩ overrides, post-hoc toggle | Perplexity default, ⇧↩ Google [3p] | Auto-routes ChatGPT vs Google |
| Context picking | Auto page chip, @ menu (5 + groups), inline tokens + chips, bundle saved per message | Auto tab chip, @tab | Site chip, "Sources ▾" in composer |
| Saved prompts | Skills hub, custom skills | "/" shortcuts that expand on submit | None found |
| "Agent acting" signal | Violet orbit trace on tab card, cursor pop, activity rail | Teal page glow, first-person step narration | Black labelled cursor, tab glyph, step header |
| Interrupt | Composer, handoff states, "Work interrupted" | Page pill Stop/Pause + square stop in composer | Page bar Take control / Stop |
| Permissions | Read vs full-access tool groups, Allowed / Always-allowed / Denied log, purchases need authorization | Once / always / never, per-site block | Read / low-risk / all tiers, pre-flight consent, logged-in vs out, sensitive mode |
| Safety transparency | "Hid part of the page" + "Wrong Call?" report | Docs only | Mode explainers |
| Memory | Being phased out | Account-level only, agent actions not stored | Separate browser memories (confusing, see anti-patterns) |
| Cost display | Trial receipt of value delivered, spend limit, credits | Not found | Credits, agentic usage limit, soft banner |

## Category rules

### Layout and docking
1. **Dock the AI on the trailing edge and keep the page interactive.** Left is primary content, right is commentary (like margin comments), and the user must read the answer next to its source. All three [obs]. Size the panel 28 to 50% of the window; below 28% answers wrap too often, above 50% the page stops being primary [inf].
2. **Put the panel toggle on the edge it opens from, as a text label, and make the same control show the close state.** A sparkle icon alone does not say what it does; Comet's "× Assistant" makes the button report its state. All three use text labels [obs].
3. **Keep panel headers to one create action, one layout/close cluster, and the current subject as title, with secondary views as tabs that carry counts** ("Answer | Sources · 1"). Narrow panels cannot hold more than 2 to 3 icons. Comet [obs].
4. **Promote a chat that produced a deliverable into the main navigation list.** It then inherits switch, pin, close, reopen and group behaviour users already know. Dia's chats sit in the tab sidebar with a "•••" working indicator [obs]. Extends L11.
5. **Put the AI verb on the object's own hover card or context surface too**, because every object is a possible context and a trip to the panel costs a step. Dia tab hover card: "chat with this tab", "create a context bundle from this tab" [obs].

### Routing and input
6. **When one input routes to several destinations, label submit with the destination ("Chat ↵"), not "Send".** "Send" hides which destination fires, and the key glyph teaches the shortcut every time it is seen. Dia [obs].
7. **Preview the route before submit in the caret, focus ring and selection colour, one hue per intent.** The eye is at the caret while typing, so the signal works at typing speed. Dia command bar: assistant caret `#fcbf49`, focus ring at 70%, hover 8%, selection 40% [obs].
8. **Give each destination its own key override and a one-click reversal after submit, and show the matched engine name before submit.** Auto-routing will guess wrong; the fix must cost one modifier (⌃⌘↩ Chat, ⇧⌘↩ Google) or one click ("Not the answer you wanted? Click to toggle between Chat and Google"), and a visible engine name makes the route predictable. Dia [obs][doc]; Atlas auto-routes the same way [obs].
9. **Put context and mode controls bottom-left of the composer and commit controls bottom-right, and show a dangerous mode (Agent) as a toggled chip inside the composer.** The user sees the mode while writing the request. Atlas "Agent" toggle turns blue when on [obs]. Extends L12.

### Context attachment
10. **Attach the current page by default, always as a visible, removable chip, never silently.** Zero setup for the common case, and the chip makes the implicit explicit. All three [obs]. State the default scope in docs and settings: Comet sends visible text, headlines and metadata, and not history, other tabs, cookies or passwords unless included [doc].
11. **Build reference pickers as: caret-anchored menu, about 5 items, "View more", then "all of X" group rows under a divider.** The cap keeps it scannable; group rows solve "attach my whole project" in one pick. Dia [obs].
12. **Insert a picked reference twice (a compact inline token in the sentence and a removable chip outside the text) and start reading it the moment it is picked.** The token keeps the prompt readable as prose, the chip row is the auditable manifest, and the early read hides fetch latency before submit. Dia [obs], 1.53.0 [doc].
13. **Save the context bundle with each user message, above the bubble, compact and expandable.** History becomes auditable: you can scroll back and see what each answer was based on. Composer-only chips vanish on send. Dia [obs].
14. **Scope AI context to a visible container (profile, workspace) and make cross-container sharing opt-in.** Dia tints the window chrome and the user's own bubble in the profile colour, so "which context am I in" is answered at a glance; data sharing between profiles is off by default [obs][doc].

### Selection and saved prompts
15. **Change selection verbs by object state (read-only, editable, empty), and give every inline result insert, copy, dismiss (Esc) and "continue in panel".** One menu for both would offer Rephrase on text you cannot edit. Comet [doc].
16. **Invoke saved prompts with "/", insert them as an editable token that takes trailing arguments, and run only on explicit submit.** Expansion lets the user add "tomorrow's meetings" and see what will run; store the full recipe (prompt, model, mode, sources). Comet [doc].

### Agent control
17. **Reserve one hue for "automation is in control", put it on the frame of the controlled surface and on the agent's cursor, and use it for nothing else.** Thinking, suggesting and acting carry different risk; acting must be visible from the corner of the eye. Dia violet, Comet teal, Atlas black cursor [obs]. Specific case of L1.
18. **Put the interrupt on the surface being acted on (floating bottom-center bar, dark, high contrast) and mirror it in the composer.** Bottom-center is least likely to cover the page's own controls. Comet pill + square stop in composer, Atlas page bar [obs].
19. **Prefer Pause or Take control over Stop when the task can resume, keep red only for the control that ends the run, and name the agent in the label** ("Pause Comet Assistant"). Comet moved from "Stop" to "Pause"; Atlas pairs "Take control" with a red "Stop"; the name says what is being stopped when other automation exists [obs].
20. **Give each agent state a distinct low-amplitude motion (looping trace while working, one-shot pop on arrival, stroke-draw on completion, gentle bounce on a source being read), never loop motion on finished items, and label the agent cursor with the current step in -ing form** ("Scrolling search results"). State reads from the corner of the eye and the page itself narrates. Dia motion [obs] (values in measured constants), Atlas cursor [obs].

### Handoff and approval
21. **Use a closed vocabulary of four "your turn" labels (Sign In, Verify, Enter Information, Take Over) with a free-text reason under it, and show it on the working object, its tab or row, and a notification.** The model could write any label; a fixed set is learned once and recognised anywhere. Dia agent prompt and strings [obs]. Feeds L17. Returning control means "resume", not "done": the agent picks up after the user signs in ("Finish signing in to continue this task.", "Handed off to you", "Waiting for you") [obs].
22. **Ask before handing control to the agent, as a yes/no question in the assistant's voice, with Continue and No thanks at equal width.** Declining must be as easy as accepting for a high-trust action. Atlas [obs].
23. **Split permissions into read, write and spend, scoped per app or site, asked as this time / always / never, and log each decision in the conversation.** Read is cheap to grant once; writes and spend stay asked. Comet [doc], Atlas tiers [obs], Dia read vs full-access tool groups and "Allowed action / Always-allowed action / Denied action" log [obs]. Specific case of L9.
24. **Make identity scope a visible, switchable mode (as you, or logged out), and for sensitive sites run only while the user is watching the tab.** Agent risk is mostly about whose identity it holds. Atlas [obs].
25. **Stage, then ask.** End every side-effecting run with the prepared state and one commit question ("Everything's ready. Would you like to check out?"). Purchases and subscriptions need explicit authorization; the agent stops before guessing task-specific form values. Atlas [obs], Dia prompt [obs]. If an action can be undone (tab closes, local edits), offer inline undo for at least 5 s instead; none of the three has a general "undo agent action", they rely on gating [obs][inf].

### Progress and receipts (extends L5)
26. **Write tool steps as verb pairs with counts** ("Gathering context around this page…" → "Gathered context", "Read 1 attachment", "Used 1 app"), on a timeline rail with dot markers, collapsing to one header when done and keeping the final answer outside the collapse. Dia rail, Atlas collapsed header [obs].
27. **Never lock the input during a run, and say so** ("You can keep typing in the meantime…"). Being locked out is the most common anxiety with a running agent. A stopped run names what stopped ("Stopped reading documents", "Context gathering stopped") in small muted text where output would have continued (Dia 12 px), so the user knows the partial state. Dia, Atlas [obs].

### Trust and safety
28. **Show AI visibility per site where the site is identified (address bar) and make it toggleable there, with sensitive defaults** (Dia avoids storing banking and health sites by default). Dia, Atlas "Decide which sites ChatGPT can see", Comet "Block Assistant on specific websites" [obs][doc].
29. **When a guard changes what the AI sees, say so in the activity ("Hid part of the page") and offer "Wrong Call?" that states where the report goes** ("this becomes an eval case for the check that made this call"). Hidden guardrails feel like bugs. Dia [obs].
30. **Keep one memory store per user, editable in one place.** Atlas had to explain that deleting chats does not delete browser memories; Comet uses the account memory only [doc][obs].

### Recovery, cost, copy
31. **Error recoveries follow the cause, with "Retry Without Attachment" when an attachment failed**, then Edit Message, New Chat, and support last, details collapsed behind "Show details". Dia [obs]. Specific case of L16.
32. **Show usage as value delivered, and at a limit disable only the costly control with a tooltip on it.** Dia's trial-end "RECEIPT" lists chat messages, tabs chatted with, sources read, artifacts generated, apps, tools, then "TOTAL $ 0.00"; attachments disable with an explanation while chat keeps working [obs]. Extends L15.
33. **Confirm browser actions in the field they came from (nav-bar status), not a toast, and when a page captures your shortcut, show "<shortcut> again to <action>".** Eyes are already in the address bar; the second press resolves conflicts without settings. Dia [obs].
34. **Before an OS password or permission prompt, say what the OS will ask, how many times and why** ("macOS will ask for your password once for each selected profile"), and relabel the button to "Waiting for password". Predicted prompts read as confirmation, not phishing. Dia import [obs].
35. **Label every sample prompt with what it will touch** ("No connected tools needed", "Searches connected apps", "Builds an artifact"). Sets expectations before anything reads the user's mail. Dia trial guide [obs].

## Measured constants

### Dia chat panel tokens [obs, shipped CSS]

| Token | Value |
|---|---|
| Insets | 8 / 16 / 20 px |
| Gaps | 10 / 12 / 14 px |
| Bubble padding | 24 × 16 px (compact 16 × 14) |
| Paragraph spacing | 22 px in answers, 14 px body; list item gap 6 px |
| Radii | tooltip 6, code 12, proposal 12, card 16, bubble 17, attachment 20, dialog 20, paper (artifacts) 3, pill 999 |
| Step rail | marker 16 px, dot 6 px, line 2 px, colour ink @9% |
| Type families | display Exposure (serif, 550), text ABC Oracle, code Inconsolata |
| Type sizes | h1 22 (weight 500), h2 17, h3 16, h4 15 (600), body 15, user bubble 14, code 14, tool title 13, label 13, thinking 12, timestamp 11, disclaimer 10 |
| Surfaces light / dark | page `#f3f3f3` / `#202020`, raised `#fff` / `#2c2c2c`, card `#0000000a` / `#ffffff0f`, token `#0000000d` / `#ffffff12` (hover 8% / 11%) |
| Text mixes | muted = CanvasText 60% over page; symbol button 30% → 85% on hover; token text 67-70% |
| Hues light / dark | blue `#3a88c4/#007fbd`, pink `#d37b8b/#bd556b`, green `#3eb489/#008b5d`, red `#c1575c/#cc4a55`, purple `#5f5b9e/#625da5`, orange `#d87249/#c95125`, yellow `#e3ac38/#c98400` |
| Command bar intents | assistant caret `#fcbf49` (ring 70%, hover 8%, selection 40%, text `#4f3400` / dark `#fff8eb`); search caret `#6395fc` (dark `#4a77d4`), text `#0f182c`; URL caret `#787d86`, focus `#b4b9c2@70%` |
| Agent acting | tab card border `#5a4de638`, conic trace `#9288ff → #d3ceff`, cursor glow `#635bff` |
| Tooltip | 28 px tall, radius 6, 12 px medium, padding 6 × 8, offset 4 px; bg `#f4f4f4` / `#262626`, 0.5 px hairline + 1 px inner highlight + `0 4px 8px` @10%; hidden on `(hover:none)` |
| Error block | centered, margin 4 rem, title 1 rem / 600 |

### Dia motion [obs, shipped CSS] (refines L19)

| Use | Value |
|---|---|
| Springs | slow 1.11303 s, fast 0.695641 s (physics-derived, used for content that changes size) |
| Micro-interactions | mostly 140-220 ms (`.15s` ×25, `.18s` ×16, `.22s` ×14) |
| Ease-outs | `cubic-bezier(.33,1,.68,1)`, `(.2,1,.3,1)`, `(.2,.8,.2,1)` |
| Overshoot (success only) | `(.34,1.56,.64,1)`, `(.2,1.5,.4,1)` |
| Collapsible | height `.18s ease`; opacity, `blur(14px)`, `scale .5` on spring-slow; origin top-left; overflow clips step-end |
| Tooltip | in 50 ms, out 100 ms, 2 px slide |
| Shimmer (L6) | `1.5s steps(90,end)` infinite; tab titles `3.6s steps(135)`; reduced motion = static text at 70% |
| Citation placeholder | opacity pulse to .4 over 1.2 s |
| Agent trace | 2.03 s linear orbit, fade in by 16%, out after 77% |
| Agent cursor | `.75s cubic-bezier(.2,.8,.2,1)`, scale .39 → 1.13 → 1; glow pulse 1.15 s alternate |
| Done check | pop `.5s cubic-bezier(.2,1.5,.4,1)` scale .5 → 1, stroke draw `.42s` |
| Tool chips | pop `.15s` with per-chip stagger |
| Source being read | bounce 1.6 s, ±3 px, ±2° |
| Entrances | empty state `.4s` Y 6 → 0; popover `.2s` 6 px + scale .98; overlay `.15s`; dialog `.2s` from Y −1 rem; hint `.35s` |
| Sounds | separate `response_done` and `response_question` cues, optional, never take headphone focus |

### Other apps

| Constant | Value | Source |
|---|---|---|
| Comet sidecar width | ≈360 of 910 px (≈40%) | Comet [obs] |
| Atlas side chat width | ≈278 of 998 px (≈28%) | Atlas [obs] |
| Atlas chrome / content | `#fcfcfc` / `#fff` (dark `#303030` / `#212121`) | Atlas [obs] |
| Atlas border | `#000@10%` (dark `#fff@8%`), elevated 20% / 16% | Atlas [obs] |
| Atlas hover | 3% / 6% (darker 5% / 12%) | Atlas [obs] |
| Atlas accent | `#007afd` (dark `#84b6ff`); critical hover `#ff0000@10%` | Atlas [obs] |
| Comet temporary session | page context kept up to 30 days | Comet [doc] |

### Dia command inventory (compact)

Keys: ⌘E open Chat (Ask on Page) [doc] · ⌃⌘↩ route to Chat, ⇧⌘↩ route to Google [doc][obs] · ⇧⌘A search tabs across windows [doc] · ⌃1-9 jump to profile [doc] · ⌥⌘T new tab in group [doc] · ⌃⌘N group from selected tabs [doc] · ⌥⇧⌘C copy URL as Markdown [doc] · ⇧⌘D pin to Favorites [doc] · ⌃⇥ / ⌃⇧⇥ MRU switcher (5 tabs) [doc] · ⌘L command bar, ⇧⌘E new chat, ⌃⇧E focus chat, ⌘\ sidebar, ⇧⌘P profile switcher [3p]. All rebindable; shortcuts work on AZERTY and Dvorak [doc]. Comet: ⌥A toggle Assistant [obs], "/" saved shortcuts, Esc closes inline result [doc]. Atlas: ⇧⌘A side chat [3p].

Menus [obs, 146 localized items, each in Title Case and sentence case]: AI commands sit beside browser verbs. Chat menu: toggle Ask on Page, new chat in Ask on Page, focus the Ask on Page field, Send Chat Prompt Now, Open Daily Brief. Notable non-AI items: Copy URL as Markdown, Show Tabs in Sidebar, Reset Pinned Tab to Base URL, Clean Tabs, Merge All Windows, Switch to Profile 1-9, Copy Diagnostics, Record Performance Issue. Rule: every shortcut also lives in a menu with its key shown, one label source with a casing variant per surface (L18).

Shortcut recorder (Atlas) [obs]: names the conflict ("already used by the “%@” menu item") and the reason a combo is rejected ("Option modifier must be combined with Command or Control").

## Anti-patterns seen

- **Two memory stores (Atlas).** Browser memories separate from account memories forced a FAQ explaining that deleting chats does not delete browser memories. Fix: one store, one delete-all.
- **Cheerleading narration (Comet).** "Perfect! I can see…", "Excellent! Now I can see…" on every step. Fix: short, flat, first-person step lines.
- **Hard Stop as the only interrupt (early Comet).** Ending the task is the wrong default when the user only wants to look. Fix: Pause or Take control, with red Stop as the separate end action (Comet's later Pause pill, Atlas).
- **No general undo for agent actions (all three).** They compensate with gating. Fix: gate irreversible steps and offer inline undo for reversible ones (rule 25).
- **Marketing demos with camera zoom (Dia).** UI durations cannot be measured from them; ship and document motion tokens instead of relying on video.
- **Dia's caret colour varies by profile theme.** The demo shows blue where the token says amber, so an intent hue that a theme can override loses its meaning [inf]. Fix: keep intent hues out of theme control.

## Steal list

1. Dock the AI on the trailing edge at 28-50% of the window and keep the page interactive, because the answer is read next to its source.
2. Label a multi-destination submit with its destination and key ("Chat ↵"), because "Send" hides which one fires.
3. Tint the caret, focus ring and selection by routed intent, because that is where the eye is while typing.
4. After auto-routing, offer a one-click "Not the answer you wanted?" switch, because routers guess wrong.
5. Attach the current page as a visible, removable chip by default, because the common case needs zero setup and no silent context.
6. Build @-pickers as caret-anchored, 5 items, "View more", then "all of X" groups, and insert both a token and a chip, because it stays scannable and auditable.
7. Save the context bundle above each user message, because history must show what each answer was based on.
8. Reserve one hue for "agent in control" on the page frame and agent cursor, because acting must be visible from anywhere.
9. Put Pause / Take control on the controlled page, bottom-center, mirrored in the composer, with red only for ending, because attention is on the page.
10. Use exactly four handoff labels (Sign In, Verify, Enter Information, Take Over) with a free-text reason, shown on the object, its row and a notification, because the user learns it once.
11. Ask "Would you like me to use your browser to work on this?" with equal-width Continue / No thanks, because declining must be as easy as accepting.
12. Split permissions into read, write and spend, asked as once / always / never per site, and log each decision inline, because cheap grants should stay granted and expensive ones visible.
13. Stage the result and ask one commit question before any purchase or send, because real-world undo rarely exists.
14. Write steps as verb pairs with counts and never lock the input ("You can keep typing in the meantime…"), because a live log should become a receipt without blocking the user.
15. Show "Hid part of the page" with a "Wrong Call?" report that says it becomes an eval case, because visible guards feel like care and hidden ones feel like bugs.
16. Make selection verbs depend on read-only vs editable vs empty, with insert, copy, Esc and "continue in panel" on every result, because the right verb depends on whose text it is.
17. Expand "/" saved prompts into editable text that runs only on submit, because macros should take arguments and never fire blind.
18. Show usage as value delivered and disable only the costly control at a limit, because graceful degradation keeps trust.
19. Warn about OS password prompts before they appear, with their count, because predicted prompts read as confirmation, not phishing.
20. Tag sample prompts with what they touch ("Searches connected apps"), because users should know before the agent reads their mail.
