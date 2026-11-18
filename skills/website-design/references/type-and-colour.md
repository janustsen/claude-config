# Type and colour for websites

Measured at a 1440px viewport from computed styles (H1 or the largest text), November 2026.

## Display type, measured

| Site | Display family | Size / weight | Line height | Tracking | Body |
|---|---|---|---|---|---|
| Vercel | Geist Sans | 64 / 400 | 1.0 | -0.06em | Geist 16 |
| Linear | Inter Variable | 64 / **510** | 1.0 | -0.022em | Inter 16, Berkeley Mono for IDs |
| Stripe | Söhne var | 48 / **300** | 1.15 | -0.02em | Söhne 16 |
| Raycast | Inter | 64 / 600 | 1.1 | 0 | Inter 16 |
| Framer | GT Walsheim | 54 / 500 | 1.0 | -0.04em | Inter |
| OpenAI | OpenAI Sans | 48 / 500 | 1.16 | -0.03em | 17px body |
| Anthropic | custom serif with a sans lead-in | 41 / 400 | 1.25 | -0.01em | custom sans 16.7 |
| Mercury | arcadiaDisplay | 49 / **480** | 1.1 | 0 | arcadia 16 |
| Cursor | CursorGothic | **26** / 400 | 1.25 | -0.013em | Berkeley Mono accents |
| Granola | quadrant (slab serif) | 86 / 400 | **0.93** | -0.02em | melange 16 |
| Arc | Exposure VAR (serif) | 76 / 600 | 1.13 | -0.032em | ABC Oracle |
| Dia | Exposure VAR, plus a swash wordmark at about 400px | 38 / 500 | 1.1 | -0.04em | ABC Oracle, Favorit Mono |
| Cosmos | custom | 72 / 700 | 1.0 | -0.04em | same family |
| Family | custom rounded | 68 / 500 | 1.1 | -0.02em | Inter |
| PostHog | custom rounded | 36 / **800** | 1.11 | -0.025em | ui-monospace |
| Basement | Geist | 87 / 600 | **0.9** | -0.04em | Geist Mono |
| Bulletproof | Sequel Sans | 109 / 400 | **0.8** | **-0.09em** | a light italic serif for accents |
| PSP | Neue Haas Grotesk Display | 96 / 700 | 0.85 | -0.03em | |
| Santal | Helvetica | **234** / 400 | 0.87 | -0.1em | |
| Sweet Tape | Futura PT Condensed | **293** / 800 | 0.73 | 0 | Inter Tight |
| Lynn Fisher | a rough storybook face | 96 / 300 | 1.0 | 0 | a storybook serif at 19.2 |
| Apple | SF Pro Display | 28-34 / 600 | | | SF Pro Text **17** |
| Paco, Emil, Are.na | Söhne / sans / custom | **16-19** / 400-500 | 1.5-1.75 | 0 | same |

## What the table teaches

