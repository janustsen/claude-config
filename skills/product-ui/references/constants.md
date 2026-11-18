# Measured constants

Hard defaults instead of adjectives. Values were read from running CSS, computed styles, `document.getAnimations()` or shipped source. Where independent products agree, the agreement is the evidence. The **Default** column is what to use when the brief does not decide.

## Layout

| Thing | Default | Measured |
|---|---|---|
| Sidebar | 240-260px, min 208px | T3 256 (min 208); ChatGPT 260; Linear 232; Perplexity 240 (resizable 200-400, rail 56); Krea 256; unslop 240-280 |
| Top bar | 44-52px, identity left, view toggles right | T3 52 |
| Reading lane | max 46rem (736px), range 680-768 | T3 736; ChatGPT 768; Claude 720; Perplexity 720; Linear issue detail 662 |
| Properties or context pane | 280-336px | T3 details card 280; Linear rail about 280; Perplexity sources 336 |
| Command palette | 576px wide, top-anchored, radius 16 | T3 |
| Gutter | 12px, 20px on wide screens | T3 |
| Nav rows | 28-32px with 2-4px gaps | Linear 28 (2px gap) at 13/510; T3 sidebar rows 36 |
| List rows | 36-40px | Linear 40 (fixed 72px ID column); T3 36 |
| Rich "needs you" card | 3 lines, about 78px; 58px when line 3 is empty | T3 |
| Spacing base | 4px; panel insets from a 4-6 step scale between 6 and 24px | Dia insets 8/16/20, gaps 10/12/14 |
| Padding inside a 1px border | `calc(n - 1px)` so text stays on the grid | T3 |
| Desktop window minimum | 840px | T3 |
| Content cap on wide screens | 1440-1600px | unslop |

Responsive behaviour: at wide widths a side panel **splits** the main area and the reading lane narrows; secondary cards collapse into a toggle. At narrow widths the panel **overlays** and tabs gain scroll arrows. On phones, panels become full sheets and side navs become icon rails.

## Type

| Role | Default | Measured |
|---|---|---|
| UI families | system UI or one neutral sans; mono for IDs, paths, figures | T3 `-apple-system, BlinkMacSystemFont, "Inter Variable"`, mono `ui-monospace, "SF Mono"`; Linear Inter Variable + Berkeley Mono |
| Voice family (generated or authored prose) | a reading serif or distinct style, never in controls | Claude `--font-voice`; Perplexity pplxSerif; Granola serif titles; Daydream Plantin |
| Chrome and meta | 12-13px | T3 12px is the dominant size (859 uses); Linear 13 (12 meta) |
| Body and controls | 14px | T3 413 uses; ChatGPT, Claude, Perplexity 14 |
| Reading prose | 15-16px, line height 1.6-1.75 | T3 14/1.625; ChatGPT 16/26; Perplexity 16/26; Claude 15/21 |
| Counters, eyebrows | 10-11px, badges only | T3 `text-2xs` .6875rem, `text-3xs` 10px |
| Weights | 500 labels, 600 titles, no bold; or variable in-betweens 510/590 | T3 500/600; Linear 400/510/590/680; Claude 330-435; Notion 450/550/650 |
| Empty-state hero | large and light: 30/36 at 400, tracking -0.75px | T3 |
| Heading scale in answers and data views | h1 at most 1.5x body; data-page section titles at body size, weight 500 | Dia body 15, h1 22; Perplexity section titles 14/20 at 500 |
| Display tracking | grows with size: -0.01em at 17px to -0.06em at 64px | Linear -0.012 to -0.022em; v0 -0.04 to -0.06em |
| Numbers that change | `font-variant-numeric: tabular-nums` | everywhere measured |
| Truncation | middle-truncate identifiers (paths, branches), end-truncate titles | T3 |
| Composer text | 1px larger than body; 16px minimum on touch | ChatGPT 17px; T3 `max(var(--font-size-prompt,1rem),16px)` |

Dense tools (Linear, Cursor) use 13px UI. Reading products (chat, docs) use 14px UI with 15-16px reading text.

## Colour

