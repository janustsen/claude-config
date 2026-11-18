# Hero, nav, sections and footer

## First screen, measured at 1440x900

| Site | H1 size / weight / tracking | Alignment | What fills the hero | CTA treatment |
|---|---|---|---|---|
| Linear | 64 / 510 / -0.022em | left | Live HTML product UI (sidebar, issue, agent panel) starting about 60% down, bleeding off the fold | One filled pill in the nav (Sign up). No button in the hero, only a "New: Loops →" link on the subhead baseline, right-aligned |
| Vercel | 64 / 400 / -0.06em | left, three-column split | A 3D logomark in the center; a three-line list on the right completes the headline | Black "Deploy now" and outlined "Talk to sales", 32-40px |
| Stripe | 48 / 300 / -0.02em | left | A WebGL colour ribbon slashing across; a live GDP ticker as eyebrow | Solid accent "Get started >" and outlined "Sign up with Google" |
| Cursor | 26 / 400 / -0.013em | left | Product windows over a full-width oil-painting landscape | Black pill "Download for macOS ↓" and pale pill "Request a demo →" |
| Dia | 38 / 500 serif, plus a giant swash wordmark | centered | Sunlit photograph, then the wordmark, then the product window, then a white horizon arc | One black pill pinned at the horizon, the platform note under it |
| Raycast | 64 / 600 | centered | Brand-stripe light streaks | White "Download for Mac" pill at the bottom center |
| Arc (farewell letter) | 76 / 600 serif | centered | Die-cut sticker logo | "Read more" grey pill; copy says "Scroll to read" |
| Teenage Engineering | the price as H1 | | One product, studio-lit, filling the screen | none above the fold |
| Family | 68 / 500 custom | centered | Mascot illustrations framing both sides | Black "Download on iOS" and grey "▶ Watch the Video" |
| OpenAI | 48 / 500 | centered | The product's input box with a typed example and suggestion chips that double as navigation | "Try ChatGPT ↗" black pill in the nav |
| Mercury | 49 / 480 | centered | A desk on a misty summit at dawn | An inline email field plus "Open account" as one capsule; the legal disclaimer as a translucent caption bar at the hero's bottom |
| Paco, Emil | 16 / 400-500 | left, narrow column | text only | none |

## First-screen rules

1. **The headline is a claim; the hero image is the proof.** Keep the headline to two lines and give the space to the product. Render the product's UI in HTML (crisp at any DPR, themable, animatable, accessible, lighter than a 2x PNG, always in sync with the app) and seed it with believable content: real-looking names, IDs and timestamps ("DRV-8852", "2min ago"). Never lorem ipsum.
2. **Bleed over the fold.** A cut-off object is the strongest scroll cue there is, far stronger than a bouncing arrow. Put the top of the hero media at 55-70% of the viewport height so 30-45% of it shows.
3. **The second line does the subtitle's job**: the headline's continuation in muted ink (Stripe), or a stacked list completing the headline on the other side (Vercel).
4. **Left-aligned by default.** Every product and tool site measured is left-aligned. Center only where there is no product UI to show (a letter, a launcher, mascots).
5. **One primary action, visible but small.** 32-48px tall. The primary is usually solid ink; the secondary a pale fill or hairline outline. Single-action sites repeat one download action as a sticky or bottom-anchored element instead of adding buttons.
6. **No pill badge above the headline.** Announcements go on the subhead row at the far right (Linear, Framer) or in a dismissible top bar (Stripe).
7. **Pre-answer the obvious question** in 12-13px under the CTA: "Available for macOS and Windows", a footnote marker on a regulated claim.
8. **Detect the platform for a download CTA** ("Download for macOS", "…Windows", "…Linux") and keep a quiet link to other platforms.
9. **If the product is an input, open on that input**: OpenAI and Cosmos make the hero the input box; v0's landing page is the working composer, and anonymous visitors can run a real generation. A typing placeholder (1 character per 100ms, 1.7s hold) and 3-5 example chips teach what to type.
10. **The agent CTA (2026).** Give the coding-agent path its own secondary button: Rive's "Start with your coding agent" with a copyable prompt box, Framer's "Install the MCP", PostHog's "Install with AI".
11. **Headline as control.** ChatGPT's headline verbs ("chat / work / code") are toggles that rotate and swap the product window below, so claim and proof are one control.
12. **One entrance, choreographed.** A single staggered rise on load (T3 Code: 0.7s `cubic-bezier(.2,.7,.2,1)` from 16px, delays 0 / 90 / 180 / 300 / 400 / 520ms for headline lines, sub, actions, screenshot), disabled under reduced motion.
13. **Mobile hero (390px):** drop the second sentence of the headline (Stripe), full-width buttons side by side or stacked, logo wall down to 3 logos, nav down to logo plus one menu button, hero media still cropped by the fold.

## Navigation forms