1. **One surprising weight is the brand.** Stripe 300, Vercel 400, Linear 510, Mercury 480, PostHog 800. A variable font at an unusual weight is the cheapest way to stop looking like Inter Bold. Calm or expensive: 300-400 at a large size. Tools: 500-520. Friendly: 700-800 in a rounded face.
2. **Tracking tightens as size grows.** Body 0. From 40px, -0.01 to -0.03em. From 64px, -0.02 to -0.06em. At 100px and up (poster type), -0.04 to -0.1em. Vercel's -0.06em at 64px works only because Geist's shapes are wide, so check every family at its own size.
3. **Line height drops below 1 at poster sizes.** Granola 0.93, Basement 0.9, Bulletproof 0.8, Sweet Tape 0.73. At 80px and up use 0.85-0.95 and check descenders. Add `text-box: trim-both cap alphabetic` where supported for optical alignment.
4. **Serif plus grotesk is the humane signal of 2026.** Arc and Dia (Exposure with ABC Oracle), Granola (quadrant with melange), Anthropic (serif with a sans lead-in), and sans headlines with an italic serif phrase inside ("Take the helm, *your way*"). AI companies use editorial serifs to feel thoughtful rather than robotic. Grotesk for UI, serif for display or one emphasised phrase, never on buttons or labels.
5. **Big products set small headlines.** Cursor 26px, Apple 28px, OpenAI's hero is a 32px question. When the product or object is the hero, a modest headline keeps it from competing. The loudest type can come at the end, at the decision point ("Try Cursor now." at 52-72px).
6. **Mono is for data, IDs and labels only**, at 11-13px: Berkeley Mono (Linear, Cursor), Geist Mono (Vercel, Basement), Favorit Mono for times (Dia), PragmataPro (Rive).
7. **Custom or uncommon faces dominate.** When the budget has no custom face, choose free distinctive families instead of Inter: Geist and Geist Mono; Switzer (Fontshare, 9 weights with italics; check self-hosting terms); Hedvig Letters Serif and Instrument Serif (Google Fonts); Geist Serif (regular weight, four shapes); Figtree; Bricolage Grotesque; Fraunces; Newsreader; Commit Mono or JetBrains Mono. Display-only picks: Savate, Sekuya, TASA Orbiter.
8. **Two-ink copy instead of title plus subtitle.** Stripe sets its headline continuation in muted slate. Anthropic's lead sentence is bold sans and the rest regular serif. Apple sets the first phrase of each chapter paragraph in bold black and the rest grey. Vercel darkens the key fragment ("over 20,000 companies"). One block reads at two depths, and it removes a heading-plus-subtitle pair. Pattern: `<p><strong class="ink-1">Claim.</strong> <span class="ink-2">Support…</span></p>`.
9. **A type scale with a gap.** Linear's size histogram is dense at 12/13/14/15px (product UI) and then jumps to 24/32/48/64/72px, with almost nothing between 16 and 22. Two registers ("product" and "story"), never a muddy middle.
10. **Fluid display type:** `font-size: clamp(2.5rem, 1.2rem + 4.5vw, 4.5rem)` for an H1. `text-wrap: balance` on headings, `pretty` on paragraphs.
11. **Small details:** `tabular-nums` on prices and live numbers; footnote superscripts in hero copy (Stripe "banking¹", Mercury, Apple); curly quotes and the real ellipsis; never change weight on hover; no weights below 400 for body text.

## Colour

- **Grounds are tinted, never pure grey.** Light: Cursor `#f7f7f4`, Dia `#fbfaf6`, Anthropic `#faf9f5`, Emil `#fdfdfc`, Agrumea `#fdf3eb`, PostHog `#eeefe9`, Lynn Fisher `#e4e2d7` with paper texture. Dark: Linear `#08090a`, Raycast `#07080a`, Arc `#0b0b0b`. Tint gives the page a material at no cost. Pick it from the brand's world: paper and ivory suit editorial or AI brands; a cool near-black suits developer tools.
- **One owned accent, used rarely.** Granola olive `#5b6f00`, Nothing signal yellow `#ffc700`, Stripe `#533afd`, Mercury periwinkle `#5266eb`, Are.na navy `#00075f`, Cursor orange (links only). Most primary buttons are ink, not accent. The accent goes on links, one CTA, status or a highlight. Derive it in OKLCH from the domain (moss for notes and farms, signal yellow for hardware) and check 4.5:1 for text on and in it.
- **Loud colour lives inside imagery, not in chrome.** Stripe's ribbon, Raycast's red streaks, Dia's yellow photograph, Mercury's dawn landscape are full of colour while the chrome stays monochrome. This is the cleanest way to be colourful without looking like a template.
- **Texture comes from real material:** crumpled paper (Sweet Tape), risograph and halftone swatches (Granola), paper grain (Lynn Fisher), film grain on light (Raycast), oil-painting canvas (Cursor). Not from generic noise overlays. Each texture says something about the product.
- **Text system:** primary, secondary and muted ink. Muted must still reach 4.5:1; never use light grey for the only copy of a fact.
- **Theme:** dark-first for developer tools (Linear, Raycast, Basement); light for AI and consumer (OpenAI, Anthropic, Cursor, Granola, Dia, Cosmos). Linear generates its whole palette in LCH from three inputs (base, accent, contrast); the contrast input yields high-contrast themes for free. Stripe puts its theme toggle inside its dark illustration band.
- **The site uses the product's own typefaces and tokens** (Dia's site uses the same faces as its in-app chat; T3 Code's site reuses the app's accent, radii and true-black surfaces), so screenshots and headlines read as one object.

## Avoid

Purple-to-cyan blobs, glass cards with coloured shadows, stock robots and brains, emoji icons, glow borders on everything, gradient text. Framer's single electric-blue glowing frame is the most glow any top site used.
