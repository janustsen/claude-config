---
name: ux-flows
description: Design or review how a whole job goes in an app, not how one screen looks - how many steps it takes, where the next action is at every screen, what confirmation and undo look like, what happens on an error, offline or a blocked dependency, what the product does on its own, and how the user gets back to their work later. Gives the decision order, a step budget and playbook for each of 14 standard jobs (first run, quick add, edit in place, organize, find, bulk action, undo, error or offline, notification or inbox, review or approve, setting, handoff, automation, leave and resume) measured on 25 apps walked on desktop and iPhone, plus the required walk-the-job check for every UI change. Use when designing a flow, adding or moving an action, merging or splitting pages, building onboarding, import, approval or notification paths, or when anything feels like too many steps or unclear what to do next. Load product-ui for the screen itself and mobile-ui for iPhone screens.
license: MIT
---

# UX flows

product-ui decides what a screen looks like and where its controls sit. This skill decides how a job goes from the moment the user wants something to the moment it is done and they can trust it: the steps, the next action at each stop, the confirmation, the undo, the failure and the return. A screen can pass every visual review and still fail here. The two failures people name first are **too many steps** and **unclear what to do next**, so this skill goes deepest on those.

The rules come from three bodies of evidence, weighted in this order:

| Tag | Evidence | What it can prove |
|---|---|---|
| [live] | Completed job walked in the signed-in app (Notion, ChatGPT, Claude: 19 jobs) | Step counts from a named start, feedback, undo |
| [rec] | Public recording or demo, frames sampled (Things, Linear, Apple Notes and Reminders, Obsidian, Attio, Airtable, Figma, Slack, Gmail) | The sequence shown; not discoverability or timing |
| [doc] | The vendor's published procedure (all 25 apps) | The route exists; counts are a reading of the procedure |
| [corr N] | N corrections from an owner's design reviews of their own products (224 corrections, 96 interview answers, about ten products) | What a real user objected to, repeatedly |

A rule supported only by one documented source was dropped. Counts on [doc] are the procedure, not the friction. No human task time was measured anywhere, so this skill budgets steps and decisions, not seconds. The evidence register, with what was dropped and why, is in [references/evidence.md](references/evidence.md).

## Rule zero: count the walk, not the screen

A job is one thing a person comes to do (add, find, fix a mistake). A **step** is one deliberate action: a click, a tap, a keystroke chord, a typed entry, a drag, a gesture. Passive transitions cost nothing. A **decision** is a point where the user must judge something; count it even when it costs no click. A **dead end** is a stop where the next action is not visible or the user must back out.

Four counting rules, each learnt from a walk:

1. **Name the start before comparing counts.** Claude's Unpin cost 1 action and ChatGPT's 2, for the same design: Claude's menu was already open [live]. A shortcut, a warm start and a fresh install are three different counts (Things capture by dragging Magic Plus is 3 steps; Obsidian's documented first vault is 4 before any note) [rec, doc].
2. **Count the return separately from the creation.** Reaching a chat again from Recents took 2 steps in ChatGPT and finding it by title took 3 [live]. A job that is cheap to do and expensive to find again is expensive.
3. **Count decisions even when they add no tap.** Shopify's documented one-unit order edit is 7 actions, and at Review changes the operator must judge whether the total is right [doc]. A decision that authorizes nothing (a confirm on an undoable action, a choice with one sensible answer) is a step to cut.
4. **Verify the consequence, not the click.** Saving an edited prompt in Claude regenerated the answer below it; editing a Notion block changed it in every other view with no Save [live]. The walk ends where the user would check, including a second view or the recipient's side.

The required check built on these rules is [references/walk-the-job.md](references/walk-the-job.md). Run it for every UI change.

## The thesis

The user arrives with intent and leaves with a result they trust. Everything between is cost. Every step and every screen in a flow passes five tests:

