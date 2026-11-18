# Creative tools (image and video generation)

AI creative tools turn a prompt, a sketch or a reference image into images or video, then help the user refine them. Users pick these tools by output quality first and loop speed second, so the one question they judge on is: does it show me great results fast, and let me nudge them toward what I want without starting over? Everything else (cost display, settings, navigation) is judged by whether it gets out of the way of that loop.

Studied:
- Midjourney (midjourney.com, web app, V8.2): public Explore feed, lightbox, mobile layout, sign-in wall and company page observed live logged out [obs]. The logged-in Create page, settings panel, Editor, Organize and live generation come from vendor docs and vendor screenshots [doc] or prior knowledge [know].
- Krea (krea.ai, multi-model suite): app shell, Image composer and all its menus, model picker, Realtime (fully working logged out), Video settings, Enhancer, Edit, Train, Nodes and Agent landings, sign-up wall, pricing and mobile observed live [obs]. Actual image/video generation, Assets and the logged-in credit meter were not reachable [know].

## What users expect

1. Taste visible before commitment. Creative buyers judge on output quality, so the best outputs must be on screen before any ask (Midjourney's gallery, Krea's template wall).
2. A fast loop. Results that appear instantly or visibly form, and a composer that keeps the prompt for the next run, because creative work is many small reruns.
3. Refinement over restarting. "A bit different" is far more common than "start over", so variation, seed, reference and edit-in-place tools matter more than the first generate.
4. Readable control. Chips and sliders with plain-language consequences; power syntax optional, because most users think in look and feel, not parameters.
5. Honest economics. Cost known before spending, and a free trial that does not lose typed work at sign-up, because generations cost real money.
6. Ownership. Privacy (Stealth), commercial licenses, and credit for creators and models, because outputs end up in portfolios and client work.
7. Chrome that disappears. Neutral grays, one accent, images carrying all color (see L1), because the UI must never tint the work being judged.
8. Many candidates per run. Side-by-side comparison is how people judge taste, so one run should return several outputs (four, or a stepper).

## The theses to choose from

### Midjourney: taste-first gallery

Core bet: the images are the interface, and iteration (not generation) is the core verb.

Signature moves:
- Logged-out home is the Explore feed: four-column masonry, 2px gaps, 12px outer corners and 2px inner corners so the grid reads as one sheet [obs].
- Tile hover shows only the creator handle (14px/600 white, drop-shadow) on a 320px eased gradient that starts at 62% height, faded in over 150ms opacity only [obs].
- Every output carries intensity-paired verbs: Vary Subtle/Strong, Upscale Subtle/Creative, Remix Subtle/Strong, Pan four ways, Zoom 1.5x/2x, Rerun, Use Style/Prompt [doc].
- Parameters are dual-coded: sliders for feel (Stylization, Weirdness, Variety) and inline text flags (`--ar 9:16`, `--chaos 20`) that render back as chips with plain tooltips [doc + obs].
- Cmd/Ctrl+Enter submits and keeps the prompt in the bar [doc].
- Cost is hidden behind speed modes (Relax, Fast, Draft at half the fast hours); subscription only, no per-action numbers [doc].

Choose this when your edge is output taste from one house model, your users iterate many times on one idea, and you can charge a flat subscription.

### Krea: breadth-first suite

Core bet: one shell holds many tools, each with the input shape its job needs, and model choice is the product, so it is made legible.

Signature moves:
- One shell (black sidebar, dark theme, glass chips, white primary button), but each tool picks its own layout: bottom glass composer (Image), right settings column (Video), single centered upload card (Enhancer, Edit), split canvas/output (Realtime), centered chat (Agent) [obs].
- The model picker is a shopping shelf: sections by intent (Fast, Intelligent, Quality, Legacy), three sample images per model, an honest "best for" line, and speed (bolts out of 3), quality (diamonds out of 3) and unit cost meters on every card [obs].
- Realtime renders a drawing live with no account, new frames every 120-200ms at "Fast 7 FPS", with no progress UI at all [obs].
- Everything works up to Generate; the sign-up wall appears only at the moment of spending compute, after the session URL is created and with the prompt preserved [obs].
- Cost shown at choice time in plan units (2 to ~150), with "~" for variable cost, and pricing translates units into outputs ("64 Nano Banana Pro images") [obs].

Choose this when you aggregate many models or tools with very different prices, your users do production work (ads, product shots, swaps), and you need breadth to stay navigable.

