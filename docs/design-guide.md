# Design guide: clean, intuitive interfaces and distinctive websites

This guide is the human-readable front of three agent skills. It explains the design thesis, how the evidence was gathered, the laws every interface should obey, how product categories differ, and where each chapter lives. The chapters themselves are the skills' reference files, so the guide and the skills never drift apart.

| Skill | Use it for | Entry point |
|---|---|---|
| `product-ui` | Any app interface: web or desktop app, dashboard, internal tool, AI product screen | [skills/product-ui/SKILL.md](../skills/product-ui/SKILL.md) |
| `ai-interaction-patterns` | The AI parts of a product: composer, streaming, work log, approvals, citations, agent status, cost | [skills/ai-interaction-patterns/SKILL.md](../skills/ai-interaction-patterns/SKILL.md) |
| `website-design` | Marketing sites, landing pages, portfolios, brand sites | [skills/website-design/SKILL.md](../skills/website-design/SKILL.md) |

They build on the craft skills that already exist (the emil-* set, apple-design, animate, choreograph, gestures, frontend-design, mobile-native, break-ui) and route to them for component-level detail instead of repeating it.

## 1. Where the evidence comes from

Four studies, run in November 2026, each written as rules with their reasons and measured values:

1. **A teardown of T3 Code**, an open-source desktop GUI for coding agents. Every screen was driven live (onboarding, the inbox sidebar, composer and pickers, a real agent turn with approvals, diff and terminal panels, the command palette, all 26 settings routes, dark mode, 1100px, 840px and 390px widths) and read alongside its source at the same tag for exact tokens, timings and shortcuts. It is the reference product because it stays calm while running ten agents at once. Case study: [t3-code.md](../skills/product-ui/references/t3-code.md).
2. **Case studies of ten AI-forward apps**: ChatGPT, Claude, Perplexity (chat and answers), Cursor and v0 (coding), Linear, Notion AI and Granola (productivity and notes), Midjourney and Krea (creative). Each was captured live where it allowed logged-out use, with design tokens pulled from the running pages by script.
3. **Studies of AI browsers, a phone app and three verticals**: Dia, Comet and Atlas; the ChatGPT iPhone app; Doctronic and Bevel (health); Perplexity Finance and Cleo (finance); Daydream and Amazon's shopping assistant (shopping). Plus a set of interaction and design resources saved from X: Beautiful UI, vercel-labs/ui, checklist.design, a clean-copy skill, heydamir/unslop, a scored screenshot review loop, font and hero posts.
4. **A website teardown of 41 live sites** at 1440x900 and 390x844: product companies (Linear, Vercel, Stripe, Cursor, OpenAI, Anthropic, Raycast, Framer, Granola, Mercury, Dia, Arc, Cosmos, Are.na, PostHog, Family, Rive), hardware and consumer brands (Apple, Teenage Engineering, Nothing), studios (Basement, Lusion, Locomotive, Active Theory), personal sites (Rauno Freiberg, Paco Coursey, Emil Kowalski, Lynn Fisher, Josh Comeau), galleries and current award winners, each measured for display type, nav, buttons, transitions and easings.

Every claim carries a provenance tag: **[obs]** observed live, **[src]** read in source, **[doc]** vendor docs, **[know]** prior knowledge not re-verified, **[inf]** inference. Rules resting only on [know] say so, so a later agent can re-check them.

## 2. Rule zero: cut words; show, don't label

What separates Perplexity, Granola, ChatGPT, Claude, Linear and T3 Code from generated UI is text economy. Their reading lanes carry 2-15 words that are not the user's content; a generated agent inbox built from an earlier version of these skills carried 64, with 8 facts shown twice. Each fact is said once, and state, kind, authorship and source are shown through position, icon, colour and avatar instead of words. Decoration (avatars, logos, favicons, imagery) stays: it replaces words. Targets: at most 15 non-content words in the reading lane, zero facts said twice, at most 3 boxed containers in the lane, at most 2 persistent columns, an ink primary button. Evidence and tests: [slop-vs-good.md](../skills/product-ui/references/slop-vs-good.md).

## 2b. The thesis

**The screen is a reading lane with tools at the edges.** The user's work (their document, record, thread, or the agent's output) is the most important thing on screen, and human attention is the scarce resource. Every element passes four tests:

1. Is it needed right now? If not, fold it, hide it behind hover, or move it to a sidecar.
2. Does it differ from the default? If not, hide it.
3. Is this where the decision is made? If not, move it there.
4. Does it need a human? If yes, make it loud and pull it to the top. If not, let it recede.
5. Is it already said, by another element, by position, by an icon or by its section? If so, delete it.

A product built this way feels calm while doing a lot, and that calm is what people mean by "clean and intuitive". For AI products one more sentence follows: **make delegation legible.** Users must see what the AI is doing, what it needs, what it changed and what it based that on, and must be able to stop, steer, correct and undo it.

For websites the thesis is different, because a site is looked at once rather than used all day: **make one strong, specific choice in each of four places (concept, art direction, a type move, a signature detail), spend loudness in exactly one place, and keep everything else neutral and fast.**

