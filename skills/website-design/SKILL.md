---
name: website-design
description: Design and build a beautiful, distinctive website (product or SaaS landing page, AI product site, fintech, hardware, food and craft brands, studio or agency, personal portfolio, directory) that does not look templated. Gives the five-line brief written before code (concept, world, type move, loud moment, signature), site archetypes with their defaults, hero, nav and section composition, display typography, colour and art direction, scroll storytelling, page transitions, measured motion numbers from 41 sites (Linear, Vercel, Stripe, Cursor, Apple, Dia, Granola, PostHog, Teenage Engineering and award winners), the performance and accessibility floor, and a capture-and-measure script. Use when asked for a website, landing page, homepage, marketing page, portfolio or brand site, or to make an existing site look less generic. For app screens use product-ui.
license: MIT
---

# Website design

Sites that feel designed are not more decorated. They make one strong, specific choice in each of four places (concept, art direction, a type move, one signature detail), spend loudness in exactly one place, and keep everything else neutral and fast. Templated sites come from making no decision at those four places.

## Step 0: write the five-line brief before any code

1. **Concept**: the metaphor the whole site lives inside. A desktop OS with draggable windows (PostHog), a film strip (a portfolio), a farewell letter (Arc), an object in a dark studio (Teenage Engineering), or "the product itself" for tools.
2. **World**: where the imagery comes from, ideally outside the product's category. A classical oil painting behind product windows (Cursor), sunlight through leaves (Dia), a desk on a mountain at dawn (Mercury), documentary photographs of coffee pickers.
3. **Type move**: the one unusual type decision. Söhne at weight 300 (Stripe), Geist 400 at -0.06em (Vercel), a swash serif wordmark at about 400px (Dia), a 16px-only page (Paco, Emil).
4. **Loud moment**: the single place where colour, motion or 3D is spent. Stripe's ribbon, Raycast's light streaks.
5. **Signature**: one detail worth a screenshot. A live "Global GDP running on Stripe" ticker; right-click on the logo offering brand assets (Vercel); a cookie banner that is a joke and also true (PostHog).

Template test: if the brief would fit a competitor, push harder. Everything not named in those five lines stays neutral: one tinted neutral ramp, one accent, hairlines, standard spacing.

Calibration: generated pages now cluster on warm cream with a clay serif, near-black with one acid accent, mono eyebrow labels, middle-dot meta strings and arrow-suffixed links. Leading sites use some of these too, but as choices tied to their world. Use one only when the brief calls for it.

## Step 1: pick the archetype

| Archetype | References | Concept default | Type default | Motion budget | Hero |
|---|---|---|---|---|---|
| Developer or B2B tool | Linear, Vercel, Raycast, Cursor, Framer | the product itself | grotesk 500-520 or 400, tight tracking, mono for data | fast (100-200ms), view transitions, CSS reveals | real product UI built in HTML, crossing the fold |
| AI assistant or consumer AI | OpenAI, Anthropic, Granola, Dia, Cosmos | the input itself, or a humane world | serif plus grotesk, warm paper ground | moderate, one cycling or typing moment | the product's input box, or the product over a nature or art image |
| Fintech or regulated | Stripe, Mercury, Family | calm, live proof | light weight (300-480), generous space | slow and soft (300-800ms), one WebGL moment at most | a live number or serene photograph, an inline email-start form, visible disclaimers |
| Hardware or physical product | Apple, Teenage Engineering, Nothing | the object | the brand's own face, a small product H1 | pinned scrubbed chapters, video sequences | one studio-lit object; price or name stated plainly |
| Food, beverage, craft | Agrumea, Delta Cafés, Sweet Tape | origin, place and people | display serif or condensed caps over full-bleed photos | smooth scroll allowed, a scroll path or process diagram | documentary or packaging photography, floating product objects |
| Studio or agency | Basement, Lusion, Locomotive, Bulletproof | an instrument or showreel | poster type at line height 0.8-0.9 | high: WebGL, custom cursor, kinetic type | an interactive scene, or a work list with hover previews |
| Portfolio for peers | Paco Coursey, Emil Kowalski, Rauno Freiberg | the index, or one idea done perfectly | 16px everything, or one character face | none to one | a name, a sentence, a list |
| Portfolio for clients | Rauno, Josh Comeau | one toy or metaphor plus a fast index | a characterful display face plus a clean body | one moment | the toy or portrait plus the claim |
| Directory or community | Are.na, Cosmos, Godly | participation | small plain type | minimal | a search box, or "add your own" |

## The build order

