# Portfolio correction review

Prepared October 18, 2026. See [the latest re-audit](reaudit.md) for subsequent naming, contact and accessibility changes. Portfolio scope only. Auto Instagram Posts has been removed at the owner's request. The Ocho is queued for separate development; its purpose has not been invented.

## Audit status

| ID | Status | Resolution and evidence |
| --- | --- | --- |
| P01 | Fixed | Replaced the original inert spans with native LinkedIn/email anchors using the owner-confirmed profile and address supplied during the latest re-audit. Mouse and Enter activation pass. |
| P02 | Fixed | Auto Instagram Posts removed entirely. The Ocho and NBA Model use the same card format as published projects, with disabled “In development” buttons, as requested in the design revision. The Ocho has explicit scope pending; NBA has a sourced planned purpose. |
| P03 | Fixed | Two published cards lead a uniform four-card grid; The Ocho and NBA follow in matching cards. The redundant project heading, navigation row and hero jump action were removed at the owner’s request. The second published heading is visible in the initial 390 × 844 viewport. |
| P04 | Fixed | NCAAB Betting Model is labeled a public preview; its disclosure states that no validated betting edge is established. Sportsbook access distinguishes the public demo from approved league membership. |
| P05 | Fixed | After restoring contact links, the first card begins around y=226 at 390px and y=278 at 1440px. All four closed cards share dimensions at each breakpoint. Biography follows project content. Browser screenshots cover 320, 390, 768, 1366 × 768, and 1440px layouts. |
| P06 | Fixed | Native disclosures contain two public screenshots and concise case studies covering audience, contribution, design, behavior and limits. The sportsbook screenshot contains synthetic data only. Working demo and historical performance links are enabled. |
| P07 | Fixed | Owner-requested portfolio names are Fantasy Sportsbook and NCAAB Betting Model. Actions are Enter the Sportsbook and Open the NCAAB Model. Demo/performance links are inside disclosures. The basketball destination still has its prior title; see re-audit scope notes. |
| P08 | Fixed | First keyboard stop is a visible-on-focus skip link. Enter moves focus to the projects main landmark; the next Tab reaches the first project’s demo link. |
| P09 | Fixed | Intro states the maker's focus; project disclosures retain contribution context and case studies. Personal biography remains available in a native disclosure below the work. No fabricated release dates or technology claims. |
| P10 | Fixed | Normal/social descriptions agree with project status. New 1200 × 630 social image uses current project names and preview labels. Canonical URL added. The existing production social URL responds 200; new local assets respond 200 through the test server. |

All original observations were checked against the current repository, not assumed from the audit. The original audit was evaluated before implementing the corrections. The owner’s later request for matching cards and development buttons supersedes the original recommendation to demote upcoming work to a compact list. The external demo and basketball research views already existed and were verified before linking them.

## Source and media provenance

- The original portfolio source provides the owner's dynasty-league motivation, sports/data interests, and planned NBA scope.
- The sportsbook's public sign-in page explicitly describes approved membership. Its `/#/demo` route explicitly states that every name, score, balance and ticket is fictional, and that betting, account changes and email delivery are disabled. Captured from a fresh, unauthenticated browser on October 18. No private league pages or member data were accessed for these assets.
- College Basketball Research's public `/#spreads` and `/#performance` routes state retrospective evaluation, uncertainty, no promoted live model, and no validated betting advantage. The image preserves those qualifiers alongside the displayed hypothetical results. No results have been copied into portfolio marketing claims.
- `assets/sportsbook-demo.webp` and `assets/basketball-research.webp` are 1280 × 900 viewport screenshots, converted to WebP. Their HTML dimensions preserve layout; alt text describes the function; captions distinguish demo and research limits. Both load lazily inside the case-study disclosures.
- `assets/cooper-share.png` is a new 1200 × 630 static social graphic consistent with the existing palette and bundled fonts.

## Verification

The site remains a static page with no build step or production dependencies.

Install development requirements, install a Playwright Chromium browser, then run:

```text
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python -m unittest discover -s tests -v
```

Set `BROWSER_CHANNEL=msedge` to use an installed Edge browser. All seven browser regression tests passed in Edge, including contact activation and text-spacing checks, plus: native skip/disclosure behavior; mouse and Enter navigation; narrow and expanded layouts; media and metadata; reduced motion. Navigation tests intercept outbound destinations to avoid app mutations. Separate public browser checks verified real routes and read-only demo tabs.

