# Website case studies

Per-site notes with measured values, captured in a headless browser at 1440x900 and 390x844 in November 2026. Part 1 covers 41 sites across product companies, consumer and hardware brands, studios, personal sites and award winners. Part 2 covers the marketing sites of ten AI products and a set of design resources. Use these as references when the brief names a site, or to calibrate a choice ("how tight does Vercel track 64px Geist?").

Tags: [obs] observed live, [doc] vendor or resource docs, [inf] inference. Blocks are [obs] unless tagged.

## Part 1: sites measured live

### Linear (https://linear.app)
- Dark #08090a page, Inter Variable at odd weight 510, H1 64/64 ls -1.408px (-0.022em), Berkeley Mono as 2nd family (102 nodes) for IDs/meta.
- Hero: left-aligned 2-line H1, subhead + "New Loops →" changelog link split to opposite ends of same baseline row (no pill badge). Below: a full-width *live-looking product UI* (sidebar, issue, agent chat panel) as the hero image, rendered in HTML not a PNG.
- Section pattern: big left title ("Intake and integrations") vs right paragraph + "Learn more →", then product UI composited (Slack thread overlaps kanban, kanban fades out to the right edge via mask).
- Nav: fixed 73px, transparent bg + backdrop blur(20px), hairline bottom border; one filled pill CTA (Sign up, #e5e5e6 on black, 32px tall, 13px/510); everything else is text.
- Motion: 233 nodes at 0.1s cubic-bezier(.25,.46,.45,.94), hovers 0.16s; 0.7s cubic-bezier(.32,.72,0,1) for bigger reveals. Has prefers-reduced-motion and view-transition CSS. No GSAP/canvas; Next.js.
- Type scale used: 12/13/14/15 dense UI text, then jump to 24/32/48/64/72: almost no 18-22 middle sizes. Huge contrast between product-UI text and display text.

### Vercel (https://vercel.com)
- Light #fafafa, Geist Sans; H1 64/64 weight 400 (not bold!), letter-spacing -3.84px = -0.06em (extremely tight, only works with Geist's wide-ish shapes at display size). Geist Mono for code/meta.
- Hero = 3-column asymmetric split: left H1 + 2 buttons, center the triangle logomark as a 3D object with soft shadow (WebGL canvas), right a 3-line stacked list ("For coding agents / To ship apps and agents / Automated by agents"): the headline is completed by the list instead of a subtitle paragraph.
- Logo wall sits at the fold line (bottom edge of first screen) so it doubles as the "scroll cue".
- Nav sticky 64px, no blur; three buttons right (Get a Demo outline, Log In outline, Sign Up solid black) all 32px tall, radius 6. Logo right-click → context menu "Copy Wordmark / Copy Logo / Download Brand Assets / Brand Guidelines" (hidden press-kit affordance exactly where designers try to grab the logo).
- Sections: big 2-line heading top-left, product screenshot rendered as greyscale wireframe-ish UI, the right column a claim with the key number in darker ink ("over 20,000 companies") and a quiet "Features" list. Mixed ink: secondary text grey, key fragment primary.
- Motion: 0.1-0.15s cubic-bezier(.4,0,.2,1) everywhere (Tailwind default ease), reduced-motion + view-transition CSS present.

### Stripe (https://stripe.com)
- Söhne var, H1 48px weight 300(!) ls -0.02em; light weight at display size is the Stripe voice (calm, expensive). Accent #533afd.
- Signature ribbon: a huge flowing multicolor WebGL gradient band slashes diagonally behind/through the headline; headline words it crosses take on color (blend). It is the ONE loud thing; everything else is white + hairlines.
- Visible vertical page-column hairlines run the whole page (construction-grid motif), logos sit in cells between them.
- Headline is two-tone: first sentence primary ink, the continuation in muted slate: one block reads as title + subtitle without a size change. "Accept payments, handle business banking,¹": a footnote superscript in the hero (legal honesty as craft).
- Live data as hero proof: "Global GDP running on Stripe: 1.75163473%" ticks in real time (mono-ish tabular digits).
- Stats band switches to deep indigo with a WebGL starburst of light rays; tiny dark-mode moon toggle placed inside the band, i.e. the illustration itself has a theme control.
- Mobile: second sentence of headline DROPPED, buttons go full-width side by side, logo wall becomes 3 across. Menu = square button with hamburger, not a pill.
- Motion: 0.3s cubic-bezier(.25,...) dominant, 0.8s cubic-bezier(.165,.84,.44,1) for reveals. No prefers-reduced-motion CSS found in readable sheets.

### Apple MacBook Pro (https://www.apple.com/macbook-pro/), the two-model chooser page
- Black page, SF Pro Text 17px body (Apple uses 17 not 16), headings SF Pro Display 600. Global nav 44px, 12px links, absolute (scrolls away): the product page's own sticky local nav takes over.
- Side-by-side comparison as two mirrored centered columns: hero image, color dots, orange "New" eyebrow (the only colored text), name, one-line claim, price with monthly split + footnote superscripts, pill blue "Learn more" (radius 980px, 44px tall) and a text "Buy >" link under it. Primary = filled pill, secondary = chevron text link: consistent across the entire Apple site.
- Spec comparison: each row = icon (line, 1.5px, white) + 1-2 lines, the key number in bold inline ("Up to **1000 nits**"), missing feature shown as an em dash, not "No". Big weight numbers "3.0 lb." with "From" eyebrow above.
- Motion: 0.32s cubic-bezier(.4,0,.6,1) dominant, 0.24s ease. Reduced-motion handled.

### Arc (https://arc.net): now "A farewell to Arc" sunset page
- Display serif "Exposure VAR" 76px/600 ls -0.032em, body ABC Oracle, mono ABC Favorit Mono. Serif display + grotesk body = editorial, humane voice for a hard message.
- Hero: centered sticker-style logo (white outline like a die-cut sticker), headline, 2-line sub that literally says "Scroll to read what's happening and see what's next." then a dark-grey pill "Read more". Centered hero is OK here because it is a letter, not a product pitch.
- Page starts black and turns white as you scroll (the dark hero is a cover, the body is a document). Timeline with dots + vertical rule for shutdown dates; dates in primary ink, explanation in grey.
- Sticky bottom bar appears after the hero: one sentence + one black "Download Dia" button (60px tall, radius 12). Persistent single CTA at the thumb zone instead of repeating CTAs per section.
- Product screenshots of Dia float right with annotations as pill callouts connected by a hairline ("Profiles").

### Dia (https://www.diabrowser.com)
- Warm paper #fbfaf6 page; display serif Exposure VAR (500, ls -0.04em) + ABC Oracle body + ABC Oracle Triple + ABC Favorit Mono (for times "10:00a"). Same type family as Arc's sunset page = brand continuity across products.
- Hero: blurred sunlit-foliage photograph in saturated yellow (light-through-leaves = "a better workday", warmth) with a GIANT swash serif wordmark "DIA" in white behind the product window; product window overlaps the wordmark's lower half (layering: photo → wordmark → product UI → CTA). Tagline small serif above, centered.
- Nav = floating centered pill (logo + 3 links) not a full-width bar; a separate "Download Dia" pill appears top-right after scrolling. Primary CTA "Download Dia for free ↓" black pill pinned at bottom center over a large convex white arc (the page's bottom edge curves like a horizon). Sub-caption "Available for macOS and Windows" under it pre-answers the obvious question.
- Feature cards: small uppercase-pill eyebrow (PROFILES, LIVE WORK), 20px sentence, product UI stacked windows with real content (Ischia, PR names) bleeding out of card bottom with fade. Inline sticker (yellow starburst seal) with cursor on the product = playful annotation.
- 4 autoplay videos, 1 canvas; 0.2s material ease. Reduced-motion yes.

### Rauno Freiberg (https://rauno.me): portfolio as a horizontal film strip
- Page bg #ededed, cards pure white; one grotesk family "X" at 32/500; vertical wheel/scroll drives a HORIZONTAL track of full-height white panels, each a project (huge geometric shape: yellow circle, orange circle, giant cropped "Craft" word). 
- Top-center minimap: a ruler of hairline ticks where the current panel is a hollow rectangle: position indicator that doubles as a scrubber; minimal label "Devouring Details" floats above the next panel's corner.
- Cursor replaced by a thin crosshair "+" (designer's tool metaphor). Bio set as staggered indented lines (every other line indented): rhythm from indentation, not size.
- Color: pure primaries (yellow #ff0, orange) as flat solid shapes, no gradients; text black. Shapes overlap text (circle behind "working with Vercel").
- Motion 0.15s ease-in-out. Lesson: a portfolio can be a single interaction idea executed perfectly.

### Paco Coursey (https://paco.me): the "document" portfolio
- White page, Söhne 16px everywhere, line-height 28px (1.75), ~560px measure, NO display size at all: name is 16px/500. Hierarchy entirely from position, weight 500 vs 400, and grey vs black ink. Total page height 1424px: the whole site fits ~1.5 screens.
- One italic serif phrase "*Crafting interfaces.*" opens the bio: the single typographic flourish.
- Three-column index (Building / Projects / Writing): grey 13px label, then link (underlined, ↗ for external) + one-line description in grey. Then "Now" section as prose.
- Links: underline with offset, external arrow glyph; 0.24s ease hover. Has view-transition CSS (page-to-page fade) and reduced motion.
- Lesson: confidence through restraint. Works when the person's work is the proof and the audience is peers.

### Saved design posts on X (visual reads)
- #3 @amananimates reel (scrolltide.co): wine site "NINE NIGHTS OF PICKING": condensed heavy display caps over full-bleed dusk vineyard photo, small serif-ish body, "The Allocation List" section; book-object site "The Long Light" (single 3D object floating on paper texture); fashion hero with oversized type behind subject; DNA helix dark 3D hero; "Take the helm, *your way*": sans + italic serif mixed inside one headline.
- #5 @uisabor: Qredible: saturated cobalt sky + product UI window half-SUNK into a photoreal grass hill (occlusion by a foreground layer = depth + "grounded"); same trick as Dia's convex white horizon. Cards reuse the hill as band texture; serif-ish light display "Automation for every department" left, explanation right (Linear split).
- Pattern named: HORIZON OCCLUSION: let a foreground layer (hill, arc, fade) cover the bottom of the product shot so it reads as placed in a world, and the fold becomes a horizon.

### Emil Kowalski (https://emilkowal.ski)
- #fdfdfc, one sans 16/24, NO display type, whole page 1854px. Name + role as two lines (black, then grey) top-left of a ~600px column. Sections "Today", "Projects", "Writing" each = 16px black label + list of (black title / grey one-liner) pairs, generous vertical gaps (~80px between sections, ~16 between items).
- Only interruption: a dismissible top announcement bar ("Enrollment ... is open! 2 days left"): underlined link sentence + ×. Zero transitions on the homepage itself (topTrans empty): the motion expert ships a static homepage. Reduced-motion rules present for the rest of the site.
- Lesson identical to Paco: peers' portfolios = an index, not a show.

### Family (https://family.co): the "playful consumer" template done right
- Custom display face "Family" (rounded geometric grotesk) 68px/500 ls -0.02em for headlines only; Inter for everything else (170 nodes). The custom face IS the brand; body stays neutral.
- Centered hero (allowed: short headline, mascot art left+right framing it symmetrically). Illustrations: flat, bright primaries, characters with faces and little legs (blob, square, triangle mascots), coins/hearts/rockets scattered: art direction of a children's book applied to crypto to defuse fear.
- Two CTAs: black pill "Download on iOS" with Apple glyph + light grey pill "▶ Watch the Video": secondary as quiet fill, not outline.
- Feature rows: phone mockup in a pale warm card left, right = tiny colored eyebrow ("Seamless" in amber), 32px headline ending in a period, grey paragraph, then a 2-column icon list in the accent color, then a "Manage your collectibles / Watch the demo" thumbnail link. Rows separated by hairlines that stop at the container edge.
- Motion: 0.2s ease-out (120 nodes), and 1s cubic-bezier(.19,1,.22,1) (expo-out) for big entrances (56 nodes). 9 videos. No reduced-motion CSS found.

### Essays and guidelines read
- Linear "How we redesigned the Linear UI (part II)": explored with opacities of black/white only, then theme generated in LCH from 3 inputs (base, accent, contrast) instead of 98 vars; contrast knob yields high-contrast a11y themes for free; aligned sidebar labels/icons to the pixel ("something you feel after a few minutes"); stress-tested direction on every main view before building; whole redesign in ~6 weeks, "always better to do a redesign quickly".
- Rauno "Invisible details of interaction design": interaction design = "experiences that fluidly respond to human intent"; reuse metaphors (swipe = stacked layers); interruptibility like a book page; lightweight actions trigger mid-gesture, destructive ones only on release; apply deltas immediately then animate past threshold; spatial consistency (things return where they came from); frequency & novelty: high-frequency keyboard actions get NO animation (cmd menus, context menus; macOS context menu only fades OUT); "fidgetability"; scroll landmarks.
- Rauno Web Interface Guidelines (interfaces.rauno.me): ≤200ms interaction animations; scale from ~0.8 not 0; press ~0.96; theme switch triggers no transitions; pause off-screen loops; scroll-behavior smooth with offset for anchors; @media(hover:hover); inputs ≥16px; tabular-nums; font weight never changes on hover; weights <400 never; clamp(48px,5vw,72px) headings; box-shadow focus rings; dropdowns open on mousedown; svg favicon that follows prefers-color-scheme; feedback relative to trigger (inline ✓ on copy, not a toast); ::selection styled; no dead zones between list items; decorative glows pointer-events:none.
- scrolltide.co: paid library of 152 scroll-driven templates/107 components/55 shaders as AI prompts (React/Next/GSAP/Three/Lenis). Use as gallery only (free previews); paid tier not used.
- footer.design: footer-only gallery (Typographic, Large Type, Animated, Illustrative, Bold...). "Large wordmark bleeding off the bottom" is a recurring editor's-choice footer.

### Raycast (https://www.raycast.com)
- Near-black #07080a; Inter 64/600, centered; hero art = diagonal red light-streaks (WebGL/canvas, grainy, like long-exposure) behind headline; the streaks echo the logo's diagonal stripes = brand mark becomes the hero texture.
- Nav: floating rounded bar inset from viewport edges (margin ~ 74px sides at 1440, radius ~12, translucent dark with hairline), 9 text links + white "Download" button with Apple glyph. A second "Download for Mac" pill sits at the hero's bottom center.
- Section eyebrow: tiny red mono uppercase "AI AGENT" over centered 32px headline (mono eyebrow = keyboard/dev product voice).
- Carousel of extension cards with prev/next round icon buttons at right and "Browse thousands more →" left: controls aligned to the container edges, not centered.
- CAUTION seen in capture: jumping to 25% scroll left a ~400px empty black void where reveal-on-scroll content had not yet animated in. Hidden-until-revealed content is fragile (fast scroll, find-in-page, screenshots, no-JS). Make reveals start visible or reveal from opacity .0→1 only inside @supports scroll-timeline.
- Motion: 0.4s cubic-bezier(.23,1,.32,1) (185 nodes) + 0.3s ease.

### Cursor (https://cursor.com)
- Warm paper #f7f7f4, custom CursorGothic (400) + berkeleyMono; H1 only 26px/400: deliberately small, plain sentence "Cursor is your coding agent for building ambitious software." Product is the hero, not the headline.
- Hero image: real product windows (Cursor Desktop + CLI) composited over a full-width classical LANDSCAPE OIL PAINTING crop. The painting = taste, craft, timelessness; the UI = precision. Distinctive and cheap (public-domain art).
- Buttons: fully round pills 43px, primary near-black #26251e with "↓", secondary pale #e6e5e0 "Request a demo →". Nav: Sign in text, Contact sales outlined pill, Download black pill (3 levels of emphasis).
- Testimonials: 3-col cards, pale warm fill, quote first, avatar + name + title at bottom; section title centered 32px "The new way to build software."
- Orange text link "Download Grok Bot →" (accent used only for links). Cookie notice is a small bottom-right card with two pill buttons: not a full-width bar.
- 0.15s material ease; reduced-motion + view-transition CSS.

### PostHog (https://posthog.com): the "desktop OS" concept site
- Whole site is a fake desktop OS: illustrated green hillside wallpaper with hedgehog, desktop icons down both edges (Home, MCP, Pricing, Docs, Demo, Talk to a human / About us, Changelog, Handbook, Store, Careers, Trash), pages open as draggable WINDOWS with close/maximize. docH=845: the document never scrolls; windows scroll inside.
- Custom rounded face "RoundHog" 36px/800 (heavy, friendly); highlighted words get a marker-highlighter background ("context layer" in blue box, "analytics, errors, replays" in yellow): emphasis by highlight, not color text.
- Pricing box inside hero = trust checklist with ✓ ("97% of users pay us $0", "No credit card required") + two chunky 3D-bevel buttons (orange "Get started", white "Install with AI").
- Humor as brand: cookie banner titled "Legally-required cookie banner", says "PostHog.com doesn't use third-party cookies" with a cut-out of Ursula von der Leyen giving thumbs up. The legal chore becomes a joke that is also true.
- Lesson: a concept (OS metaphor) can carry an entire site's navigation; works because PostHog's product is many apps. Cost: heavy, unusual; only when the metaphor IS the product.

### Teenage Engineering (https://teenage.engineering)
- Pure black, product studio-lit (single top spotlight, heavy falloff) as a full-screen photograph: the object is the hero, no headline.
- Nav: wordmark top-left in two lines, then 4 nav items, each a thin-line PICTOGRAM + lowercase label + 3 tiny sub-links (products: instruments/audio/designs), then a block of tiny Japanese text, then the "TO" logomark: nav as a typographic specimen. Everything lowercase, custom faces TechnoType + te-20.
- Price as the H1 ("$399"): the biggest text on the page is the price, stated plainly.
- Mid-page: blurred, vignetted transitions between product scenes (soft focus pulls): cinematic camera language.

### Mercury (https://mercury.com)
- Custom arcadia / arcadiaDisplay at 49px/480 (odd variable weight between regular and medium). Centered hero over a full-bleed surreal PHOTOGRAPH: an office chair + desk with laptop on a grassy summit above misty valleys at dawn (calm, solitude, ambition: banking as serenity, not as finance-blue). Top of the photo fades into a soft warm sky that carries the white text.
- Hero form inline: email input + "Open account" (accent periwinkle #5266eb, pill) + "Contact sales" (translucent pill) as ONE glassy capsule row: the CTA is a form, so starting = typing.
- Legal disclaimer ("Mercury is a fintech company, not an FDIC-insured bank...") placed as a dark translucent caption bar at the bottom of the hero: regulatory text designed as part of the composition, not hidden in the footer. Footnote ¹ in subhead.
- Nav: "Launch demo" outlined pill + "Open account" filled pill: two-tier. 0.3s expo-ish ease.

### Nothing (https://nothing.tech)
- Typography IS the brand: Ndot (dot-matrix display face echoing the phones' glyph LEDs), NType82 serif-ish for H1 48/400, Geist Mono + LatteraMono for UI labels in uppercase mono ("BLACK FRIDAY", "SHOP NOW >"). Accent: signal yellow #ffc700 buttons with square corners (radius 4).
- Product photography: transparent earbuds/cases floating at angles, cropped by viewport edges, on light grey: the transparency is the product's design language, so photography shows internals.
- Region modal: mono microcopy "LOOKS LIKE YOU'RE IN: / United States / BUT YOU'RE BROWSING THE STORE FOR: / United Kingdom" + yellow "GO TO: UNITED STATES" + underlined text alternative. Even a utility modal speaks in brand voice/type.
- Uses Lenis smooth scroll (lenis class present). No reduced-motion CSS found.

### Granola (https://www.granola.ai)
- White page; display "quadrant" (a slab/typewriter-ish serif) 86px/400 ls -0.02em, line-height 0.93: huge, tight, left-aligned, 4 lines; body "melange". Accent: olive/moss green #5b6f00 (unusual, earthy, owned) on the primary "Download for free ↓" pill (56px tall: bigger than nav buttons).
- Hero right: collage of textured paper/print swatches (lime, halftone, risograph-like texture) behind the product window + a floating video-call PiP + a "||| Transcribing" status pill. Analog print textures = notepad metaphor.
- Small "New | Voice typing by Granola →" chip above H1 (they DO use the announcement chip, but in neutral grey with lime "New" tag, not a glowing gradient). Under CTA: icon + "Available for macOS, Windows, iOS, Android".
- Nav: on scroll it morphs from full-width bar into a floating rounded pill with shadow (inset from edges), and the Download button turns from grey to the green accent: the nav earns emphasis once the hero CTA is gone.
- Scrollytelling: sticky left rail "Before the meeting / In the meeting / After the meeting" with an underline progress bar on the active item; right side scrolls chapters each with serif title + paragraph + product shot over a painted landscape. A narrative mapped to the user's timeline.

### Basement.studio (https://basement.studio)
- Black, Geist 87px/600, line-height 0.9, ls -0.04em; "flauta" for accents; mono for small labels. Nav: tiny 36px fixed bar, counts as superscripts ("Showcase ⁽²⁹⁾", "Blog ⁽²⁹⁾"), a live dot "● Online ⁽⁹⁾" (people on the site right now), dotted divider.
- Hero: full-screen real-time WebGL point-cloud/voxel scene (dark cave with pixelated light), toggle "HUMAN | MACHINE" mono switch at bottom center changes the render: the hero is an instrument.
- Client logo wall as a strict grid of hairline-bordered cells (6 cols), white logos. Section header "Featured Projects" 60-80px grey-to-white.
- 3 canvases; 0.06s linear (cursor follower) + 0.3s material.

### Lusion (https://lusion.co): 3D studio
- Pale lavender-white #eef page, Aeonik only. Statement (36px/400, 3 lines) placed in the CENTER column of the nav row, not below it: logo | statement | controls: the header IS the hero copy, freeing the whole viewport for the 3D.
- Hero = rounded-corner (≈16px) inset WebGL canvas of physics-simulated chunky 3D jacks in cobalt/black/white: tactile toy objects that react to cursor. Below: "+" crop marks at the four quadrant edges and "SCROLL TO EXPLORE" mono caps: print/registration-mark vocabulary.
- Controls: round icon button ", ", dark pill "LET'S TALK •", light pill "MENU ••" (dot glyphs as tiny decorative state). Full-screen menu overlay.
- docH=845: custom scroller (virtual scroll), WebGL everything. No reduced-motion CSS.

### Locomotive (https://locomotive.ca)
- Black; huge distorted/sliced display type animating (glitch-sliced "MTL" + time "15:56" + temperature-ish numbers + arrows): the hero is kinetic typography showing their LOCAL TIME/city (Montréal), not a product. Below: "OPS|DES|DEV" boxed tag diagram + "Locomotive® / Digital-first Design Agency✳" in condensed serif (LocomotiveNew) 70px with ® and superscript "LOCO" logo.
- Nav: one line, comma-separated links "Work, Agency, Careers, Store": nav written as a sentence. Lenis smooth scroll (they authored Locomotive Scroll), view-transition CSS, reduced-motion yes.

### Active Theory (https://activetheory.net)
- Pure WebGL experience: chrome iridescent "a" logo on a looping ribbon with bokeh particles, ambient audio toggle, nav is a tiny glowing capsule "WORK , ,  CONTACT" top-right. Body text set in fallback Times (no HTML content; everything in canvas). The extreme end: an experience not a document; inaccessible, slow; only valid for studios selling exactly this.

### Framer (https://www.framer.com)
- Black; GT Walsheim 54/500 ls -0.04em left-aligned, 2 lines; subhead grey; buttons: white "Get started for free" + dark grey "Install the MCP" (both small, 32px). Announcement on the right of the button row "New: Image and Shader Generation →" (same placement as Linear).
- Hero media: Framer's own editor showing a CMS table on left, and a website preview card with an electric-blue glowing border (the only glow) on right; portraits in the preview are motion-blurred photos: real-looking content, not placeholders.
- Logo right-click/hover menu: "Copy logo SVG / Brand guidelines" (same affordance as Vercel). Cookie card bottom-LEFT with Reject (grey) / Accept (black) equal size (honest consent).

### Rive (https://rive.app)
- Black; display Orbitron 48/900 uppercase (sci-fi game UI face) + PragmataPro mono (170 nodes) + Inter. Hero = a LIVE Rive demo (car console: 3D SUV in mountain scene + dashboard widgets) rendered in-page; 31 canvases on page: every demo is the product running, not a video.
- Right column "01 / 09 NOW PLAYING / DASHBOARD" + spec table (RUNS ON / USE CASE) + mono outlined buttons "TRY IT LIVE" "GET SOURCE": a media-player metaphor for a showcase carousel with progress bar.
- Agent-era CTA: "Start with your coding agent. No account needed to try it." + a copyable prompt box (gradient hairline border) with "COPY" button: "Install the Rive CLI from rive.app/cli. Let's build a car center console...": the CTA is a prompt to paste into an agent. (Framer: "Install the MCP"; PostHog: "Install with AI".) NEW 2026 pattern: agent-install CTA as secondary action.

### Cosmos (https://www.cosmos.so)
- Off-white (lab 100), custom cosmosOracle 72/700 ls -0.04em, centered. Hero: tilted image tiles (lamps) floating in 3D depth around the headline (depth of field: far tiles small + blurred), and the headline's second line CYCLES through queries with a blur crossfade ("lamp with character" ← "go-to outfit"), showing what you can search.
- The hero CTA is a SEARCH BOX ("Search for lamps") + round color-palette button (search by color): the site lets you use the product immediately. Black pill "Join Cosmos for free" below. Bottom-right floating card "Get the app" with QR code (desktop→phone handoff). Chevron-down round button as scroll cue.

### Are.na (https://www.are.na)
- White, one font "areal" at 19.2px; the homepage is a numbered definition list: "Are.na is / a. Online software for saving and organizing... / b. A toolkit for assembling new worlds from the scraps of the old / c. [+]": the "+" invites you to add your own definition (participation as hero). "For the last **15 years and 101 days**": live-computed age, bold.
- Buttons: tiny, radius 3, navy #00075f "Sign up" + grey "Download the app". Product screenshot "How it works" with a right-side rail of steps (Capture / ...) using a vertical line + dot timeline. Anti-marketing tone = credibility with its audience.

### Lynn Fisher (https://lynnandtonic.com): annual redesign ("v. XIX")
- Paper texture bg #e4e2d7, Victorian/storybook display face Hubano-Rough 96px + Sydonia Atramentiqua body; nav as a BOOK TABLE OF CONTENTS with dot leaders and roman numerals (ABOUT ...... I, WORK ...... II). Version number "v. XIX" + sun icon theme toggle centered at bottom.
- One concept executed fully; she redesigns yearly so each version can commit to an extreme idea. docH=845 (fits in one screen).

### Josh W. Comeau (https://www.joshwcomeau.com)
- Wotfard (rounded humanist sans); sky-blue header with illustrated clouds and a 3D clay avatar sitting on a dashed rainbow arc; pink uppercase tracked section labels ("ARTICLES AND TUTORIALS"); tag chips in pale blue. Header icons: search, SOUND toggle (site has sound effects on interactions), theme, RSS.
- Whimsy budget spent on the header + micro-interactions with sound; the article list itself is plain and readable. 0.125s ease hovers.

### Anthropic (https://www.anthropic.com)
- Warm ivory #faf9f5, anthropicSerif + anthropicSans (custom pair). H1 41px: FIRST sentence in bold SANS ("AI research and products that put safety at the frontier."), continuation in SERIF regular: a sans/serif switch inside one paragraph replaces title+subtitle (cf. Stripe's two-ink headline).
- Nav: split around a CENTERED wordmark; every item is a small pale pill (28px, #f5f4ed fill) with chevron; search + menu as round icon buttons. Hero media: full-width rounded video of an aurora over Earth (nature, scale, awe; no AI imagery).
- 0.15-0.2s ease-out. Reduced-motion + view transitions.

### OpenAI (https://openai.com)
- White, OpenAI Sans 17px body, H1 48/500 ls -0.03em. The hero IS the product input: centered "What can I help with?" + a ChatGPT-style composer with a typed example ("Plan a surf trip to Costa Rica in August") + suggestion chips (Learn about ChatGPT Business / Talk with ChatGPT / Research / API Platform / More): the chips double as site navigation.
- Below: rounded media cards (a comet-like particle arc on dark, "Cyber at the Frontier" card) as a news grid. Nav: "Talk to us" pale pill + "Try ChatGPT ↗" black pill (36px, radius 40).

### Galleries
- godly.website: masonry of looping site/motion previews, left sidebar categories (Design ● new, Launch Videos, Websites, OG Images, App Screenshots, App Icons; Resources: Tools, Skills, Jobs), filter chips (Web, Interface, Branding, Motion, Illustration, Posters, Print). Current visual climate on Godly: 3D chrome/iridescent objects, editorial book typography, iridescent coins, deep-black hero objects, posters with neon green.
- awwwards SOTD (Nov 2026 feed): Lynksen/PSP production (red-jumpsuit crowd photo, Money-Heist-like, big caps overlay), bikebear "STICK BY YOU" sweet-tape (neon lime, tape strips, sticker collage), Bulletproof ("TO BE LEFT ONE", teal laptop + hands), SANTAL (giant spaced wordmark), Preymaker, Delta Cafés, Auge, Cyera, Zirka, Extrafazant, Justin Jefferson, VIV, Agrumea Farm. Filters available by Font and Color = Awwwards treats type and palette as primary search axes.
- siteinspire: featured "maximale": huge chrome/serif wordmark overlapping a moody interior photo, with justified paragraph links inline ("Studio, Projects, News, Contact" inside the sentence); "Sydopia": centered small serif statement + eye icon + strip of project thumbnails. Categories offered: Typographic, Minimal, Grid Layout, Unusual Layout, Art Direction.
- land-book: galleries split into Websites, SECTIONS, Mobile, Motion, OG Images, HEADLINES: useful to study one section type at a time (e.g. all pricing sections). Filters by page type (Landing, Pricing, About, Case Study, Sign Up, Blog Post).

### Awwwards Sites of the Day (November 2026)
- agrumea farm (Sicilian marmalade): peach #fdf3eb page, centered crest logo, IT/EN round toggle top-left, outlined "MENU" pill + orange dot button top-right; jars of product float/tilt in a 3D carousel over a big maroon rounded-polygon with orange text set ON A CIRCLE ("...SERVE · WISDOM...") rotating; "SCROLL TO DISCOVER" tiny caps. Fonts ivymode (display serif) + ivystyle-sans. Lenis + WebGL. Packaging illustrations ARE the art direction (site extends the label).
- bulletproof (agency): grey studio backdrop, a 3D-rendered ampersand made of candy/food particles, giant "CREATE DESIRE / THAT DISRUPTS" in Sequel Sans at 109px, ls -0.09em, line-height 0.8, words staggered across the grid (left/right offsets) and partly occluded by the 3D object (text BEHIND object = depth). Nav = 3 outlined pill links (WORK/ABOUT/NEWS). Mixta Pro Light Italic serif for accents. 0.8s expo-out (281 nodes).
- santal (architecture): headless capture after 2.5s was a BLANK grey screen (preloader / intro still running); 234px Helvetica "WE" ls -0.1em later. Lesson: intro loaders cost first impression and break link previews/screenshots; keep any intro <1s and skippable.
- sweet tape (bubble-gum tape brand): acid lime crumpled-paper texture, Futura condensed 800 at 293px, words slightly rotated (sticker feel), "WE'RE [logo] HERE TO" small around the logo, curved dark green horizon below (again a convex horizon!), tab "PULL ME" hanging from top-right like a tape dispenser tab (physical metaphor as interaction), sound toggle bottom-right. 
- delta cafés: dark coffee-brown #2b1b14, full-bleed documentary photo of coffee pickers, thin line-drawn circular "process" diagram overlaid (Roast / Tasting) along a dashed path = the journey of coffee as a scroll path; big serif "THE JOURNEY OF COFFEE" partly behind nav; nav split around centered logo; 0.45-0.675s back/expo eases. Cookiebot banner covers 40% of the screen (consent UX failure on an award site).
- psp production (film production): black, full-screen looping commercial footage, bracketed mono-ish nav "[ WORK ] [ DIRECTORS ] ...", centered list of "[01] PORSCHE MACAN" in uppercase with a yellow duotone video-preview block appearing on hover over the list, side panel "[Made by] Aspekt [Director] RGB6" + project title + still + BACK/NEXT. Hover-to-preview list = the index IS the hero. GSAP + ScrollTrigger present. Neue Haas Grotesk Display 96/700 lh 0.85.
- viv (artist management): white, Helvetica Now Display 24px for everything incl. H1, Garamond Narrow accent, single screen (docH 845): minimal index of roster.

### Apple AirPods Pro 3 (https://www.apple.com/airpods-pro/), the flagship scroll page
- docH 28,743px (≈32 screens), 16 videos. Local sticky nav (44px): product name left, "Overview" (active w/ underline) / Hearing Health / Tech Specs / Compare + blue "Buy" pill right: the global Apple nav scrolls away, local nav stays.
- Chapter pattern: object (single earbud, white on light grey) centered/right with a short paragraph left where the FIRST PHRASE IS BOLD BLACK and the rest grey ("**A new multiport acoustic architecture** with more precise airflow control: ..."): same two-ink trick as Stripe/Anthropic, at paragraph level. Video sequences scrubbed by scroll (pinned).
- H1 small (28px): product name is the nav; the big type appears in chapter headlines.

## Part 2: AI product sites and design resources

What the marketing sites of ten AI products do, measured, plus website lessons from a set of design resources (font specimens, hero studies, scroll and shader galleries, a footer gallery). Each site block lists its moves with values; the cross-site rules at the end are the transferable part.

Tags: [obs] observed live, [doc] vendor or resource docs, [inf] inference. Site blocks are [obs] unless tagged.

### ChatGPT (chatgpt.com/overview)

- Hero: one centered H1, "Now you can chat, work & code all in one place.", OpenAI Sans 100.08px/100.08px, weight 700, letter-spacing -4.70px (about -0.047em), three lines. Page is 6,818px tall at 1440 wide.
- A macOS-framed product window starts at the fold, so the cut-off window pulls the eye down.
- The headline verbs "chat", "work", "code" are `aria-pressed` buttons that auto-rotate; the active word is painted letter by letter in four brand colors with a matching gradient underline, and the window below swaps mode. The headline is the tab bar.
- Type: one family in two moods. Hero 700 with heavy negative tracking; H2 48px/55.68px, 500, -1.44px; card titles 22px/500; body on the system stack.
- Color: page `rgb(252,252,252)`, text `rgb(13,13,13)`, feature cards `rgb(243,243,243)` at 6px radius (sharper than the app's 16-28px). Color appears only in product UI and the rotating word.
- Decoration is sticker-like: a black asterisk glyph, a tilted "GPT-6.2 Flagship Model" tag, a line globe, a tilted code card behind the window. No gradient blobs.
- Product UI is real and believable: Codex mid-task ("Worked for 2m 30s", red/green diff, "Unstaged +23 -24", "Commit"); the chat app with a dinner-planning thread.
- Scroll moment: a sticky frame (`position: sticky; top: 132px; height: 768px`) beside a Chat / Work / Codex accordion that advances on scroll.
- Carousel: seven 370×578 cards, each with a short paragraph and a real UI fragment cropped off the bottom right edge.
- CTAs: nav reuses the app's "Log in" (black) and "Sign up for free" (outline) pills; hero has one black pill "Try it now*" (109×40, 14px/500, full radius) and "Download the app ↗" as a plain link.

### Claude (claude.com)

- The homepage hero is the sign-in form: serif H1 "Question what's next" (56px/64.4px, 400), serif subtitle, a rounded card with "Continue with Google" / "OR" / black "Continue with email" and a legal line. The right half is a tall video of a person reading at a paper-strewn desk.
- Product page hero: "Give Claude more" (serif 72px/79.2px, 500) centered, sans subtitle 20px/32px `rgb(94,93,89)`, floating in a field of task tiles captioned "Campaign readout", "QBR deck", "Call prep", "Contract redline", fading out toward the bottom.
- Type: serif headlines at 400-500 with normal tracking (no tight negative tracking); H2 52px/62.4px; plan names serif 32px/500; prices sans 24px/600; body sans at 1.6 line height. The headline serif is the same voice the assistant writes answers in.
- Color: page `rgb(250,249,245)`, text `rgb(20,20,19)`, bands `rgb(240,238,230)`; demo panels in sage, lavender and peach with faint white root-like line drawings; plan cards white, 1px `rgb(240,238,230)` border, 24px radius.
- Tier icons are botanical line drawings that gain branches per tier (Free a sprout, top tier a full flower).
- Demos are stylized, simplified UI on colored panels with "Modify prompt ↗" and "Replay ↻": a composer, a clarifying question from the assistant, a tool card, source chips. Simplified UI never goes stale.
- Scroll moment: a day timeline with hour ticks (8AM, 12PM, 4PM) and a moving dot; each stop is a task at that time, with a "For everyone ⌄" role switcher.
- Role tabs (Everyone, Marketing, Sales, Finance, HR, Legal, Product) each carry a one-line promise; the selected tab is a white card on the darker band.
- CTAs: fixed nav with "Contact sales" (outline) and "Try Claude" (black, 108×36, radius 8, 15px/500); every plan card repeats "Try Claude" full width with "No commitment · Cancel anytime" under it.
- Motion: the nav slides down once on load (1000ms); demos animate inside their panels; no parallax or scroll-jacking.

### Perplexity (/hub, /comet, Discover, Finance)

- Hero: "AI *for* the curious" in GT Canon VF at 180px with "for" in italic, semi-translucent over a dark painted meadow. Headline animates in over 2.2s, subhead over 0.9s.
- A real-looking composer sits under the headline with a vertical ticker of example prompts, so the product's verb (asking) is in the first viewport.
- Type: three voices with jobs. Display serif (GT Canon), reading serif for section heads, sans for body; Comet uses GT Canon Black at 56px/-1.6px with GT Standard for UI and GT Standard Mono uppercase in the footer.
- Warm paper, not white: Hub `rgb(250 248 245)`, Comet `rgb(251 250 244)`. Dark sections end in a curved elliptical edge that reveals the paper beneath.
- Texture: grainy noise-shaded planet spheres and thin orbit lines; paper-grain fills on use-case cards.
- Scroll-scrubbed statement list: four huge serif statements stacked; only the one in focus is full ink, the rest ghosted near the background.
- Product cards show frosted, skeletonized UI ("41 sources" with colored dots) over photography, with two-tone copy (first clause white, rest dimmed) and a small pill CTA.
- The app's agent-state glow (teal inner glow, "Pause Comet Assistant" chip) is reused as a section motif.
- CTAs: two pills top-right ("See a demo" filled, "Try Perplexity" outlined); the nav flips dark to light as the page moves from dark hero to paper. Comet pins a teal "Download" pill top-right while the header collapses to floating circular buttons.
- Content and data pages: Discover alternates a hero story (serif 28/35), a 3-up card row and a mirrored story; articles use a 36.8/46 serif title and a 720px serif body. Finance uses hairline stat grids, sparkline cards and a dot-grid chart backdrop with semantic red/green and arrow glyphs.

### Cursor (cursor.com)

- Hero: a small statement and a big product. H1 is one 26px/400 sentence over two lines, left-aligned, with two pill CTAs; below, a 1300px stage (radius about 4px) holds a live HTML product window.
- Backdrops behind the app windows are soft classical landscape paintings and muted solid panels; no other dev tool uses fine-art texture.
- Product UI is real HTML animated by script, not video: crisp at every DPR, localizable, croppable, and each demo has an `aria-live` description for screen readers.
- Type: custom grotesk (CursorGothic) for marketing, system-ui inside product mocks so they feel native, Berkeley Mono for code, a serif only inside the demo's generated page.
- Palette: bg `#f7f7f4`, ink `#26251e`, cards one or two tones darker, orange `#f54e00` only on links.
- Feature copy is "Title. Gray continuation sentence." at 22px in one paragraph, then an orange "Learn more →". No bullet lists.
- Section shells: a rounded card split into a 1/3 text column and a 2/3 stage, alternating sides.
- Social proof is a grid of product-specific quotes from named builders, each with avatar and title.
- CTA: Download in the sticky header, the hero, and a giant closing "Try Cursor now." at 52-72px with one button; the loudest type is at the end.
- Changelog: a date rail, a 645px prose column, 36px title, 22px bold subheads with # anchors. Footer has a three-state theme switch and compliance badges inline with the copyright.

### v0 and vercel.com

- The product is the hero: v0's landing is the working composer ("What do you want to create?", a 690px box with chips).
- An announcement pill above the H1 ("Use your ChatGPT plan in v0 ›") with a partner logo carries one timely message without a banner.
- Geist with aggressive negative tracking at display sizes: -0.04em at 32px, -0.06em at 48-64px; weight 600 on v0, 400 on vercel.com.
- Monochrome canvas (`#fafafa` page, `#171717` ink); color comes only from product imagery (template thumbnails, integration icons, swatches).
- Bento grid: 3 columns, radius about 16px, white cards with a 1px alpha ring on `#fafafa`; each card has a title, a one-line benefit and a small live mini-illustration (a button with a crosshair cursor, a node diagram, a phone).
- A template gallery of real community output (avatars, view counts, likes) sits right under the hero as social proof.
- vercel.com hero: 64px left-aligned two-line H1, black and white pill CTAs, one centered black triangle with a soft radial glow, and a right column of three audience lines.
- Logo marquee at 24s linear, large and grayscale, below the fold.
- Closing band: "Start building with v0" at 48px, one sentence, one black "Get Started" pill, then a 4-column footer.
- Header buttons on v0 are 6px-radius, square-ish ("Log In" white with 1px ring, "Sign Up" black); pills on vercel.com. Smaller radii read more tool than marketing.

### Linear (linear.app)

- The hero is a 1320×720 live HTML/CSS replica of the app (sidebar, issue, activity feed, agent panel, a working workspace menu) using the same CSS variables as the product, with animated state ("Thinking…" shimmer, "Working…" pill, a ticking "00:07"). Feature pages fall back to raster images.
- No CTA in the hero: only the H1, a gray one-line subline and a quiet "New Loops →" link pinned right on the same baseline. "Sign up" in the header is the only filled button on screen.
- Composition: left-aligned 2-line H1 at 64px/1.0, weight 510, -0.022em, `#f7f8f8`; 15px/24px subline; about 70px of air; then the app frame at full content width with 60px gutters at 1440.
- Type: Inter Variable (`cv01`, `ss03`, optical sizing) at 510 for every headline from 38px (mobile) to 72px (prefooter); Berkeley Mono 12px for captions ("FIG 0.1", "NOV 12, 2026"); a display serif loaded for editorial moments.
- Two-tone paragraph headlines: white first sentence, the rest continuing in tertiary gray in the same 48px-ish block.
- Monochrome at `#08090a` / `#010102`; product state colors only inside renders; one late color break in the customer-quote cards (pale blue, neon yellow-green).
- Depth from lighting, not gradients: a radial top-down light on each stage, vignettes and fade masks (`--fade-left/right: 400px`, `--fade-bottom: 300px`); the /ai hero is a tilted, blurred render with depth of field.
- Hairlines and double bezels: 1px 5-8% white lines, 12-22px radii; showcase panels use an outer 22px radius with 8px padding around an inner 12px.
- Section scaffold repeated four times (about 1,230px each): H2 left, about 22px gray paragraph plus "Learn more →" right, full-width render, a row of expandable "+" feature items. Then a 4-up changelog timeline with mono dates, quotes, prefooter, footer.
- Timings: nav link color 100ms; "Learn more →" arrow fades in 200ms ease-out-quart after a 120ms delay, out 120ms; mega-menu scale .98→1 plus opacity at 180ms from center-top; tooltips 120ms scale .9→1; header 72px, `#0b0b0bcc` with 20px backdrop blur. No scroll-linked motion; ambient motion lives inside the renders (2.4s shimmer, 1.6-3.2s `steps()` loaders). Every page has a `.md` twin and `/llms.txt`.

### Notion (notion.com, notion.site)

- Hero: H1 NotionInter 64px/64px, 700, -2.125px (about -0.033em), `rgba(0,0,0,0.95)`; H2 42px/48px, -1.5px.
- CTAs: primary solid blue `#0075DE`, 8px radius, 48px tall (11px 20px padding); secondary "Request a demo" in pale-blue tint; nav CTA 36px tall.
- Brand texture: black-line hand-drawn faces with stipple shading and flat orange/blue/yellow circles; the same face family is the in-product AI avatar.
- The AI Meeting Notes hero is a working HTML replica of the block (tabs, waveform, Pause/Stop, transcript, summarizing checklist, citations) built with the app's tokens, cycling recording → summarizing → summary.
- Hand-lettered uppercase margin annotations with a thin rule pointing at the mock, entering at 250ms.
- Product panels sit on textured pastel grounds (peach paper grain), with a floating chat bubble overlapping the frame.
- A tabbed carousel of four large tab cards drives one big panel under the hero.
- Product-page headlines are self-aware ("We also have AI note-taking, yada yada yada."), conceding table stakes to spend attention on the differentiator.
- Pricing is embedded in the feature page, with hover tooltips on each line item.
- Cookie banner: "Accept all" and "Reject all" are identical outline buttons.

### Granola (granola.ai)

- Editorial serif at poster scale: hero H1 86.4px, line-height 0.93, -0.02em; H2 48px; a later "For the doers" line at about 200px spanning the page; body 16/24.
- The hero plays the product's real loop as HTML: Typing → Transcribing → Generate notes → Enhancing → My notes / Enhanced, with the app's own inks and write-head.
- Collage and grain behind the product: halftone posters, rock art, nature photos with film grain, framing a clean note window.
- Scroll-driven sticky demo: the hero window shrinks into a sticky card beside the claims; the before/during/after section uses a sticky step list with a progress tick.
- Hand-drawn icons for trust claims (a robot with ×, a padlock with a tick), each in a ruled row with dashed vertical guides.
- Nav becomes a floating bordered pill inset 8px on scroll, and "Download" flips from a 6% olive tint to solid olive.
- One CTA verb repeated in brand color: "Download for free ↓" (olive pill, 56px tall), "Download for Mac"; "Talk to sales" is the only secondary.
- Handwritten flourishes: one footer word as an SVG handwriting image; "Made with ♥ in Shoreditch".
- A dark `#292929` testimonial band with line-boxed quotes and black-and-white portraits.
- The chat page hero is a giant rounded input "/Coach me" with a lime send button over a field of tilted note, folder and person cards.

### Midjourney (/home, sign-in, /updates, Explore)

- One visual metaphor across every public surface: a CRT monitor with scanlines, a barrel-distorted bezel and an ASCII-art logotype, on both /home and the sign-in wall.
- Mono as the company voice (JetBrains Mono headings 30px/400 and body), humanist sans (DM Sans) in the app.
- Hero is art, logotype and three pills with no headline: "Sign up" (green icon), "Log in" (amber icon), "Explore" (pink icon).
- On scroll the CTAs split to the corners as separate dark pills: Documentation and Explore top-left, Sign up, Log in and a globe top-right.
- "Projects" tiles: eight 196px squares, 8px radius, 1px white/10 border, stippled blue single-hue figures labeled "TBA Software" / "TBA Hardware".
- Colored line icons mark sections in long text (purple info beside "About", green person beside "Careers") next to 30px mono headings.
- Deep navy-black ground with blue glows instead of flat `#000`.
- The product is shown by its outputs: logged-out Explore (masonry of top images) is the de facto landing page.
- Editorial tokens: display `clamp(2.6rem,8vw,5rem)` at 0.95 line height and -0.03em; body 1.76 line height; 0.22em eyebrow tracking; gold `#e8b455`; radial glow and vignette backgrounds.
- Changelog is a calm feed with "All / Announcements / Changelog" pills and date and time per post.

### Krea (krea.ai feature pages, pricing)

- The hero is the product working: a full-bleed fashion photo with live edit annotations (numbered colored pins, bounding boxes with handles, labels being typed "Make the coat cherr|"), above a real composer with "1:1 ⌄", shuffle, model picker and send.
- Two-tone headlines: white first line, gray second line ("Free AI Image Generator" / "Create AI Photos and Images from Text or References"), carrying the SEO phrase and the brand claim in one heading.
- One family, huge ratio: H2 72px/500 with -2.16px (-0.03em) in Suisse Intl; H3 16px/500/-0.48px.
- Dark hero, then white sections with black type for documentation-like content.
- Expanding-card carousel: the active model card is wide with a caption and a progress bar; inactive cards are narrow slices with only a logo chip.
- A floating bottom-center section-nav pill ("Styles / Models / Features / Pricing / FAQ", active item white) with a separate blue "Start generating" button beside it.
- Header CTA pair flips with background: on dark, "Sign up for free" white and "Log in" black; on light, "Sign up for free" outlined and "Log in" black.
- Pricing: colored cards by material (Free dark glass, Basic gray gradient, Pro saturated blue "Most popular", Max warm orange), each with a white "Get X" pill; color temperature encodes tier.
- Crafted motion tied to one element each: `aurora-sweep` light bands, `border-beam-rotate` around a card border, flip-clock countdown digits, a rating with a heartbeat pulse.
- The mega menu pairs each tool with an outcome line ("Upscaler / Images and video up to 22K").

### Fonts from the design posts

From two font posts bookmarked on X; licences and weights from Google Fonts, Fontsource, vercel.com/font, Fontshare and MyFonts listings [doc]; looks [obs] from specimens.

| Font | Licence | Weights | Role |
|---|---|---|---|
| Switzer (Indian Type Foundry) | ITF Free Font License, free for commercial use; one source says self-hosting needs ITF consent, check fontshare.com/terms | 100-900, 9 weights plus italics, variable | Body and headlines; the best single-family choice |
| Figtree (Erik D. Kennedy) | OFL 1.1 | 300-900 variable, italics | Warmer consumer body |
| TASA Orbiter (Local Remote) | OFL 1.1 | 400-800 variable, no italics found | Body; an Inter alternative with open apertures |
| Geist Serif (Vercel) | OFL 1.1 for the Geist family (serif file not opened) | Regular only, four shapes on an `ELSH` axis (Regular, Square, Triangle, Heart) | One display level; Triangle has triangular i-dots |
| Hedvig Letters Serif | OFL | 400 only | One display or editorial level |
| Savate (Plomb Type) | OFL | 200-900 variable with italics | Website display only; reversed-contrast flared geometric |
| SEKUYA | OFL | 400, uppercase display | Poster and wordmark only |
| brodine | Commercial, about $12.50 per style | not verified | Skip; Figtree covers the role |

- A display face with character (Geist Serif Triangle, Savate, SEKUYA) carries distinctiveness at hero size; keep the body in a plain sans.
- Regular-only serifs have no weights or italics to build hierarchy, so they can hold one level only.
- Prefer the Fontshare CDN or written consent before self-hosting Switzer.

### Hero studies (uisabor, Figma only)

Four hero designs shared on X as Figma frames, no code [doc] [obs]:

- Qredible: a saturated cobalt sky over painted grass hills; a thin high-contrast serif headline, centered and tight; the product screenshot rises out of the hills with grass layered in front of it; use-case cards reuse the grass along their bottom edge.
- Orbit CRM: a one-ink blue halftone engraving; a pixel display font with a huge left-aligned headline; mono buttons; a trust strip acting as a second nav row; white UI cards floating on duotone engraving tiles.
- Xenora: photographed sky and a temple; a left-aligned, tight-tracked sans headline; a huge product screenshot bleeding off the bottom; annotation pills with connector lines ("Across Teams") tying the CTA to the product.
- Qredible dark: a sunset, a serif headline, connector pills on both sides, one warm peach accent; the product fades into black and the logo strip overlaps the fade.
- Weaknesses by unslop's signs: uppercase tracked nav, a pill badge above the headline ("99.9% WORKFLOW RELIABILITY"), an unverifiable "Used by 5,000+".

### Scroll, shader and motion galleries

- scrolltide.co [doc]: 152 templates and 55 shaders as copy-paste prompts (React, GSAP, Three.js, Lenis); $299 lifetime, prompts behind sign-in. Free SELENE: six parallax layers, dust clearing on landing, a trajectory line drawing to "384,400 km" on scroll. Component tweak panels expose Motion: duration 620ms, bounce 0.45, spring toggle, plus Copy JSX.
- scrollshaders.com [doc]: 117 WebGL2 fragment shaders on 11 shelves (mesh gradients, grain, dither, halftone, fluted glass…), each one self-contained React file used as `absolute inset-0 -z-10`. Built in: pause off-screen and in hidden tabs, `maxDpr` 2, a still frame under reduced motion.
- motionin.design [obs]: 54 sections whose card descriptions are full engineering specs: one `requestAnimationFrame` clock owns live motion and GSAP owns only the entrance; honours reduced motion with a composed still; pauses when hidden or off-screen; caps DPR; one budgeted redraw at a quarter of the frame rate because a row cost more than 5ms of a 16ms frame; one named place where the frame spends its color.
- Scroll stories seen in the posts [obs]: a wine bottle that decants on scroll with the cue "SCROLL TO DECANT"; a book that rotates and opens; flowers growing over a figure; a zoom across scales to "YOU ARE HERE"; a Morning / Night toggle that switches the scene; a point-cloud building with mono figure labels ("FIG. 01", "YAW 009 / PITCH 57") and a live stat bar.

### footer.design

- A gallery of roughly 850 footers [inf from "1 / 66" pages at about 13 each], filterable by 11 styles (Typographic, Large Type, Animated, Cards, Dark…) [doc].
- Wordmark at display size bleeding off the bottom edge, small grouped link columns above, a closing CTA ("Book a demo") [obs].
- A huge serif wordmark under "Let's talk." with two pill buttons [obs].
- A dense dark keycap-style sitemap plus a hanging lamp, "Pull the cord on your way out", that toggles the page theme [obs].
- The email address as the largest element on the page [obs].
- A mono uppercase legal row over a textured image band [obs].

## Cross-site rules from the AI product sites

### Hero

1. Make the product, working, the hero object: a live HTML render with the real tokens (Linear, Cursor, Notion, Granola) or a usable input (v0, Perplexity, Krea), because it proves the product exists, stays crisp at every DPR and theme, can animate state, localizes, and never goes stale against a screenshot.
2. Fill the render with believable domain data ("Reduce ETA jitter", "Worked for 2m 30s", "Unstaged +23 -24"), never lorem, because fake content is the fastest tell of a template (Linear, ChatGPT).
3. Choose one composition axis and commit: a centered giant sentence with a window rising out of the fold (ChatGPT), or a left-aligned modest H1 over a full-width product (Linear 64px, Cursor 26px), because a mixed axis reads as a centered template stack.
4. When the product needs an account, consider making the sign-in form the hero (Claude), because it removes a click; when the brand is already known, art plus logotype plus pills can replace the headline (Midjourney).
5. Let one object or the product overlap the scene (grass in front of the screenshot, a bottle crossing the headline, a product bleeding off the bottom into a fade), because overlap creates depth and an abstract blob proves nothing.
6. Make interactive headline words into the hero's tab bar when the product has 2-4 modes (ChatGPT's rotating verbs), because the claim and its proof become one control.

### Type

7. Pair one display face with character against a plain sans body, display only on H1, H2s and one big number at 64-120px with tight tracking, because the display face is the fastest signal that the page was not generated and a display body kills readability (Perplexity 180px serif, Granola 86.4px serif, Claude serif, uisabor).
8. When staying in one sans family, use negative tracking that grows with size (v0 -0.04em at 32px to -0.06em at 64px; Notion -0.033em at 64px; Krea -0.03em at 72px) and a large size ratio (72:16), because tight display tracking makes a neutral grotesk feel bespoke.
9. Prefer medium weight (500-510) headlines to 700-800, because medium reads engineered and calm and bold headlines are what imitators of the restrained look add (Linear 510, Krea 500).
10. Write two-tone headlines, ink first line or clause then muted ink-2 for the rest, or an italic serif closing phrase, because one block carries headline and subhead with fewer elements (Linear, Krea, Perplexity, Cursor's "Title. Gray sentence.").
11. Add a mono caption layer (12px, uppercase, dates and figure numbers) only for technical, data or science products, because on those it reads as instrumentation and elsewhere it reads as costume (Linear "FIG 0.1", Perplexity footer, Midjourney).
12. Use the app's answer typeface for site headlines when the product writes prose (Claude's serif), because the site then sounds like the product.

### Color and texture

13. Use warm paper instead of pure white (`#f7f7f4`, `rgb(250,249,245)`, `rgb(250 248 245)`) or hue-tinted dark instead of `#000`, because pure white and black read as default SaaS and a tinted ground reads as atmosphere (Cursor, Claude, Perplexity, Midjourney).
14. Let one world image or the product imagery carry all the color and keep chrome monochrome with one accent, because a saturated world plus neutral chrome reads as art direction and color spread across UI reads as a template (v0, ChatGPT, uisabor, motionin's one named color place).
15. Save one saturated moment for late in the page (Linear's quote cards after 8,000px of gray), because a single color break is memorable and many are noise.
16. Build depth with lighting (radial top light, vignettes, 300-400px fade masks, depth of field) instead of gradient blobs, because light implies a physical object (Linear).
17. Add texture from a hand-made source (grain, halftone, duotone engraving, line drawings, painted landscapes, collage), because it is cheap and is the fastest way out of flat-template territory (Perplexity, Cursor, Granola, Claude, Notion, uisabor Orbit). Prefer one-ink halftone or dither over photoreal 3D when there is no 3D budget.
18. Draw structure with hairlines and double bezels (1px at 5-8% white; outer 22px radius with 8px padding around inner 12px) instead of boxed cards, because structure should be felt, not seen (Linear).
19. Carry one visual metaphor or the hero world across hero, auth, error pages and later sections (Midjourney's CRT, Qredible's grass on use-case cards), because continuity at the edges makes a site feel authored.

### Section rhythm and scroll

20. Repeat one section scaffold and vary only the demo (Linear's H2 left, copy right, full-width render, "+" features; Cursor's 1/3 text, 2/3 stage, alternating sides), because readers learn the pattern by section two and scan faster.
21. Use a sticky product frame that swaps content as an accordion or step list advances on scroll (ChatGPT `top: 132px; height: 768px`, Granola, Claude's day timeline), because scroll becomes a guided demo without autoplay video.
22. Tie at most one scroll-driven change to the product's own story and cue it once ("SCROLL TO DECANT"), because meaningful scroll motion is remembered and fade-up on every section is the AI tell.
23. Keep site motion at app speed (100-200ms hovers, .97 press, 180ms menus) and put ambient motion inside the product demos, not on scroll, because the site should feel like the product (Linear, Claude). See L19.
24. Write any motion brief as an engineering spec: who owns the frame loop (one rAF clock, GSAP for the entrance only), the reduced-motion still, pause off-screen and in hidden tabs, DPR cap 2, teardown on unmount, where assets swap, because agents fill gaps with defaults and a specific spec is how a one-shot comes out unique (motionin).
25. Use at most one shader or 3D scene, behind the hero only (`absolute inset-0 -z-10`), paused off-screen, DPR capped at 2, with a still poster before WebGL loads and under reduced motion; run glyph, halftone and duotone effects at 8-12fps (unslop), because a looping GPU background costs about as much as a video and three make the page a demo reel.
26. Crop UI fragments off card edges in carousels (ChatGPT 370×578 cards), because a crop implies the UI continues and feels more real than a fully framed mock.

### CTAs and navigation

27. Show one filled button per view and repeat one CTA verb everywhere (Granola "Download", Claude "Try Claude", Cursor "Download"), because a binary decision converts and a CTA everywhere is what imitators get wrong.
28. Reuse the app's own buttons in the site nav (ChatGPT, v0 6px-radius tool buttons), because site and app then read as one product.
29. Strengthen the CTA as the visitor scrolls (Granola's nav pill flips 6% tint to solid; Perplexity and Krea flip nav and button contrast with the background), because the CTA should be loudest when the visitor has read enough to act.
30. Make the loudest type on the page the closing CTA (Cursor 52-72px "Try Cursor now.", v0 48px, one button on an empty band), because the end of the page is the decision point.
31. On long pages, keep the conversion action reachable with a floating section-nav pill or corner pills instead of a heavy sticky header (Krea, Midjourney), because orientation and action stay one click away without covering content.
32. Put a reassurance line under the plan button ("No commitment · Cancel anytime"), because it removes the main objection at the moment of clicking (Claude).
33. Write mega-menu items as tool plus outcome ("Upscaler / Images and video up to 22K"), because the nav itself sells and visitors scan by job (Krea).

### Proof, content and trust

34. Use product-specific quotes from named people with avatar and title, in a contrasting band, not generic praise or unverifiable counts ("Used by 5,000+"), because specific, attributable proof is the only kind a skeptic believes (Cursor, Granola).
35. Show real community output as proof for generative tools (v0 template gallery, Midjourney Explore), because the artifact sells more than the workflow.
36. Publish a dated changelog as editorial content (Linear's 4-up mono-dated timeline, Cursor's 645px column, Midjourney's filterable feed), because dated evidence proves velocity.
37. Serve a `.md` twin per page and `/llms.txt` (Linear), because agents now read and buy too and it is nearly free.
38. Give consent choices equal weight (Notion's identical "Accept all" / "Reject all"), because honest consent is a trust signal.
39. Embed pricing where interest peaks, on the feature page, and encode tier by color temperature rather than badges (Notion, Krea), because the deciding question is answered in place.

### Footer and checklist

40. Treat the footer as the last brand moment: wordmark at display size bleeding off the bottom edge, one closing CTA or the email as the largest text, small grouped link columns, a small mono legal row, at most one playful object (a pull-cord theme switch), because it is where a visitor who read everything lands (footer.design; Cursor's three-state theme switch).
41. Before shipping, run checklist.design's landing-page list (a headline written for a skeptic, one primary CTA, social proof just below the fold, an FAQ that handles objections, the CTA repeated at the bottom), then unslop's template check: swap in a competitor's name, and if the page still fits, push copy, visual and signature harder, because a page any competitor could sign is a template.

### Avoid

- Uppercase tracked nav as the default, pill badges above the H1 that carry no news, unverifiable counts, and a newsletter modal on scroll (uisabor weaknesses, unslop; the modal seen on beautifului.dev). An announcement pill is fine only when it carries one timely message (v0).
- Purple glow and gradient blobs, glowing borders, several accents, 700-800 headlines, everything centered, scroll animation instead of product animation, and static blurry screenshots with lorem data: the list of what imitators of Linear get wrong.
