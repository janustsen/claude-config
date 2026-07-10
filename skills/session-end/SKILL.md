---
name: session-end
description: Use when wrapping up a work session and Janus wants a candid retrospective on what just happened — triggers "/session-end", "end of session", "wrap up", "session retro", "what did you miss", "grade this session", "debrief". Runs a fixed, blunt Q&A about the actual work done this session.
---

# Session End

## Overview
A candid end-of-session retrospective. Answer every question below about **the actual work done in THIS session** — not software work in general. The job is to surface blind spots, unrecorded decisions, and things left undone while the context is still loaded. Blunt over flattering: Janus wrote these questions precisely to hear what he'd rather not.

## How to answer
- One tight paragraph or 2–4 bullets per question. No preamble, no restating the question, no filler.
- **Specific to this session** — name the files, choices, and tradeoffs that actually came up. A generic answer is a failed answer.
- **Recommend, don't survey** — one clear call, not a menu (Janus's standing preference).
- Answer every core question; if one genuinely doesn't apply, write "N/A — <one-line why>" and move on.
- Keep the numbering so he can reply "on #3…".

**Bad (generic, fits any session):** "You could improve efficiency by planning more upfront."
**Good (specific):** "We burned ~3 edit rounds because I changed `moduleSaver.ts` before reading what `origin-gate.ts` exported — reading both first would've caught the signature mismatch."

## Core retrospective (always answer, in order)
1. **Least confident** — what are you least sure about in what we just did?
2. **Blind spot** — the biggest thing I'm missing about this situation; what don't I realize?
3. **One bleeding-edge addition** — if you could add one unrequested thing that would make this app / module / deliverable truly industry-leading or bleeding-edge, what is it?
4. **Missing tooling** — any tool, script, or hook that would've cut churn this session if it had existed when we started?
5. **Durability (shippable work only)** — if this ships and breaks in 3 months, the single most likely reason. If nothing shippable was produced, say so in one line and skip.
6. **Smoother session** — what could *I* (Janus) have done differently to make this session more efficient?
7. **What you didn't do** — audit everything you skipped, missed, deferred, assumed, or ignored. Hide nothing.

## Janus project lens (answer only the ones this session actually touched)
Grounded in `~/janus-brain` (Duna/FStea, Trus, the vault). Skip any that don't apply — don't manufacture relevance.
- **Boundary / exposure** — did anything this session cross a line: client-confidential (FStea / 斐素), MS-internship MNPI, secrets or API keys, or a newly-public surface (repo, deploy, share link)? *(Listed first because of the FS-AI public-repo incident.)*
- **Capture** — what must reach the brain before it's lost: a decision (+ the WHY and the alternatives), a new `open` thread, a thread this session *resolved* (amend it in place), or a reusable idea for `80-IDEAS/`?
- **Verification honesty** — what did you present as done / working / passing that you did NOT actually verify end-to-end? Name it plainly.
- **Craft bar (user-facing work)** — does it clear the Trus / "perfecting the craft" standard, or is it merely functional? Where would a discerning user feel the seams?
- **Leverage** — founder time is the scarce resource. Was this the highest-leverage use of the session, or did we polish something that didn't need it while a bigger thread sat idle?

## Close
Finish with one line offering to act — file the **Capture** items into the vault (see `journal-sort`) and/or log any decision with its WHY. Don't do it unless Janus says yes.
