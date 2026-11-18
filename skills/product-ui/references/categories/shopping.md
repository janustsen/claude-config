# AI shopping

AI shopping products help people find, compare and buy physical goods by describing what they want ("a coat for NYC winters under $400") instead of filtering a catalog, and increasingly let an agent watch prices or check out for them. The center of gravity is one question: can I trust what it shows me and what it does with my money? Shoppers judge on whether results honor their constraints, whether every price, seller and claim is checkable, and whether delegated purchases stay inside limits they set.

Studied:
- Daydream (daydream.ing, AI-native fashion discovery): chat, refinement, visual search, product pages, browse and filters driven live logged out on desktop and 390px mobile [obs]. App-only features (Stylist, My Tasks, Try It On, Buy for me cart) from the App Store listing and Terms of Service [doc].
- Amazon Alexa for Shopping (AI layered into the scale store; Rufus was folded into it in May 2026): the "Customers say" AI review summary observed live on a product page [obs]. The assistant panel, price history, compare, Auto Buy and Buy for Me need sign-in and come from Amazon's articles, help pages and App Store screenshots [doc].
- Google AI Mode agentic checkout appears only as a reference point in the checkout contract (homepage entry [obs], results captcha-walled, rules [doc]).

Tags: [obs] observed live, [doc] vendor docs, App Store or ToS, [inf] inference from observation. Pattern IDs (A1-A24 Daydream, B1-B11 Amazon) are kept from the source study.

## What users expect

1. Visual comparison over prose. The answer is a grid of images with prices; AI prose is one or two sentences of trade-off, because shoppers decide by looking, not reading.
2. Relative refinement. "Like this but cheaper, longer, in camel" beats specifying attributes, so the anchor product must stay visible in the turn.
3. Seller and money on every action. Who sells it, the total, shipping and returns are trust-critical in a way chat apps have no analogue for.
4. Constraints that accumulate and are honored or openly relaxed. A silently dropped budget is a betrayal; a stated relaxation is fine.
5. Time-based agency. Price watches, restock alerts and auto-buy are core shopping jobs, so users need a list of what the agent is watching for them.
6. Evidence from other people, not the model. Aggregated reviews with counts and verbatim quotes beat the AI's own opinion.
7. Taste and fit memory (sizes, brands, budget, style) that is inspectable and editable, because it matters more than conversational memory.
8. A register that matches the category. Fashion discovery is leisure, so editorial type and ambient motion are welcome; value stores signal urgency. The same discount is shown differently per brand promise.

## The theses to choose from

### Daydream: the chat is the store

Core bet: the conversation is the primary surface and the product grid is the AI's answer format; every card carries AI actions.

Signature moves:
- One docked composer on every page, including classic browse; results render as the same product cards the catalog uses [obs].
- Every answer is one sentence naming the trade-off it noticed, a two-option question, and 5-8 attribute chips extracted from this result set [obs].
- Item-anchored refinement: "✦ more like this" and "✦ lower $" presets plus a free-text "Change something specific?", with the anchor product rendered inside the user's turn [obs].
- Outbound buy names merchant and amount ("Buy on Nordstrom · $233.16 ↗") and carries the chosen color and size to the retailer [obs].
- One indigo accent, lab(29 45 -83), reserved for the ✦ AI glyph and money signals; AI prose set in the editorial serif (Plantin 18px/28px) [obs].
- App agent layer: "My tasks" (Watching / Done / Try asking) and "Buy for me" with a single-use, 30-minute approval that any total change voids [doc].

Choose this when you are AI-native, the catalog is aggregated from many merchants, and shoppers arrive with fuzzy, occasion-shaped intent.

### Amazon Alexa for Shopping: AI as a layer on the store

Core bet: users already type into search and already hesitate at reviews, price and alternatives, so the AI lives in those places instead of replacing the grid.