## 3. The laws, in one line each

Full text with reasons, evidence and anti-patterns: [laws.md](../skills/product-ui/references/laws.md).

**Colour, ink and type**
- **L1** Chrome recedes; colour means state. The user's content is the most colourful thing on screen.
- **L2** Every neutral is an alpha of one tinted ink; borders are 1px alpha rings inside the shadow stack.
- **L3** Four text roles; body text is never pure black or white.
- **L4** The primary output is an unboxed document; only the human's input is boxed; generated prose gets its own typographic voice.

**Attention and structure**
- **L17** "Needs me" is the top-level grouping, and the order is stable: nothing reorders on background activity.
- **L21** Controls live at the point of decision; choices that can no longer change leave the screen.
- **L22** Density follows urgency: rich cards for needs-you, one-line rows for done.
- **L23** Defaults are invisible, and one control morphs instead of multiplying.
- **L24** Every way in has a way out; undo beats confirm; only the irreversible confirms.
- **L11** New capability lives on existing objects, at three distances (cursor, object, workspace).

**Output, progress and trust**
- **L5** Progress is one live line, then a receipt ("Worked for 2m 13s ›").
- **L6** Shimmer the words, not the box; only "live" moves.
- **L7** Provenance is one gesture away from every generated claim.
- **L8** Proposals look different from accepted truth.
- **L9** Approval is proportional to rollback cost.
- **L10** Never destroy the original or the history.
- **L14** Reserve the output's space before it exists.
- **L15** Cost, limits and context are ambient meters, never surprises.
- **L16** Every blocked or failed state names the cause and the next action.

**Input and keyboard**
- **L12** One composer, a morphing primary slot, small pills for expensive choices.
- **L18** Every verb has a key; ⌘K does everything; menus and tooltips teach the keys.

**Motion and onboarding**
- **L19** Instant for frequent, short for occasional, nothing loops.
- **L13** Reach the "aha" before the wall; onboard over the real product.
- **L20** Empty states teach by being minimal: a question plus the input, or real examples that fill rather than send.

## 4. The decision order

For any app screen, write each decision down before code ([product-ui SKILL.md](../skills/product-ui/SKILL.md)):

0. Fill in what the request left out (users, the one job, realistic records, the few fields the job needs).
0. Brief first: an interview that looks up the facts, asks only the product decisions, and writes a five-part brief with no style words ([brief-interview.md](../skills/product-ui/references/brief-interview.md)). "Just build" skips to inferring it.
1. Category and center of gravity.
2. Scarce resource, core loop, one-sentence thesis.
3. Shell: attention inbox, reading lane with its input, on-demand tools, sheets over the work.
4. Objects and their closed state vocabulary; every verb with its inverse.
5. Text budget: one home per fact, the cheapest carrier first (position, icon, colour, chip, then a word).
6. Control placement at the point of decision.
7. Density by urgency.
8. Progressive disclosure: receipt, sentence with counts, typed rows, detail.
9. Every state, before styling.
10. Tokens.
11. Motion.
12. Keyboard.
13. Copy, deleting first.
14. Review on screenshots of the real build, starting with the word count.

For a website ([website-design SKILL.md](../skills/website-design/SKILL.md)): archetype, the five-line brief (concept, world, type move, loud moment, signature), tokens, first screen, nav, sections, imagery, motion, copy, mobile, the floor, the final check.

## 5. Categories differ

The same laws carry different weight per field. Each chapter gives what users expect, the competing theses and when to choose each, a comparison table, 30-odd category rules, measured constants, anti-patterns and a steal list.

| Category | Users judge it on | Chapter |
|---|---|---|
| Chat assistants and answer engines | Can I trust and use the answer, and steer the next one? | [chat-and-answer-engines.md](../skills/product-ui/references/categories/chat-and-answer-engines.md) |
| Coding agents | What did it change, and can I undo it? | [coding-agents.md](../skills/product-ui/references/categories/coding-agents.md) |
| Productivity and notes | Is my work still mine, and is it faster? | [productivity-and-notes.md](../skills/product-ui/references/categories/productivity-and-notes.md) |
| Creative tools | Is it beautiful, and can I steer it? | [creative-tools.md](../skills/product-ui/references/categories/creative-tools.md) |
| AI browsers and agents on pages | Do I know what it sees, what it will do, and how to stop it? | [ai-browsers.md](../skills/product-ui/references/categories/ai-browsers.md) |
| Mobile AI apps | Can I read, approve and steer with one thumb? | [mobile-ai-apps.md](../skills/product-ui/references/categories/mobile-ai-apps.md) |
| Health | Am I okay, and what should I do next? | [health.md](../skills/product-ui/references/categories/health.md) |
| Finance | Can I trust this number, and what does it mean for my money? | [finance.md](../skills/product-ui/references/categories/finance.md) |
| Shopping | Does it honour my constraints, and is it safe with my money? | [shopping.md](../skills/product-ui/references/categories/shopping.md) |
| Internal operations dashboards | What needs me, and is the system working? | [internal-ops-dashboards.md](../skills/product-ui/references/categories/internal-ops-dashboards.md) |