| Role | Default | Measured |
|---|---|---|
| Canvas | tinted near-white paper, or true or near black | T3 `#fcfcfc` / `#000`; Cursor `#f7f7f4`; Linear `#08090a` |
| Raised surfaces | white in light; about `#111` in dark | T3 card `#fff`, dark `color-mix(in srgb, oklch(14.5% 0 0) 97%, #fff)` |
| Chrome vs content | a 1-2% luminance step plus a 10% hairline | Atlas chrome `#fcfcfc` on content `#fff`; T3 sidebar `#fafafa` |
| Text ladder | ink at about 100 / 75 / 60 / 45%. Measure on the real surface: the tertiary role (meta, descriptions) must reach 4.5:1, so darken it until it does; the quaternary 45% role is only for placeholders, disabled text and decorative icons | Cursor 100/92/60/50/40; Perplexity 100/75/50; T3 muted zinc-500 `#71717b` (4.70:1) |
| Borders | ink 6-10% light; white 5-8% dark | T3 zinc-200 `#e4e4e7`, dark white 8%; Linear 5-8% white |
| Hover fill | foreground at about 4% | T3 zinc-100 `#f4f4f5`, dark white 4% |
| Selected row | foreground at 6-9%, never the accent; must still reach 3:1 against neighbours via fill, outline or weight | T3; vercel-labs/ui |
| Accent | one hue, derived from the domain; on the single primary action per region, checked controls, sliders and focus | T3 `oklch(0.488 0.217 264)` light, `oklch(0.571 0.21 264)` dark |
| Primary button | often ink, not accent (near-black on light, off-white on dark) | Perplexity, Cursor, unslop dark rule |
| Button mix | about 1 filled per 6; outline about 1/3, ghost about 2/5 | T3 33% outline, 38% ghost, 17% primary |
| User bubble | soft neutral | T3 `#ebebed` / `#1e1e1e` |
| Status | a word + an icon + a semantic hue used for nothing else, never the accent (needs-you is carried by position, weight, a count badge and an attention hue such as amber, so the accent stays free for the one action and focus); status pills at about 15% alpha, fills 8% light / 16% dark | T3; Beautiful UI |
| Direction (up/down) | colour plus sign or arrow; muted mid-dark hues, alpha ladder 100 / 65 / 9 / 5.5% | Perplexity `#016B1D` / `#A23544`, dark `rgb(83,158,85)` / `rgb(220,105,115)` |
| Dark mode | true or near black, raised `#111`, white-alpha borders, not grey fills; off-white primary; inset highlight `inset 0 1px 0 rgba(255,255,255,.12)` | T3; unslop |
| Contrast | compute it: primary text 7:1, secondary 4.6:1; let users scale contrast (50-200%) | T3 theme generator |

## Radius

| Use | Default | Measured |
|---|---|---|
| Items, small chips | 4px | T3 |
| Tooltips | 6px | T3, Dia |
| Controls, inputs, menus | 8px | T3 `--control-radius: .5rem` |
| Alerts, cards | 12px | T3, Dia code blocks |
| Dialogs, composer, palette, bubbles | 16px | T3; Dia card 16, bubble 17, dialog 20 |
| Large composers | 20-32px | ChatGPT 28; Perplexity 26 frame / 20 field; Krea about 32 |
| Pills, round send button | 9999px | |
| Documents and artifacts | near-square (about 3px) so they read as paper, not controls | Dia |
| Nesting | inner = outer minus padding (T3 uses outer minus 1px for tight insets) | Perplexity 26 = 20 + 6 |

## Elevation and material

