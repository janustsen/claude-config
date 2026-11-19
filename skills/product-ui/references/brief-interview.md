# Brief interview

Most bad screens come from a guessed brief, not from bad styling. A one-line request ("a page to manage routes") leaves the real questions open: who opens it, what they decide there, which of forty stored fields that decision needs, what the awkward real record looks like. Built from guesses, the screen comes out generic. Built from the answers, the same skill produces a screen that only fits this product.

This is a grilling session (`grilling`) aimed at one screen. It ends in a five-part brief written to a file. The build reads that file and nothing else about content.

## When

- **Default** for a new screen or a redesign, when someone can answer questions.
- **Fast path:** the user says "just build", "skip the questions" or similar, or no one can answer (you are a sub-agent, a batch job, an eval). Do the lookups below, answer every question yourself with your recommendation, write the brief marked `Assumed: yes`, and build. Never stall waiting for answers that will not come.
- **Skip** for a change to one part of an existing screen ("move the filter", "fix the empty state"): the screen and its brief already exist.

## The five-part brief

The output, in this order. Every part is content. **No style words**: nothing about layout, colour, type, components or mood ("sidebar", "card", "pill", "bold", "dark", "clean", "modern", "minimal"), and no placement ("beside", "next to", "above", "on the left"): say what the user needs *with* what ("the draft, with the message it answers"), and let the build place it. Those are the skill's job, decided in steps 1-13 from the content. A brief that names components gets built as a pile of those components.