Signature moves:
- One search box for keywords and questions ("Search or ask a question"), with intent routed server-side; a dedicated AI tab is secondary (5th slot in the mobile bottom nav) [doc].
- AI at decision points: "Customers say" review summary, 30/90/365-day price history, "Compare with Similar", "Why you might like this" [doc, summary obs].
- The review summary is checkable: provenance line, aspect chips with polarity glyph and mention counts, drill-down to positive/negative split and verbatim quotes with the matched phrase bolded [obs].
- Standing rules in one sentence: "Buy these headphones when they're 30% off", "Set a price alert for when this face cream is $75" [doc].
- Buy for Me confirms on Amazon's own checkout page and allows up to $15 of price drift before asking again [doc].

Choose this when you already have a store and traffic, users know your search box, and the AI's job is to remove hesitation at known decision points.

## Comparison

| Dimension | Daydream | Amazon Alexa for Shopping |
|---|---|---|
| Where the AI lives | Primary surface; composer docked on every page [obs] | Inside existing search box, product pages, one nav tab [doc] |
| Answer format | Product grid (28 cards) under ≤2 sentences [obs] | AI overview above standard results; summaries inside PDP sections [doc] |
| Refinement | Attribute chips, "more like this / lower $", free text [obs] | Chat follow-ups, compare multi-select [doc] |
| Evidence for claims | Merchant named; no price freshness [obs] | Provenance line, aspect counts, verbatim quotes [obs] |
| Streaming | None: status line, then whole result set at ~7-8s [obs] | Not observed |
| Stop / retry | None [obs] | Not observed |
| Visual search | Crop step, per-garment category rows [obs] | Lens: best match card, one AI fact, question chips [doc] |
| Memory | Implicit from searches and saves; profile asked after first result [obs] | Remembers preferences, purchases, conversations; inspect by asking [doc] |
| Background agents | My tasks: Watching / Done [doc] | Price alerts, Auto Buy, Scheduled Actions [doc] |
| Agentic checkout | Buy for me, multi-store, ≤30 min approval [doc] | Buy for Me single item, +$15 tolerance; Auto Buy at target [doc] |
| Discount styling | Bold black price, strikethrough, indigo "% off" [obs] | Red "-17%" 24px/300, strikethrough list price [obs] |
| Sponsored disclosure | "PROMO" badge unexplained; affiliate not stated [obs] | Grey "Sponsored ⓘ" on ad modules [obs] |
| Logged-out access | Full chat and refinement [obs] | No assistant; review summary visible [obs] |

## Category rules

### Layout and information architecture

1. Put the AI input on every surface as a docked element, including classic browse pages, and render AI answers in the same card and grid components the catalog uses, because shoppers alternate between knowing and not knowing and should never switch modes to ask. (A1, Daydream [obs])
2. If you already have a store, accept questions in the existing search box and route them server-side; add a dedicated AI entry only as a secondary path, because users already know where to type. (B1, Amazon [doc])
3. Embed AI where shoppers already hesitate (reviews, price history, alternatives) instead of asking them to open a chat to get it. (B2, Amazon [doc])
4. Call conversation history "searches", name each entry after the intent (AI-written, Title Case, 2-4 words), and group by day, because shoppers treat sessions as disposable and re-findable, not as a messaging thread. (A2, Daydream [obs])
5. When an input contains several objects (an outfit photo), split results into one labeled row per detected object, because one merged ranking mixes coats with sweaters. (A12, Daydream [obs])

### Product cards and pages

6. Order card content by decision weight (image 4:5, then brand in serif 15px/500, then one-line title with price right-aligned at 13px), keep every text row to one line, and badge variants as "+N" on the image, because aligned rows scan and variants should not explode the grid. (A11, Daydream [obs])
7. Give the most common card action (save ♡) its own corner and put everything else in one ⋯ menu in the opposite corner, both 44x44 translucent discs (white 50%) until hover or focus, because the two never get mis-tapped and the photo stays dominant. (A4, Daydream [obs])
8. Lead the card ⋯ menu with the AI action ("✦ Shop more like this") and include negative feedback ("Suggest less"), because preference forms on the object, not on the AI's sentence. (A5, Daydream [obs])
9. Choose discount styling by category promise: red percent for value and urgency stores, strikethrough plus bold black price for premium, never both on one card, because the same discount carries a different emotional register. (B6, Amazon and Daydream [obs])
10. On an aggregator's product page, show who sells it, that merchant's shipping and returns terms, and stock per variant (struck-through swatch with screen-reader "Out of stock") next to the buy button, then show the item in context (outfit by occasion) before "similar", because the merchant fulfils and that is the trust question. (A13, Daydream [obs])

