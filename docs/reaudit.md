# Portfolio re-audit — October 18, 2026

Owner-requested naming: **NCAAB Betting Model**. Primary actions are **Enter the Sportsbook** and **Open the NCAAB Model**. The sportsbook action now opens the application entry page; the public demo is available inside its project disclosure. The four matching project cards and disabled “In development” buttons are preserved.

The owner supplied `https://www.linkedin.com/in/coopergurrie/` and `cooper.gurrie@gmail.com` in this chat. Both are now native contact links, with visible icon/text labels and 44px minimum height. No email was sent.

## Corrected audit findings

- `index.html:42` — Fixed card heights could clip content after text-spacing changes. Replaced them with shared minimum heights and natural growth. Default closed cards remain equal: 350px desktop, 370px tablet, 360px mobile, and 400px at 320px width.
- `index.html:29` — Removed continuous decorative orbit animation. The finite entrance animation and pointer interactions respect reduced motion; decorative SVG remains hidden from assistive technology.
- `index.html:99` — Restored semantic contact anchors using the owner's confirmed addresses; removed the old placeholder behavior.
- `index.html:124` — Gave repeated project disclosures distinct accessible names while retaining their consistent visible label and native Enter/Space behavior.
- `index.html:7` — Updated normal/social descriptions, social image text and alt text to the owner-requested project identity.

Reviewed against the [Web Interface Guidelines](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md), with the owner's design and naming preferences taking precedence over generic style suggestions.

## Verification

- **Seven browser regressions pass** in Edge: skip/focus/disclosures, mouse/Enter project navigation, narrow and expanded layout, media/metadata, reduced motion, mouse/Enter contact activation, and increased text spacing. Email activation was intercepted during testing so no mail client or send operation was triggered.
- **Responsive visual inspection:** 320, 390, 768 and 1440px, plus a 1366 × 768 laptop viewport. All four closed cards share dimensions at each size. Expanded content loads and remains readable.
- **Text spacing:** line height 1.5, letter spacing 0.12em, word spacing 0.16em, and paragraph spacing 2em. No clipped cards or horizontal overflow at the tested widths.
- **Zoom:** 200% CSS zoom in closed and expanded states; no horizontal overflow. This is a reflow simulation, not a native browser-menu zoom test.
- **Accessibility scan:** no violations in the tested WCAG 2 A/AA, 2.1 AA and 2.2 AA rules. The tool still marks part of color analysis incomplete around complex visual content; this is not an accessibility certification. Manual palette calculations and visual review supplement it. Sample text/button contrast ratios range from 4.81:1 to 18.52:1.
- **Links:** sportsbook entry/demo, basketball entry, historical performance and spread-model views all returned HTTP 200 and rendered in a browser. LinkedIn destination uses the exact owner-supplied URL; activation was verified with intercepted navigation, not an authenticated LinkedIn profile check. Email uses the exact supplied `mailto:` address.
- **Assets:** screenshots have alt text, explicit dimensions and lazy loading. Local image/font requests load. Social image is 1200 × 630 and matches the current project name. No portfolio page JavaScript errors were observed.
- **Scope:** no account mutations, production writes, deployment or other application source changes.

## Remaining limits

The linked basketball application and captured screenshot still use their own existing “College Basketball Research” identity. Its separate owner must change that application title if the rename should extend beyond this portfolio. Historical comparisons and model limitations remain disclosed; the portfolio makes no new claim of live recommendations or proven betting returns.

Native browser-menu zoom, screen-reader speech output, Safari and Android Chrome were not tested. No unresolved blocking portfolio issue was found within this audit's scope.

## Subsequent owner edits

Project screenshots and their assets were removed at the owner’s request; earlier screenshot-specific checks are historical. No generated replacement illustration is used. The social preview remains. Both disabled buttons now say “In Development,” “upcoming” is removed from the NBA description, and the biography disclosure follows the contact row. Seven browser checks pass after these edits.