The index, with the emotional register per field (colour, density, motion, prose, evidence, commits, voice), is [categories/README.md](../skills/product-ui/references/categories/README.md).

## 6. Chapters

**Product UI**
1. [Laws](../skills/product-ui/references/laws.md): the thesis and 24 laws with reasons, evidence and anti-patterns.
2. [Measured constants](../skills/product-ui/references/constants.md): layout, type, colour, radius, elevation, motion, waits, controls and keyboard, with a default for each.
3. [Shell, navigation, placement and command surfaces](../skills/product-ui/references/shell-and-navigation.md): IA, the attention inbox, where every button goes and why, menus, the command palette, keyboard, settings, onboarding, responsive.
4. [States, copy and safety](../skills/product-ui/references/states-copy-safety.md): the full state set, the copy deletion ladder and voice rules, reversibility and confirmation.
5. [Interaction defaults](../skills/product-ui/references/interaction-defaults.md): tooltip timing, dismissal and focus, drag and hold thresholds, undo grouping, toasts, stick-to-bottom, press scale by size, and the anatomy of AI-native primitives.
6. [Review](../skills/product-ui/references/review.md): the ship checklist, the verification loop, the redesign pass order, per-screen checklists and the scored screenshot loop.
7. [T3 Code case study](../skills/product-ui/references/t3-code.md): the teardown the thesis comes from, its keyboard map, and what not to copy.
8. [Category playbooks](../skills/product-ui/references/categories/README.md): ten chapters.

**AI interaction**
9. [Pattern library](../skills/ai-interaction-patterns/references/patterns.md): about 60 patterns with anatomy, states, values and sources, from the morphing composer slot to single-use money approvals.
10. [Rules](../skills/ai-interaction-patterns/references/rules.md): 73 rules grouped by input, streaming, recovery, evidence, authorship, agency and trust.

**Websites**
11. [Type and colour](../skills/website-design/references/type-and-colour.md): display type measured on 22 sites, font picks, two-ink copy, grounds, accents, texture.
12. [Hero, nav, sections and footer](../skills/website-design/references/hero-nav-sections.md).
13. [Imagery, scroll, motion and the build stack](../skills/website-design/references/imagery-and-motion.md), with paste-ready CSS and browser support.
14. [Copy, mobile and the floor](../skills/website-design/references/copy-mobile-floor.md), with the verification steps for a site build.
15. [Website case studies](../skills/website-design/references/case-studies.md): one block per site.
16. [measure.js](../skills/website-design/scripts/measure.js): measure any live page's type, nav, buttons and motion in one eval.

## 7. Where the sources disagreed, and the call made

| Conflict | Resolution |
|---|---|
| Menus instant (T3 Code) vs 100-180ms pops (Linear) | Menus, selects and keyboard-driven highlights open instantly or within 100ms; anchored popovers take 150ms. Anything hit hundreds of times a day must feel instant. |
| Press scale .96 (emil-ui-polish) vs .97 (Linear, T3, emil-design-eng, apple-design) vs by size (Beautiful UI) | .97 for buttons; shrink less as elements grow (icons .94, rows .98, wide controls .99); menu triggers do not scale. |
| Symmetric 150ms hover (emil-ui-polish) vs instant-on, eased-off (Linear, Notion) | In dense app lists, instant on and 100-150ms off; symmetric 100-160ms is fine on marketing pages. |
| One sans keeps UI quiet vs a serif for AI prose | Both: one sans for all UI and data; a serif or distinct style reserved for generated narrative only, never in controls. |
| Suggestion chips in the empty state (v0, ChatGPT) vs none (T3 Code) | Returning-user tools: a question plus the input. First-run consumer and creative products: real examples that fill the input, never auto-send. |
| Morph send into stop (most chat apps) vs keep Stop separate (Cursor's orchestrator) | Morph for turns of seconds; separate fixed Stop for runs of hours. |
| Sparklines in stat cards (Beautiful UI, Perplexity) vs numbers only (unslop) | Stat cards hold label, figure and change against a named reference; add a trend only when the trend is the subject, always with a reference line. |
| Red for bad (finance) vs no red (health) | Field register: muted red for change against a reference in finance and ops; never in health; red elsewhere only for real failure. |
| A personal welcome (checklist.design) vs no greeting (unslop) | No greeting and no summary sentence: counts live on the sections they count. A since-last-visit line only on a screen with no counted sections. |
| Warm cream, near-black and mono labels are what leading sites use vs what generated pages now cluster on (frontend-design) | Use them when the brief's world calls for them, never as the default for an unchosen axis. |

## 8. Credits

Resources summarised or paraphrased: T3 Code (open source); vercel-labs/ui; Beautiful UI; checklist.design by George Hatzis (MIT); heydamir/unslop by Damir Sokolovsky (CC BY 4.0); the clean-copy skill shared by Rachel on X (paraphrased, no text copied, as its licence is not stated); Rauno Freiberg's "Invisible Details of Interaction Design" and Web Interface Guidelines; Linear's "How we redesigned the Linear UI"; MDN browser-compat-data. Measured values from public sites are facts about those sites; no product's assets are included.
