# Building it in React Native / Expo (SDK 58, Nov 2026)

How to get each native iPhone pattern in Expo. API names were checked against current docs (docs.expo.dev, reactnavigation.org, Software Mansion and Shopify docs) on 2026-11-21; nothing here was tested on a device. Expo SDK 58 (2026-10-15) targets iOS 27 with React Native 0.88, Reanimated 4.7, Gesture Handler 3.3, react-native-screens 4.30, FlashList 2.3, keyboard-controller 1.22, `@expo/ui` 58 and `expo-widgets` 58. Install with `npx expo install` so versions match. Motion (springs, press feedback, gesture recipes, haptic moments, reduced motion) is in `animate-expo`; this file does not repeat it.

## Rule → API, the short table

| Rule in this skill | Expo |
|---|---|
| 3-5 native tabs, Search trailing, minimize on scroll | `NativeTabs` from `expo-router/native-tabs`, `role="search"` trigger, `minimizeBehavior="onScrollDown"` |
| Persistent status above the tab bar (running job, player) | `NativeTabs.BottomAccessory` (two instances render: keep state outside) |
| Large title on tab roots, collapsing | native `Stack`, `headerLargeTitleEnabled: true`, scroll view first child with `contentInsetAdjustmentBehavior="automatic"` |
| Glass nav buttons and pull-down menus | `Stack.Toolbar` with `Stack.Toolbar.Button icon="<sf symbol>"`, `Stack.Toolbar.Menu` |
| Search at the bottom | `role="search"` tab, or `Stack.SearchBar` / `headerSearchBarOptions` (with `allowToolbarIntegration`) |
| Sheet with detents for a detour | `presentation: 'formSheet'`, `sheetAllowedDetents: [0.5, 1]`, `sheetGrabberVisible: true`; `usePreventRemove` on dirty forms |
| Multi-step flow over the app | `presentation: 'modal'` with its own stack |
| Immersive or blocking screen | `presentation: 'fullScreenModal'` |
| Persistent map-style sheet with a peek | `@gorhom/bottom-sheet` (the one case a JS sheet is right) |
| Long-press menu with preview on rows that open something | `Link` + `Link.Trigger` + `Link.Preview` + `Link.Menu` |
| Long-press menu elsewhere, pull-down menus in content | `@expo/ui/swift-ui` `ContextMenu`, `Menu` |
| Switch, segmented control, date picker, settings form | `@expo/ui/swift-ui` `Toggle`, `Picker` + `pickerStyle('segmented')`, `DatePicker`, `Form`/`Section` |
| Data lists | FlashList v2 (`@shopify/flash-list`); chat: Legend List |
| Swipe actions | FlashList rows: `ReanimatedSwipeable` from `react-native-gesture-handler/ReanimatedSwipeable`; SwiftUI list: `@expo/ui` `SwipeActions` |
| Reorder | `@expo/ui` `List` with `onMove`, or `react-native-reorderable-list` / `react-native-sortables` |
| Pull to refresh | `RefreshControl` |
| Semantic colours, dark mode | `Color.ios.*` (expo-router), `DynamicColorIOS` for custom pairs, `ThemeProvider` with `DarkTheme`/`DefaultTheme` |
| Dynamic Type per role | `dynamicTypeRamp` on every `Text` role; `maxFontSizeMultiplier` only on chrome |
| Tabular numbers | `fontVariant: ['tabular-nums']` |
| SF Symbols | `SymbolView` from `expo-symbols` (`.fill` when selected) |
| Glass on a custom floating control | `GlassView` from `expo-glass-effect` (never on content; never animate its opacity) |
| Keyboard never covers the commit | `KeyboardProvider` at the root; `KeyboardAwareScrollView`, `KeyboardStickyView`, `KeyboardToolbar` |
| Haptics with meaning | `expo-haptics`: `notificationAsync(Success/Warning/Error)`, `selectionAsync()`, `impactAsync(Light)` |
| Notification actions | `expo-notifications` `setNotificationCategoryAsync` |
| Widget, Live Activity | `expo-widgets` (`createWidget`, `createLiveActivity`) |
| Layered app icon | Icon Composer `.icon` in `ios.icon` |

## 1. Navigation (expo-router 58)

