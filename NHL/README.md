# NHL Data

## Overview
This tree contains the production NHL datasets.

- Keep the folder structure stable across refreshes.
- Prefer public, unauthenticated NHL JSON endpoints over HTML scraping.
- Use the matching utility scripts in `utils/NHL/` for refreshes.

## Collection Summary
- Standings come from the public NHL standings endpoint, using `now` for the current snapshot and date-based requests for historical season backfills.
- Team totals come from the NHL stats REST layer, using live standings for current snapshots and season-end standings snapshots for historical team lists.
- Player files come from the NHL skater summary REST endpoint.
- Team-player files are derived from the player season exports by splitting rows into team-specific files, with a one-season legacy fallback for `2004-2005`.

## Source Access
- Standings data is retrieved from [`https://api-web.nhle.com/v1/standings/now`](https://api-web.nhle.com/v1/standings/now) for current-season snapshots and [`https://api-web.nhle.com/v1/standings/{date}`](https://api-web.nhle.com/v1/standings/{date}) for historical season snapshots.
- Team data is retrieved from [`https://api-web.nhle.com/v1/club-stats/{team}/{season}/{gameType}`](https://api-web.nhle.com/v1/club-stats/{team}/{season}/{gameType}), with team codes resolved from [`https://api-web.nhle.com/v1/standings/now`](https://api-web.nhle.com/v1/standings/now) for current snapshots and [`https://api-web.nhle.com/v1/standings/{date}`](https://api-web.nhle.com/v1/standings/{date}) for historical backfills.
- Team-player files are derived from the player season CSVs under `player/`.
- Player data is retrieved from [`https://api.nhle.com/stats/rest/en/skater/summary`](https://api.nhle.com/stats/rest/en/skater/summary).
- Example notebooks in each section show how the CSVs can be loaded from the shared data repository root.

## Supporting Documentation
- [Unofficial NHL API reference](https://github.com/Zmalski/NHL-API-Reference)
- [NHL stats site](https://www.nhl.com/stats)

## Section Index
- [standings/README.md](standings/README.md) - standings source notes and standings field glossary
- [team/README.md](team/README.md) - team stats source notes and team field glossary
- [player/README.md](player/README.md) - player stats source notes and player field glossary
- [team_players/README.md](team_players/README.md) - per-team player split notes, field glossary, and aggregate file rules

## Collection Rules
- Do not bypass authentication, paywalls, or rate limits.
- Do not scrape rendered HTML if the same data is available from a public JSON endpoint.
- Keep request volume low and cache intermediate responses during experiments.
- Preserve official NHL IDs and team codes as the join key across sections.