### Choosing between them

- If your edge is taste, lead with the gallery. If it is breadth and workflow, lead with the input and use examples as runnable templates.
- If outputs are the product, put verbs on the output. If tools are the product, make "send to tool" the verb and keep each tool's input ready to receive.
- Chips with plain-language menus are the approachable default; add text flags only if your audience already speaks a syntax.
- One house model on a flat subscription can hide unit costs; an aggregator with per-model price spreads of 75x must show cost at choice.

## Comparison

| Dimension | Midjourney | Krea |
|---|---|---|
| Logged-out landing | Explore gallery, no hero copy [obs] | App Home: launch carousel, teaser composer, template wall [obs] |
| Where the wall sits | Before any generation; composer visible but disabled [obs] | At Generate, after session is created and prompt kept [obs] |
| No-signup magic moment | Browsing the gallery | Realtime live render |
| Composer | 54px full-width bar, top (desktop), radius 12 [obs] | 896px floating glass bar, bottom, radius 32 [obs] |
| Parameters | Settings popover (4 cards) plus inline `--flags` [doc] | Chips with menus inside the composer [obs] |
| Iteration | Intensity-paired verbs on every output [doc] | Seed chip, count stepper, model compare, send to another tool [obs] |
| Progress | Blurry-to-sharp in final slot, percent to 100% [doc/know] | Continuous output (Realtime); shimmer/breathing ring for jobs [obs keyframes] |
| Cost display | Speed modes only (Relax/Fast/Draft) [doc] | Unit price per model card; units to outputs on pricing [obs] |
| Model choice | House versions (Standard/HD, Raw, `--preview`) [doc] | ~40 third-party models, normalized cards, compare mode [obs] |
| Power path | Inline text flags [obs + know] | Node Editor graph [doc] |
| Chrome palette | Cool grays, one warm accent #f2330d [obs] | Zero-chroma grays, white primary, one blue for upload/selection [obs] |
| Theme | Light and dark token ladders, follows system [obs] | Dark by default; light tokens for marketing [obs] |

## Category rules

### Layout and navigation

1. Make the gallery the logged-out landing with no hero copy when your edge is taste, because the outputs are the strongest pitch and they cost no explanation. (Midjourney [obs])
2. Use 2px gutters between images and round only the grid's outer corners (12px outer, 2px inner, set per tile), because the grid then reads as one surface and no pixels go to separation. (Midjourney [obs])
3. Virtualize image feeds, position tiles absolutely, and cap columns with a max-column breakpoint (1608px), because creative feeds are endless and ultra-wide screens should gain margin, not a seventh tiny column. (Midjourney [obs])
4. Open details as an overlay route with its own URL over the still-mounted feed, blur the feed behind (12px) instead of dimming it, and page with arrow keys, because users deep-link, keep scroll position, and flick through dozens of images. (Midjourney [obs])
5. Give the media detail view three zones (image, info panel, filmstrip) and mark the current filmstrip item by size (56px to 68px), not color, because people judge, read and browse at once and color competes with thumbnails. (Midjourney [obs])
6. In a suite, keep the shell materials identical (nav, theme, chip style, primary button) and let each tool choose its own input layout, because consistency belongs in materials, not in forcing every job into one form. (Krea [obs])
7. Split suite nav into workspace destinations (Home, Agent, Assets) and a pinnable Tools list with a hover "..." to unpin, backed by a search palette that matches tools and models, because catalogs grow faster than sidebars. (Krea [obs])
8. Auto-collapse the nav to a 52px rail in canvas tools and restore it on exit, because drawing space is the product there. (Krea [obs])
9. Give upload-first tools one centered card (~380px, radius ~32px) with a visual before/after hint and two buttons (Upload, Select asset), because the first step is "pick a file" and nothing else. (Krea [obs])

### Composer and parameters