### Composer and refinement

11. Seed the input with examples that show the query shape only AI handles (occasion plus constraint plus taste: "Black tie gown for a winter wedding"), rotate them as a typewriter placeholder, and keep 4-6 one-tap chips below, because the shape teaches the grammar without a tutorial (extends L20). (A7, Daydream [obs])
12. End every result with one sentence naming the trade-off in the results, a two-option question, and 5-8 chips for the most discriminating attributes in the current set; never a generic "anything else?", because chips drawn from the actual set are always relevant. (A8, Daydream [obs])
13. Let users refine from any result ("like this, but...") with 2 presets for the most common deltas plus a free-text field, and render that turn with the anchor product visible, because relative edits are how people express taste and the anchor keeps history legible. (A9, Daydream [obs])
14. Source deterministic filters and conversational chips from one AI-normalized attribute layer (neckline, closure, length), because the two must never disagree and the layer makes facets richer than retailer feeds. (A10, Daydream [obs])
15. Show the active constraint set (budget, material, color) as visible, removable chips or a summary line, because multi-turn context drifts; Daydream's "lower $" turn silently dropped "wool". (A19, Daydream [obs])
16. For visual input, let users crop the region before searching and label the action with the realistic outcome ("Find the closest product"), because a scoped photo is a precise query and "closest" sets the right expectation. (A17, Daydream [obs])
17. After visual recognition, show the best match as an actionable card first, then one AI fact and 2-3 likely follow-up questions about that object. (B8, Amazon [doc])
18. On submit in a long thread, scroll the new user turn to the top of the viewport so the answer fills downward, because results otherwise land below the fold. (A15, Daydream [obs])

### Output and progress

19. Stream prose but batch ranked visual results; while batching show a scoped status line ("✦ Searching from 10,000+ brands…") instead of skeleton cards that will reshuffle, and offer Stop when the wait can exceed ~5s, because a half-filled grid reorders under the cursor (category form of L5). Daydream has no Stop; that is a gap. (A16, Daydream [obs])
20. Keep AI replies to a fixed shape (verdict on fit to the constraint, the trade-off noticed, a two-option question) and ≤2 sentences when results are visual, because the grid is the answer. (Daydream [obs])

### Trust and evidence

21. Label every AI summary with its source corpus in plain words ("Generated from the text of customer reviews") and end the summary with the strongest disagreement, because the mixed signal is what a buyer most needs (extends L7). (B3, Amazon [obs])
22. Break AI summaries into named facets with polarity glyph and evidence count ("↗ Quality (263)", "~ Sizing (54)"), encoding polarity in shape and aria-label, not color alone. (B4, Amazon [obs])
23. Give every AI claim a one-click drill-down: counts by polarity ("30 positive", "24 negative"), then verbatim excerpts with the matched phrase in bold and "Read more ›" to the full source, because it shifts trust from the model to the evidence. (B5, Amazon [obs])
24. Show a price-freshness cue ("Price checked 2h ago at Nordstrom") wherever a price comes from a third party, and use one price source per screen, because Daydream's own marketing shows the same item at $158 and $345. (A20, Daydream [obs + doc])
25. Explain any badge that could read as paid on hover or tap, and disclose affiliate earnings once, near the buy action, in plain words, because Daydream's "PROMO" badge is unexplained and its buy links carry affiliate parameters the button does not mention. (A21, Daydream [obs + doc])
26. Mark generated or simulated imagery with a persistent label ("✦ Try-on preview") and put the next decision (buy, save, try another size) on the same screen, because it manages fit expectations and keeps the user in the decision. (A24, Daydream [doc])

### Recovery

27. When constraints cannot be met, say which one was relaxed ("these aren't all under $15"), offer the nearest feasible value as a chip, and sort results by distance from the violated constraint, because leading with a $4,350 item after a $15 budget undercuts the honest message (see L16). (A18, Daydream [obs])
28. Any action that leaves your product names the destination and amount in its label, shows an outbound glyph (↗), and carries the user's selections (color, size) to the destination, because the wrong-variant landing is the most common handoff failure. (A6, Daydream [obs])