1. **Could the product do this itself?** It has the data, the match is certain, the answer has one sensible value: do it and show what it did. [corr 17]
2. **Is this where the user decided to act?** If the trigger lives elsewhere, move it onto the object. [corr 18]
3. **Is the next action obvious from here?** One visible next action, named by its verb, where the eye already is. [corr 9, rec]
4. **Can they take it back?** If yes, skip the confirm and offer undo. If no, show the full scope first.
5. **Will it stay done?** Later evidence, refreshes and imports must not reopen what was settled. [corr 12]

## Decision order

Write each decision down (a line or two) before building or changing a flow.

0. **Name the jobs this change touches**, from [the 14](#the-14-jobs-at-a-glance). A new page touches find and leave-and-resume at least; a new action touches undo; anything that waits touches error or offline.
1. **Name the start and the finish** for each job: the screen and state the user starts from, and the thing they would look at to know it is done.
2. **Give each job one home.** One recognizable destination per job, and the object's facts, history and controls on the object, not behind a second interface. Merging pages must not make a job disappear from navigation; splitting must not make the user compare two pages to decide. [corr 19, 11 interviews; screen rules in product-ui shell-and-navigation §1]
3. **Put the trigger on the object.** The action sits on the row, card, record or input where the user makes the decision, visible without hover, and a small edit stays in its list instead of opening a floating editor. Reserve a dimmed modal for a genuine detour (reviewing a whole draft with its thread). From an open Attio record a note is a swipe and a tap; from an open HubSpot deal a stage change is two taps [doc]. [corr 18; placement rules in product-ui §6]
4. **Set the budget and spend it.** Look up the job's budget below, walk the planned route, and justify every step over budget by the consequence it authorizes. Merge duplicate entry points into one action with a choice (two research buttons that differ by depth become one button with a depth option) [corr 4, 4 interviews].
5. **Decide who does each part.** For every step: the product does it (it has the information), the product proposes and the user commits (it is consequential or uncertain), or the user does it (it is their judgment or their authorship). Write down who starts it, what it may spend or change, and who commits it. Approval of a prepared action means do it, not hand it back. [corr 12, 18 interviews]
6. **Name the next action at every stop.** After each step the user should see what to do next without reading instructions. Design the stop after success too: where the user lands, with the new thing selected. See [next-action clarity](#next-action-clarity).
7. **Design the confirmation.** Show the result where the user acted, in the place they will look for it later, with the same scope that was promised (Vercel's rollback dialog names the current and target deployments; its completion view confirms each affected domain) [doc + rec]. Quiet for success; the state change itself is the confirmation (Pin becomes Unpin, the chat moves into Pinned) [live].
8. **Design the undo.** The inverse lives where the verb lived (Pin and Unpin in the same menu slot in ChatGPT and Claude) [live], ⌘Z reverses the last structural edit exactly (Notion: one ⌘Z restored Alpha, Beta, Gamma) [live], and an intended multi-record change (an import, a bulk edit) is one operation with one approval and one undo [2 interviews + rec]. Timing and notice anatomy are in product-ui (5s, ⌘Z).
9. **Design the failure.** Name the cause where it happened, keep the user's input, offer the fix on the spot, and return to the job when it is fixed. A missing connection is a setup flow at the point of need, not a warning banner. [corr 7, 4 interviews; [demo] Linear names the empty required field]
10. **Design the return.** Leaving and coming back (closing the tab, switching device, following a notification) reopens the same object with its state, draft and history. Long work keeps running when the view closes and shows its stage on return. [corr 11, 5 interviews; [live] ChatGPT Recents]
11. **Keep settled things settled.** A later reply, a refresh, a second source or a re-import updates the existing object instead of reopening it or duplicating it. Remember the user's answers (same person, not interested, already replied). [corr 12, 6 interviews]
12. **Walk it.** Run [references/walk-the-job.md](references/walk-the-job.md) on the real build, before and after.

## Step count

The budgets below are the best route measured for that job, from a stated start. They are budgets for the visible route a newcomer takes, not for a shortcut. The study did not support one universal click limit; it supports a budget per job from a named start.

Where steps come from, and the cut for each:

| Source of extra steps | Cut | Evidence |
|---|---|---|
| The user re-enters what the product already knows (transcribing a file into records, filing a document, re-answering an identity question) | Read it, match it, fill it; ask only about conflicts | [corr 17]; [corr 12] for remembered answers |
| Every item goes through a review queue | Apply what is corroborated or unambiguous; queue only genuine uncertainty; re-judge the backlog when the rule changes | [corr 9, 6 interviews] |
| Two entry points for one job (two buttons, two pages, two engines) | One entry point with a choice inside it | [corr 19] |
| A menu, then a dialog, then Save, for a one-field edit | Edit in place: click, type, Enter or blur. Claude renames a title in 3 steps by clicking it; ChatGPT's menu-and-dialog rename takes 4 [live] | [live] |
| Prepared work handed back ("now click here to do it") | Approval executes; a requested expensive action is one prepared card with its cost | [corr 12, 18 interviews] |
| Per-item approvals for one intended change | One summary approval with affected records visible, one undo | [2 interviews] |
| Manual focus changes between fields that have a fixed format | Auto-advance (day to month to year) | [corr 1] |
| Scrolling to reach the primary action or a short settings list | Fit the job's input and its commit on one screen | [corr 2] |
| Navigating to configure before acting | Configure on the input that triggers the action (product-ui §6) | [corr 18] |

Two kinds of step are worth keeping: a step that authorizes a consequence the user would want to stop (spending money, sending outward, changing other people's data, deploying), and a step that is the user's own judgment or authorship. Everything else is a candidate to cut.

## Next-action clarity

At every stop the user should be able to point at the next action in under three seconds. The walks and corrections found the same failures repeatedly.

1. **One next action per stop, visible, named by its verb.** Not behind hover (a collapse control that appeared only on hover was a correction) [corr 18], not one of several equal-weight links, not below the fold (the primary action outside the first view was corrected twice) [corr 2].
2. **The empty state names the action.** Obsidian's empty canvas tells the user where to drag or double-click [rec]. One line plus the action (product-ui states-copy-safety §1).
3. **The plain path is not buried under the promoted one.** Attio's onboarding offers manual entry below identity-provider buttons and customer logos: the path exists and is hard to find [rec]. If a newcomer must hunt, it is a dead end.
4. **After success, the user lands where the next job starts.** Things returns to the original project after capturing to Inbox, and the Inbox count shows where the task went [rec]. ChatGPT moved a pinned chat into a named Pinned section [live]. The new or changed item is visible and selected; no "Success!" page with nothing to do.
5. **After a step fails, the next action is the fix.** A field error names the field (Linear rejected an empty title and named it) [demo]; a missing connection opens its setup there and returns [corr 7]. Generic retry that fails the same way is a dead end [corr].
6. **Gestures and shortcuts are accelerators, never the only route.** Things' pull-down search and Superhuman's directional gestures are fast, and neither recording shows a newcomer discovering them [rec]. Keep a visible route; measure the gesture separately.
7. **The landing view answers what needs the user next.** Due-soon and waiting-on-you work first, the full inventory one destination away; replies waiting longest on top of one merged list [corr 9, 5 interviews; product-ui shell-and-navigation §1].
8. **Name things in the user's words, with enough context to act.** Cover the rest of the page: can the user say who the row is about, what happened, and what the button will do? Machine IDs, internal concept names and unexplained app vocabulary make the next action unclear even when it is visible [corr 17].
9. **Running work says what it is doing.** Which item, which stage, waiting or failed, so the user knows whether the next action is theirs [corr 7; ai-interaction-patterns progress patterns].

## The 14 jobs at a glance

Budgets count deliberate steps from the start given. "Best measured" is the lowest count with the strongest evidence; others are in the playbooks.

| Job | Start | Budget | Best measured | Next action lives |
|---|---|---|---|---|
| J1 First run to first value | Signed in, empty product | 2 to the first useful result; each setup question before it needs a reason | ChatGPT 2 (type, Enter) [part] | The product's one input |
| J2 Quick add | The list or object open | 1-2; 3 when choosing another destination | Notion 1 [live]; ChatGPT, Claude 2 [live]; Things 3 with destination [rec] | Inline at the list or composer |
| J3 Edit in place | The value visible | 1 for a toggle; 3 for text (click, type, commit) | Things checklist 1 [rec]; Claude title 3 [part] | On the value itself |
| J4 Organize | The item visible | 2 (menu, verb) or one drag | ChatGPT, Claude pin 2 [live]; Notion reorder 3 by keyboard [live] | The item's menu or drag handle |
| J5 Find | Anywhere | 3 (open search, type, choose); 2 for a recent item | ChatGPT 3 by search, 2 by Recents [live]; Apple Notes tag 1 [rec] | One search entry, always in the same place |
| J6 Bulk action | List visible | Select + 1 per extra item + 1 action | Notion 4 for two blocks [live]; Things 4 for three tasks [rec] | A selection bar that names the count |
| J7 Undo | Just after the mistake | 1; 2 later via the inverse verb | Notion ⌘Z 1, Claude 1 with menu open, ChatGPT 2 [live] | The notice, ⌘Z, or the verb's own slot |
| J8 Error or offline | Mid-job | 0 to keep input; 1 to the fix | Linear names the empty field [demo] | At the failed item |
| J9 Notification or inbox | The notification | 1 to the exact object with its next action | No live walk (gap) | On the notification and the object |
| J10 Review or approve | The item to judge | 1 decision with its context visible | ChatGPT, Claude 2 [live, advisory] | End of the item it affects |
| J11 Setting | The object it affects | 3 from the object | Notion page notifications 3, confirmed with Undo [live] | On the object, or one settings sheet |
| J12 Handoff | The finished thing | Measure at the destination | Same-account second view 1 [part]; Slack recording [rec] | Share on the object; landing on the recipient's side |
| J13 Automation and its cue | The product acting on its own | 0 for the user; a visible cue | Notion autosave 0 extra [live] | The cue where the result appears |
| J14 Leave and resume | Away from the work | 2 back to the last thing | ChatGPT New chat → Recents 2 [live] | Recents, pinned, or the notification |

## Per-job playbooks

Each playbook: budget, where the next action lives, confirmation and undo, error and offline, evidence. Screen-level anatomy (toasts, dialogs, skeletons) lives in product-ui; it is pointed to, not repeated.

### J1 First run to first useful action
- **Budget.** From signed in to the first useful result: 2 steps when the product is one question (type, submit: ChatGPT [part]). Every input asked before that result needs a reason the user would accept; ask for the minimum and teach the rest in context [corr 6 + 2].
- **Next action.** Inside the empty work area, not around it: Obsidian's blank canvas says where to drag or double-click [rec]; Linear's composer opens with focus in the title [demo]. The plain path is never a text link under integration logos (Attio) [rec].
- **Confirm and undo.** End inside a working state: the first real item, selected. If the work will not be saved (a guest session, a private mode), say so next to the input before the user commits; Perplexity accepted a guest prompt and then hid the answer behind "This session is private" [part].
- **Error.** A wall after the user typed keeps what they typed. One sign-in, not two stacked gates [corr 2].
- **Dead ends seen.** Verification email or install before any value (Figma 8, Granola 7 documented); setup before the first item (Todoist creates a project first, 8; Obsidian a vault, 11) [doc]; a Get Started button that leads to an extension install (Superhuman) [part]; Compose clicked with no editor and no loading or failure state (Gmail) [part].
- Screen rules: product-ui shell-and-navigation §6 and laws L13.

### J2 Quick add
- **Budget.** 1-2 from the open list or object (Notion 1; ChatGPT, Claude 2 [live]). 3 when the user picks a destination other than the current one (Things: drag Magic Plus to Inbox, type, Save [rec]). Routes of 7-8 steps (HubSpot, Stripe, Shopify [doc]) are navigation and a form in front of the add: put the add on the list instead.
- **Next action.** Inline at the end of the list or in the composer, focused, with defaults taken from the current view (Linear [demo]). Enter commits and leaves the user ready to type the next one (Apple Reminders, Things [doc]).
- **Confirm and undo.** The new item appears where it was added, and the user stays where they were (Things returns to the project and the Inbox count shows where it went [rec]). Parsed values show as chips beside the text, and clicking a misread word turns it back into text (Todoist [rec + doc]).
- **Error.** An empty required field is named at the field and the composer stays open with the input (Linear [demo]).
- **Watch for.** A quick add with a heavy side effect (Granola's New note starts audio capture [doc]). Name the effect on the control.

### J3 Edit in place
- **Budget.** 1 for a toggle or checkbox (Things checklist [rec]). 3 for text: click the value, type, Enter or blur (Claude title [part]). A menu, a dialog and Save is 4 (ChatGPT rename [live]); a separate editor page is 5-7 (Stripe, Shopify, HubSpot, Vercel [doc]). Cut both.
- **Next action.** On the value itself. Selecting the object and editing its text look different (Figma's layer outline vs text caret [rec]). A small edit stays in its list; a floating editor that covers the context was a repeated correction [corr 18].
- **Confirm and undo.** The changed value is the confirmation; no Save button where saving is automatic (Notion [live]; Linear, Apple Notes [doc]). Esc keeps the edit and closes; ⌘Z reverts. When the edit changes something else (Claude regenerates the answer below [live], an edit propagates to every published use in Shopify [doc]), show that consequence before or as it happens.
- **Error.** Invalid input is refused at the field with the reason; the prior value stays visible until the new one is valid.

### J4 Move, reorder or organize
- **Budget.** 2: open the item's menu, choose the verb (ChatGPT, Claude Pin [live]). Or one drag between visible groups (Things, Apple Reminders [rec]); count the scroll if both groups are not on screen. A single key from a selected item is the accelerator (Linear, Superhuman L to label [doc]). Slack's 10-step private section and HubSpot's 8-step route [doc] are what to avoid.
- **Next action.** On the item: its menu, a drag handle, or a dropdown in its side panel. Drop targets show the result before release (a blue insertion line, Things and Reminders [rec]; a target labelled with its effect, Todoist [rec]).
- **Confirm and undo.** The item moves visibly into a named section and stays highlighted where it landed (ChatGPT Recents → Pinned [live]; Things, Reminders [rec]). The inverse verb replaces the verb in the same slot (Pin → Unpin) [live].
- **Watch for.** Organizing with a sharing side effect (moving a Figma file into a folder can give its members access [doc]). Show the new audience before the drop.

### J5 Find it later
- **Budget.** 3: open search, type, choose (ChatGPT [live]; Things on iPhone [rec]). 2 for something recent (Recents, a pinned list: ChatGPT [live]). 1 for a filter the user already has (Apple Notes tag [rec]). The job ends when the item is open, not at the result list: count the reopen.
- **Next action.** One search entry, in the same place on every screen, opened by one key, with results as the user types (Things, Figma, Shopify, Obsidian [doc]). A detail pane beside results lets the user check before opening (Raycast [doc]). The active filter is stated above the results (Apple Notes [rec]).
- **Confirm.** The opened item is the one asked for, scrolled to the match.
- **Error and empty.** No results offers the broader query or clears the filter (product-ui states). Say when recent items may not be indexed yet (Figma [doc]). Never offer a result for something deleted: ChatGPT kept a deleted chat in search and opening it gave an access error [live]; Claude's search showed a searching status, then five unrelated results and not the chat [part].
- **Watch for.** Search scoped silently to the current view (Airtable) or excluding some folders (Gmail) [doc]. Show the scope.

### J6 Bulk action
- **Budget.** Selecting the first item + 1 per extra item + 1 action. Notion duplicated two blocks in 4 keystrokes [live]; Things moved three tasks in 4 [rec]; Reminders three items in 3 [rec]. HubSpot's 9-step bulk move [doc] is navigation, not selection.
- **Next action.** The same verb, key or drag as for one item, applied to the selection (Linear, Reminders, Todoist [doc, rec]); a bar above the selection with the common actions (Todoist, Shopify [doc]).
- **Confirm and undo.** Show the scope before committing: the selected items highlighted and the floating stack showing how many move (Things [rec]), the count in the button ("Move 3 tasks"). After, the selection stays highlighted where it landed with order preserved (Reminders [rec]). One bulk operation is one undo.
- **Watch for.** An implicit set with no preview (Select all, a time window, everything in a view) and bulk deletes that cannot be recovered (Superhuman, Raycast, Slack, Perplexity [doc]). Implicit scope needs the count on the confirm and an undo.

### J7 Undo a mistake
- **Budget.** 1 right after the mistake: ⌘Z (Notion [live]) or the Undo in the notice (Gmail Sent banner reopens the filled draft [rec]). 2 later: the inverse verb in the menu the verb came from (ChatGPT [live]). Recovering a deletion: at most 3 from the deletion notice, which names where the item went (Apple Notes Recently Deleted [rec]).
- **Next action.** The undo appears where the mistake happened, for long enough to read (product-ui: 5s, ⌘Z). Later recovery is findable from the same object or its list, not only from settings.
- **Confirm.** The restored state is the exact original, checked against neighbours and other views (Notion's reorder [live]). The item returns to where it was: Apple Reminders restores a deleted reminder to the default list, not its own [doc].
- **Dead ends seen.** The reverse control hidden with the item (a completed reminder vanishes; reversing it takes View → Show Completed → click, 3 [rec]); short, unextendable windows (Superhuman 10s [doc]); recovery through a 5-step Trash route (Gmail [doc]); no undo at all (Perplexity sessions, a Vercel rename [doc]).
- **Rule.** Every lifecycle verb has its inverse; every intended multi-record change (import, bulk edit) has one undo that restores created records and original values [2 interviews].

### J8 Hit an error or go offline
- **Budget.** 0 steps to keep the user's input; 1 to reach the fix from where the error appears. Recovery that sends the user through a long external checklist (Raycast 9 into system settings, Attio 13, Shopify 7 [doc]) is a design failure to fix in the product.
- **Next action.** The error sits on the failed object with its recovery beside it: Superhuman's red Send failed with Edit or Discard [doc]; Slack's Restart under the error [doc]; Linear's "Title required" at the field [demo]. A missing dependency (a connection, a permission) opens its setup there and returns to the job [corr 7].
- **Offline.** Work done offline waits in a named, inspectable state and completes on reconnect (Gmail's Outbox, Superhuman [doc]); unsynced changes show a cue and are never discarded silently (Figma, Todoist [doc]). State rules: product-ui states-copy-safety §1.
- **Failed sources.** When part of a job fails, do the rest, say exactly what is missing, and do not present a thin result as complete [corr 12].
- **Gap.** No live offline session or error recovery was walked; these patterns are documented.

### J9 Act on a notification or clear an inbox
- **Budget.** 1 from the notification to the exact object with its next action ready (Attio opens the comment itself; Granola's notice opens the note [doc]). 1 key or swipe to clear an item from an inbox (Things, Linear [doc]; Gmail, Superhuman swipes on iPhone [doc]).
- **Next action.** On the notification and again on the object it opens. A reply notice opens the reply with a draft ready, in the product where it is answered [corr 9].
- **Send once, to who can act.** Notify the person who can finish the job, in the channel they already work in, once; expire notices that went stale; never replay history as fresh alerts; a digest that repeats a place the user checks daily is noise [corr 9 + 3]. Stay quiet while the user is already looking at the item (Perplexity, Raycast [doc]).
- **Confirm and undo.** Opening marks it read; cleared items stay in a filter or archive, not deleted (Slack, Vercel [doc]). Prefer per-item actions to "mark all read".
- **Gap.** No delivered notification was received and followed in the study.

### J10 Review or approve
- **Budget.** 1 decision with everything needed to make it visible: ChatGPT and Claude returned an approve-or-hold verdict with its reason in 2 steps [live]. A review that first needs a 6-step interface built (Airtable [doc]) is over budget.
- **Next action.** The commit button at the end of the item it affects, named by its consequence (product-ui region rules). Current and proposed values side by side with the reason, editable before Accept (Attio, Vercel, Slack's change card [doc, rec]). One click from a claim to its source (Granola, Perplexity [doc]).
- **Distinguish the outcomes.** "Viewed" is not "approved": Linear's review keeps a file's viewed check while the review itself stays open [rec]. Request changes takes a message and a way to ask for review again (HubSpot [doc]).
- **Confirm and undo.** The approved item leaves the queue and can be brought back (Figma show-resolved [doc]). Approvals that cannot be reversed (Shopify, Attio [doc]) need the scope shown first.
- **Queue only real decisions.** Corroborated, unambiguous items apply themselves; the queue holds conflicts and genuine uncertainty, shown with both sides; answers are remembered through refresh [corr 9 + 6]. Gate rules: ai-interaction-patterns "Choosing the gate".

### J11 Change a setting
- **Budget.** 3 from the object it affects: Notion page notifications took Actions → Notify me → choice, confirmed "Subscribed to replies and @mentions" with Undo [live]. Item settings live on the item or its side panel (Things, Notion Calendar, Todoist [doc]); Cursor's 8 steps to a rule and Stripe's 6 [doc] are too deep.
- **Next action.** On the object, or one settings sheet with search (product-ui shell-and-navigation §5). A route that ends on a settings page without the control (Perplexity [doc]) is a dead end. Rare mode switches live in settings, not in the main workspace [corr].
- **Confirm and undo.** The effect shows on the item (a mark, a pinned group) and the inverse is equally simple. Say whether the change applies to existing items or only future ones, and who else it affects (Figma, Vercel [doc]).

### J12 Share or hand off
- **Budget.** Unmeasured to a real recipient. The sender's side: Copy link in the item's menu, copied in one step (Todoist, Airtable, Shopify, Notion Calendar [doc]).
- **Next action.** Share on the object. The recipient lands on the same object, with the same context, and a way back (Slack's recording shows the actor and the old and new value on both sides [rec]).
- **Say what crosses.** Before the user chooses, state what goes and what does not (Cursor: history but not files or credentials; Granola: summary and link, not the transcript [doc]), whether the link is live or fixed, and when it expires (Vercel branch vs commit, Shopify 2-day preview [doc]). Default to the narrowest audience. Keep personal and shared work apart through every intake and view [corr 8 + 9].
- **Verify at the destination.** A second tab only proves persistence (ChatGPT, Claude, Notion [part]). Moving to another device through settings and credentials (Things 9) or export-transfer-import (Raycast 7, Arc 6) [doc] is the anti-pattern.

### J13 What the app does automatically, and how it tells you
- **Budget.** 0 steps for the user when the product has what it needs: Notion persists every edit with no Save [live]; fill blanks, link the meeting to its notes, file the document, mark the replied-to task done [corr 17]. Setting up an automation from a builder costs 10-15 documented steps (Stripe, Slack, Shopify, Attio [doc]); offer it prepared from a description and let the user review and schedule (Claude [doc], Perplexity [part]).
- **The cue.** Show what happened where the result appears: suggestions offered with a count and a remove control per item before they apply (Todoist, Superhuman, Linear [rec, demo, doc]); the automatic actor named in the timeline (Linear, Slack [demo, rec]); cadence and next run shown; a run log per run with fix and rerun (Stripe, Attio [doc]).
- **Undo.** Ambient automation keeps checkpoints the user can retrieve (Figma versions, Obsidian snapshots [doc]). Silent daily auto-archive with no restore (Arc [doc]) and inferences that change several properties at once (Notion Calendar [doc]) are the anti-patterns.
- **Settled stays settled.** Later evidence updates the existing object (a later acceptance supersedes an earlier maybe; a sent reply closes the task); refreshes and re-imports never reopen settled items or duplicate them [corr 12 + 6]. Fix contradictory generated output before the reader sees it, or withhold the part that cannot be fixed [corr 6].

### J14 Leave and resume
- **Budget.** 2 back to the last thing (ChatGPT: New chat → the chat in Recents [live]); 1 from a list or sidebar row (Todoist, Vercel, Airtable [doc]). Navigating all the way in again (HubSpot 6, Things 5, Figma 5 [doc]) is over budget.
- **Next action.** Recents, pinned items (a short user-controlled set), a quick switcher, or the notification. Show what changed since the last visit on the object, once [corr 11 + 5].
- **Confirm.** The same object, scroll position, draft and selection. Drafts survive navigation and reopen with the composer (Linear, Gmail [doc]); generated outputs (documents, charts, answers) are kept in history and reopen [corr].
- **Long work.** Keeps running when the view closes and shows its stage on return; never strands a run because the tab closed [corr].
- **Watch for.** Drafts kept only locally and lost on logout (Linear [doc]); a deleted item still reachable from search (ChatGPT [live]); undo history lost on background or lock (check it on a phone).

## On a phone

The jobs and budgets are the same; what changes is where the next action sits and which interruptions are normal. Screen rules (thumb zone, sheets, swipe pairs, keyboard) are in `mobile-ui`; phone web mechanics in `mobile-native`. What a desktop-first flow misses:

1. **The main verbs are invisible.** Swipes, pull-down and long-press carry organize, clear, search and edit (Gmail, Superhuman, Apple Notes, Slack [doc]; Things, Superhuman pull-down search [rec]), and direction or user mapping decides the meaning. Count them as accelerators: the same verb needs a visible route (a selection mode, a menu, a button) for anyone who has not learnt the gesture.
2. **Dragging the add button picks the destination.** Things' Magic Plus dragged to Inbox captures there and returns to the project the user was in, 3 steps [rec]; Todoist's insertion drag does the same [doc]. Quick add on a phone has a destination step that desktop composers do not.
3. **Undo is a banner, a shake or nothing.** Gmail's Undo on the Sent banner reopens the filled draft in 1 tap [rec]; Slack and Superhuman offer 1-tap undo [doc]; some apps leave undo out on iOS entirely [doc limit]. Budget J7 at 1 tap from the banner and check it survives locking the phone (Apple Notes keeps undo only while the note stays open; Todoist warns before closing with unsynced changes [doc]).
4. **Offline is opt-in, per device and capped.** HubSpot's offline cache is chosen in advance, read-only, capped per object type, and shows its record count and last sync [doc]; Notion downloads only the pages picked, per device [doc]; Todoist marks pending changes and warns before discarding them [doc]. Show what is cached and how fresh, and never lose pending edits silently.
5. **The work happens outside the app.** Live Activities, Lock Screen notifications and widgets start, show and finish jobs (Granola's capture and its "notes ready" notice, Cursor's finished-turn push, a Reminders widget completing a task in 1 tap) [doc]. A notification lands on the exact object (Attio opens the comment itself) [doc].
6. **Another app may own the commit.** Claude hands a draft to Mail or Messages, which owns Send [doc]; share sheets pick the destination before saving (Apple Notes 4 steps) [doc]. Walk the handoff to where the commit happens.
7. **The phone has fewer features, so say where the rest is.** Design editing, admin settings, some searches and integrations are desktop-only in Figma, Notion, Notion Calendar and Granola [doc limits]. An honest read-only view with a route to the desktop beats a dead end.
8. **Interruptions decide what survives.** Lock, background and calls: walk J14 by locking the phone mid-edit, not by switching tabs.

None of the phone evidence is a real-device walk: 18 rows are vendor recordings, the rest documentation. Treat phone counts as lower bounds.

## Which skill does what

| Need | Skill |
|---|---|
| Layout, placement, states, copy and visual review of the screen | `product-ui` |
| AI composer, streaming, approvals, citations, agent status, cost meters | `ai-interaction-patterns` |
| iPhone screens: tabs, sheets, swipes, keyboard, notifications | `mobile-ui` |
| Forms, validation timing, submit and destructive actions | `emil-forms-and-inputs` |
| Worst-case data | `break-ui` |
| Driving the real app for the walk | the project's `verify-<app>` skill, `chrome-devtools-axi` |

## Reference map

- [references/walk-the-job.md](references/walk-the-job.md): the required check for every UI change: start, finish, count, next action at each stop, one mistake, one error, the return, and how to record it.
- [references/evidence.md](references/evidence.md): every rule with its evidence class and sources, the rules dropped for weak evidence, and the gaps the study could not settle.