10. Pin the generate input on every creative page, browse pages included, because inspiration converts to creation only if the input is already in view (extends L12). (Midjourney [obs])
11. Offer "submit and keep prompt" (Cmd/Ctrl+Enter) beside plain submit, because creative users rerun with small edits and this one shortcut carries the iteration loop. (Midjourney [doc])
12. Show parameters as chips that state their current value; when a power syntax exists, make each chip equal its text flag (accessible name `--chaos 20`, visual "chaos 20") with a plain-language tooltip, because chips teach the syntax while staying readable. (Midjourney [obs], Krea [obs])
13. Match the control to the value's shape: segmented controls for 2-4 discrete choices, sliders for continuous taste values, a live shape preview for aspect ratio, ordered portraits then landscapes, because ratios and feel are spatial, not numeric. (Midjourney [doc], Krea [obs])
14. Write the placeholder to name every input mode ("Describe an idea or upload an image to edit it..."), because one sentence teaches the composer's range. (Krea [obs])
15. Let a dropped reference image choose its role at drop time (style, content, edit, animate starting frame) and offer a lock to keep references across prompts, because one image can mean four different things. (Midjourney [doc])
16. For multi-input jobs (video) stack labeled cards in a fixed right column (~330px) and allow `@` mentions of references in the prompt, because order and references matter more than prose once there are 6+ parameters. (Krea [obs])
17. Show fewer chips in teaser composers (Home: 4) than in the full tool (6), and on phones drop advanced chips rather than shrink them below 36px, because the first touch should be simple and targets beat options. (Krea [obs])

### Output and progress

18. Return several candidates per run (four, or a count stepper) laid out side by side, because comparing is how people judge taste. (Midjourney [doc], Krea [obs])
19. Under ~1s per frame, update output continuously with no indicator; for multi-second jobs, show the partial image forming blurry-to-sharp in the final tile slot; never use a bare spinner for creative output, because a forming image holds attention and avoids layout shift (category form of L5/L6). (Krea [obs], Midjourney [doc/know])
20. Label speed presets with real numbers ("Cinematic 24 FPS" to "Slowest 1 FPS", plus "Manual Click Vary"), because creators trade latency for quality on purpose. (Krea [obs])
21. Stack a small preview (640px webp) under the full image in the detail view and replace it in place, because a blank frame in a lightbox reads as broken. (Midjourney [obs])
22. Autoplay video tiles muted and looped in feeds, because motion is the content and a play button hides it. (Midjourney [obs])

### Iteration and recovery

23. Express every regenerate verb as an intensity pair (Subtle/Strong, Subtle/Creative, 1.5x/2x) on the output itself, because the choice is the action and "a bit different" is the common case. (Midjourney [doc])
24. Expose the seed as a visible chip in exploratory tools, because "keep this, vary that" needs a stable seed. (Krea [obs])
25. Keep drawn or placed canvas elements as selectable objects with a context menu, because creators revise composition constantly. (Krea [obs])
26. Remove actions that cannot run on an object (failed jobs lose Vary and Upscale) instead of disabling them on the media; but in settings menus keep unavailable options visible with the unlock condition as their description ("Add a reference image to use Ultra"), because a dead button on an image reads as a bug while a menu entry teaches the path. (Midjourney [doc], Krea [obs])
27. Send trash to a recoverable place (Organize), because generations cost money and taste is retrospective (see L10). (Midjourney [doc])

### Cost, gating and trust

28. Let users type, configure and start a session before the auth wall, then preserve all of it through sign-up, because typed work is the strongest reason to sign up (extends L13). (Krea [obs])
29. If generation is paid-only, keep browsing completely free, keep the composer visible but disabled with copy naming the gate ("Log in to start creating..."), and redirect gated routes with a callback URL plus a "Return home" escape, because the gallery is the free trial and walls you cannot back out of get resisted. (Midjourney [obs])
30. For an aggregator, normalize every vendor's model into one card format (samples, best-for line, speed, quality, unit cost) and allow "Select models to compare", because comparability is the reason to use an aggregator. (Krea [obs])
31. Show cost at the moment of choice in plan units, mark variable cost with "~", and translate units into concrete outputs on pricing, because nobody can value "5,000 units" and a precise-looking wrong number reads as bait-and-switch (extends L15). (Krea [obs])
32. Disclose every parameter and the model on shared outputs and credit the creator and model on sample outputs (including inside the auth wall), because transparency turns the gallery into a tutorial and the wall into a demo. (Midjourney [obs], Krea [obs])
33. Make privacy (Stealth, public/private) a toggle in generation settings, because people decide visibility before they create. (Midjourney [doc])
34. State upload limits before upload ("Max 75MB / 15 seconds", "Smallest dimension should be at least 96px"), because rejecting a file after a long upload wastes the user's time (see L16). (Krea [obs])

### Onboarding and copy

