# Review

Run this on screenshots of the real build (simulator, device, or Expo web at the phone viewport for a first pass) before calling a screen done. Order matters: count and cut first, then check the platform, then polish.

## 0. Count words, cut, recount (always first)

1. Screenshot at 393x852pt.
2. Count non-content words: labels, metadata words, status words, helper copy, button text, section headers. Not the user's data, not tab bar labels.
3. Targets: at most 12 on a list or home screen, at most 15 on a detail screen; zero facts said twice.
4. For each word, try the cheaper carrier: position or section, glyph or avatar, colour, a chip. Delete what the tab bar, title or section already says.
5. Recount. Then check you did not over-cut: tab labels kept, mode and filter chips keep their word, tables with more than two value columns keep headers, glyphs and avatars still there.

## 1. Ship checklist

### Structure
- [ ] One hero per screen; everything else uniform rows or modules.
- [ ] 3-5 tabs including Search, native bar, no action in the tab bar; create is a separate + or toolbar button.
- [ ] Tab roots have a large title that collapses; pushed screens have a minimal back button and no repeated tab name.
- [ ] Each task uses the right layer: push deeper, sheet for detours (detents, grabber), full screen only when immersive; never a sheet on a sheet; no popovers.
- [ ] Search is at the bottom (or there is a reason it is not).
- [ ] Sheets and navigation stacks: the same object or row recorded before expansion, after expansion and after closing; the visible back or close route named and the return position checked.

### Reach and actions
- [ ] The primary action sits in the bottom third; commit buttons are full-width capsules above the home indicator or the tinted ✓ in a sheet.
- [ ] Exactly one prominent (filled) control per screen; destructive is never filled and never the default swipe.
- [ ] Every tappable thing has a 44x44pt hit area; borderless icon buttons are 24pt apart.
- [ ] Commit facts (cost, time, count) sit directly above the commit; no confirm dialog for reversible actions; undo snackbar exists.

### Lists
- [ ] Row density matches frequency of use; one unread or status cue per row; separators inset or none.
- [ ] Swipe pair defined (complete one way, defer or toggle the other); swipe actions mirrored in the context menu and VoiceOver actions.
- [ ] Long-press context menu with preview on every content row; its items exist elsewhere.
- [ ] Inline add at the end of lists, or a draggable +; new items pre-filled from context.

### Input
- [ ] Keyboard type, return key and autofill set on every field; inputs at least 16pt.
- [ ] The keyboard never covers the focused field or the commit; interactive dismiss works.
- [ ] Quick capture parses one line and shows what it understood.
- [ ] Capture run twice from the Home Screen, once from a clean launch and once into a resumed app: launch, type choice, text entry, save and verification counted separately, with the destination and the keyboard-focus cue in the evidence.

### Visual
- [ ] System font through Dynamic Type styles; no letter-spacing on SF; at most four sizes; `tabular-nums` on numbers.
- [ ] Semantic colours; one tint; colour only for identity, state or tap; glass only on controls; no glass on glass; no bar backgrounds or hairlines.
- [ ] Margins 20pt for modules and cards, 16pt for dense lists; concentric radii; continuous corners.
- [ ] Dark mode screenshot checked: no white flashes, every custom colour has a dark value, status colours readable.

### States
- [ ] First run, permission primer (one button), empty (one line + action), loading (skeleton after 400ms), error (cause + fix in place), offline and stale (labelled in place), gated.
- [ ] Celebration only for the set or a milestone; haptics only for meanings.

### Accessibility
- [ ] Screenshot at the largest accessibility text size: rows grow, side-by-side parts stack, nothing scrollable truncates.
- [ ] Every icon-only button has a label; row contents are grouped into one accessible element; Reduce Transparency and Increase Contrast checked on custom glass.

### Sizes
- [ ] Screenshots at 375pt and 440pt widths: nothing clipped, nothing floating in a dead gap.

### System surfaces (only those the product has)
- [ ] Notifications are full sentences with 1-3 actions that finish the job.
- [ ] A widget shows one glanceable fact and deep-links each tap.
- [ ] A Live Activity exists only for a bounded process, with a stop control, ended when done.

## 2. The screenshot review loop

1. Build from the decision order. 2. Screenshot at 393x852 in light and dark. 3. Run step 0 (count and cut). 4. Blur the screenshot: the hero should read first, the primary action second, nothing else. 5. Compare side by side with the category's reference app screens (the evidence folder has them under firstmate `data/mobile-design-skill/evidence/shots/<app>/`): for each region, which is better and why, and write the general rule, not the fix for this page. 6. Fix, re-screenshot, recount. Stop when the screen holds up next to the reference.

## 3. The questions a reviewer asks first

- What is the hero, and does it read first?
- Where does my thumb go for the main thing, and is it within reach?
- What would I swipe, and what happens if I swipe by mistake?
- Which words could a glyph, a colour or the section carry?
- Does anything look like a web page in an app frame (a custom tab bar, a hamburger for main navigation, a centred modal, a grey hairline under a header, a hover-style button)?