### Agents, memory and money

29. Give background agents a Tasks surface with status buckets (Watching / Done / Failed), a one-line current value with a "since" timestamp ("Now $640 · since today"), and example asks to seed new tasks, because invisible ongoing work is either forgotten or creepy (extends L17). (A3, Daydream [doc])
30. Let users create standing rules in one sentence, then echo the parsed rule back as a structured card (object, condition, action, payment) with Cancel before it goes live, because a sentence is fast but a misparse spends money. Amazon describes no confirmation card for Auto Buy [inf]; that is a gap. (B9, Amazon [doc])
31. Make AI memory inspectable and editable in the same channel the user talks in ("What does my order history say about me?") and advertise that prompt, because shoppers need to correct sizes, family members and dietary needs. (B11, Amazon [doc])
32. Ask for a profile or account only after the first useful result, framed as an upgrade to those results ("These results aren't personalized to your style yet"), and when onboarding state the step count and the payoff ("Two quick details before we build your feed") (extends L13). (A23, Daydream [obs])
33. Split suggested prompts into "For you" (from the user's data, with a tiny product thumbnail when the prompt refers to an item) and "New things to try" (capability discovery), because personal prompts prove value and discovery prompts teach features without a tour. (B7, Amazon [doc])
34. Follow the agentic-checkout contract below for any agent-initiated purchase (applies L9 to money).

## The agentic-checkout contract

What exactly the user confirms when an agent buys:

| | Daydream Buy for me [doc] | Amazon Buy for Me [doc] | Amazon Auto Buy [doc] | Google agentic checkout [doc] |
|---|---|---|---|---|
| Trigger | Tap "Buy for me · $345" or "Buy all · 3 items, 3 stores" | Tap "Buy for Me" on a brand-site item | Sentence: "Buy … when they're 30% off" | "Track price" with size, color, budget |
| What is confirmed | One order, displayed total or approved maximum | Address, taxes, shipping, payment on an Amazon checkout page | Target condition; default payment | Notification or email to confirm purchase, payment method, shipping address |
| Price drift | Any change voids approval; re-confirm | Auto-OK up to +$15; above that, asked again | Buys at target | Buys only if final price ≤ confirmed; otherwise no charge |
| Expiry | Unused approval expires ≤30 min | n/a | Cancel any time before the order is placed | n/a |
| Multi-merchant | Yes, per-store subtotals | Single item only | n/a | Select merchants accepting Google Pay |
| Returns | Merchant | Brand | Amazon or seller | Merchant |

Daydream's terms, which are the clearest model [doc]:
- "Starting a purchase authorizes preparing checkout… It does not authorize submission of an order."
- "When you confirm the order, you authorize Daydream and its checkout provider to place that one order."
- "An unused approval expires no later than 30 minutes after confirmation."
- "Any change to the displayed total or approved maximum cancels the earlier approval and requires a new confirmation."
- The merchant "handles shipping, returns, refunds".

Daydream's cart [doc]: lines grouped by store with per-store "Subtotal"; each line shows "Color · Size" and "Edit"; "+ Add more from Rack"; footer "Items $1,245.00 + shipping and tax"; one CTA "✦ Buy all · 3 items, 3 stores". It compares each store's total, promo codes included, and lets the user keep browsing while it checks out. Try-on ends in "✦ Buy for me · $345"; an outfit card shows "Look total $556" with "✦ Buy the look".

Amazon Buy for Me [doc]: a separate search section "Shop brand sites directly"; confirmation happens on Amazon's familiar checkout page; Amazon then submits encrypted details on the brand's site; single item only, no promo codes; orders file under "Buy for Me Orders"; the brand handles returns and support.

The contract. An agent purchase UI must state:
1. Amount and recipients in the button label ("Buy all · 3 items, 3 stores", "Buy for me · $345"), because multi-merchant means several charges and several return processes.
2. What changes void the approval (any total change, or a stated tolerance in money: "up to $15 more"), because drift is where delegated spending goes wrong.
3. How long the approval lives (single use, ≤30 minutes), because a stale approval is an open cheque.
4. Who handles returns and support, because the agent is not the fulfiller.
5. Where the resulting order will be listed (its own bucket, labeled with who fulfils), because an agent-placed order must be findable.

And it must split "prepare" from "submit": starting a purchase prepares checkout; only the explicit confirm places that one order. Confirm on your own familiar checkout UI when buying from a third party. Google's "only if the final price is the same or lower" is the simplest user-facing promise; use it as the default sentence.

## Measured constants

| Item | Value | App, tag |
|---|---|---|
| Card radius / border | 16px / 1px lab(89 0 0) (≈#e0e0e0) | Daydream [obs] |
| Card image ratio | 4:5 (0.800), object-fit cover | Daydream [obs] |
| Card brand / title / price | Plantin 15px/500 / 13px/400 one line / 13px | Daydream [obs] |
| Corner buttons | 44x44, radius 200px, white 50% + 1px white border, opacity 0.3s | Daydream [obs] |
| Card ⋯ menu | 194px wide, radius 16, padding 8; items 44px tall, radius 8, 14px/500 | Daydream [obs] |
| Grid columns | 4 at 1200px, 2 at 390px | Daydream [obs] |
| First answer | 28 cards (14 on sale, 4 PROMO), ≤2 sentences of prose | Daydream [obs] |
| Answer latency | status line at ~0.3s; full set at ~7-8s (image query ~7s) | Daydream [obs] |
| Refine modal | 360px, radius 16, padding 16; scrim blur(8px) + black 45%, 0.3s; presets 44px tall; input 16px | Daydream [obs] |
| Buy button | 480x52, radius 200px, 14px/500, black | Daydream [obs] |
| Uppercase labels | 11px/700, letter-spacing 0.88px | Daydream [obs] |
| Discount pill | 13px/700 indigo on indigo 6% alpha, radius 16, padding 4x8 | Daydream [obs] |
| H1 / AI reply / H2 | Plantin 56px/76px 500 -0.84px / 18px/28px / 24px/36px | Daydream [obs] |
| Text alphas | black 0.92 primary, 0.65 secondary, 0.55 label, 0.22 border | Daydream [obs] |
| AI and money accent | lab(29 45 -83) (≈#3b2bd0, approximate) | Daydream [obs] |
| Segmented toggle | 34px tall; 0.3s cubic-bezier(0.4,0,0.2,1), 0.1s delay | Daydream [obs] |
| Press feedback | 100ms cubic-bezier(0.4,0,0.2,1) | Daydream [obs] |
| State / appear | 300ms same curve (card shadow, image scale, results entrance) | Daydream [obs] |
| Composer expand on focus | 700ms same curve | Daydream [obs] |
| Ambient composer loops | ring 8000ms, aurora 6000ms, breathe 8000ms linear | Daydream [obs] |
| Card hover slideshow | ken-burns crossfade + progress bar, 3000ms linear each | Daydream [obs] |
| Loading line | shine 8000ms, pulse 2000ms; send becomes 1000ms spinner | Daydream [obs] |
| Typewriter placeholder | ~1 char/100ms typing, ~3 chars/100ms deleting, ~1.7s hold | Daydream [obs] |
| Filter drawer | ~448px desktop; sticky "Clear all" + "Show results" | Daydream [obs] |
| Past-searches drawer (mobile) | ~77% width, left | Daydream [obs] |
| Approval expiry | ≤30 min, single order | Daydream [doc] |
| "Customers say" heading / body | Amazon Ember 20px/700 rgb(15,17,17) / Arial 14px/20px | Amazon [obs] |
| Discount percent | Arial 24px/300, rgb(204,12,57) | Amazon [obs] |
| Price | "$" 13px raised, whole 28px, cents 13px raised; list price 12px grey strikethrough | Amazon [obs] |
| Price history windows | 30 / 90 / 365 days | Amazon [doc] |
| Buy for Me drift tolerance | +$15 over estimate | Amazon [doc] |

## Anti-patterns seen

- No Stop and no retry during a ~7-8s batched answer. Fix: a Stop that replaces the send button for the whole wait, and a retry on the result. (Daydream [obs])
- An impossible "$15 cashmere ballgown" query honestly said the budget was relaxed, then led with a $4,350 item. Fix: sort by distance from the violated constraint and lead with the relaxed chip's range. (Daydream [obs])
- A "lower $" refinement silently dropped the earlier "wool" constraint. Fix: show active constraints as removable chips on every turn. (Daydream [obs])
- No price-freshness cue on third-party prices, and the vendor's own marketing shows one item at $158 and $345. Fix: "Price checked 2h ago at <merchant>" and one price source per screen. (Daydream [obs + doc])
- "PROMO" badge with no explanation next to a "ZERO ADS" claim, and affiliate parameters on the buy link with no disclosure on the button. Fix: tap-to-explain on any paid-looking badge, one plain affiliate line near Buy. (Daydream [obs + doc])
- The image-upload button had no accessible label. Fix: label every icon-only input control. (Daydream [obs])
- Anonymous chats did not survive a browser restart; the old chat link redirected to the landing page. Fix: persist anonymous sessions locally or say up front that they are temporary. (Daydream [obs])
- The mobile chip row clips its last chip as the only scroll affordance. Acceptable, but pair it with an edge fade so the clip reads as intentional. (Daydream [obs])
- Auto Buy, as documented, has no echoed confirmation card for the parsed rule before it can spend. Fix: show object, condition, action and payment as a card with Cancel. (Amazon [doc + inf])
- No assistant at all for logged-out desktop users. Fix: let the AI answer before sign-in and gate only memory and purchasing (see L13). (Amazon [obs])

## Steal list

1. Do dock the AI composer on every page, browse included, and render answers as your native product cards, because asking must never need a mode switch.
2. Do end every answer with the trade-off noticed, a two-option question, and 5-8 chips drawn from the current result set, because it turns chat into fast faceted narrowing.
3. Do make every result an anchor for "like this, but..." with 2 presets plus free text, and show the anchor in the turn, because relative edits are how people express taste.
4. Do keep the active constraint set visible and removable, because multi-turn context drifts silently.
5. Do state which constraint was relaxed and offer the nearest feasible value as a chip, because an honest relaxation keeps trust and a silent one destroys it.
6. Do give every AI summary a provenance line, facet chips with polarity glyph and counts, and a drill-down to bolded verbatim quotes, because claims become checkable in one click.
7. Do batch ranked visual results behind a scoped status line ("Searching 10,000+ brands…") and offer Stop past ~5s, because half-filled grids reshuffle under the cursor.
8. Do name the merchant and amount on any outbound button, add ↗, and carry the chosen variant across, because wrong-size landings are the top handoff failure.
9. Do show the seller's shipping and returns terms and per-variant stock next to Buy on an aggregator, because the merchant, not you, fulfils.
10. Do follow the agentic-checkout contract: amount and recipients in the button, void on any total change (or a stated $ tolerance), single-use approval ≤30 minutes, named returns owner, own order bucket, and "prepare" separate from "submit".
11. Do give background agents a Tasks list (Watching / Done / Failed) with current value and "since", because invisible ongoing work is forgotten or creepy.
12. Do echo a one-sentence standing rule back as a structured card with Cancel before it can spend, because a misparsed trigger moves money.
13. Do make memory inspectable by asking ("what do you know about me?") and advertise that prompt, because fit and family details must be correctable.
14. Do ask for a profile only after the first useful result, framed as an upgrade to those results, because value first feels fair.
15. Do reserve one accent hue for AI-originated elements and money signals and set AI prose in its own typeface, because users learn "colored means the AI did this" in seconds.
16. Do pick discount color by category promise (red for value, bold black for premium), never both, because the same discount carries a different register.
17. Do let users crop a photo before visual search and promise the "closest product", because scope makes the query precise and the wording sets the right expectation.
18. Do label simulated imagery ("Try-on preview") persistently and put buy, save and try-another-size on the same screen, because it manages fit expectations and keeps the decision in place.
