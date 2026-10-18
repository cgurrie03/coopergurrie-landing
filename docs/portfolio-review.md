# Portfolio correction review

Prepared October 18, 2026. Portfolio scope only. Auto Instagram Posts has been removed at the owner's request. The Ocho is queued for separate development; its purpose has not been invented.

## Audit status

| ID | Status | Resolution and evidence |
| --- | --- | --- |
| P01 | Fixed | Removed inert LinkedIn/email spans. No confirmed profile URL or contact address exists in the repository. Keyboard flow has no placeholder stops; supplying contacts later is optional. |
| P02 | Fixed | Auto Instagram Posts removed entirely. The Ocho moved to a compact ideas section with explicit scope pending. NBA Model has a sourced, planned purpose and no disabled launch control. |
| P03 | Fixed | Two public projects lead; unpublished ideas follow. Both projects have navigation links above the first card, and the second heading enters the initial 390 × 844 viewport. |
| P04 | Fixed | College Basketball Research is labeled a public research preview with no validated betting edge. Sportsbook access distinguishes the public demo from approved league membership. |
| P05 | Fixed | First card begins around y=299 at 390px and y=351 at 1440px. Biography follows project content. Browser screenshots cover 320, 390, 768, 1366 × 768, and 1440px layouts. |
| P06 | Fixed | Native disclosures contain two public screenshots and concise case studies covering audience, contribution, design, behavior and limits. The sportsbook screenshot contains synthetic data only. Working demo and historical performance links are enabled. |
| P07 | Fixed | Names match the live applications: Fantasy Sportsbook and College Basketball Research. Action labels identify the demo, sign-in, research, and historical winner performance destinations. |
| P08 | Fixed | First keyboard stop is a visible-on-focus skip link. Enter moves focus to the projects main landmark; the next Tab reaches project navigation. |
| P09 | Fixed | Intro states the maker's focus; project cards include contribution context and case studies. Personal biography remains available in a native disclosure below the work. No fabricated release dates or technology claims. |
| P10 | Fixed | Normal/social descriptions agree with project status. New 1200 × 630 social image uses current project names and preview labels. Canonical URL added. The existing production social URL responds 200; new local assets respond 200 through the test server. |

All original observations were checked against the current repository, not assumed from the audit. No complete audit item was already resolved in the portfolio. The external demo and basketball research views already existed and were verified before linking them.

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

Set `BROWSER_CHANNEL=msedge` to use an installed Edge browser. All five browser regression tests passed in Edge: native skip/disclosure behavior; mouse and Enter navigation; narrow and expanded layouts; media and metadata; reduced motion. Navigation tests intercept outbound destinations to avoid app mutations. Separate public browser checks verified real routes and read-only demo tabs.

Additional visual checks: 320/390/768/1440px, short 1366 × 768 laptop, expanded case studies, and 200% CSS zoom. No horizontal overflow in closed or expanded states. The scan found no WCAG A/AA violations; automated contrast analysis had an incomplete result for screenshot content, so the scan is not a blanket accessibility certification. Text and controls were visually reviewed. Native browser-menu zoom, screen-reader speech output, iOS Safari and Android Chrome were not exercised.

The production portfolio remains unchanged until a separate authorized deployment. New media URLs can only be verified in production after that deployment. No sitemap was added because case studies are in-page disclosures, not separate pages; missing robots.txt is not treated as an indexing defect.

## Cross-project link contract

| Destination | Current verified route | Portfolio label |
| --- | --- | --- |
| Public sportsbook demo | `https://sportsbook.coopergurrie.com/#/demo` | Explore the sportsbook demo |
| Private league access | `https://sportsbook.coopergurrie.com/` | League member sign-in |
| Basketball entry | `https://cbb.coopergurrie.com/` | Explore basketball research |
| Historical spread comparison | `https://cbb.coopergurrie.com/#spreads` | Compare historical spread research |
| Historical winner performance | `https://cbb.coopergurrie.com/#performance` | Explore historical winner performance |
| Return to portfolio | `https://coopergurrie.com/` | Back to portfolio |

Both applications already show a return link to the portfolio. Preserve these routes or provide redirects when their navigation changes. Suggested identity strings are the current application names above, with Cooper Gurrie as the portfolio owner. No messages were sent to other chats; direct owner coordination is still needed to promise long-term route stability or obtain bespoke media. A stable individual-game deep link has not been confirmed and is not invented here. The verified historical comparison and performance destinations work independently of that future link.

## Scoped feature proposals

### Case studies and changelog

Extend the two existing disclosures into dedicated project pages only when there is enough approved release material to justify them. Cooper maintains portfolio summaries; each application owner supplies approved release notes and sanitized media. Dependencies: shipped commit/release references, agreed author contributions, source dates, stable project slugs. Acceptance: each change links to a release, each case study states current limits, navigation works without JavaScript, new pages have canonical URLs and appear in a sitemap. Check links on every portfolio change; review screenshots/status after each application release and at least quarterly. Mark stale content after a failed link check or an app release that changes the depicted behavior. Do not use today's date as a product-release date.

### Public sportsbook demo entry

The minimal integration is implemented using the existing public synthetic route and screenshot. Next increment: obtain the sportsbook owner's commitment to the demo route and a versioned fixture/media contract. Dependencies: synthetic fixture provenance, no account mutations, explicit disabled transaction behavior, route redirect policy. Acceptance: anonymous visitors can view markets, tickets and standings; the demo cannot submit bets or change balances; no private data is returned; member sign-in remains separate. The portfolio does not implement or alter sportsbook access controls or betting logic.

### Basketball research tour entry

The minimal integration is implemented with verified spread/performance routes and research labels. Next increment: the basketball owner supplies a stable curated historical-game URL and confirms the relevant model/data release. Dependencies: event identifier and route format, source dates, historical odds timing, replay behavior, approved performance context. Acceptance: a first-time visitor can reach one historical game, reproduce its displayed comparison, and reach aggregate evaluation; retrospective results remain distinct from prospective forecasts and hypothetical returns remain labeled. The portfolio does not change models, probabilities, data or promotion policy.

## Remaining information

- Confirmed LinkedIn URL and contact email, only if the owner wants those links restored.
- The Ocho's audience, intended task, benefit, and initial scope before its project development begins.
- Owner-backed individual historical-game URL and long-term route/media contracts for the optional tour extensions above.
