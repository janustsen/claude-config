# What separates Perplexity, Granola, ChatGPT, Claude, Linear and T3 Code from AI-slop UI

Evidence: screenshots of the live products (Perplexity answer, ChatGPT finished answer, Claude shared chat, Linear inbox, Granola notes, T3 Code approval) and an agent-inbox sample generated from an earlier version of these skills.

The short version: the good apps say each thing once, and say most things without words. Slop labels everything it shows, shows everything it knows, and boxes each piece separately.

## 1. Text economy (the lead difference)

**Method.** Hand count of visible words on one 1440px screen that are not the user's content (not the answer, the draft, the note or the item titles). Counted: labels, metadata, status words, helper copy, section headers, button text, placeholders. Each number or timestamp counts as one word. Logged-out promos (Perplexity's "Hire your first teammate", ChatGPT's "Get responses tailored to you") are excluded because they are sign-up marketing, not the product's design. Counts are ±10%.

| Screen | Work area (lane + any rail) | Sidebar / list | Facts said twice or more |
|---|---|---|---|
| ChatGPT, finished answer | 2 ("Ask ChatGPT"); copy and share are bare icons | 9 nav items | 0 |
| Granola note | 3-5 (a date chip, an attendee chip, "Add to folder") | n/a | 0 |
| Linear inbox | 3 ("Inbox", "Priority 4", "Other 12"); each row is title + one human sentence + age | 0 labels per row | 0 |
| T3 Code, approval | about 12 ("Working for 3m 44s", "Running node", "Waiting for approval · Decline Approve More", model, "Supervised") | 1 state word per needs-you row | 0 |
| Perplexity, finished answer | about 15 (3 tabs, Share, "Finished 2s", "Sources 10", 5 host chips, placeholder, 3 composer pills) | 12 nav items | 0 |
| Claude, shared chat | one receipt line per tool step ("Ran 3 commands, created a file"), nothing else | n/a | 0 |
| **Generated agent inbox** | **64** | **36** | **8** |

What the 64 + 36 + 10 (top bar) = **110** words were, and what each one already duplicates:

| Old string | Words | Why it is slop |
|---|---|---|
| Top bar "Ferrowell / Inbox / Follow-up to Mira Okafor" | 7 | The title is the third copy on screen (row, H1, crumb). "Inbox" names the only view there is. |
| "Live · checked 12:12" | 3 | Nobody wondered. Freshness only matters when it is stale, so show it only then. |
| "Since yesterday 17:40: 4 need you, 11 done, 1 failed" | 10 | Restates the badge (4), the shelf ("Done 11") and the red row (1 failed) that sit right below it. |
| Row line 2 "Approval · Quill · Halden Freight" ×4 | 14 | The section header already says these need you; the mail icon already says draft; the agent name is not a decision input; the client is in the title or the summary. |
| Detail header "Approval · Quill drafted this for you · Halden Freight · 4m ago" | 10 | Every token is already on the selected row 400px to the left. "Drafted this for you" is narration: the Send button and the draft itself say it. |
| "To" / "Subject" labels and the full address | 3 | Position says which line is the subject. The recipient is a person: an avatar chip with a name, the address on hover. |
| "Check before sending." | 3 | The amber highlight and the warning icon already say "check". The sentence after it carries the information. |
| "From sam@ferrowell.example · 1 recipient · 5s to undo after sending" | 10 | The sender is the default (defaults are invisible). "1 recipient" restates the button "Send to Mira Okafor". The undo appears when it exists. |
| "Worked for 1m 48s ›" | 4 | Keep. This is the one receipt the good apps all show. |
| Rail "Based on · 3" + three source cards with kind, metadata and quote | 28 | "Based on" labels what a source list obviously is; "3" counts three visible cards; "Stage: Pilot proposal · Owner: Sam Achebe" is unused metadata. Perplexity does the same job with one "Sources 10" pill and host-named chips in the sentence. |