1. **Who, where, why, in one sentence.** Who opens it, when and how often, what they decide or do there, and what is true when they leave. "The morning dispatcher at a 40-van courier opens this at 6:30 on a desktop to reassign the routes of drivers who called in sick; they leave when every stop has a van."
2. **The real data, verbatim, in two tiers.** Real names, numbers, dates and text, copied from the data, not paraphrased. Every fact listed here becomes something on screen, so a fact kept "for context" or "nice to know" belongs in part 5.
   - **Focus:** the one thing this visit is for, which gets the screen. Its headline is the answer the user came for, in one sentence ("3 drivers called in sick; 47 stops have no van"), or the record being judged, **whole**: the full draft, email or answer at its real length, never an excerpt (an excerpt builds an empty screen). Then only the evidence that answer rests on. Where no stored text exists, write the full stand-in at real length and say so.
   - **One step away:** what the user may need this visit but does not decide on first: the queue the focus came from, the focus included so the user keeps their place (8-15 real records, with the awkward cases the data actually has: the longest title, a failure, a duplicate, another language), secondary checks, scores. Records that need no decision today (done, someone else's, blocked, waiting) are a count, not rows.
3. **What the user can do, as verbs.** One line each, with the shortcut if one exists and the consequence if it is not reversible ("send the reply; it cannot be unsent"). Mark the one verb that settles the decision; every other verb is secondary, and rare ones are one step away (a menu). What blocks the settling verb is its state, said once where it is blocked, not a row of separate items. Six equal verbs build a toolbar of six equal buttons.
4. **The current state.** The one moment to build: which item is selected (the one that exercises the job: it carries an awkward case or the thing the user must check, not merely the first in sort order), what is running, what just failed, what is empty, whether it is online. One state per brief; other states are listed as their own one-liners for step 9.
5. **Also stored, nothing here has to be shown.** Every other field the record has: IDs, timestamps, internal flags, raw payloads, scores. Listing them lets the build cut them on purpose instead of displaying them because they exist.

Add one line at the end: `Never shown:` anything that must stay off this screen (secrets, other people's private data, internal notes), or `none`.

## The design tree

Map the screen's open decisions as a tree. A decision can be asked once its parents are settled; the frontier is every decision whose parents are settled. Ask the whole frontier in one round.

```
the screen's job: who, when, the one decision, done looks like      <- round 1, always
├── which records, and which of their fields that decision needs     <- needs the job
│   ├── the focus, and what is one step away                         <- needs the fields
│   └── what is stored but not shown                                 <- needs the fields
├── the verbs, the one that settles it, which cannot be undone       <- needs the job
├── how often and where: glance many times a day, or a sit-down;
│   laptop or phone                                                  <- needs the job
└── edge states: the awkward real record, empty, failed, too many    <- needs the records
    ├── which state to build now                                     <- needs the edge states
    └── what must never be shown                                     <- needs the records
```

Usually two or three rounds. A screen whose job the user states fully in the request starts at the second level.

When the user names several decisions ("is the run sound, what moved, how do past calls score"), ask which one leads. That one is the focus; the others become one line each, or one step away, and a healthy check collapses to nothing. A screen that answers three questions at equal weight is a dashboard of panels, and it loses to a screen with one headline and one picture.

## Facts are looked up, decisions are asked

Before round 1, and in parallel with it, look up every fact you can. Dispatch a sub-agent when the search is wide; ask the questions that do not depend on it meanwhile.

| Look up, never ask | Ask, never assume |
|---|---|
| The data model: tables, fields, enums, states | Who the screen is for and the one thing they decide there |
| Real records: 8-15 of them, plus the longest, the oldest, the failed, the empty | Which fields that decision needs; which are stored only; which one thing leads |
| Existing screens, routes and navigation the new one sits among | What the user must see first |
| The product's words for things (field names, statuses, button copy in use) | What success looks like when they leave |
| Which actions the code makes irreversible (sends, payments, deletes) | What must never be shown |
| Volume: how many records, how fast they arrive | Which edge state matters most; which moment to build |
| Existing tokens and components (for the build, not the brief) | Trade-offs the code allows both ways |

When the data is private, use it verbatim in the brief anyway: the brief stays in the project. When no data exists yet, write records that are true to the domain and say so in the brief.

## A round

The `grilling` format: numbered, one recommended answer each, multiple choice when the options are knowable. Lead with what you found, so the user corrects a fact rather than supplying one.

```
❓ **Q1** - **The one job**: Found 612 stops on 38 routes today in `routes` and `stops`; 3 drivers are marked sick, leaving 47 stops unassigned. What does the dispatcher decide on this screen?
  a. Who takes each unassigned stop (reassign before vans leave)
  b. Whether today's plan is sound overall (review every route)
  c. Both, reassignment first

➡️ a: the request says "manage routes", but the only thing that changes at 6:30 is the 47 orphaned stops.

---

❓ **Q2** - ...
```

When asking which fields a decision needs, recommend the fewest that decide it; the user adds back what they miss. A brief that lists twenty facts per record builds a screen of labels.

Never ask about style ("card or table?", "what colour?", "sidebar?"). If a question would change only the look, it is yours to answer in the build. If the user volunteers a style wish, note it outside the brief, for step 10.

## Writing the brief

When the frontier is empty, write the brief to `docs/briefs/<screen>.md` in the project (or beside the screen's code when the project keeps docs there). Show it, and wait for an approval or edits before writing code. Then build from decision step 1, using:

| Brief part | Feeds |
|---|---|
| 1. Who, where, why | Steps 1-2: category, scarce resource, the thesis sentence; step 3: what the user lands on |
| 2. Data: focus, one step away | Step 4 objects and states; the focus gets the screen and the richest component, everything one step away is a list, a count or a shelf the user opens |
| 3. Verbs | Step 6 control placement; step 12 shortcuts; irreversible verbs name their consequence |
| 4. Current state | The state the first screenshot shows; the others go to step 9 |
| 5. Stored, not shown | Step 5 text budget: these are cut before anything is drawn |

Check the finished brief with two tests. Could it describe a competitor's screen? Then part 2 is not real data yet. Does the focus hold more than one thing, or does the brief put more than about seven items of any list on the first screen? Then move the rest one step away: the brief decides what is on screen, and a brief that lists everything builds a busy screen however good the build is.

The lookups often find problems that are not design: a template signed from the wrong account, a field the screen needs that the pipeline throws away, a link between records that exists only in a log. List them after the brief, for whoever owns the data; do not design around them silently.
