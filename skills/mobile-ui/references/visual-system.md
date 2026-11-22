# Visual system: materials, type, colour, dark mode, numbers and charts

The look of a current iPhone app comes mostly from using the platform correctly: the glass control layer, the system font through Dynamic Type, semantic colours, and one tint. Character comes from the content layer: a brand hue, a page tint, category colours, imagery, a display face for one role. Tags: [meas] [doc] [obs] [web] [know]. Numbers are in constants.md.

## 1. Materials: glass is for controls

- **Liquid Glass** (the interactive, lensing material) is the material of the control layer: bars, floating buttons, the tab bar, sheets, menus. Never content: no glass cards, rows or page backgrounds; never glass on glass [doc WWDC25 219].
- Over a live camera viewfinder, keep controls opaque or on Clear glass with the dim (Halide keeps its camera chrome opaque).
- **Regular** glass works anywhere. **Clear** glass only over photos or video, with a 35% dark dim behind it when the media is bright [doc].
- Labels on glass are monochrome. Tint goes on the background of the one prominent action, not on its symbol [doc].
- Bars have no fill colour and no hairline; content scrolls under them and the system blurs the edge. Colourful content may scroll under the glass but should not sit under it at rest [doc].
- Users can push glass from ultra clear to fully tinted (iOS 27), and Reduce Transparency makes it frosted: design so both read [doc]. Custom glass in RN (`GlassView`) needs a solid fallback under Reduce Transparency.
- Standard blur materials are fine on content over imagery: Apple Weather sets its data modules on a darker translucent material over the sky. That is a content material, not Liquid Glass; keep text contrast constant on it.
- Cards on the content layer: solid white (or the grouped secondary background) on a grey or tinted page. A soft two-layer shadow on a light tinted page is acceptable (Amie, Todoist); no borders and shadows together.

## 2. Shape

- Concentric: inner radius = outer radius − padding. Capsules (radius = half height) for buttons near the screen edge, chips and bars [doc].
- Continuous corners (`borderCurve: 'continuous'` in RN) on every rounded rectangle.
- Radius ladder seen: 6pt event blocks, 10-12pt small cards and form cards, 16pt sheet cards (Maps), 20pt listing and list cards (Airbnb, Amie), 25-26pt health cards and inset grouped lists, capsules for buttons and chips [meas].

## 3. Type