Additional visual checks: 320/390/768/1440px, short 1366 × 768 laptop, expanded case studies, and 200% CSS zoom. No horizontal overflow in closed or expanded states. The scan found no WCAG A/AA violations; automated contrast analysis had an incomplete result for screenshot content, so the scan is not a blanket accessibility certification. Text and controls were visually reviewed. Native browser-menu zoom, screen-reader speech output, iOS Safari and Android Chrome were not exercised.

The production portfolio remains unchanged until a separate authorized deployment. New media URLs can only be verified in production after that deployment. No sitemap was added because case studies are in-page disclosures, not separate pages; missing robots.txt is not treated as an indexing defect.

## Cross-project link contract

| Destination | Current verified route | Portfolio label |
| --- | --- | --- |
| Public sportsbook demo | `https://sportsbook.coopergurrie.com/#/demo` | Try the public demo |
| Private league access | `https://sportsbook.coopergurrie.com/` | Enter the Sportsbook |
| Basketball entry | `https://cbb.coopergurrie.com/` | Open the NCAAB Model |
| Historical spread comparison | `https://cbb.coopergurrie.com/#spreads` | Compare historical spread models |
| Historical winner performance | `https://cbb.coopergurrie.com/#performance` | Explore historical winner performance |
| Return to portfolio | `https://coopergurrie.com/` | Back to portfolio |

Both applications already show a return link to the portfolio. Preserve these routes or provide redirects when their navigation changes. Portfolio identity uses the owner-requested NCAAB Betting Model name; the destination app still uses its prior title. Cooper Gurrie is the portfolio owner. No messages were sent to other chats; direct owner coordination is still needed to promise long-term route stability or obtain bespoke media. A stable individual-game deep link has not been confirmed and is not invented here. The verified historical comparison and performance destinations work independently of that future link.

## Scoped feature proposals

### Case studies and changelog

Extend the two existing disclosures into dedicated project pages only when there is enough approved release material to justify them. Cooper maintains portfolio summaries; each application owner supplies approved release notes and sanitized media. Dependencies: shipped commit/release references, agreed author contributions, source dates, stable project slugs. Acceptance: each change links to a release, each case study states current limits, navigation works without JavaScript, new pages have canonical URLs and appear in a sitemap. Check links on every portfolio change; review screenshots/status after each application release and at least quarterly. Mark stale content after a failed link check or an app release that changes the depicted behavior. Do not use today's date as a product-release date.

### Public sportsbook demo entry

The minimal integration is implemented using the existing public synthetic route and screenshot. Next increment: obtain the sportsbook owner's commitment to the demo route and a versioned fixture/media contract. Dependencies: synthetic fixture provenance, no account mutations, explicit disabled transaction behavior, route redirect policy. Acceptance: anonymous visitors can view markets, tickets and standings; the demo cannot submit bets or change balances; no private data is returned; member sign-in remains separate. The portfolio does not implement or alter sportsbook access controls or betting logic.

### Basketball research tour entry

The minimal integration is implemented with verified spread/performance routes and research labels. Next increment: the basketball owner supplies a stable curated historical-game URL and confirms the relevant model/data release. Dependencies: event identifier and route format, source dates, historical odds timing, replay behavior, approved performance context. Acceptance: a first-time visitor can reach one historical game, reproduce its displayed comparison, and reach aggregate evaluation; retrospective results remain distinct from prospective forecasts and hypothetical returns remain labeled. The portfolio does not change models, probabilities, data or promotion policy.

## Remaining information

- The Ocho's audience, intended task, benefit, and initial scope before its project development begins.
- Owner-backed individual historical-game URL and long-term route/media contracts for the optional tour extensions above.

## Owner-directed design revision

The revised page uses one four-card grid with equal closed card dimensions, padding, borders and button positions at each breakpoint. Yellow/blue identify published work; purple/red identify The Ocho and NBA. Secondary destinations and case studies remain inside native disclosures. Opening a disclosure allows that card to grow to fit its content. Development buttons are intentionally disabled and excluded from the keyboard tab order. The redundant “Explore the projects” heading, navigation row, hero action and “Ideas in progress” section have been removed. Five browser checks pass after updating navigation expectations; responsive screenshots cover the new layout.