35. Open canvas tools with a pre-made example already rendered (Realtime's pre-drawn lamp), name templates "input to outcome" ("Sneaker sketch to prototype photo"), and label examples by input type (Camera, Draw, 3D), because users pick by what they have and a working loop removes all doubt (extends L20). (Krea [obs])
36. Make every public example reusable in one click ("+ use text", "Use Style"), because copying is how novices learn prompting. (Midjourney [obs])
37. Name verbs for the audience: craft verbs (Vary, Remix, Pan, Zoom) for artists, job verbs (Swap, Restyle, Recreate) for marketers, never ML verbs (regenerate, inference). Write model/tool one-liners as spec plus honest trade-off ("Cheapest upscaler. Max 8K.", "Realistic textures, weak diversity."), because pros compare on limits and candor builds trust in a list of unfamiliar names. (Midjourney [doc], Krea [obs])

## Measured constants

| Item | Value | App, tag |
|---|---|---|
| Image grid gap | 2px | Midjourney [obs] |
| Grid outer / inner corner radius | 12px / 2px | Midjourney [obs] |
| Desktop columns at 1440 | 4 x 296px | Midjourney [obs] |
| Mobile columns at 390 | 2 x 178px, 16px gutter | Midjourney [obs] |
| Max-column breakpoint | 1608px | Midjourney [obs] |
| Feed thumbnail | 384px webp via `image-set()` | Midjourney [obs] |
| Lightbox preview layer | 640px webp under full jpeg | Midjourney [obs] |
| Lightbox backdrop blur | 12px | Midjourney [obs] |
| Filmstrip thumb / current | 56px / 68px, current shifted left 12px | Midjourney [obs] |
| Hover overlay fade | opacity 150ms ease | Midjourney [obs] |
| Hover gradient | 320px tall, transparent until 62% | Midjourney [obs] |
| Handle chip | 14px/600, drop-shadow 0 3px 3px rgba(0,0,0,0.12) | Midjourney [obs] |
| Composer (top bar) | 54px tall, radius 12, 1px #e3e4e8, shadow 0 7px 21px rgba(51,51,51,0.05), 16px/24px text | Midjourney [obs] |
| Mobile bottom region | 114px; composer 366x54, 12px margins | Midjourney [obs] |
| Nav width | 214px | Midjourney [obs] |
| Accent | #f2330d; tint ramp #feebe7 to #300a03 | Midjourney [obs] |
| Light / dark page bg | #fcfcfd / #0d0e12 | Midjourney [obs] |
| Skeleton light / dark | #ebecef / #16181d | Midjourney [obs] |
| Lightbox open (editorial) | fade 0.22s ease; pop scale 0.92 to 1 over 0.26s cubic-bezier(.2,.7,.2,1) | Midjourney [obs] |
| Press ring | 2px ring on :active; pulse-in 0.3s scale 1 to 0.96 to 1 | Midjourney [obs] |
| Mobile menu sheet | 300ms cubic-bezier(0,0,.2,1), backdrop blur 12px | Midjourney [obs] |
| Ambient loaders | shimmer 6s linear; drifts 50s linear | Midjourney [obs] |
| Composer (glass) | 896x117 at 1440, bg oklab(0.27 0 0 / 0.8), blur 40px, 0.5px oklch(1 0 0 / 0.15) border, radius 32px | Krea [obs] |
| Composer chips | 36px tall, pill; generate button 40px round | Krea [obs] |
| Mobile composer | 358px wide, ~157px tall, 16px margins | Krea [obs] |
| Sidebar | 256px default, resizable 52-320px; rows 240x36, radius 10 | Krea [obs] |
| Sidebar / content bg | oklch(0 0 0) / rgb(16,16,16) | Krea [obs] |
| Gray steps | oklch 14.5%, 20.5%, 26.9% lightness, zero chroma | Krea [obs] |
| Radii | base 10px, popover 16, modal 24, composer and cards 32 | Krea [obs] |
| Model picker modal | 1280x810, radius 24 | Krea [obs] |
| Aspect popover | 236x257, radius 16, enter 0.15s | Krea [obs] |
| Realtime frame interval | 120-200ms at "Fast 7 FPS" | Krea [obs] |
| Realtime presets | 24, 13, 7, 2, 1 FPS, Manual | Krea [obs] |
| Model unit cost range | 2 (Krea 2 Turbo) to ~150 (ChatGPT 1.5) | Krea [obs] |
| Free tier | 100 units/day, no card | Krea [obs] |
| Chrome transition / press | 150ms cubic-bezier(.4,0,.2,1) / 80ms ease-in-out | Krea [obs] |
| Sheet curve | opacity 0.42s cubic-bezier(0.32,0.72,0,1) | Krea [obs] |
| Signature spring | `linear()` overshoot to 1.232, undershoot 0.946; transform .25s | Krea [obs] |
| Breathing ring | box-shadow 0 to 4px white/30 | Krea [obs] |
| Type | Suisse Intl, book weight 450, tracking-snug -0.015em | Krea [obs] |

## Anti-patterns seen

- Five simultaneous urgency surfaces during a sale (first-load modal, top countdown banner, flip-clock block on Home, gradient Pricing row, mobile banner) crowd out the work. Fix: cap promotion at two surfaces (one banner plus the pricing nav item). (Krea [obs])
- The mobile composer's second chip row was cut off at the bottom edge at 844px. Fix: pad bottom-docked composers by `env(safe-area-inset-bottom)` plus about 16px. (Krea [obs])
- Cmd+K did not open the tool palette, which was reachable only from a sidebar button. Fix: bind the palette to Cmd+K (see L18) and keep the footer key hints. (Krea [obs])
- A long sidebar grows with every new tool. Fix: pinning plus search, which Krea does; default to a short pinned set. (Krea [obs])
- Cryptic flags (`--sref`, profile codes) stay meaningless until you hover a tooltip. Fix: show the plain name on the chip and keep the flag as the accessible name and copy value. (Midjourney [obs])
- "Top month" is styled like a menu trigger but is a static label logged out, so clicking does nothing. Fix: render it as plain text until the menu exists, or open a menu with the gated options marked. (Midjourney [obs])
- The "Light mode" nav button did not change the theme while logged out. Fix: a theme control must work in every state or not be shown. (Midjourney [obs])
- No free generation at all; logged-out users can only browse. This is a deliberate bet that works only for a brand whose gallery is already the pitch. Fix for everyone else: a no-signup live tool or a small free daily allowance. (Midjourney [doc])

## Steal list

1. Do make the gallery the logged-out home with no hero copy when you sell taste, because the outputs are the strongest pitch.
2. Do use 2px gutters and round only the grid's outer corners (12px), because the grid reads as one surface and every pixel goes to the work.
3. Do show one thing on media hover (author or primary verbs) with an opacity-only fade of 150ms, because scaling or extra chrome in a dense grid hides the image and causes misclicks.
4. Do attach intensity pairs to every iteration verb (Subtle/Strong, 1.5x/2x), because it removes a settings step.
5. Do offer Cmd/Ctrl+Enter to submit and keep the prompt, because creative users rerun with small tweaks.
6. Do open details as a URL-addressable overlay over the still-mounted feed, arrow keys to page and Escape to close, because browsing must stay fast and shareable.
7. Do stream generations blurry-to-sharp in the final tile slot, or update continuously when frames take under ~1s, because a forming image holds attention and avoids layout shift.
8. Do let users type, configure and create a session before the auth wall, then preserve everything, because typed work is the strongest reason to sign up.
9. Do ship one no-signup live tool (Realtime), because a felt loop converts better than a demo video.
10. Do present models as cards with samples, a "best for" line and speed/quality/cost meters in one row, because people choose by trade-off, not by name.
11. Do show cost at choice time in plan units with "~" for variable cost, and translate units into outputs on pricing, because abstract credits are unreadable.
12. Do keep unavailable menu options visible with the unlock condition as their description, because it teaches the path.
13. Do show parameters as value-stating chips that round-trip to text flags with plain tooltips, because chips teach syntax while staying readable.
14. Do keep one shell across tools and let each tool choose its input layout (bottom composer, settings column, upload card, canvas), because jobs differ but materials should not.
15. Do auto-collapse nav to a 52px rail in canvas tools, because canvas space is the product there.
16. Do open canvas tools with a rendered example and name templates "input to outcome", because a working loop and a stated transformation remove blank-canvas paralysis.
17. Do build dark mode as its own token ladder on a cool near-black (#0d0e12) or zero-chroma grays with depth from blur, because photos look muddy on inverted surfaces and shadows vanish on dark.
18. Do label speed presets with real numbers (24/13/7/2/1 FPS), because creators trade latency for quality on purpose.
