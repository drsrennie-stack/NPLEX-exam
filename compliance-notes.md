# Accessibility compliance notes

- Project: NPLEX Part I Collaborative Board Review, student web app (MedMasters Collaborative)
- Author: Dr. Sharilyn Rennie
- Files covered: `index.html` (the whole app), `nplex-content.js` (generated data, built by `tools/build_bundle.py`), `nplex-competencies.js` (blueprint data)
- Date: 2026-10-07
- Target: WCAG 2.2 Level AA

## Per-criterion status

| Criterion | Status | Notes |
|---|---|---|
| 1.1.1 Non-text content | Pass | Logo SVG has role="img" and an aria-label. Decorative icons (chevrons, check and X marks) are aria-hidden and always sit next to text. Bar charts have role="img" with an aria-label that gives the number. |
| 1.3.1 Info and relationships | Pass | Landmarks: header, nav, main, footer. One h1 per view, and the heading order was checked by script on every view. Charts are real tables with th scope="col" and scope="row" plus a caption. Answer choices are a radio group inside a fieldset with a legend. Every input has a label (for/id), checked by script. |
| 1.3.2 Meaningful sequence | Pass | DOM order matches visual order. |
| 1.3.4 Orientation | Pass | Works in portrait and landscape. |
| 1.3.5 Identify input purpose | Not applicable | No personal data fields. |
| 1.4.1 Use of color | Pass | Every status chip shows a text label. Exam review marks answers with the words "Correct answer" and "Your answer" plus an icon. Coverage grid cells carry the status in aria-label and title. |
| 1.4.3 Contrast (minimum) | Pass | Every text pair is 4.5:1 or higher in both themes (table below). |
| 1.4.4 Resize text | Pass | rem and em sizing throughout; usable at 200% zoom. |
| 1.4.10 Reflow | Pass | No horizontal page scroll at 390px wide, tested by script on 8 views. Wide tables scroll inside their own keyboard-focusable region. |
| 1.4.11 Non-text contrast | Pass with a note | Focus ring, inputs, and dashed or solid status borders pass 3:1. The light-theme gold "In progress" border (#C9A14A on white) is 2.42:1. This is the brand gold, and the chip always carries its "In progress" text label, so the state never relies on the border alone. |
| 1.4.12 Text spacing | Pass | No fixed-height text containers. |
| 1.4.13 Content on hover or focus | Pass | No hover-only content. |
| 2.1.1 Keyboard | Pass | Everything works by keyboard. Arrow keys move through answer choices; Tab reaches Sure/Not sure and Submit; Enter submits. Collapsibles are buttons. |
| 2.1.2 No keyboard trap | Pass | No modals or traps. Confirmations are built into the page. |
| 2.2.1 Timing adjustable | Pass with a note | Practice timing is optional (off by default). The diagnostic is untimed. The full exams are timed on purpose to mirror the real exam, and the clock can be hidden. Sessions save and resume after reload. |
| 2.2.2 Pause, stop, hide | Pass | Brain dump timer has start, pause, reset, and hide. No auto-moving content. |
| 2.3.1 Three flashes | Pass | Nothing flashes. |
| 2.4.1 Bypass blocks | Pass | Skip link is the first Tab stop and moves focus to main (verified by script). |
| 2.4.2 Page titled | Pass | document.title updates on every view. |
| 2.4.3 Focus order | Pass | On a view change, focus moves to the h1 (or to the question stem on question screens, or to the feedback heading after Submit). |
| 2.4.4 Link purpose | Pass | Link text names the unit or action. External video links say they open in a new tab (screen reader text). |
| 2.4.6 Headings and labels | Pass | Plain question-style headings. |
| 2.4.7 Focus visible | Pass | 3px terracotta outline, 3px offset, on :focus-visible. |
| 2.4.11 Focus not obscured | Pass | No sticky or fixed overlays. |
| 2.5.3 Label in name | Pass | Accessible names start with the visible text. |
| 2.5.7 Dragging movements | Not applicable | No dragging. |
| 2.5.8 Target size (minimum) | Pass | Buttons 36 to 44px tall; question navigator buttons 42px; checkboxes sit inside larger clickable labels. |
| 3.1.1 Language of page | Pass | html lang="en". |
| 3.2.1 / 3.2.2 On focus, on input | Pass | No context change on focus. Changing a filter re-renders the form in place and keeps focus on the same control. |
| 3.2.6 Consistent help | Not applicable | No help mechanism. |
| 3.3.1 Error identification | Pass | Missing answer, missing confidence, or empty filters show a text message in a role="alert" region. |
| 3.3.2 Labels or instructions | Pass | Every control is labeled; short instructions on each view. |
| 3.3.7 Redundant entry | Pass | Nothing is asked twice. |
| 3.3.8 Accessible authentication | Not applicable | No login. |
| 4.1.2 Name, role, value | Pass | aria-expanded on every collapsible, aria-pressed on toggle buttons (theme, tabs, flag, hide clock, review filter), aria-current="page" on the active nav item, aria-current="step" in the question navigator. |
| 4.1.3 Status messages | Pass | One aria-live="polite" region announces view changes, results of Submit, saved scores, timer events, and theme changes. |
| Reduced motion | Pass | prefers-reduced-motion turns off all transitions and the hover lift. |

## Color contrast

Computed with the WCAG 2.x relative luminance formula (script in the build session). Semi-transparent colors were blended over their background first. Text needs 4.5:1; non-text borders need 3:1.

| Theme | Foreground | Background | Ratio | Result |
|---|---|---|---|---|
| Light | Text navy #0B1530 | page #FFFFFF | 18.04:1 | Pass |
| Light | Text navy #0B1530 | soft #FAFAF9 | 17.27:1 | Pass |
| Light | Secondary rgba(11,21,48,.72) | page #FFFFFF | 7.23:1 | Pass |
| Light | Secondary rgba(11,21,48,.72) | soft #FAFAF9 | 7.12:1 | Pass |
| Light | Terracotta #8B3A2E (eyebrows, links) | page #FFFFFF | 7.66:1 | Pass |
| Light | Terracotta #8B3A2E (eyebrows, links) | soft #FAFAF9 | 7.33:1 | Pass |
| Light | Terracotta hover #6B2A20 | page #FFFFFF | 10.62:1 | Pass |
| Light | Terracotta hover #6B2A20 | soft #FAFAF9 | 10.17:1 | Pass |
| Light | White on navy button | #0B1530 | 18.04:1 | Pass |
| Light | White on navy button hover | #1C2A4E | 14.09:1 | Pass |
| Light | White on terracotta button | #8B3A2E | 7.66:1 | Pass |
| Light | White on terracotta button hover | #6B2A20 | 10.62:1 | Pass |
| Light | Navy on mastered fill (navy at 7%) | blended #EEEFF1 | 15.68:1 | Pass |
| Light | Strong border rgba(11,21,48,.55) (non-text) | page #FFFFFF | 4.05:1 | Pass |
| Light | Gold border #C9A14A (non-text) | page #FFFFFF | 2.42:1 | See 1.4.11 note |
| Dark | Text #EEF1F6 | page #060A18 | 17.43:1 | Pass |
| Dark | Text #EEF1F6 | soft #0A1222 | 16.52:1 | Pass |
| Dark | Text #EEF1F6 | card #0E1A2E | 15.38:1 | Pass |
| Dark | Text #EEF1F6 | raised #16243B | 13.74:1 | Pass |
| Dark | Secondary #B6C0D0 | page #060A18 | 10.75:1 | Pass |
| Dark | Secondary #B6C0D0 | soft #0A1222 | 10.19:1 | Pass |
| Dark | Secondary #B6C0D0 | card #0E1A2E | 9.49:1 | Pass |
| Dark | Secondary #B6C0D0 | raised #16243B | 8.48:1 | Pass |
| Dark | Terracotta-light #E09A8C | page #060A18 | 8.62:1 | Pass |
| Dark | Terracotta-light #E09A8C | soft #0A1222 | 8.17:1 | Pass |
| Dark | Terracotta-light #E09A8C | card #0E1A2E | 7.60:1 | Pass |
| Dark | Terracotta-light #E09A8C | raised #16243B | 6.79:1 | Pass |
| Dark | Link hover #EDB8AE | page #060A18 | 11.34:1 | Pass |
| Dark | Link hover #EDB8AE | card #0E1A2E | 10.01:1 | Pass |
| Dark | #060A18 on light button | #EEF1F6 | 17.43:1 | Pass |
| Dark | #060A18 on terracotta button | #E09A8C | 8.62:1 | Pass |
| Dark | #060A18 on terracotta button hover | #EDB8AE | 11.34:1 | Pass |
| Dark | Text on mastered fill (light at 10%) | blended over #0E1A2E | 11.77:1 | Pass |
| Dark | Gold border #DCB45C (non-text) | card #0E1A2E | 8.89:1 | Pass |
| Dark | Border rgba(255,255,255,.45) (non-text) | card #0E1A2E | 4.43:1 | Pass |

## Keyboard navigation flow (verified by script)

1. First Tab reaches "Skip to main content"; Enter moves focus to main.
2. Header: brand link, then the theme buttons (System, Light, Dark), then the six nav links.
3. Path view: week buttons expand and collapse with Enter or Space; step checkboxes toggle with Space.
4. Question screen: focus lands on the question stem. Arrow keys choose an answer, Tab moves to Sure/Not sure, then Submit, Flag, Previous, Next, the question navigator, and Finish. After Submit in tutor mode, focus moves to the feedback heading.
5. Finish asks for confirmation inside the page (no browser dialog), and focus moves to the confirm button.
6. Results: filter buttons (Missed, Flagged, All) and each question review expand by keyboard.

## Screen reader notes

Automated checks only so far: Playwright scripts checked labels, duplicate ids, heading order, one h1 per view, button names, aria-expanded on collapsibles, no italic text, and no en or em dashes in visible text. The live region and focus moves were checked by reading the DOM. A manual pass with NVDA (Windows, Firefox or Chrome) and VoiceOver (macOS and iOS Safari) is still needed before launch, especially for the question radio group, the timer announcements, and the results page.

## Known limitations

- Progress is stored in the browser only (localStorage). Clearing site data, private windows, or a different device starts fresh. Some LMS iframes block storage; the app then keeps progress in memory for the visit only.
- The full exams are timed on purpose, as on the real exam. The clock can be hidden but not extended.
- Until the case bank covers every system, Forms 1 to 3 run as previews using the systems that are ready, with 90 seconds per question.
- Fonts load from Google Fonts. If blocked, the app falls back to system sans-serif fonts.
- Embedded third-party videos are links that open YouTube in a new tab; their accessibility depends on YouTube.

## Reviewer

Automated review: Claude (AI assistant), 2026-10-07. Human review pending: Dr. Sharilyn Rennie.
