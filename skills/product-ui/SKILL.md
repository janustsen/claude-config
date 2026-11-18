---
name: product-ui
description: Design or build an application interface (web or desktop app, dashboard, internal tool, agent or AI product screen) so it feels clean and intuitive on the first try. Gives the decision order, measured defaults for layout, type, colour, radius, motion and keyboard (from T3 Code, Linear, ChatGPT, Claude, Perplexity, Cursor, Notion and others), playbooks for ten product categories, and a review checklist. Use when starting a new app screen or shell, redesigning one, deciding where buttons, menus, panels and states go, or reviewing an app UI for intuitiveness. For marketing or personal websites use website-design. For AI surfaces (composer, streaming, approvals, citations, agent status) also load ai-interaction-patterns. For component-level polish use the emil-* skills.
license: MIT
---

# Product UI

Build app interfaces that feel obvious. The method comes from a teardown of T3 Code (live app plus source) and case studies of twenty AI-forward products, measured from their running CSS. It is written as decisions to make in order, with defaults for every decision nobody makes on purpose.

## The thesis

The screen is a reading lane with tools at the edges. The user's work (their document, thread, record or the agent's output) is the most important thing on screen, and the human's attention is the scarce resource. Every element passes four tests:

1. **Is it needed right now?** If not, fold it, hide it behind hover, or move it to a sidecar.
2. **Does it differ from the default?** If not, hide it.
3. **Is this where the decision is made?** If not, move it there.
4. **Does it need a human?** If yes, make it loud and pull it to the top. If not, let it recede.

A product built this way feels calm while doing a lot. That calm is the product.

## Decision order

Write each decision down (a line or two) before writing code. Skipping one is how a screen ends up generic.

1. **Category and center of gravity.** Find the product's category in [references/categories/README.md](references/categories/README.md) and read its chapter. Each category is judged on one question (chat: can I trust the answer; coding: what changed and can I undo it; notes: is my work still mine; creative: is it beautiful and steerable; ops: what needs me and is the system working). The richest components go to that question.
2. **Scarce resource and core loop.** Name what the user runs out of (attention, time, money, trust) and the loop they repeat (T3: prompt, watch, review, settle). Everything serves the loop. Write a one-sentence design thesis.
3. **Shell.** Lay out zones from [references/shell-and-navigation.md](references/shell-and-navigation.md): an attention-sorted list on the left, one item in a centered reading lane with its primary input, on-demand tools on the right, settings and analytics as sheets over the work. Land the user on the primary input, never a dashboard of tiles.
4. **Objects and their state vocabulary.** One noun per concept. Give each object a closed set of one-word states with an icon and a semantic colour (Working, Needs you, Failed, Done). Every lifecycle verb gets its inverse (pin/unpin, settle/un-settle, snooze/wake).
5. **Control placement.** Put each control where its decision is made: settings for the next action on the input that sends it, context choices in a strip under the input (removed once locked), item actions in place of the item's metadata on hover, rare global destinations in the bottom-left corner. One primary action per region, in a fixed spot, whose verb changes with state.
6. **Density by urgency.** Items that need action get a rich card. Done items become one-line rows on a collapsed shelf with a count. Background work recedes (70% opacity). Needs-you items never recede.
7. **Progressive disclosure.** Outcome first, process folded: a receipt ("Worked for 2m 13s ›"), then one sentence with counts, then typed one-line rows, then the detail. Never fold a failure.
8. **Every state, before styling.** Empty, loading, partial, error, offline, disabled, success, gated. See [references/states-copy-safety.md](references/states-copy-safety.md).
9. **Tokens.** Apply [references/constants.md](references/constants.md): one tinted ink, one paper, alpha neutrals, four text roles, one accent with one job, a radius ladder, glass only on floating layers.
10. **Motion.** Instant for frequent things, short for occasional ones, nothing looping. Values in constants.md; mechanics in `animate` and `emil-design-eng`.
11. **Keyboard.** A ⌘K palette with every action and its live shortcut, conventions borrowed from the category, chords shown in every tooltip and menu row, focus returned to the primary input.
12. **Copy.** Delete first, then word it. Sentence case, verb plus object, counts in labels, one-word statuses, consequences in destructive dialogs, fixes in errors.
13. **Review.** Run [references/review.md](references/review.md) on screenshots of the real build before calling it done.

If the product has any AI in it, load `ai-interaction-patterns` at step 4 and define every AI surface with its full state set.

## Twelve moves to carry everywhere