| Thing | Default | Measured |
|---|---|---|
| Glass | only on floating layers (menus, popovers, dialogs, toasts, the composer): background at 80%, `blur(12px) saturate(1.14)`; dark 16px / 1.08; user-tunable, off at 100% opacity | T3 |
| Dialog shadow | `0 24px 64px -24px rgb(0 0 0 / 65%)` | T3 |
| Popup shadow | `0 16px 40px -18px rgb(0 0 0 / 55%)` (dark 80%) | T3 |
| Composer shadow | `0 1px 2px rgb(0 0 0 / 5%)` light; `0 14px 32px -18px rgb(0 0 0 / 75%)` dark; or a three-layer stack ending in an 80px halo at 2.4% | T3; ChatGPT |
| Border as ring | `0 0 0 1px <ink 8%>` inside the shadow stack | v0, Linear |
| The lip | bordered controls: 1px bottom shadow at black 4% light, top highlight at white 6% dark; primary buttons inset top `0 1px rgb(255 255 255 / 16%)` | T3 |
| Modal backdrop | background at 60% plus `blur(4px)`: the app recedes, it does not vanish | T3 |
| Focus ring | inset: `box-shadow: 0 0 0 1px <bg> inset, 0 0 0 3px <accent> inset; outline-offset: -2px`, never clipped by scroll containers | T3 |
| Grain | 3.5% noise baked into backgrounds, not overlaid | T3 |
| Flat surfaces | a hairline and an optional lip, no drop shadow | T3, Linear (shadow tokens `none` at root) |

## Motion

One strong ease-out for the product, a short duration ladder, and exits faster than entrances.

| Element | Default | Measured |
|---|---|---|
| Menus, selects, comboboxes | instant (0ms), or a 100ms fade at most | T3 0; Linear 100-180 ease-out-quad |
| Keyboard-driven highlight (list focus, palette selection) | instant, never eased | vercel-labs/ui; Rauno |
| Hover background | instant on, 100-150ms off | Linear 0 / 150; T3 0; Notion 20-80 |
| Hover colour on marketing-grade surfaces | 100-160ms ease-out | Perplexity 75; Linear site 160 |
| Tooltip | wait 500-600ms first, then instant within a 400ms warm window; fade in 50-150ms, close at once, open instantly on keyboard focus, never on touch | ui-sdk 600 / 400; Dia 50 in / 100 out; T3 150 |
| Hover card | open after 250-300ms (provenance cards) or 600ms (rich previews); close 300ms | Perplexity about 280; ui-sdk 600 / 300 |
| Popover, anchored picker | 150ms opacity + scale .98 from the anchor, then width and height transitions as content changes | T3 |
| Pop from scale | start at .95-.98, never 0 | Perplexity .95; T3 .98 |
| Dialog, sheet, palette | 200ms `cubic-bezier(.4,0,.2,1)` opacity + scale .98; nested modals push the parent back 10% per level | T3 |
| Mobile sheet | 300ms in `cubic-bezier(.16,1,.3,1)`, 150ms out ease-in; drag-driven sheets settle with `cubic-bezier(.32,.72,0,1)` | Doctronic; vaul 500ms |
| Height morph (stepper, palette pages) | 200ms ease-out `(0,0,.2,1)`; never animate height across many rows | T3; Dia 180ms |
| Disclosure chevron | 200ms rotate | T3 |
| Press | `scale(.97)` over 100-150ms; shrink less as elements grow (icons .94, rows .98, wide controls .99); menu triggers do not scale | T3, Linear .97; Claude .975; Beautiful UI by size |
| Hover swap (time becomes an action) | 150ms opacity, content frozen first | T3 |
| Content arrival (banners, notices) | 150ms opacity via `@starting-style`; exits cut | T3 |
| Crossfade both ways | exit 100ms, enter 150ms after a 50ms delay | T3 |
| Removal | fade over the first half, then collapse height over the second | Doctronic |
| Entrance offset | 8px or less | Perplexity 5; Dia 6 |
| Toast | top-right or bottom, 5s, at most 3 visible, 500ms `cubic-bezier(.22,1,.36,1)` stack in 10% scale steps, swipeable | T3; ui-sdk |
| Copied confirmation | icon morphs Copy to Check, anchored "Copied!" for 1000ms | T3 |
| Panels (sidebar, right panel, drawer) | 0ms by default, optional 0-400ms setting with `cubic-bezier(.32,.72,0,1)` | T3 |
| Status pulse | 2s, `steps(6)` / `steps(8)`, about 40% hold, only in-progress states | T3 |
| Working shimmer | 0.65-2.4s, one synced clock, paused off-screen and when the tab is hidden | T3 2.2s `steps(30)`; Cursor 1.6s |
| Skeleton | 2.4s stepped pulse | T3 |
| Streaming text | finished blocks fading in over 600ms, or words at about 60ms each; never replay finished text | T3; Beautiful UI; ChatGPT |
| Live data | batch silent swaps every 15-60s; animate at most one hero number | Perplexity |
| Success overshoot | only for "done": `cubic-bezier(.34,1.56,.64,1)` | Dia |
| Ambient "AI is here" | 6s or longer, linear, never on content being read | Daydream |
| Spinner | rare; 1s linear; prefer a worded status | T3 about 5 uses in the whole app |