1. **Archetype and audience** in one line each.
2. **Five-line brief.** Pass the template test.
3. **Tokens.** A tinted neutral ramp (page, raised, line at 6-10% ink, ink 1/2/3); one accent in OKLCH checked for 4.5:1; a type scale with a register gap (12/13/14/16/18, then 24/32/48/64/clamp(56-96)); radii by size (4-6 / 8-10 / 12-16 / 20-24); two easings (`--ease-ui: cubic-bezier(.2,0,0,1)`, `--ease-out: cubic-bezier(.16,1,.3,1)`) and two duration bands (150ms feedback, about 500ms storytelling). If the site belongs to an app, reuse the app's tokens.
4. **First screen.** A left-aligned claim of at most two lines; the continuation in a second ink instead of a subtitle; one primary action plus one quiet secondary; hero media crossing the fold (its top at 55-70% of the viewport); a small pre-answer caption under the CTA ("Available for macOS and Windows").
5. **Nav.** The form that fits the archetype; three emphasis tiers on the right (text link, pale pill, one solid pill); the nav CTA earns colour after the hero CTA scrolls away.
6. **Sections.** Split statements (heading left, paragraph right on the same top line), product compositions with real-looking data, unequal feature layouts, at most one stats band, named testimonials, the logo wall on the fold line or in a strict grid.
7. **Imagery.** One source world; depth by horizon occlusion or text behind the object; brand-mark geometry as texture.
8. **Motion.** CSS reveals guarded by `@supports` and reduced motion, never hiding content by default; cross-document view transitions on; one storytelling device only if it explains something; hover at 100-160ms.
9. **Copy.** The category noun in the headline; the objection answered in the subhead; real numbers; delete every subtitle that restates its heading.
10. **Mobile.** Cut copy rather than shrinking it; full-width buttons at least 44px; a re-cropped hero that still crosses the fold.
11. **Floor.** LCP is the hero; preload the display font; one canvas, paused off-screen; no hidden content; 4.5:1 contrast for grey text; visible focus; skip link; reduced motion gives a calmer site, not a broken one.
12. **Final check.** Squint (is the loud moment the only loud thing?), swap the brand name (does it still fit someone else?), screenshot at 1440x900 and 390x844, jump-scroll to 25 / 50 / 75% and look for empty voids, keyboard-only pass, reduced-motion pass. Measure your build with [scripts/measure.js](scripts/measure.js) and compare against the reference numbers.

## Defaults when the brief does not decide

- Left-align. Center only for letters, single-object pages and playful consumer brands.
- Display tracking: 0 for body, -0.01 to -0.03em from 40px, -0.02 to -0.06em from 64px, -0.04 to -0.1em at 100px and up; line height 0.85-0.95 at 80px and up.
- One surprising display weight: 300-400 for calm or expensive, 500-520 for tools, 700-800 in a rounded face for friendly.
- Serif plus grotesk is the humane signal; the serif never goes on buttons or labels.
- Big product, small headline (Cursor 26px, Apple 28px) when the product is the hero.
- Primary buttons are ink (black on light, near-white on dark) more often than brand colour; 32-48px tall in the hero, 28-36px in the nav, never giant.
- Loud colour lives in imagery, not chrome.
- No pill badge above the headline; put announcements on the subhead row ("New: Loops →") or in a dismissible top bar.
- No smooth-scroll library on product, docs or pricing pages.
- Light theme by default unless the archetype is a developer tool; offer the other theme.
- No helper text that restates a heading. No summary number tiles repeated across sections.

## Which skill does what

| Need | Skill |
|---|---|
| Strip generated-looking tells after a first pass | `emil-unslop-design` |
| Aesthetic direction from the subject matter | `frontend-design` |
| Choosing and pairing typefaces, variable axes, scales | `emil-typography` |
| OKLCH ramps, accent derivation, contrast | `emil-color` |
| One animation; several coordinated (hero entrance, stagger) | `animate`; `choreograph` |
| Frame budget, janky scroll effects | `animation-performance` |
| Pre-launch sweep (metadata, OG images, focus, layout shift) | `emil-prep-for-prod` |
| An app screen inside the site (dashboard, product UI) | `product-ui` |

## Reference map

- [references/type-and-colour.md](references/type-and-colour.md): display typography measured on 22 sites, font picks, two-ink copy, neutrals, accents, texture, theme.
- [references/hero-nav-sections.md](references/hero-nav-sections.md): first-screen craft, nav forms, section rhythm, logo walls, testimonials, footers, consent, hidden details.
- [references/imagery-and-motion.md](references/imagery-and-motion.md): art direction ranked, scroll storytelling patterns, micro-interactions, page transitions, motion numbers per site, the build stack with paste-ready CSS and browser support.
- [references/copy-mobile-floor.md](references/copy-mobile-floor.md): copy voice, responsive rules, performance and accessibility floor.
- [references/case-studies.md](references/case-studies.md): one block per studied site with measured values and its lesson.
- [scripts/measure.js](scripts/measure.js): run in any page (for example `chrome-devtools-axi eval "$(cat scripts/measure.js)"`) to get its display type, type histogram, nav, buttons, dominant transitions and easings, reduced-motion and view-transition support, and libraries.
