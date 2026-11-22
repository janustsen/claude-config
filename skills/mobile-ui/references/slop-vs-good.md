# What separates the best iPhone apps from generated phone UI

Evidence: word counts from 43 case studies (firstmate `data/mobile-design-skill/evidence/cases/`), and a validation round in which the same six content-only briefs (a reminders Today list, a mail inbox, a finance dashboard, a CRM task list, a CRM people table, a flight detail over a map) were built three ways and judged blind by a different model (Codex) against each other: the real app's screen, a build from a capable model with no skill ("make a polished, modern iPhone screen"), and a build from this skill. Files: firstmate `data/mobile-design-skill/validation/`.

## 1. Text economy

Measured non-content words on the reference screens (OCR, same corpus for every version of a screen):

| Screen | Real app | No-skill build | Skill build (round 1) |
|---|---|---|---|
| Reminders Today | 2 | 6 | 3 |
| Gmail inbox | 11 | 7 | 4 |
| Copilot dashboard | 12 | 18 | 6 |
| Attio tasks | 12 | 14 | 5 |
| Attio people table | 8 | 14 | 5 |
| Flighty flight detail | 17 | 12 | 10 |

The skill's builds cut words the most, and the judge still preferred the real app on five of six: past a point, fewer words stop helping and hierarchy, rhythm and native placement decide. Counting words is the first test, not the last.

## 2. The generated signature (what the no-skill builds did, and the judge's reasons)

| Generated habit | Seen as | The real app instead |
|---|---|---|
| A count under the title ("6 reminders") | chrome that competes with the title | nothing; the list is the count |
| A + on every section header plus a big "New Reminder" pill | four competing add buttons | one + bottom-right; a dotted blank row at the end of each section |
| "Urgent", "Due today" spelled on rows | words for what colour and section already say | a red time; the section header |
| A large black button for a batch action ("Mark both as reviewed") | a secondary action pulling focus from the hero | a light tinted capsule inside the card |
| A legend under the chart ("Spent so far · Ideal pace") and a long status badge | a reading task | one tag on the line itself ("$268 under") |
| Every piece of metadata in its own pill (date, assignee, linked) | metadata as loud as titles | one quiet grey meta line with small avatars |
| A popover menu with icons, dividers and a heavy shadow for a two-option filter | an oversized control | a compact menu: two words and a checkmark |
| Spelled-out toolbar labels ("Sorted", "Filters", "+ Field") | width spent on what glyphs say | glyphs; only the active filter tinted, with its count |
| Two airport columns side by side, gate and terminal in boxed cards, facts repeated across cards | squeezed, repeated, boxed | stacked blocks: identity line, big time, one status line, a gate badge |
| Taller rows and bigger avatars than needed | fewer records per screen | 44-52pt rows, small avatars |

## 3. What the skill fixed, and what still lost

The skill builds beat the no-skill builds on all six screens (judge means 8.25 vs 7.3, confidence 4 of 5 on each): search moved to the bottom, labelled tabs, one + in the thumb zone, glyph toolbars, fewer pills, no repeated facts.

Against the real apps the skill builds lost five of six (judge means 7.0 vs 8.5; won the Gmail inbox 8.2 vs 7.6). The losing regions became the "Region rules from side-by-side reviews" in SKILL.md:
- black section headings competing with the title (real: small grey section headers)
- a rule under every row plus large gaps (real: space, one inset divider between groups)
- tick circles tinted by list in a mixed view, diluting the one red cue
- wrapped titles in dense rows
- identical grey category pills
- a filled batch button competing with the hero
- a large title on a pushed database screen with a toolbar row
- tinted sort buttons; a third column peeking and truncating the second
- dropping avatars and the noun after a glyph count (over-cutting)
- a whole status sentence in green instead of the one value
- a rail of actions at the top of a map instead of the sheet footer

### Final numbers (blind Codex judge, scores 1-10)

| Comparison | Skill wins | Mean scores |
|---|---|---|
| Skill vs no skill, tuning screens (6) | 6/6 | 8.25 vs 7.32 |
| Skill vs no skill, held-out screens never used for tuning (Notion database, Spark inbox, Linear projects, Apple Weather) | 3/4 | 8.15 vs 7.70 |
| Real app vs no skill (10) | real 10/10 | 8.63 vs 7.00 |
| Skill round 1 vs real (6) | 1/6 | 7.02 vs 8.45 |
| Skill round 2 (after region rules) vs real (6) | 1/6 | 7.28 vs 8.45 |
| Skill round 2 vs round 1 (6) | 4/6 | 8.05 vs 7.60 |
| Skill vs real, held-out (4) | 1/4 (beat Notion) | 7.55 vs 8.30 |

The skill reliably beats an unguided build and closes about half the gap to the real apps on unseen screens (−0.75 against −1.6 for no skill). It does not yet match the best apps screen for screen; the region rules after the held-out round were added from those losses and are not yet measured.

## 4. Tests to run on every screen

1. **Count** non-content words: ≤12 on a list or home, ≤15 on a detail. Then stop cutting.
2. **Blur** the screenshot: the hero reads first, the primary action second.
3. **One large text:** only the title or the hero is big; section headers are small and grey.
4. **One loud colour cue per region:** if several things are coloured, the urgent one no longer stands out.
5. **Thumb test:** the primary action and search are in the bottom third.
6. **Repeat test:** no fact appears twice (title and tab, row and detail header, card and card).
7. **Pill test:** metadata is a quiet line, not a row of boxes.
8. **Native test:** system tab bar, glass circles for nav buttons, sheets with grabbers, no centred modal, no hairline under the header.
9. **Over-cut test:** avatars, logos, flags and glyphs are still there; tab labels kept; ambiguous glyph counts keep their noun.