1. **Inbox, not tree.** Sort the main list by what needs the user, not by where things are stored. Background activity never reorders it.
2. **Controls at the point of decision.** Model, mode, permission and attach live on the input that triggers them.
3. **One accent for "act now" and "focus".** Everything else is neutral; colour carries state only. Selection is neutral alpha, never the accent.
4. **Density follows urgency.** Three-line cards for needs-you, one-line rows for done.
5. **Outcome first, process folded.** A receipt with counts on top, the trail one click away.
6. **Morph, don't multiply.** One send button carries send, stop, steer, queue and resume. A split button relabels to the object's state.
7. **Defaults are invisible.** A control appears only when its value differs from the default.
8. **Loud when it needs a human, quiet otherwise.**
9. **Instant for frequent, animated for occasional.** Menus and hovers are instant; popovers 150ms; dialogs 200ms; layout animation off.
10. **Say it in words.** "Working for 12s", not a spinner. "Run `codex login` and try again", not "Error".
11. **Keyboard is first class and taught where you act.** Shortcuts are data rendered into every tooltip, menu row and palette row.
12. **Every way in has a way out.** Reversible actions get a 5s ⌘Z undo instead of a confirm. Only irreversible ones confirm, with Cancel focused.

The full laws with their reasons and evidence are in [references/laws.md](references/laws.md).

## Defaults when nothing else decides

| Thing | Default |
|---|---|
| Sidebar | 240-260px, min 208px, nav rows 28-32px, list rows 36px |
| Reading lane | max 46rem (736px), centered; extra width goes to sidecars, never longer lines |
| Properties sidecar | 280px |
| Type | 13px chrome and meta, 14px body and controls, 15-16px reading prose (AI output), weights 500 labels and 600 titles (or variable 510/590), no bold |
| Controls | 24 / 28 / 32px buttons, 32px inputs, 28px menu rows, 44px hit areas on touch, 16px inputs on touch |
| Radius | 4 items · 6 tooltips · 8 controls and menus · 12 cards and alerts · 16 dialogs, composer, bubbles · full pills; nested = parent minus padding |
| Colour | one tinted ink and paper, text roles at about 100 / 70 / 55 / 40% ink, borders 6-10% ink, hover 4%, selected 6-9%, one accent |
| Motion | hover background instant on, 100-150ms off · press scale .97 · popover 150ms opacity + scale .98 · dialog 200ms · menus and keyboard-driven highlights instant · layout animation off · ease `cubic-bezier(.16,1,.3,1)` |
| Waits | nothing for 400ms, then a label or skeleton; explain at 15s; offer an escape at 20s |
| Undo | 5s inline notice bound to ⌘Z for every reversible action |

## Which skill does what

| Need | Skill |
|---|---|
| AI composer, streaming, work log, approvals, citations, agent states, cost meters | `ai-interaction-patterns` |
| Marketing site, landing page, portfolio | `website-design` |
| Visual hierarchy, spacing, paired right/wrong calls | `emil-design-foundations` |
| OKLCH palettes, contrast, dark mode tokens | `emil-color` |
| Type selection, scales, OpenType features | `emil-typography` |
| Shadows, borders, concentric radii, elevation | `emil-surfaces` |
| Hover, press, focus, truncation, layout shift details | `emil-ui-polish` |
| Forms, inputs, buttons, validation timing | `emil-forms-and-inputs` |
| Touch, keyboard, screen readers, reduced motion | `emil-touch-and-accessibility` |
| Component API shape (React) | `emil-component-design` |
| Building one animation; coordinating several | `animate`; `choreograph` |
| Springs, gestures, sheets, Apple-style material | `apple-design`, `gestures` |
| Phone web quirks (100vh, tap highlight, zoom) | `mobile-native` |
| Strip AI-generated visual tells | `emil-unslop-design` |
| Worst-case data stress test | `break-ui` |
| Code-level UI review against a craft bar | `emil-ui-review` |
| Library choice (toasts, command menu, drawers) | `pick-ui-library` |
| Several genuinely different variants behind a picker | `prototype` |
| Turning a user's design corrections into rules | `learn-taste` |

Where this skill and an emil-* skill disagree on a number, this skill's value comes from measurements of dense, all-day apps: press scale .97 (not .96), hover instant on and eased off (not a symmetric 150ms). Keep the emil values for marketing pages.

## Reference map

- [references/laws.md](references/laws.md): the thesis and 24 laws, each with why, evidence and anti-pattern.
- [references/constants.md](references/constants.md): every measured number (layout, type, colour, radius, elevation, motion, timing, keyboard, touch).
- [references/shell-and-navigation.md](references/shell-and-navigation.md): IA, the attention inbox, action placement, menus, command palette, keyboard map, settings, onboarding, responsive and mobile.
- [references/states-copy-safety.md](references/states-copy-safety.md): empty, loading, error and offline states; copy voice and the deletion ladder; reversibility and confirmation.
- [references/interaction-defaults.md](references/interaction-defaults.md): measured behaviour defaults (tooltips, dismissal, focus, toasts, drag, undo grouping) and AI-native primitive anatomy.
- [references/review.md](references/review.md): the ship checklist, per-screen checklists and the scored screenshot review loop.
- [references/t3-code.md](references/t3-code.md): the T3 Code teardown the thesis comes from, including what not to copy.
- [references/categories/](references/categories/README.md): ten category playbooks (chat and answer engines, coding agents, productivity and notes, creative tools, AI browsers, mobile AI apps, health, finance, shopping, internal ops dashboards).