Curve families: entrances `cubic-bezier(.16,1,.3,1)` (or `.22,1,.36,1` / `.23,1,.32,1`, the same family); symmetric modals `cubic-bezier(.4,0,.2,1)`; drawers and resizes `cubic-bezier(.32,.72,0,1)`; departures that must animate `cubic-bezier(.4,0,1,1)`.

Reduced motion keeps meaning: blinks become holds, shimmer becomes static dim text, smooth scroll becomes instant, scale and slide drop to an in-place fade of 150ms or less.

## Timing and waits

| Situation | Default | Source |
|---|---|---|
| Show loading UI | after 400ms | T3 |
| Reconnect banner | after 2s grace | T3 |
| "Some requests are slow" with detail | after 15s | T3 |
| Escape hatch ("Disconnect server", "Cancel") | after 20s | T3 |
| Stop control for a batch | any batch that can exceed 5s | Daydream gap |
| Inline undo | 5s, ⌘Z | T3 |
| Arm-then-confirm for remote irreversible actions | disarms after 3s | T3 |
| Typing guard | hold incoming approval prompts while the user typed in the last 1.5s | T3 |
| Scroll-follow | stick to bottom while within 24-40px of it; any upward scroll releases; "Jump to latest" after a 150ms debounce, naming what waits below ("· 2 queued") | T3; vercel-labs/ui |
| Modifier hint | number badges after holding ⌘ 200ms | T3 |
| Hold-to-quit | ⌘Q held 1.2s or double-pressed within 500ms | T3 |
| Typeahead buffer | 500ms | ui-sdk |
| Submenu safe area | 300ms | ui-sdk |
| Drag threshold | 3px | ui-sdk |
| Long press | 500ms with 10px tolerance | ui-sdk |
| Stepper repeat | 400ms, then every 60ms | ui-sdk |
| Undo grouping | merge edits within 500ms, keep 100 steps | ui-sdk |

## Controls and touch

| Thing | Default | Measured |
|---|---|---|
| Button heights (desktop) | 24 xs / 28 sm / 32 default | T3 |
| Input height | 32px | T3, ui-sdk |
| Menu item | min 28px | T3 |
| Round primary slot in a composer | 32-44px | T3 32; ChatGPT 44 |
| Icon buttons in bars | 28px | T3 panel toggles |
| Icons | lucide-style, stroke 1.75: 16px in controls, 14 in rows, 12 in badges | T3 |
| Disabled | `opacity: .64`, with a hover reason | T3 |
| Touch hit area | at least 44px (invisible expansion is fine) | T3; ChatGPT mobile; Apple |
| Mobile composer | 48px | ChatGPT mobile web |
| Mobile primitives | build mobile-first at 16px text and 36px controls, then densify at the desktop breakpoint | T3 |

## Keyboard (borrow per surface)

| Surface resembles | Borrow |
|---|---|
| IDE | ⌘B sidebar, ⌘J terminal or drawer, ⌘P go to file, ⇧⌘F search, F6 cycle areas |
| Browser | ⌘[ ⌘] back and forward, ⌘T / ⌘W / ⇧⌘T tabs, ⌘1-9 jump |
| Chat | ⌘K palette, ⇧⌘O new chat, ↑ recall last prompt, Enter send, ⇧Enter newline |
| Mail or triage queue | J / K next and previous, Enter open, E done or archive, R reply, ⌘Enter send, H or S snooze, # delete, Z undo (Gmail, Superhuman) |
| Issue tracker | single-key verbs on the selected row (C create, A assign, S status, L label, P priority), G-chords to navigate, `?` for the sheet |
| Agent run | Esc or ⌘. stops when the input is empty; ⌘Enter queues instead of steering |

The full T3 map is in [t3-code.md](t3-code.md).
