# Copy, mobile and the floor

## Copy voice

- **Say the category plainly, in one sentence.** "The AI notepad for back-to-back meetings" (Granola). "Cursor is your coding agent for building ambitious software." "Radically different banking" (Mercury). "Your shortcut to everything." (Raycast). Nouns over adjectives.
- **Pre-answer the objection in the subhead.** "Notes, actions and memory. Without a meeting bot." "Apply online in 10 minutes." "97% of users pay us $0 · No credit card required."
- **Specific numbers beat claims.** "Global GDP running on Stripe: 1.75163473%", "15 years and 101 days", "over 20,000 companies", "$399" as the biggest text on the page.
- **Honest and human for hard news.** Arc's sunset page: "A farewell to Arc… Scroll to read what's happening and see what's next."
- **Humour that is also true.** PostHog's "Legally-required cookie banner", which says the site uses no third-party cookies.
- **Utility text in brand voice** (Nothing's mono region modal).
- **Definitions and participation.** Are.na: "Are.na is a. … b. … c. [+]", inviting the visitor to finish the sentence.
- **Instructions as copy only where the interaction is unusual** ("Scroll to explore", "PULL ME"). Product sites never say "scroll".
- **One CTA verb, repeated** ("Download for free ↓"), with a single secondary ("Talk to sales").
- **Delete every subtitle that only rephrases its title.** The deletion test: would the visitor have wondered? Is the value meaningless without it?
- **Cheek belongs on the site, not in the product.** T3 Code's app is literal; its site says "Steal our code (legally)" and "Tolerated by over N devs".
- **Never fabricate proof.** Real numbers, real quotes with real names, or no section.

## Responsive and mobile (390x844)

- **Cut copy; don't shrink it.** Stripe drops the second half of its headline on mobile. Mark optional fragments `<span class="desktop-only">`.
- **Buttons go full-width** (side by side when two are short, stacked when long), at least 44px tall.
- **The hero media still crosses the fold**, cropped to its most important part (the agent panel, not the sidebar). Prepare a separate mobile crop with `<picture>` rather than scaling the desktop composition down.
- **Nav:** logo, one menu button, at most one CTA. Floating capsules become edge-to-edge bars.
- **Horizontal compositions turn vertical:** split statements stack heading then paragraph; logo walls show 3 logos or become a slow marquee; side-by-side comparisons become swipeable.
- **Touch:** no hover-only information; guard hover styles with `@media (hover: hover)`; inputs at least 16px; safe-area insets on full-bleed sections; sticky bars use `env(safe-area-inset-bottom)`.
- **Desktop to phone handoff:** a small "Get the app" card with a QR code (Cosmos).

## The floor (non-negotiable)

- **LCP is the hero.** The hero image or headline paints first. Preload the display font (`<link rel=preload as=font crossorigin>`), use `font-display: swap` with a metric-matched fallback (`size-adjust`, or a framework font loader that does it), and give the hero image `fetchpriority="high"` with no lazy loading.
- **One canvas, paused off-screen.** Every WebGL site that felt good had a single canvas or a video standing in for it. Pause with IntersectionObserver and `visibilitychange`. Provide a static poster for reduced motion and low-power devices (`navigator.hardwareConcurrency <= 4` or Save-Data). Effects such as halftone or duotone can run at 8-12 fps.
- **Autoplay video:** `muted playsinline loop`, a poster frame, paused off-screen. Anything looping for more than 5s needs a pause control (WCAG 2.2.2).
- **Never hide content behind JS.** Reveals start from a visible state when JS or `animation-timeline` is missing.
- **Reduced motion means a calmer site, not a broken one.** Swap scroll-scrubbed motion for a static layout; keep opacity fades of 150ms or less.
- **Contrast:** grey secondary text is the house style of every product site, and it must still reach 4.5:1.
- **Hit targets** of at least 44px on touch (Apple's pill is exactly 44px tall).
- **Skip link** as the first focusable element (Linear, Vercel).
- **Semantics:** one real `<h1>`, landmarks (`header`, `nav`, `main`, `footer`), and `alt` text on product shots that says what the product is doing ("Issue DRV-8852 with an agent chat panel open"), not "screenshot".
- **Focus:** a visible `:focus-visible` ring (an outline of 2px in the accent with a 2px offset is the site default).
- **Metadata:** a real title and description per page, an OG image, an SVG favicon that follows `prefers-color-scheme`.
- **Explanation pop-ups get their own URL** (`?modal=…`) so support and marketing can link to them; exported charts carry a watermark and timestamp.

## Verification for a website build

1. Screenshot at 1440x900 and 390x844.
2. Jump-scroll to 25, 50 and 75% of the document and screenshot each; any empty region is a hidden-until-revealed bug.
3. Run [../scripts/measure.js](../scripts/measure.js) on the build and compare display tracking, line height, transition durations and easings with the brief's tokens.
4. Keyboard-only pass: skip link, focus order, visible rings, menus and dialogs close with Escape and return focus.
5. Reduced-motion pass (emulate `prefers-reduced-motion: reduce`).
6. Lighthouse or a performance trace for LCP and layout shift.
7. Squint test and brand-swap test from the brief.