**Targets** (product-ui rule zero):
- Reading lane: **≤ 15 non-content words** (Perplexity's level), excluding the primary action.
- Whole screen: **≤ 40** including navigation.
- List row: title, one content line, one right-aligned token (age or a state icon). **Zero label words** when the row sits under a section header that already names its state.
- **Zero facts said twice.** Selecting a row must not produce a header that repeats the row.

## 2. Show, don't label: how each reference carries information without words

| Information | Good app, and how | Slop | Test |
|---|---|---|---|
| Item state | Linear: an icon on the right of the row (empty circle, half circle, green check), an unread dot before the title. T3: one state word only on needs-you rows. | "Approval", "Input", "Failed" spelled on every row and again as a pill in the header. | Under a section header, a row carries no state word; state is the section, the icon, or the colour. |
| Kind of item and who it is from | Linear: a small glyph badge on the avatar (assign arrow, quote mark, @). | "Quill · Halden Freight" as text. | Kind is an icon; people and companies are avatars or logos. |
| AI vs human text | Granola: AI text in grey, the user's own words in black ink. No "AI-generated" label. | "Quill drafted this for you", "AI summary" headings. | Authorship is ink colour, typeface or position, not a sentence. |
| Sources | Perplexity: a host-named chip after the sentence ("jpl.nasa"), one "Sources 10" pill with a favicon stack that opens a pane on demand. | Numbered superscripts plus a permanent rail of bordered cards with kind, title, metadata and quote. | Sources fold into one pill or inline chips; a rail is opened, not permanent. |
| Metadata | Granola: two outlined chips with icons ("Today 10:30", an avatar + "Jack"). | A middle-dot string of five facts. | At most two metadata chips under a title, each with an icon; no middle-dot meta strings. |
| Actions | ChatGPT: copy and share as bare icons under the answer. T3: "Decline Approve More" as plain text buttons on the row they affect. | Labelled outline buttons plus a helper line under them. | Secondary actions are icons or plain text; only the primary is filled. |
| Progress | Claude and T3: "Ran 3 commands, created a file", "Working for 3m 44s". | Progress plus a "Started by you at 14:03 · read-only, Scout does not contact anyone" caption. | One line of status; scope or permission copy only where the user grants it. |
| Counts | Linear: "Priority 4" on the tab itself. T3: "Settled 100" on the shelf. | The same counts again in a summary sentence above. | Each count appears once, on the thing it counts. |

## 3. Chrome: boxes, borders, cards

| Screen | Bordered or filled containers in the reading area |
|---|---|
| ChatGPT answer | 2 (user bubble, composer) |
| Perplexity answer | 3 (user bubble, Sources pill, composer); citation chips are 7% fills |
| Granola note | 0 around content; 2-3 hairline chips |
| Old sample | 10 (doc card, its header divider, caveat box, outline Edit button, receipt divider, three source cards, selected-row outline, plus the sidebar and top-bar rules) |

Good apps put content straight on the page. The AI's answer is never in a card; only the human's turn or an input is boxed. **Test: ≤ 3 bordered or filled containers in the reading lane; no card inside a card; no divider between two things already separated by space.**

## 4. One loud thing, real scale contrast

- Granola: the note title is a serif at about 2.2× body size, then the chips, then content. Nothing else is loud.
- Perplexity and Claude: the answer prose is the largest, darkest block on screen; chrome is 13-14px grey.
- Old sample: a 19px title over 14px UI (1.36×), a pill, a saturated blue button, an amber box and three cards all compete for second place.

**Test: blur the screenshot; the content reads first and the primary action second, nothing else. A detail title is at least 1.6× body size, or the content itself is the headline.**

## 5. Colour of the primary action

ChatGPT ("Log in") and Perplexity ("Sign in", Share) use near-black ink buttons; Granola uses its own olive. T3 uses ink text buttons for Approve. The old sample used a stock indigo-blue filled button with a keycap inside it. **Test: the primary button is ink or a brand-specific hue chosen in the brief; framework blue (hue 255-270, high chroma) only if it is the brand. No keycap inside a filled button; shortcuts belong in the tooltip and ⌘K.**

## 6. Columns

Perplexity: sidebar plus one centred lane; sources open as a pane on demand. ChatGPT: two columns. Granola: one. The old sample keeps three permanently filled columns at 1440. **Test: at most two persistent columns; a third opens on demand and closes.**

## 7. Whitespace and rhythm

Granola leaves 80-120px around its document column and 24-32px between blocks; Perplexity keeps a 680-700px lane with 24px between paragraphs. The old sample packs 12px gaps between unlike blocks (draft, caveat, buttons, helper, divider, receipt). **Test: gaps between unlike blocks are at least 24px and come from one scale; the lane is 640-720px.**

## 8. Typeface with a purpose

Perplexity and Claude: serif means "the AI's prose". Granola: serif means "document title". The old sample used the serif for the draft, the source quotes and the question text, so it means nothing. **Test: each typeface has one role nameable in a word.**

## 9. Decoration is not slop

The good apps are not bare: Linear has avatars with glyph badges, Granola has photo backgrounds and avatar chips, Perplexity has favicon stacks and a logo mark, T3 has coloured project badges. These carry identity at a glance and replace words. **Rule: delete words and boxes, keep icons, avatars, favicons and imagery.** A screen stripped of text should get more pictorial, not more empty.

## 10. The one-line summary for the skills

Cut words; show, don't label. Every non-content word must answer a question the user would otherwise ask, and must not already be visible somewhere else on the screen. State, kind, authorship and source go into position, icon, colour and avatar. Boxes only around inputs and the human's own turn. One loud thing.

## How these rules were tested

Fresh agents rebuilt real screens from content-only briefs using only these skills; the builds were measured (OCR word counts, text sizes, boxes, hues, whitespace) and judged blind against the real screens by a model from another family, with brand marks masked.

| Set | Build judged better than the real screen | Non-content words, build vs real (median) |
|---|---|---|
| 9 tuning screens from 6 apps | 6 of 9 | 1.0x (max 1.25x) |
| 5 held-out screens from 3 apps never seen while tuning, full brief, two builds each | 8 of 10 | 0.9-1.05x (max 1.17x) |
| Same screens from a casual one-line request | 5 of 5 | 0.3x |
| Same screens from a one-line request with no domain detail | 5 of 5 | 1.0x |

The judge agreed with a human designer on 2 of 6 calibration pairs and tended to pick a side where the human called it even, so treat the judge as a tiebreaker after the word counts, not as proof. Giving the builder example screenshots on top of the skill did worse (3 of 5) than the skill alone (4 of 5).
