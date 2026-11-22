# Walk the job

The required check for every UI change. A screen can pass every visual review and still take seven steps where two would do, or leave the user staring at it with no idea what comes next. This check catches that. It takes minutes per job. Run it on the real build (the project's `verify-<app>` skill, `chrome-devtools-axi`, a simulator), never by reading code.

## When

Before calling any UI change done, for every job in the [14 standard jobs](../SKILL.md#the-14-jobs-at-a-glance) the change touches. A change that touches no job (a colour token, a copy fix with no effect on what is clicked) records "no job touched" and stops. When unsure, the job is touched.

## The walk

Do this once on the build before the change and once after, from the same start with the same data. A walk is only comparable to another walk with the same start and finish.

1. **Name the start.** The screen, what is open, what is selected, which menu is already open, the data (one named test item, never a real person's record). "Menu already open" and "menu closed" are different starts: Claude's Unpin cost 1 action from an open menu and ChatGPT's cost 2 from a closed one, for the same design.
2. **Name the finish** the user would recognise as done: the item visible where they expect it, the message sent, the record changed. Not "the API returned 200". "Saved" and "back where I started" are separate finishes: an edit can commit in place while the exit is one more step, so record both.
3. **Walk it and count.** One step per deliberate action: a click, a tap, a keystroke chord, a typed entry (one field = one step however long the text), a drag, a gesture. Passive transitions add nothing. Write each step down. Every deliberate action counts, including one that lands in the wrong place and the steps back from it. Arrival is a separate check: the screen shows the object you meant and a landmark of the destination you meant (its title, its heading). A hit that opens somewhere else is a dead end, and after a move, check the destination itself, not the source view.
4. **Count decisions separately.** Every point where the user must judge something (is this total right, which of these two, do I want to send) is a decision even when it costs no click. A step that adds a decision must buy a real consequence (spending money, sending outward, changing someone else's data); otherwise cut it.
5. **Name the next action at every screen.** At each stop, write the one thing the user should do next and where it is. If you cannot name it in under three seconds, or it is behind hover, below the fold, inside a menu with no hint, or one of several equal-weight options, mark a **dead end** at that step.
6. **Compare with the budget.** Each job's budget is in the [playbooks](../SKILL.md#per-job-playbooks). Over budget: every extra step needs a written reason (it authorizes a consequence) or it is a defect.
7. **Make one mistake and undo it.** Do the job wrong once in the most likely way (wrong item, wrong list, wrong value, accidental delete or archive), then reverse it. Count the undo steps, and reach a notice's Undo inside its real lifetime as a user who reads first would; record the window and flag a notice under 5s (product-ui). Check the restored state against the original: the item, its neighbours and any downstream view (the list, search, a second tab). Notion's reorder test is the model: a known order Alpha/Beta/Gamma, a move, one ⌘Z, and the exact original order checked.
8. **Hit the error path.** Trigger one harmless failure: an empty required field, a missing connection, a failed request, offline mid-edit. Check that the cause is named where it happened, the fix is offered there, the user's input survives, and the fix returns to the job instead of to a settings page with no way back.
9. **Leave and come back.** Close the view mid-job (or reload, or open a second tab) and return the way a user would (Recents, search, the notification). Count the steps back separately from the steps to do the job. Check the same object opens with its state and history, and nothing reappears that was settled or deleted (ChatGPT's search kept offering a deleted chat, which then opened to an access error).
10. **Check the consequence beyond the screen.** What else changed: a regenerated answer after an edit (Claude), a value shown in another view (Notion), a recipient on another device, a record in another system. For a handoff, look at the destination; if you cannot reach it, label that part of the walk partial.

## Record

One block per job, kept with the change (PR body or the task's proof folder):

```
Job: J2 Quick add      Start: Today list open, nothing selected      Finish: task visible in Inbox
Before: 5 steps, 1 decision, 1 dead end (step 3: Add hidden in overflow menu)
After:  2 steps, 0 decisions, 0 dead ends      Budget: 2  ✓
Next action named at: list (+ in toolbar) → composer (Enter) → list (new row selected)
Mistake: added to wrong list → moved back in 2 steps; neighbours unchanged ✓
Error: empty title → inline "Add a title", input kept ✓
Return: reload → task in Inbox, selected ✓
```

Attach the before and after screenshots of the step where the count changed.

## Pass

- Every touched job is at or under budget, or each extra step has a reason that names the consequence it authorizes.
- Zero dead ends.
- The mistake was undone in at most the budgeted undo steps, with the original state restored exactly.
- The error path named its cause in place and returned to the job with the user's input intact.
- Returning reached the same object with its state.

A walk that fails is a defect in the change, not a note for later. Fix it, then walk again from the same start.

## Cheap ways to cheat, which do not count

- Counting from a start chosen to flatter the after-walk (menu pre-opened, item pre-selected) when the before-walk began elsewhere.
- Counting a keyboard shortcut or gesture as the route. Shortcuts and gestures are accelerators; walk the visible route a newcomer would take, and record the shortcut separately.
- Skipping the mistake or the error because "nothing obvious to break". Every job has a wrong item to pick and a required input to leave empty.
- Declaring a handoff done from the sender's side.
