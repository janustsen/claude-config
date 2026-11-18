# Imagery, scroll, motion and the build stack

## Art direction, ranked by how much it separates a site from the template

1. **Imagery from outside the category.** Cursor: a classical oil-painting landscape behind product windows. Mercury: a desk and chair on a misty summit at dawn. Dia: sunlight through yellow leaves. Anthropic: an aurora over Earth. Delta Cafés: documentary photos of coffee pickers. Every competitor shows dashboards on gradients, so nature, art or documentary photography wins attention instantly and carries values (calm, craft, humanity). Choose one source world (public-domain paintings from museum open-access collections, nature photography, documentary images) and use it in every section's background band.
2. **Horizon occlusion.** Dia's convex white arc, Sweet Tape's dark green curved horizon, a product window half-sunk into a photoreal grass hill. A foreground layer covers the bottom of the hero media, which grounds the object in a world, adds depth with no 3D, and turns the fold into a horizon. Use an SVG ellipse or path, or a photo cut-out, absolutely positioned over the bottom 10-20% of the hero media, filled with the page background.
3. **Text behind the object.** Bulletproof's 3D ampersand covers part of its headline; Dia's product window covers the lower half of the giant "DIA". Layering (background, type, object, UI) creates depth and makes type part of the image. Cut-out PNG, WebP or canvas above the headline; cover at most 30% of any glyph.
4. **The real object, lit like a product shot.** Teenage Engineering lights one product under a single top spotlight on black; Apple shows a single earbud on light grey; Nothing crops transparent earbuds by the viewport. One object per screen, large, generous negative space, a consistent light direction across the page.
5. **Mascots and illustration for fear-heavy categories.** Family uses children's-book blobs with legs for crypto; PostHog uses hedgehogs for analytics. Friendliness lowers perceived risk. Only with a consistent illustration system (one stroke weight, one palette), never mixed with stock 3D.
6. **Brand mark as texture.** Raycast's hero streaks repeat the diagonal stripes of its logo; Stripe's ribbon is its gradient identity. Extract one geometric gesture from the logo and scale it up.
7. **One visual metaphor carried everywhere.** Midjourney's CRT-terminal look appears on its hero, sign-in wall and company page, so the brand is recognisable in one frame.

## Scroll storytelling, lightest to heaviest

| Pattern | Seen on | Mechanism | When it earns its place |
|---|---|---|---|
| Bleed and reveal (content crosses the fold, sections fade and rise once) | nearly all | CSS `animation-timeline: view()` or an IntersectionObserver, once | always; the default |
| Sticky chapter rail (chapters on the left, active one underlined with a progress bar, content scrolling right) | Granola ("Before / In / After the meeting"), Are.na, Arc | `position: sticky` rail; IntersectionObserver sets the active item; progress from `view()` | when the product maps onto a sequence the visitor recognises (time, steps, stages) |
| Pinned scrubbed chapter (one object holds still while text or video advances) | Apple AirPods (32 screens, 16 videos) | GSAP ScrollTrigger `pin` and `scrub`, or sticky plus video `currentTime` driven by scroll | hardware and physical products where each claim has a visual |
| One idea at a time (huge statements, only the focused one in full ink) | Perplexity | scroll-scrubbed opacity on a list | a manifesto or a few strong claims |
| Dark cover into a light document | Arc | background change at the section boundary | a statement on top, reading below |
| Horizontal track driven by vertical scroll | Rauno (white panels on grey with a minimap ruler) | sticky container, `translateX` from scroll progress | portfolios with few large items; provide the minimap and keyboard support |
| Scroll path or diagram | Delta Cafés (a dashed path linking line-drawn process circles over photos) | SVG `stroke-dashoffset` from scroll | process and origin stories |
| Sticky bottom CTA bar | Arc, Dia | `position: sticky; bottom: 0` | single-action sites |
| Whole-site virtual scroll or WebGL world | Lusion, Active Theory | custom scroller and canvas | only studios selling exactly that; inaccessible and blank before load |