| Pattern | Library / API | Key options | Gotchas | Src |
|---|---|---|---|---|
| Push stack, native back swipe | `Stack` from `expo-router` (a native UINavigationController via react-native-screens) | `gestureEnabled` (default true), `fullScreenGestureEnabled` (swipe back from anywhere; changes the animation to `simple_push`), `headerBackButtonDisplayMode: 'minimal'`, `headerBackButtonMenuEnabled` (long-press history menu, default true) | Do not replace it with `expo-router/js-stack` (the JS stack). Doing so loses Liquid Glass headers and the native back gesture. The docs offer it only as an opt-out of Liquid Glass. | [doc] https://docs.expo.dev/router/advanced/stack |
| iOS 26+ header look | Default in SDK 58 | On iOS 26+, `headerTransparent` now defaults to `true` when Liquid Glass is available: a glass header with content running underneath it. `headerUserInterfaceStyle: 'light' \| 'dark'` per screen (new in SDK 58) | Content hides under the header unless the root scroll view sets `contentInsetAdjustmentBehavior="automatic"`. A screen without a scroll view should set `headerTransparent: false`. **Do not use `SafeAreaView` to push content below the header**: it applies only the status-bar inset, or doubles the inset under an opaque header. On iOS 26+ headers use the system font; set `fontFamily` in `headerTitleStyle` / `headerLargeTitleStyle` to override. `enableLegacyHeaderAppearance()` exists but is deprecated. The options table on the Stack page still says the default is `false`; the SDK 58 migration guide is the newer source. | [doc] https://docs.expo.dev/router/migrate/sdk-57-to-58 |
| Large title that collapses on scroll | `headerLargeTitleEnabled: true`, or the composition form `<Stack.Title large>` | `headerLargeStyle` ({backgroundColor}), `headerLargeTitleStyle` (fontFamily, fontSize, fontWeight, color), `headerLargeTitleShadowVisible` | It collapses only if a `ScrollView` / `FlatList` is the **first child** of the screen. A wrapper needs `collapsable={false}`. It does not collapse if the content is shorter than the screen. `headerLargeTitle` is deprecated. | [doc] https://docs.expo.dev/router/advanced/stack#large-title-does-not-collapse-when-scrolling |
| Header search bar | `headerSearchBarOptions` (options API) or `<Stack.SearchBar placeholder onChangeText />` | `placement`: `automatic` (default), `stacked`, `integrated`, `integratedButton`, `integratedCentered` (the last three are iOS 26+; `inline` is deprecated). Also `hideWhenScrolling` (default true), `obscureBackground`, `allowToolbarIntegration` (default true: on iPhone the system may move the search bar into the bottom toolbar). `Stack.Toolbar.SearchBarSlot` puts it in the bottom toolbar on iOS 26+. | Needs `contentInsetAdjustmentBehavior="automatic"` on the scroll view. The Stack guide marks the composition components (`Stack.Title`, `Stack.SearchBar`) as **alpha**; the options API is the stable fallback. | [doc] https://docs.expo.dev/versions/latest/sdk/router/stack ; [doc] https://reactnavigation.org/docs/native-stack-navigator (8.x, `placement` list) |
| Header buttons and pull-down menus | `<Stack.Toolbar placement="left" \| "right">` with `Stack.Toolbar.Button icon="<SF Symbol>"`, `Stack.Toolbar.Menu icon="ellipsis.circle"`, `Stack.Toolbar.MenuAction` (`isOn`, `destructive`, `icon`), a nested `Stack.Toolbar.Menu inline title="Sort By"` for an inline section, `Stack.Toolbar.Badge`, `Stack.Toolbar.Spacer`, `Stack.Toolbar.View` (custom RN view) | Buttons and menus get Liquid Glass capsules for free. `hidden` toggles items without remounting. | **Stable in SDK 58** [doc changelog]. Badges work only in header placements. A bottom toolbar can only be declared in a page file, not a layout. Toolbars cannot be nested. On iOS 26+ the system collapses right-side items into an overflow menu when space runs out (`visibilityPriority` is iOS 27+). | [doc] https://docs.expo.dev/router/advanced/stack-toolbar ; [doc] https://reactnavigation.org/docs/native-stack-navigator |
| Bottom toolbar (Mail / Notes style) | `<Stack.Toolbar>` (default placement is `bottom`) | Flexible `Stack.Toolbar.Spacer` with no width on iOS | Page components only. No badges. | [doc] same |
| Native tab bar (Liquid Glass) | `NativeTabs` from **`expo-router/native-tabs`** (SDK 58; earlier SDKs used `unstable-native-tabs`). Children: `NativeTabs.Trigger name`, `.Trigger.Icon sf={{default:'house', selected:'house.fill'}} md="home"`, `.Trigger.Label`, `.Trigger.Badge` | `tintColor`, `labelStyle`, `hidden` (whole bar), `disableHiddenAnimation`, per-trigger `disablePopToTop` and `disableScrollToTop` | Every tab screen renders eagerly; defer heavy content with `useIsFocused` or a first-focus flag. You cannot measure the bar's height. No nested native tabs. `backgroundColor` / `blurEffect` have no effect on iOS 26 (the system draws the glass). **Wrap the app in `ThemeProvider` (from `expo-router`) with `DarkTheme` / `DefaultTheme`**, or you get a white flash and flickering glass buttons in dark mode. The tab's root `ScrollView` must be the first child (or the wrapper needs `collapsable={false}`), or scroll-to-top and minimize stop working. **FlatList does not support scroll-to-top or minimize-on-scroll.** | [doc] https://docs.expo.dev/router/advanced/native-tabs |
| Tab bar minimizes on scroll | `<NativeTabs minimizeBehavior="onScrollDown">` | `'never' \| 'automatic' \| 'onScrollDown' \| 'onScrollUp'`; iOS 26+ | Needs a ScrollView-based list (see the FlatList limit above). | [doc] https://docs.expo.dev/versions/latest/sdk/router/native-tabs |
| Search tab (separate glass circle) | `<NativeTabs.Trigger name="search" role="search">`, with `search/_layout.tsx` = `<Stack />` and the screen using `Stack.SearchBar` | In SDK 58, selecting the tab activates the field and opens the keyboard (iOS 26.1+). Opt out with `disableAutomaticSearchActivation`. | Changing `role` remounts the tab. On iOS 27 the tab shows separately only while search activation is on. | [doc] same + migration guide |
| Bottom accessory (mini player / "now running" strip) | `<NativeTabs.BottomAccessory>` | `NativeTabs.BottomAccessory.usePlacement()` returns `'regular' \| 'inline'` | **Two instances render at once**, so keep its state outside the accessory. | [doc] https://docs.expo.dev/router/advanced/native-tabs#bottom-accessory |
| Prominent tab / sidebar | `prominent` on a trigger; `preferredPlacement="sidebar" \| "tabBar"` | Compile with Xcode 27; takes effect on iOS 27+ | Only one tab can be prominent. | [doc] same |
| Sheet with detents | `presentation: 'formSheet'` on the `Stack.Screen` | `sheetAllowedDetents: [0.25, 0.5, 1]` or `'fitToContents'`, `sheetInitialDetentIndex` (number or `'last'`), `sheetGrabberVisible` (default false), `sheetCornerRadius`, `sheetLargestUndimmedDetentIndex` (`'none'` / `'last'` / index), `sheetExpandsWhenScrolledToEdge` (default true) | The detent array must be ascending. `fitToContents` cannot use `flex: 1` and needs explicit content size; numeric detents can use `flex: 1` (SDK 55+). For a Liquid Glass sheet background set `contentStyle: { backgroundColor: 'transparent' }`. The Platform column in the Stack options table says "Android" for these options; that is a doc error, and the modals guide shows them on iOS. | [doc] https://docs.expo.dev/router/advanced/modals#form-sheet-presentation ; [doc] expo skill visual-effects.md |
| Page sheet / modal / full-screen cover | `presentation: 'modal'` (page sheet that swipes down to dismiss; can hold a nested stack), `'fullScreenModal'` (UIModalPresentationFullScreen, no swipe), `'transparentModal'`, `'containedModal'` | iOS controls the duration of modal and sheet animations; it cannot be changed | Use `usePreventRemove` from `expo-router` to guard unsaved edits on swipe-down. | [doc] https://docs.expo.dev/router/advanced/modals#presentation-options |
| Zoom transition (card to detail) | `<Link href asChild><Link.AppleZoom>…</Link.AppleZoom></Link>`; `Link.AppleZoomTarget` on the destination; `usePreventZoomTransitionDismissal()` | `alignmentRect`, `unstable_dismissalBoundsRect` | **Alpha**, iOS 18+. Avoid it between screens that have headers (known glitches). There is about 1s of latency on rapid open and close (expo/expo#42797). Combined with `Link.Preview`, the target must be modal. Only one child is allowed. | [doc] https://docs.expo.dev/router/advanced/zoom-transition |
| Peek preview and context menu on a link | `<Link href><Link.Trigger>…</Link.Trigger><Link.Preview /><Link.Menu><Link.MenuAction title icon destructive onPress/></Link.Menu></Link>`; nest `Link.Menu title icon` for a submenu | `Link.Preview style={{width,height}}` or custom children; `useIsPreview()` | iOS only. `replace` is not supported. The lifted child gets rounded corners: **set `borderRadius` on the `Link.Trigger` child** to keep your own radius. A missing `Link.Trigger` throws. | [doc] https://docs.expo.dev/router/reference/link-preview |
| Pending-navigation feedback | `router.setTransitionMode('always')`, `unstable_useIsNavigating()` | Modes: `preload-only` (default), `always`, `never` | Experimental, SDK 58. | [doc] https://docs.expo.dev/router/advanced/navigation-transitions |
| Back destination for deep links | `export const unstable_settings = { anchor: 'index' }` | `{ withAnchor: true }` on imperative navigation | The `initialRouteName` prop is removed in SDK 58. | [doc] migration guide |

**Rules**
- Use the native `Stack` plus `NativeTabs` and never a JS-drawn bar, because Liquid Glass, minimize-on-scroll, the search tab, back-swipe and the back-button history menu come only from the native controllers.
- Make the screen's scroll view its first child and give it `contentInsetAdjustmentBehavior="automatic"`, because large-title collapse, glass header insets, tab scroll-to-top and tab minimize all depend on it.
- Use `formSheet` with detents for anything that is a task on top of context (filters, quick edit, pickers). Use `modal` for a multi-step flow with its own stack. Use `fullScreenModal` only for immersive or blocking flows. This matches how UIKit apps split them, and swipe-to-dismiss comes for free.

---

## 2. Native UI pieces

| Pattern | Library / API | Key options | Gotchas | Src |
|---|---|---|---|---|
| SwiftUI components inside RN | `@expo/ui/swift-ui`; every tree is wrapped in `<Host>` | Components: Alert, BottomSheet, Button, ColorPicker, ConfirmationDialog, ContextMenu, ControlGroup, DatePicker, DisclosureGroup, Form, Gauge, Label, List (with `onMove`, `onDelete`, `editMode`, `refreshable`, `listStyle`), Menu, NavigationStack and NavigationSplitView (SDK 58), Picker, Popover, ProgressView, Section, SecureField, Slider, SwipeActions, TabView, Text, TextField, Toggle, Toolbar, plus a large modifier set (`glassEffect`, `presentationDetents`, `redacted`, `monospacedDigit`, `searchable`, `scrollEdgeEffectStyle`…) | Yoga flexbox stops at `Host`: lay out inside with `HStack` / `VStack`. RN children inside SwiftUI are wrapped automatically; SDK 58 fixed their measuring and touches (`RNHostView`). Segmented, wheel and date pickers stretch to their given width, so `matchContents` collapses them; give the `Host` a size. Works in Expo Go (SDK 56+). | [doc] https://docs.expo.dev/versions/latest/sdk/ui ; https://docs.expo.dev/versions/latest/sdk/ui/swift-ui ; changelog SDK 58 |
| Cross-platform forms of the same | `@expo/ui` Universal (BottomSheet, Button, Checkbox, FieldGroup, List/ListItem, Picker, Slider, Switch, TextInput…) and drop-in replacements (BottomSheet compatible with @gorhom, DateTimePicker, Menu, Picker, SegmentedControl, Slider, PagerView, MaskedView) | | The drop-in BottomSheet does not support `BottomSheetFlashList`, `BottomSheetVirtualizedList`, `BottomSheetFooter`, `useBottomSheetSpringConfigs` and similar, or a persistent inline peek. On iOS, a sheet on top of another must be **nested** inside the first one's content. | [doc] https://docs.expo.dev/versions/latest/sdk/ui/drop-in-replacements/bottomsheet |
| Liquid Glass surface or button | `GlassView` and `GlassContainer` (`spacing`, which merges shapes) from `expo-glass-effect` | `glassEffectStyle: 'regular' \| 'clear' \| 'none'` or `{style, animate, animationDuration}`; `isInteractive` (controls only); `tintColor`; `colorScheme: 'auto' \| 'light' \| 'dark'`. Guards: `isLiquidGlassAvailable() && isGlassEffectAPIAvailable()` | iOS 26+; falls back to a plain View elsewhere. **Never animate `opacity` on a GlassView or its ancestors** (glass stops rendering at low alpha); animate `glassEffectStyle` with `animate: true` instead. Never put `overflow: 'hidden'` on it or an ancestor (that clips the rim highlight). With Reduce Transparency on (`AccessibilityInfo.isReduceTransparencyEnabled()`), use a solid `systemBackground`. SwiftUI-side glass is available as the `glassEffect` modifier in @expo/ui. | [doc] https://docs.expo.dev/versions/latest/sdk/glass-effect ; [doc] expo skill visual-effects.md |
| SF Symbols | `SymbolView` from `expo-symbols` | `name` (or `{ios, android, web}`), `size`, `tintColor`, `weight` (ultraLight…black), `scale` (small/medium/large), `type: 'monochrome' \| 'hierarchical' \| 'palette' \| 'multicolor'`, `colors`, `animationSpec` (`bounce` / `pulse` / `scale`, variable colour), `fallback` | Apple-only: give Android a Material name. Match the symbol weight to the adjacent text weight. Use `.fill` for selected states. In SDK 58 it is an optional peer of the router (needed for Android `md` tab icons). | [doc] https://docs.expo.dev/versions/latest/sdk/symbols ; expo skill icons.md |
| Classic blur (pre-26 fallback, overlays) | `BlurView` from `expo-blur` | `tint`: prefer `systemMaterial`, `systemThinMaterial`, `systemUltraThinMaterial`, `systemThickMaterial`, `systemChromeMaterial` (these adapt to dark mode); `intensity` 0–100 | Rounded corners need `overflow: 'hidden'`. Android needs `BlurTargetView` (SDK 55+). Do not animate intensity (animate-expo). | [doc] https://docs.expo.dev/versions/latest/sdk/blur-view |
| Long-press context menu on any view | `Link.Menu` / `Link.Preview` when the item navigates. Otherwise @expo/ui `ContextMenu` with `ContextMenu.Trigger`, `ContextMenu.Items` (Buttons with `systemImage`, `role="destructive"`, nested `Menu`, `Section`, `Divider`, `Toggle`, `Picker`) and `ContextMenu.Preview` | | Zeego (v3.0.6, last published 2025-03, depends on react-native-ios-context-menu) still works but is now the third choice; the first-party options cover it. | [doc] https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/contextmenu ; npm |
| Pull-down (tap) menu | Header: `Stack.Toolbar.Menu`. In content: @expo/ui `Menu` ("For single-tap menu interactions, use Menu") | `menuOrder`, `menuIndicator`, `menuActionDismissBehavior` modifiers | | [doc] contextmenu page |
| Date / time picker | @expo/ui `DatePicker` | `selection`, `onDateChange`, `displayedComponents: ['date'] \| ['hourAndMinute']`, `title`, `datePickerStyle(...)` modifier (compact / graphical / wheel) | Or `@react-native-community/datetimepicker` 9.2.1 (`mode`, `display: 'compact' \| 'inline' \| 'spinner'`, `minuteInterval`): native and with built-in haptics. Do not add your own haptic. | [doc] https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/datepicker ; expo skill controls.md |
| Segmented control | @expo/ui `Picker` with `modifiers={[pickerStyle('segmented')]}` and `tag(value)` on each `Text` | | Or `@react-native-segmented-control/segmented-control` (`values`, `selectedIndex`, icon segments). Keep it to 4 options or fewer with 1–2 word labels, and do not recolour it. | [doc] https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/picker ; controls.md |
| Switch | @expo/ui `Toggle isOn onIsOnChange label systemImage`, or RN `Switch` | | Do not recolour (native dark mode, built-in haptic). | [doc] https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/toggle |
| Grouped settings form | @expo/ui `Form` / `Section` (SwiftUI), or Universal `FieldGroup` | | Best for short, fixed rows such as Settings. | [doc] ui overview |
| Bottom sheet | Route sheet: `presentation: 'formSheet'`. In-place sheet: @expo/ui `BottomSheet` (`isPresented`, `onIsPresentedChange`, `presentationDetents(['medium','large'])`, `presentationDragIndicator`, `presentationBackgroundInteraction`, `interactiveDismissDisabled`) | | `@gorhom/bottom-sheet` 5.2.14 (last release 2026-05) is a JS sheet. Keep it only for a persistent, non-modal peek sheet (Maps style), which the native options do not offer. | [doc] https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/bottomsheet ; npm |
| Alerts and action sheets | RN `Alert.alert`, or @expo/ui `Alert` / `ConfirmationDialog` | | Confirm destructive actions with ConfirmationDialog anchored to the source. | [doc] ui overview |

**Rules**
- For any control (switch, picker, segmented, date, slider, menu, sheet), use the first-party native control (`@expo/ui` or the router's) before a JS library. Expo's own agent skill says "check `expo-ui` first", because native controls bring haptics, accessibility, dark mode and Liquid Glass for free [doc expo-native-ui SKILL.md].
- Treat Liquid Glass as a material for controls that float over content (buttons, toolbars, the tab bar). Do not use it for content cards, because Apple reserves it for the navigation layer and it costs readability. Always ship the Reduce Transparency fallback.

---

## 3. Lists

| Pattern | Library / API | Key options | Gotchas | Src |
|---|---|---|---|---|
| Long, virtualized list | **FlashList v2** (`@shopify/flash-list` ~2.3.2): JS-only, New Architecture only | No `estimatedItemSize` needed. `getItemType` gives separate recycling pools. `maintainVisibleContentPosition` is on by default. `masonry`. `stickyHeaderIndices` | Recycling means a row's local state leaks between rows: keep state in data. NativeTabs scroll-to-top and minimize are only guaranteed for ScrollView-based lists, so test them with FlashList (the docs call out FlatList). | [doc] https://github.com/Shopify/flash-list README ; https://docs.expo.dev/versions/latest/sdk/flash-list |
| Chat or bidirectional list | **Legend List** (`@legendapp/list` 3.7.x, import `@legendapp/list/react-native`) | `alignItemsAtEnd`, `maintainScrollAtEnd`, `maintainVisibleContentPosition`, `recycleItems` (default false) | Not bundled by Expo; plain `npm install`. Pick it over FlashList only for chat or infinite lists in both directions. | [doc] https://github.com/LegendApp/legend-list README |
| Short list (< ~100 rows), settings | `ScrollView` + map, `FlatList` / `SectionList`, or @expo/ui SwiftUI `List` | SwiftUI `List` now recycles with `data` + `keyExtractor` + `List.ForEach` (SDK 58) | `FlatList` is fine for short lists, but see the NativeTabs limits. | [doc] changelog SDK 58 |
| Section headers | `SectionList` `stickySectionHeadersEnabled` / FlashList `stickyHeaderIndices` / SwiftUI `Section` + `headerProminence` | | iOS uses plain-style sticky headers, or inset-grouped headers that do not stick. | [doc] / [know] |
| Swipe actions | SwiftUI: @expo/ui `SwipeActions` + `SwipeActions.Actions edge="leading" \| "trailing" allowsFullSwipe` with `Button systemImage role="destructive"`, inside `List` / `Section`. RN rows: `ReanimatedSwipeable` (`import Swipeable from 'react-native-gesture-handler/ReanimatedSwipeable'`) with `renderLeftActions` / `renderRightActions`, `friction`, `leftThreshold` / `rightThreshold`, `overshootLeft` / `overshootRight`, `overshootFriction`, `onSwipeableOpen` | | The SwiftUI version matches Mail exactly (full swipe, colours, haptic) but needs the list itself in SwiftUI. The RNGH version keeps FlashList rows but you build the full-swipe, haptic and colours yourself (animate-expo has a swipe-to-delete recipe). | [doc] https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/swipeactions ; [doc] RNGH docs `components/reanimated_swipeable.mdx` |
| Drag to reorder | SwiftUI `List` with `onMove` (+ `editMode`, `moveDisabled`). RN: `react-native-reorderable-list` 0.18.3 (FlatList-based) or `react-native-sortables` 1.10.1 (grids and flex, Reanimated) | | `react-native-draggable-flatlist` has had no release since 2025-05; avoid it. | [doc] swift-ui list page ; npm |
| Pull to refresh | `RefreshControl` on the ScrollView / FlashList `refreshControl` (`refreshing`, `onRefresh`, `tintColor`), or the SwiftUI `refreshable` modifier | | Works with large titles: the spinner sits above the title. | [doc] https://reactnative.dev/docs/refreshcontrol |
| Large title collapsing with scroll | The native header (section 1), never a scroll worklet | | See the first-child rule. | [doc] |
| Skeleton / loading placeholder | No native RN skeleton. Use a Reanimated CSS-animation opacity pulse (animate-expo), or `redacted` on @expo/ui SwiftUI views | | Do not show the empty state while the first load is still running [doc expo skill]. | [doc] swift-ui modifiers |

**Rules**
- Default to FlashList v2 for data lists and SwiftUI `List` for short settings-style lists, because FlashList recycles without size estimates and SwiftUI List gives Mail-grade swipe and reorder for free.
- Put destructive swipe actions on the trailing edge and state toggles (pin, read) on the leading edge, each with an SF Symbol, because that is the Mail and Reminders convention users already know [know].

---

## 4. Text and colour

| Pattern | API | Key options | Gotchas | Src |
|---|---|---|---|---|
| Dynamic Type | `Text` `allowFontScaling` (on by default), `maxFontSizeMultiplier` (≥1; 0 = no cap), **`dynamicTypeRamp`** (iOS: `caption2` … `largeTitle`, default `body`, scales a fixed size along Apple's ramp for that style), `useWindowDimensions().fontScale` | | Without `dynamicTypeRamp`, RN scales every size linearly, so headings grow as much as body text. Set the ramp per role. Cap only chrome text (tab labels, badges) at about 1.3–1.5; never cap body text. Test at the largest accessibility size. | [doc] https://reactnative.dev/docs/text#dynamictyperamp-ios |
| Semantic iOS colours | `Color.ios.label`, `.secondaryLabel`, `.systemBackground`, `.secondarySystemBackground`, `.systemGroupedBackground`, `.separator`, `.systemBlue`… from `expo-router` (a typed `PlatformColor`) | Centralise them in `theme/colors.ts` with `Platform.select({ ios, android: Color.android.dynamic.*, default: hex })` | They are opaque native values: **do not pass them into Reanimated styles**. Some props need a cast to `string` (expo-image `tintColor`). On Android call `useColorScheme()` so components re-render. | [doc] https://docs.expo.dev/router/reference/color ; expo-native-ui SKILL.md |
| Custom light/dark pair | `DynamicColorIOS({ light, dark, highContrastLight?, highContrastDark? })` | | iOS only. | [doc] https://reactnative.dev/docs/dynamiccolorios |
| Dark mode | `useColorScheme()`; set `userInterfaceStyle: "automatic"` in app config; `ThemeProvider` from `expo-router` with `DarkTheme` / `DefaultTheme` | | Without ThemeProvider you get a white flash between screens and tabs and flickering glass buttons [doc native-tabs]. `Appearance.setColorScheme` does not restyle the iOS 26 tab bar. | [doc] https://docs.expo.dev/develop/user-interface/color-themes |
| Tabular numerals | `fontVariant: ['tabular-nums']` (also `lining-nums`, `oldstyle-nums`, `small-caps`); SwiftUI side: `monospacedDigit` modifier | | Use it for every counter, time, amount and table column. | [doc] https://reactnative.dev/docs/text-style-props |
| SF Pro weights | Leave `fontFamily` unset (it resolves to SF Pro, with optical sizes chosen automatically) and use `fontWeight` `'100'`…`'900'` or `'bold'` | | Do not bundle SF Pro yourself. Headers on iOS 26+ use the system font unless you override it. | [doc] / [know] |
| Custom fonts | `expo-font` config plugin (preferred, embedded at build) or `useFonts`; SDK 58 adds **variable fonts** and RN 0.88 adds `fontVariationSettings` on `Text` | | Custom fonts do not get Dynamic Type unless you also use `dynamicTypeRamp`. Apply custom fonts to the header explicitly. | [doc] https://docs.expo.dev/develop/user-interface/fonts ; changelog SDK 58 |
| Copyable data | `<Text selectable>` | | Use it on IDs, emails and error messages [doc expo skill]. | [doc] |

**Rules**
- Use system colours (`Color.ios.*`) and the system font by default. Introduce a brand colour only as the tint, because semantic colours get dark mode, increased contrast and the iOS 26 materials right with no work.
- Give every text role a `dynamicTypeRamp`, because linear scaling breaks the type hierarchy at accessibility sizes.

---

## 5. Input and keyboard

| Pattern | API | Key options | Gotchas | Src |
|---|---|---|---|---|
| Keyboard avoidance (forms) | `react-native-keyboard-controller` (1.22.7 in SDK 58; needs a dev build, Reanimated, and `<KeyboardProvider>` at the root): `KeyboardAwareScrollView bottomOffset`, `KeyboardAvoidingView`, `KeyboardStickyView` (a composer pinned above the keyboard), `KeyboardToolbar` (prev / next / done) | Hooks: `useKeyboardHandler`, `useReanimatedKeyboardAnimation`, `useKeyboardState`. Views: `KeyboardGestureArea` (interactive dismiss), `OverKeyboardView`, `KeyboardExtender`, `KeyboardBackgroundView` | Core RN `KeyboardAvoidingView` is fine for prototypes; set `behavior="padding"` on both platforms. **Never `Keyboard.addListener` + a timing animation** [doc expo skill]. | [doc] https://docs.expo.dev/guides/keyboard-handling ; GitHub docs dir `docs/docs/api` |
| Chat composer | `KeyboardChatScrollView` (`keyboardLiftBehavior: 'always'` and others, `inverted`, `freeze`) | | With an inverted FlashList, raise `drawDistance`. | [doc] keyboard-controller `keyboard-chat-scroll-view.mdx` |
| Accessory bar | `KeyboardToolbar`, or RN `InputAccessoryView` + `inputAccessoryViewID` (iOS); `inputAccessoryViewButtonLabel` | | | [doc] https://reactnative.dev/docs/inputaccessoryview |
| Return keys | `returnKeyType` (`done`, `next`, `search`, `send`, `go`), `returnKeyLabel`, `enablesReturnKeyAutomatically`, `submitBehavior` (`submit` / `blurAndSubmit` / `newline`) | | Chain fields with `next`, then `done` on the last one. | [doc] https://reactnative.dev/docs/textinput |
| Autofill | `autoComplete` (cross-platform, preferred) or iOS `textContentType` (`username`, `password`, `newPassword`, `oneTimeCode`, `emailAddress`…); `passwordRules` with `newPassword` | | Do not set both; `textContentType` wins. | [doc] same |
| Keyboard type and dismissal | `keyboardType`, `keyboardAppearance`, `clearButtonMode`; ScrollView `keyboardDismissMode="interactive"`, `keyboardShouldPersistTaps="handled"` | | The primary action must never sit under the keyboard [doc expo skill]. | [doc] |

**Rules**
- Install keyboard-controller on day one and wrap the root in `KeyboardProvider`, because every form, search and quick-capture screen needs it, and it tracks the keyboard frame by frame on the UI thread.
- Set `keyboardShouldPersistTaps="handled"` and `keyboardDismissMode="interactive"` on scrollable forms, because a first tap that only dismisses the keyboard feels broken.

---

## 6. Feedback

| Pattern | API | Key options | Gotchas | Src |
|---|---|---|---|---|
| Haptics | `expo-haptics`: `Haptics.impactAsync(ImpactFeedbackStyle.Light \| Medium \| Heavy \| Rigid \| Soft)`, `Haptics.notificationAsync(NotificationFeedbackType.Success \| Warning \| Error)`, `Haptics.selectionAsync()`; `performAndroidHapticsAsync(AndroidHaptics.*)` on Android | | Silent in Low Power Mode, with the Taptic Engine off, while the camera is active and during dictation. For custom patterns or haptics on worklets, Expo now points to **Pulsar** (docs.swmansion.com/pulsar). Which moment gets which haptic is in animate-expo §8. | [doc] https://docs.expo.dev/versions/latest/sdk/haptics |
| Springs, CSS transitions, layout animations | Reanimated 4.7 + Worklets 0.13 | See animate-expo §3–6 | | animate-expo |
| Reduced motion | `useReducedMotion()`, `ReduceMotion.System` (Reanimated) | | animate-expo §9 | animate-expo |
| Reduced transparency | `AccessibilityInfo.isReduceTransparencyEnabled()` | | Use a solid surface instead of glass or blur. | [doc] expo skill visual-effects.md |

---

## 7. System surfaces

| Pattern | API | Key options | Gotchas | Src |
|---|---|---|---|---|
| Notification actions | `expo-notifications`: `setNotificationCategoryAsync(identifier, actions[])`, where each action is `{ identifier, buttonTitle, options: { opensAppToForeground, isDestructive, isAuthenticationRequired }, textInput?: { placeholder, submitButtonTitle } }`; set `categoryIdentifier` on the content; handle with `addNotificationResponseReceivedListener` / `useLastNotificationResponse()` | `interruptionLevel: 'passive' \| 'active' \| 'timeSensitive' \| 'critical'`, `threadIdentifier` (grouping), `setBadgeCountAsync`, `requestPermissionsAsync({ ios: { allowProvisional } })` | SDK 58: **foreground notifications show by default** unless `setNotificationHandler` says otherwise (`shouldShowBanner`, `shouldShowList`; `shouldShowAlert` is deprecated). Ask for permission in context, not at launch [know]. | [doc] https://docs.expo.dev/versions/latest/sdk/notifications |
| Home and Lock Screen widgets | **`expo-widgets`** (first-party; iOS, and Android since SDK 58): config-plugin `widgets[]` with `name`, `displayName`, `description`, `ios.supportedFamilies` (`systemSmall`/`Medium`/`Large`, `accessoryCircular`/`Rectangular`/`Inline`), `ios.configuration` (configurable widgets); write layouts as `createWidget(name, Component, initialProps)` with @expo/ui SwiftUI components; update with `updateSnapshot` / `updateTimeline` / `reload` | Interactive `Button` whose `onPress` return value becomes the new props; `widgetsDirectory` for images; `addUserInteractionListener` | Widget components start with the **`'widget'` directive** and run in an isolated runtime: no hooks, no async, no imports, **not even module-level consts**. Every root needs the `containerBackground(..., 'widget')` modifier on iOS 17+. Needs a dev build. | [doc] https://docs.expo.dev/versions/latest/sdk/widgets |
| Live Activities / Dynamic Island | `createLiveActivity(name, Component)` returning `{ banner, compactLeading, compactTrailing, minimal, expandedLeading, expandedTrailing, expandedBottom }`; `.start(props, url, staleDate)`, `instance.update`, `instance.end(dismissalPolicy)`, `getPushToken` / `addPushToStartTokenListener` | Plugin `enablePushNotifications`, `frequentUpdates` | Do **not** add a `widgets[]` entry for a Live Activity. Remote updates use the `liveactivity` push type with topic `<bundle id>.push-type.liveactivity`. | [doc] same |
| Fully custom Swift extensions | `@bacons/apple-targets` 5.0.0 (widgets in Swift, App Clips, share extensions) | | Use it only when expo-widgets' SwiftUI subset is not enough. | npm ; expo skill SKILL.md |
| Siri, Shortcuts, Spotlight | `expo-app-intents` (new in SDK 58): Swift inline modules in `app-intents/`, Spotlight indexing, donations, `appEntityIdentifier()` | | On-screen identification needs iOS 18.4+ and Xcode 27. | [doc] changelog SDK 58 ; https://docs.expo.dev/versions/latest/sdk/app-intents |
| App icon (iOS 26+ Liquid Glass: light, dark, tinted, clear) | Icon Composer's `.icon` directory: `"ios": { "icon": "./assets/app.icon" }` | Icon Composer handles the dark and tinted variants | Supported since SDK 54. | [doc] https://docs.expo.dev/develop/user-interface/splash-screen-and-app-icon |
| Splash screen | `expo-splash-screen` plugin: `image`, `imageWidth`, `backgroundColor`, `dark: { image, backgroundColor }`; runtime `SplashScreen.preventAutoHideAsync()`, `hideAsync()`, `setOptions({ fade: true })` | | PNG only. Test in a release or preview build, not Expo Go or a dev client. | [doc] https://docs.expo.dev/versions/latest/sdk/splash-screen |
| Home-screen quick actions | `expo-quick-actions` 6.0.2 (Evan Bacon): `QuickActions.setItems([...])` with icons `symbol:<sf name>`; hooks for the callback | | Not an `expo-*` SDK package. | [doc] https://github.com/EvanBacon/expo-quick-actions README |
| Share sheet (send) | Text or URL: RN `Share.share({ message, url })`. Files: `Sharing.shareAsync(uri, options)` | | | [doc] https://reactnative.dev/docs/share ; https://docs.expo.dev/versions/latest/sdk/sharing |
| Receive shares (share extension) | `expo-sharing` now has `useIncomingShare()`, `getSharedPayloads()`, `getResolvedSharedPayloadsAsync()` with activation rules | | Needs a dev build. | [doc] sharing page |

---

## 8. Safe areas and insets

| Pattern | API | Gotchas | Src |
|---|---|---|---|
| Content under glass header and tab bar | `contentInsetAdjustmentBehavior="automatic"` on the root ScrollView / FlatList / SectionList / FlashList. NativeTabs enables it automatically for the first ScrollView of each tab on iOS (`disableAutomaticContentInsets` opts out) | With padding plus automatic insets, the **larger** of the padding and the inset is used, not their sum. Pad with `contentContainerStyle`, never padding on the ScrollView itself. | [doc] https://reactnative.dev/docs/scrollview ; native-tabs guide |
| Screens without a header (full-bleed, camera, onboarding) | `useSafeAreaInsets()` / `SafeAreaView` from `react-native-safe-area-context` (never RN's removed `SafeAreaView`) | Do not combine with a stack header (double inset). On web in SDK 58, use CSS `env(safe-area-inset-*)`. | [doc] https://docs.expo.dev/develop/user-interface/safe-areas |
| Edge-to-edge | Default (Android is edge-to-edge; iOS draws under bars) | `statusBarBackgroundColor`, `navigationBarColor` and `statusBarTranslucent` are deprecated. | [doc] stack options table |
| Scroll edge blur under bars | `scrollEdgeEffects` screen option (iOS 26) / SwiftUI `scrollEdgeEffectStyle` | | [doc] stack options table |

---

## Defaults for a new Expo app

**Packages** (install with `npx expo install` so versions match SDK 58):

```
expo-router  @expo/ui  expo-symbols  expo-glass-effect  expo-blur  expo-haptics  expo-image  expo-font
react-native-reanimated  react-native-worklets  react-native-gesture-handler
react-native-safe-area-context  react-native-screens
@shopify/flash-list  react-native-keyboard-controller
expo-notifications  expo-splash-screen  expo-sharing
# only when needed: expo-widgets (widgets / Live Activities), expo-app-intents (Siri),
# expo-quick-actions, react-native-reorderable-list (RN drag reorder), @legendapp/list (chat)
```

**The 10 choices**
1. **Navigation shell**: `NativeTabs` from `expo-router/native-tabs`, each tab holding its own `Stack`, with `minimizeBehavior="onScrollDown"` and a `role="search"` tab. The real Liquid Glass bar, with minimize, the search tab and the bottom accessory, comes free.
2. **Headers**: the native `Stack` with `headerLargeTitleEnabled` on tab roots, `headerBackButtonDisplayMode: 'minimal'` on deeper screens, and `Stack.SearchBar` / `headerSearchBarOptions` for search. Keep the SDK 58 transparent glass header.
3. **Header actions**: `Stack.Toolbar` with SF Symbol `Button`s and a `Menu` (`ellipsis.circle`) for overflow; `Stack.Toolbar` with bottom placement for document-style screens. No custom `headerRight` views.
4. **Every scroll root** is the first child of its screen and has `contentInsetAdjustmentBehavior="automatic"`. Use `useSafeAreaInsets` only on headerless screens.
5. **Theme**: `ThemeProvider` (expo-router) switched by `useColorScheme()`, colours from `Color.ios.*` in one `theme/colors.ts`, one brand tint, the system font, `dynamicTypeRamp` on every text role, `tabular-nums` on numbers.
6. **Overlays**: `presentation: 'formSheet'` with `sheetAllowedDetents` and `sheetGrabberVisible: true` for tasks over context; `modal` for flows; `fullScreenModal` only for immersive or blocking screens; `usePreventRemove` on dirty forms.
7. **Controls**: @expo/ui SwiftUI (`Toggle`, `Picker` segmented or menu, `DatePicker`, `Menu`, `ContextMenu`, `Form` / `Section`, `BottomSheet`) before any community library; `@gorhom/bottom-sheet` only for a persistent peek sheet.
8. **Lists**: FlashList v2 for data, with `RefreshControl`, sticky headers and `ReanimatedSwipeable` rows (trailing destructive, leading toggles); SwiftUI `List` for settings and anything needing native swipe or reorder; `Link.Menu` / `Link.Preview` on rows that navigate.
9. **Input**: `KeyboardProvider` at the root; `KeyboardAwareScrollView` + `KeyboardToolbar` for forms; `KeyboardStickyView` for quick-capture bars; `autoComplete` / `returnKeyType` set on every field.
10. **Feedback and system**: haptics per animate-expo (`selectionAsync` on pickers and toggles you build yourself, `notificationAsync(Success)` on completion); Reanimated 4 for motion; an Icon Composer `.icon` app icon; `expo-widgets` for a home-screen widget when the app has glanceable state.

## Traps (what makes an RN app feel non-native, with the fix)

| Trap | Fix |
|---|---|
| JS tab bar (`Tabs` / a custom bottom bar) on iOS 26+: no glass, no minimize, no search tab | `NativeTabs` from `expo-router/native-tabs` |
| JS stack or custom header: no Liquid Glass, back swipe only from the edge, no back-history menu, a fake large title | Native `Stack` + `headerLargeTitleEnabled`; never `expo-router/js-stack` unless you are opting out of glass on purpose |
| Content hidden under the transparent iOS 26 header, or a doubled top inset | `contentInsetAdjustmentBehavior="automatic"`; never `SafeAreaView` under a header; `headerTransparent: false` for non-scrolling screens |
| Large title will not collapse; tab tap will not scroll to top; tab bar will not minimize | Put the ScrollView first in the screen or add `collapsable={false}` to the wrapper; use a ScrollView-based list, not FlatList, under NativeTabs |
| White flash on push or tab switch in dark mode; flickering glass buttons | Wrap in `ThemeProvider` with `DarkTheme` / `DefaultTheme`; set `contentStyle` background |
| Ionicons or FontAwesome glyphs, emoji as icons | `SymbolView` / `sf` props with weight matched to text; Material names on Android |
| Hard-coded hex greys that are wrong in dark mode or increased contrast | `Color.ios.label` / `secondaryLabel` / `systemBackground` / `separator` |
| Text that does not grow, or grows uniformly so headings swamp body text | Leave `allowFontScaling` on; set `dynamicTypeRamp` per role; cap only chrome text with `maxFontSizeMultiplier` |
| Numbers that jitter as they update | `fontVariant: ['tabular-nums']` |
| JS-drawn switches, segmented controls, date pickers or menus (wrong haptics, wrong press states, no glass) | @expo/ui `Toggle`, `Picker` with `pickerStyle('segmented')`, `DatePicker`, `Menu`, `ContextMenu`; `Stack.Toolbar.Menu` in the header |
| JS bottom sheet for a simple task: wrong spring, no grabber, no system detents | `presentation: 'formSheet'` + `sheetAllowedDetents` + `sheetGrabberVisible` |
| Long-press does nothing, or opens a custom JS popover | `Link.Menu` + `Link.Preview` on navigable rows; @expo/ui `ContextMenu` elsewhere; set `borderRadius` on the trigger child |
| Keyboard covers the input or the Save button, or jumps out of sync | keyboard-controller `KeyboardAwareScrollView` / `KeyboardStickyView`; `keyboardShouldPersistTaps="handled"` |
| Glass that flickers out or loses its rim | Do not animate `opacity` on `GlassView` or its parents (animate `glassEffectStyle`); no `overflow: 'hidden'` around glass; fall back to a solid surface under Reduce Transparency |
| Splash that pops instead of fading; icon that looks flat on iOS 26 | `SplashScreen.setOptions({ fade: true })` + `preventAutoHideAsync`; an Icon Composer `.icon` in `ios.icon` |
| Notification permission prompt at first launch; buttonless notifications | Ask in context; `setNotificationCategoryAsync` with actions; `interruptionLevel` set honestly |

## Updates for animate-expo (out of date as of SDK 58)

- animate-expo imports `NativeTabs` from `expo-router/unstable-native-tabs`. In SDK 58 it is **`expo-router/native-tabs`**, and native tabs are stable [doc migration guide].
- animate-expo writes gestures as `Gesture.Pan()`. SDK 58 bundles **react-native-gesture-handler ~3.3**, whose primary API is hooks: `usePanGesture({...})`, `useTapGesture`, and `useSimultaneousGestures` / `useCompetingGestures` / `useExclusiveGestures` replace `Gesture.Simultaneous` / `Race` / `Exclusive`. The builder API now sits under "legacy gestures" [doc RNGH `guides/upgrading-to-3.mdx`]. That skill's maintainer should update its recipes.
- Its `headerLargeTitleEnabled` advice still holds.