| Form | Measured on | When | Why |
|---|---|---|---|
| Full-width transparent bar, hairline bottom, blur | Linear: fixed, 73px, `backdrop-filter: blur(20px)` | product sites with long pages | content stays visible under it; the hairline is the only chrome |
| Plain sticky bar, no blur | Vercel 64px, Cursor 52px, Anthropic 84px | light themes | cheaper and crisper on light backgrounds |
| Floating inset capsule | Raycast (inset about 74px, radius about 12, translucent dark); Dia (a centered pill with the logo and 3 links); Granola (morphs from a full bar into a floating pill with a shadow once scrolled) | consumer and tool sites that want to feel like an app | an object on the page that frees the corners; the morph is a free moment of craft |
| Split around a centered wordmark | Anthropic, Delta Cafés, Agrumea | brands where the logo is the identity | symmetry signals editorial or luxury; only with 3-6 items |
| Nav as typographic specimen | Teenage Engineering (pictogram + lowercase label + 3 tiny sub-links); Lynn Fisher (a table of contents with dot leaders and roman numerals); Locomotive ("Work, Agency, Careers, Store" written as a sentence); PSP (`[ WORK ] [ DIRECTORS ]`) | portfolios, studios, concept brands | the nav carries the concept, so it is the first proof someone designed the site |
| Local product nav | Apple: the global 44px nav scrolls away and a sticky local nav takes over (product name, Overview / Tech Specs / Compare, blue "Buy" pill) | multi-page product sections | the next action and the visitor's place are always visible |
| No nav | Paco, Emil, Are.na (only a "Log in" chip) | one-page sites | nothing to navigate |

Nav details:
- **Three emphasis tiers on the right:** a text link (Log in), an outlined or pale pill (Contact sales), one solid ink pill (Sign up, Download). Never more than one solid button in the nav.
- **Nav buttons are small:** 28-36px tall, 13-14px text. The hero CTA, when there is one, is larger (43-56px).
- **The nav CTA earns colour after the hero CTA scrolls away** (Granola's grey Download turns green; Dia adds a Download pill after scrolling). Use an IntersectionObserver on the hero CTA and toggle a class.
- **The logo is a hidden press kit:** right-click or hover offers "Copy Logo / Copy Wordmark / Download Brand Assets / Brand guidelines" (Vercel, Framer).
- **Counts and live state can live in the nav:** "Showcase ⁽²⁹⁾", "● Online ⁽⁹⁾" (Basement).
- **Mega-menus** open on hover intent with a fade of about 150ms; use a prediction cone for nested panels; menus open on `pointerdown`.
- **Long pages** can use a floating bottom pill for section navigation with the one CTA attached instead of a heavy sticky header (Krea).
- **Mobile:** logo plus one square or round menu button plus at most one CTA.

## Section rhythm

- **The split statement.** A big heading in the left column and a paragraph plus "Learn more →" in the right column on the heading's top line, then a full-width product composition. 12-column grid: heading spans 1-6, paragraph 8-12, top-aligned. Section padding 120-160px on desktop. Linear repeats this frame for every section.
- **Product compositions, not screenshots.** Overlap two HTML-built pieces by 10-20% (a Slack thread card on a kanban board), mask one edge with `mask-image: linear-gradient(to right, #000 70%, transparent)`, use real-looking data. A composition tells a story ("conversation becomes issue"); a screenshot shows a screen. Simplified vector UI with real copy, one interaction per card, also stays crisp and themable (Comet).
- **Sticky demo beside an accordion** that advances on scroll gives a guided demo with no autoplay video (ChatGPT). A replayable animated mini-conversation with "Replay" and "Modify prompt" shows behaviour a screenshot cannot (Claude).
- **Density follows the audience.** Developer sites pack product detail. Consumer sites show one idea per screen. Peers' portfolios fit in 1-2 screens (Paco 1,424px tall, Emil 1,854px). Apple's AirPods page is about 32 screens because each chapter is one claim with one object.
- **Logo walls** sit exactly on the fold line, doubling as the scroll cue (Vercel), or in a strict hairline-bordered grid (Basement's 6 columns, Stripe's page hairlines). Never under a "Trusted by" heading.
- **Testimonials** from named, recognisable people. Cursor: 3 columns of pale warm cards, quote first, avatar, name and title at the bottom, under one centered 32px title. Anonymous praise is weak; fabricated praise is a lie.
- **Stats, if any, are one band** (Stripe: one dark band, 4 large numbers with grey captions). Nobody repeats stat tiles across sections.
- **Feature grids are unequal.** Dia: 2-up then 1+2 cards, an uppercase-pill eyebrow, a 20px sentence, product UI bleeding out of the card bottom. Family: alternating image and text rows. Nobody ships a three-column icon-title-text grid.
- **The trust section is a first-class block**: one concrete claim and one link ("Privacy first with you in control … Learn more →"), not a footer link.
- **Pricing translates units into outcomes** ("64 images") and can give each tier its own colour temperature (Krea).
- **The changelog is editorial**: a date rail plus a 645px prose column (Cursor). It proves velocity and doubles as the product-thinking blog.

## Footer, consent and hidden details

- **Legal text designed in, not hidden.** Mercury's "not an FDIC-insured bank" disclaimer is a translucent caption bar at the bottom of the hero; Stripe and Apple use footnote superscripts. Regulated products build trust by showing fine print with confidence.
- **Cookie consent as a small card**, bottom-left or bottom-right, with two equal buttons (Cursor, Framer). If the site uses no third-party cookies, say so or show nothing (PostHog's "Legally-required cookie banner… doesn't use third-party cookies" is a joke that is also true). The failure: a consent sheet covering 40% of the first screen.
- **Footers** can carry the brand's loudest type: a large wordmark bleeding off the bottom edge, a newsletter field, 3-4 link columns.
- **Hidden details that get screenshotted:** the logo press kit, live counters (Stripe's GDP share, Are.na's "15 years and 101 days", "● Online (9)"), a version stamp ("v. XIX"), a theme toggle as a sun icon, sound toggles, a minimap ruler.
- **Utility text in brand voice:** Nothing's region modal in mono caps ("LOOKS LIKE YOU'RE IN: United States / BUT YOU'RE BROWSING THE STORE FOR: United Kingdom").