Rules:
- **Scroll motion must explain something**: a path that traces a process, a rail that maps the user's day, a pinned object whose features light up one by one. Decorative parallax does not.
- **Never hide content until it is revealed.** One captured site left a 400px empty void at a 25% jump-scroll; another was blank for 2.5s behind a loader. Fast scrolling, find-in-page, screenshots, link previews and slow devices all hit this. Start content visible and animate only inside `@supports (animation-timeline: view())` and `prefers-reduced-motion: no-preference`.
- **Smooth-scroll libraries (Lenis)** appear only on brand and story sites (Nothing, Locomotive, Agrumea, Sweet Tape). No product or tool site used one. They break find-in-page, anchor jumps, keyboard scrolling and screen-reader focus.

## Micro-interactions

- **Hover is colour and opacity at 100-160ms.** Linear has 233 nodes at 0.1s and hovers at 0.16s `cubic-bezier(.25,.46,.45,.94)`; Vercel 0.1-0.15s `cubic-bezier(.4,0,.2,1)`. `transition: color .15s, background-color .15s, opacity .15s`, never `all`.
- **Press `scale(.97)` on buttons only.** Cards do not scale on hover; none of the top product sites did it.
- **Hover-to-preview lists:** a list of works plus one floating preview that follows the pointer with a lerp of 0.1-0.2 (PSP's duotone video next to the pointer). Cheap with one `<video>`.
- **Cycling headline words:** change one noun every 2-3s with a 200-300ms `blur(4px)` and opacity crossfade; pause on hover and under reduced motion (Cosmos).
- **Live numbers:** any honest live metric (Stripe's GDP share, Are.na's age, Basement's online count), with tabular numerals and no layout shift.
- **One instrument in the hero** (a "HUMAN | MACHINE" switch that changes the render, a "PULL ME" tab, a sound toggle): at most one per site, discoverable, never required.
- **Inline feedback beside the trigger:** a "COPY" button whose copied state is an inline check, not a toast.
- **Cursor replacement** only for portfolios and studios, and only under `(hover: hover) and (pointer: fine)`.
- **Gate ambient motion** (pointer parallax, marquees) on fine pointers, visibility (IntersectionObserver plus `visibilitychange`) and reduced motion. Duplicated marquee tracks are `aria-hidden` and `tabindex=-1`. Marquees are slow (24-76s per loop).
- **A visible "Pause animations" control** that remembers the choice, in addition to the system setting, for any site with ambient motion (Doctronic).

## Page transitions

- Linear, Vercel, Paco, Cursor, Framer, Anthropic, Cosmos, Are.na and Locomotive ship `view-transition` CSS. Cross-document view transitions are the standard way to make a multi-page site feel like an app.
- `@view-transition { navigation: auto; }` on every page; `view-transition-name: site-header` on the persistent header so it does not flicker; the same `view-transition-name` (set inline per item) on a card's image and the destination hero so the image morphs into place; root crossfade 200-250ms; under reduced motion `::view-transition-group(*) { animation: none; }`.
- Loaders and intros: under 1s, skippable, never on repeat visits (a `sessionStorage` flag).

## Motion numbers per site

| Site | Most common | Next | Easings in CSS |
|---|---|---|---|
| Linear | 0.1s `cubic-bezier(.25,.46,.45,.94)` (233 nodes) | 0.16s same; 0.7s `(.32,.72,0,1)` for reveals | `(.32,.72,0,1)`, `(.66,0,0,1)` |
| Vercel | 0.1s `(.4,0,.2,1)` | 0.15s | `(.16,1,.3,1)`, `(.2,0,0,1)` |
| Stripe | 0.3s | 0.8s `(.165,.84,.44,1)` | |
| Apple | 0.32s `(.4,0,.6,1)` | 0.24s ease | |
| Raycast | 0.4s `(.23,1,.32,1)` | 0.3s ease | `(.16,1,.3,1)` |
| Cursor | 0.15s `(.4,0,.2,1)` | 0.6s ease | |
| Dia | mostly 0.15 / 0.2 / 0.25s `(.4,0,.2,1)` | expressive curves only for section reveals | |
| Family | 0.2s ease-out | 1s `(.19,1,.22,1)` for entrances | |
| Bulletproof | 0.8s `(.19,1,.22,1)` | 0.2s | |
| PSP | 0.65s `(.16,1,.3,1)` | 0.36s `(.22,1,.36,1)` | |
| Godly | 0.12s `(.2,0,0,1)` | 0.18s | `(.65,0,.35,1)`, `(.16,1,.3,1)` |
| Emil Kowalski's homepage | no transitions at all | | |

House rules that fall out:
- **Two speeds.** Feedback (hover, press, toggle) 100-200ms with a UI ease (`(.4,0,.2,1)` or `(.2,0,0,1)`). Storytelling (entrances, reveals, page swaps) 400-800ms with a strong expo-out (`(.16,1,.3,1)`, `(.19,1,.22,1)`, `(.22,1,.36,1)`). Product sites sit at the fast end; studios and brands at the long end.
- **No ease-in for anything the user triggered.** Ease-in exists only for exits.
- **Springs overshoot only on playful brands** (`(.07,.7,.35,1.35)`, `(.175,.885,.12,1.775)`). Never on finance or tools.
- **The site uses the product's own micro-timings** where there is a product.
- **Write motion briefs as specs**: what moves, from where, duration, easing, trigger.

## The build stack: reach for the lowest rung

| Effect | Lowest rung | Escalate to |
|---|---|---|
| Hover, press, focus | CSS `transition` on named properties, 100-200ms | nothing |
| Page-to-page fade or morph | `@view-transition { navigation: auto; }` plus `view-transition-name` on shared elements | `document.startViewTransition()` in an SPA, or router hooks |
| Reveal on scroll, progress bars, explanatory parallax | `animation-timeline: view()` with `animation-range: entry 0% cover 30%`, inside `@supports` and `prefers-reduced-motion: no-preference` | GSAP ScrollTrigger for pinning, scrubbing and multi-element choreography |
| Pinned chapter | `position: sticky` and a tall wrapper, inner state from `view()` | ScrollTrigger `pin: true, scrub: 0.5-1` |
| Smooth wheel inertia | nothing; native scroll | Lenis, only on story-first sites |
| Popover, dialog, menu enter and exit | `@starting-style` plus `transition-behavior: allow-discrete` | Motion `AnimatePresence` |
| Height `auto` (accordion, FAQ) | `interpolate-size: allow-keywords` (Chrome) or the `grid-template-rows: 0fr → 1fr` trick | Motion `layout` |
| Tooltip or popover anchored to a trigger | CSS anchor positioning | Floating UI |
| Living numbers | `requestAnimationFrame` writing `textContent`, `tabular-nums` | |
| Hero object or brand moment in 3D | a pre-rendered video or image sequence | Three.js / R3F / OGL or a shader; one canvas per page, paused off-screen |
| Text effects (split lines, words) | CSS on spans wrapped at build time | GSAP SplitText |

Browser support (MDN browser-compat-data 8.1.9, November 2026): cross-document `@view-transition` Chrome 126, Safari 18.2, Firefox preview only; same-document `startViewTransition` Chrome 111, Safari 18, Firefox 144; `animation-timeline` Chrome 115, Safari 26, Firefox 159; `@starting-style` all three; `interpolate-size` Chrome only; anchor positioning all three; `text-wrap: balance` all three, `pretty` Chrome and Safari; `oklch()`, container queries and `:has()` all three. Every one is progressive enhancement: without support the state changes instantly, which is acceptable.

```css
/* page transitions between same-origin pages */
@view-transition { navigation: auto; }
::view-transition-old(root), ::view-transition-new(root) { animation-duration: 220ms; animation-timing-function: cubic-bezier(.2,0,0,1); }
.site-logo { view-transition-name: logo; }

/* scroll reveal that never hides content when unsupported */
@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .reveal { animation: rise linear both; animation-timeline: view(); animation-range: entry 0% cover 25%; }
    @keyframes rise { from { opacity: 0; translate: 0 16px; } }
  }
}

:root { --ease-out: cubic-bezier(.22,1,.36,1); --ease-ui: cubic-bezier(.2,0,0,1); }
```
