# Category playbooks

The same laws apply everywhere, but each category has a different center of gravity: the one question users judge the product on. Get that right first; the rest is craft. Find the product's category, read its chapter, and give the richest components to its question.

| Category | Users judge it on | The richest components go to | Restraint goes to | Chapter |
|---|---|---|---|---|
| Chat assistants and answer engines | Can I trust and use the answer, and steer the next one? | Reading typography, provenance (citation chips, source panes), follow-ups, the composer | Chrome, bubbles, decoration | [chat-and-answer-engines.md](chat-and-answer-engines.md) |
| Coding agents | What did it change, and can I undo it? | Diffs or previews, +/− counts, the review queue, checkpoints and versions | Chat chrome; the transcript is a log | [coding-agents.md](coding-agents.md) |
| Productivity and notes (AI inside a tool people own) | Is my work still mine, and is it faster? | Inline proposal UI, attribution, keyboard verbs, row anatomy | AI branding; AI must not take over the tool | [productivity-and-notes.md](productivity-and-notes.md) |
| Creative tools | Is it beautiful, and can I steer it? | The canvas or grid, iteration verbs, parameter controls, forming previews | UI colour; images own all colour | [creative-tools.md](creative-tools.md) |
| AI browsers and agents on other people's pages | Do I know what it sees, what it will do, and how to stop it? | Context chips, routing, agent control, the handoff vocabulary, stop on the page | Anything over the page itself | [ai-browsers.md](ai-browsers.md) |
| Mobile AI apps | Can I read, approve and steer with one thumb? | The fixed bottom slot, sheets, voice, system entry points | Authoring on a small screen | [mobile-ai-apps.md](mobile-ai-apps.md) |
| Health | Am I okay, and what should I do next? | Reassurance, verbal likelihoods, evidence in the user's words, own-baseline comparison, safety stops | Red, alarm, false precision | [health.md](health.md) |
| Finance | Can I trust this number, and what does it mean for my money? | Number state and freshness, arithmetic shown, direction encoded twice, computed (not generated) maths | Motion on live data; persona inside numbers | [finance.md](finance.md) |
| Shopping | Does it honour my constraints, and is it safe with my money? | Visual result grids, relative refinement, review evidence, the checkout contract | Prose; urgency surfaces | [shopping.md](shopping.md) |
| Internal operations dashboards | What needs me, and is the system working? | The needs-you queue, decision cards, agent state, the audit feed, freshness | Charts and tiles that drive no decision | [internal-ops-dashboards.md](internal-ops-dashboards.md) |

## Emotional register by field

The same component carries different emotions in different fields. Pick the register deliberately.

| Dimension | Chat and browsers | Health | Finance | Shopping | Ops dashboard |
|---|---|---|---|---|---|
| First job of the UI | Get out of the way; make context visible | Lower anxiety, then help | Make every number trustworthy | Show options visually, narrow fast | Show what changed and what needs me |
| Colour | Neutral chrome, one hue for "AI acting" | No red; warm neutrals; one action blue; identity hues per metric | Muted green and red with arrows; mostly ink | Fashion: black plus one accent. Value retail: red urgency | Neutral, one accent, muted status pills; red only for real failure |
| Density | Narrow side panel, 13-15px | Low; one thing at a time | High; tables with arithmetic | Medium; image grid | High but quiet; 13-14px, 32px rows |
| Motion | Fast (140-220ms); a signature per agent state | Gentle; 300ms sheets; a pause control | Almost none; batched silent updates; one live marker | Delight allowed: hover slideshows, ambient glow | Fast and minimal; nothing on live data |
| AI prose | Full answers, compressed headings | Validating, verbal likelihoods | Serif narrative around live widgets; computed numbers | At most two sentences above the grid | Short summaries with entity chips, regenerated visibly |
| Evidence | Context chips, sources | "Fits / doesn't fit what you described"; own baseline | Source count, trust tiers, "as of" | Review counts and quotes | Every AI claim linked to its source record |
| Agent commits | Purchases and sends need an OK; handoff labels | Nothing written to the record without approval | Read-only linking stated at the click | Single-use, 30-minute, change-voided approval | Drafts as approval cards; campaigns as agent runs with pause |
| Voice | Plain, verb-first | Warm, non-alarming | Wire-service neutral; persona only in nudges | Editorial, a little playful | Plain, terse, no greetings |

## Choosing between theses inside a category

Each chapter lists the studied products' theses with "choose this when". For chat, the short version:
- **ChatGPT pattern** (system font, one blue accent, pill composer, inline blocks, soft gating): mass-market tools with short interactions, a free tier and a broad international audience.
- **Claude pattern** (a prose serif, warm neutrals, a card composer with cost controls at Send, side-panel deliverables, a collapsed process ledger): professional work tools whose outputs are documents, code or analyses.
- **Perplexity pattern** (serif article answers, source chips and panes, scoped composers on every page): any product whose value is trustworthy information.

An internal work tool usually mixes them: Claude's ledger and side-panel deliverables, Perplexity's provenance chips, ChatGPT's single-accent restraint, and Linear's density and keyboard model (see [productivity-and-notes.md](productivity-and-notes.md)).