- **The system font** (SF Pro) through Dynamic Type styles for all UI. It handles optical size and tracking; never set letter-spacing on it [doc]. RN: leave `fontFamily` unset and set `dynamicTypeRamp` per role.
- **Hierarchy by weight and style before size**: Headline (17 semibold) over Body (17 regular) over Subhead (15) and Footnote (13) in secondary colour. At most four sizes on a screen.
- **Title scale by role**: tab roots 34pt large title; a pushed object's own title 26-28pt bold with its glyph; destination titles never repeat the tab label in the content.
- **Rounded SF** for numbers and headlines in health and habit apps (Apple Health, Gentler Streak) [obs]; Streaks uses bold condensed caps and Oura a light geometric sans: a wellness app can also get softness from weight and spacing.
- **A display face for one role only** if the brand needs it: Oura's serif for the one interpretive sentence, Wise's display face for the balance, Airbnb's own sans throughout. The face must scale with Dynamic Type and respond to Bold Text [obs/doc].
- **Reading text** at 16-17pt, line height 1.5-1.7, 20-30pt margins (Bear, Apple Notes, Craft, Obsidian) [meas].
- **Condensed bold caps** for short labels under big icons when names must fit (Streaks); tiny tracked caps (11-13pt semibold) for module headers (Carrot, Weather, Amie's coloured form labels) [obs/meas].
- At accessibility sizes, stack side-by-side row parts vertically, drop to one column, let rows grow, never truncate scrollable text [doc].

## 4. Colour

- **Semantic system colours by name** (label, secondaryLabel, tertiaryLabel, systemBackground, systemGroupedBackground, secondarySystemGroupedBackground, separator). They adapt to dark mode, elevation, Increase Contrast and future retunes. System blue changed to #0088FF in iOS 26; hard-coded #007AFF is now visibly off [doc].
- **One tint** for interactive things and the one prominent action. Never decorative text in the tint [doc].
- **Category or identity colours** do a label's job: each list, project, calendar, metric or account has one hue used on its glyph, its title, its add button and its completed state (Reminders, Apple Health, Things) [obs]. Use the same hue for the same meaning everywhere; never one hue for two meanings.
- **Status colours** only on live, confirmed values: green, amber, red and grey for not-yet (Flighty #00A05A / #FFC100 / #ED0001) [meas]. Pair colour with a glyph shape: solid, ring, dashed, check (Fantastical, Notion Calendar's dashed outline for needs-response) [obs].
- **Red means now, today or real failure**, nothing else (calendar now line, overdue dot, failed job).
- **Money:** colour the change line and the chart by direction; leave rows of spending neutral; only income green and only over-budget red (Copilot, Wise). Revolut does the reverse (white hero change line, coloured row percentages): pick one place for direction colour, never both. On dark backgrounds down is orange (#FF5000, Robinhood) with sign and arrow [meas/obs]. Offer a colour-blind palette for good/bad pairs (Copilot) [obs].
- **Health:** no alarm red; a semantic scale (blue optimal, teal good, amber needs care, Oura); status word in the scale colour above the value [doc/obs].
- **Page tint for character:** a warm off-white page with white cards (Todoist #F8F5F2), a #F5F5F5 page (Amie), a full-screen colour field for a metric's detail screen (Gentler Streak), a background that encodes overall state (Apple Weather's sky; a calm/degraded/incident band for system health) [meas/obs].
- **Two-tier ink** for brand apps: #222 for primary text, #6C6C6C for secondary (Airbnb) [web].

## 5. Dark mode

- Ship light and dark for every custom colour, even if the app looks best in one [doc].
- Follow the system; no in-app toggle [doc].
- Dark can be pure black for numbers apps (Robinhood) or a brand-tinted charcoal for calmer tools (Things #1D2229) [meas]. Modal and popover surfaces lift automatically to the elevated background [doc].
- Re-check every status colour against its dark background (Flighty ships separate dark values, e.g. green #00FF8E) [meas].
- Text on photos or colour fields stays white or warm off-white over a dark gradient; test contrast (Revolut users complained) [obs/3p].
- Expo: `ThemeProvider` with `DarkTheme` / `DefaultTheme`, `Color.ios.*`, `DynamicColorIOS` for custom pairs; otherwise the tab bar and transitions flash white.

## 6. Numbers

- `tabular-nums` on every counter, time, amount and table column [know].
- **Hero number anatomy:** a small label, the number, then a change line (signed amount and percent in the direction colour, the period word in plain ink), then a full-width chart. Robinhood: value about 30pt, change line 13-15pt semibold, chart 345x196pt [meas].
- Shrink everything around the digits: a raised smaller currency symbol (Copilot), decimals at about 45% (Revolut), shrink-to-fit for long values (Wise, `adjustsFontSizeToFit`) [meas].
- Roll changing digits like an odometer so the eye sees which digit moved (Robinhood) [meas].
- Units smaller and grey on the baseline after the number (Apple Health) [obs].
- A changed value shows big, with the old value struck through beside it (Flighty) [obs].
- Counts once, on the thing they count.

## 7. Charts on a phone

- Full bleed: the chart takes the full width while text and cards keep the margins (Gentler Streak) [meas].
- No gridlines; at most one dotted reference line (previous close, target, ideal pace) [meas Robinhood, Copilot].
- Axis labels: min and max only, on the right; about four x ticks; polar words where units mean nothing ("Below / Above", Oura) [obs].
- Scrubbing: touching the chart rewrites the hero number, the change line and a floating time label above the chart, dims the rest of the line to 50%, plays selection haptics, and restores on release (Robinhood) [meas].
- Show "normal for you" as a shaded band behind the line, or a thin bar with range ends and a dot for today (Gentler Streak, Oura) [obs].
- Annotate extremes and the latest point in place (MAX, MIN) instead of a legend (Apple Health) [obs].
- Range chips under the chart: 1D 1W 1M 3M YTD 1Y ALL, the selected one filled; a "LIVE" dot chip for real-time (Robinhood) [obs]. A rarely changed range goes in a small menu capsule beside the headline (Gentler Streak) [obs].
- One chip row can drive every chart on the screen (Carrot) [doc].
- A pace chart (actual vs ideal-to-date, dashed) answers "am I on track" faster than a number (Copilot) [obs].
- Expo: `victory-native` (Skia) or `react-native-svg` paths animated with Reanimated.

## 8. Icons and imagery

- SF Symbols everywhere in chrome, weight matched to the adjacent text; `.fill` variants for selected tabs [doc]. Expo: `expo-symbols`. No Ionicons or emoji as UI icons.
- Real identity imagery over generic icons: avatars, merchant logos, app icons, favicons, photos (Copilot, Opal, Airbnb) [obs].
- Brand illustration or 3D objects belong in the content, sparingly (Airbnb's 3D tab icons are the exception that defines its brand) [obs].
