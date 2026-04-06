# NHL Data

## Overview
This tree contains the production NHL datasets used for classroom and analysis examples.

The data is organized into four views:
- `standings/` - season standings tables with team records, points, and ranking fields.
- `team/` - one row per team per season with season totals.
- `player/` - one row per player per season with skater statistics.
- `team_players/` - per-team player files split from the season player data for roster-level examples.

## Collection Summary
- Standings are collected from the NHL standings endpoint, with a live snapshot for the current season and historical snapshots for backfilled seasons.
- Team totals come from the NHL club-stats endpoint and use the standings team list for the matching season.
- Player files come from the NHL skater summary endpoint.
- Team-player files are derived from the player season exports by splitting rows into team-specific files.

## Source Access
- Source disclosure for the NHL datasets:
  - Standings data comes from [`https://api-web.nhle.com/v1/standings/now`](https://api-web.nhle.com/v1/standings/now) and [`https://api-web.nhle.com/v1/standings/{date}`](https://api-web.nhle.com/v1/standings/{date}).
  - Team data comes from [`https://api-web.nhle.com/v1/club-stats/{team}/{season}/{gameType}`](https://api-web.nhle.com/v1/club-stats/{team}/{season}/{gameType}).
  - Player data comes from [`https://api.nhle.com/stats/rest/en/skater/summary`](https://api.nhle.com/stats/rest/en/skater/summary).
- The `team_players/` files are built from the season player CSVs in this same tree.

## Supporting Documentation
- [Unofficial NHL API reference](https://github.com/Zmalski/NHL-API-Reference)
- [NHL stats site](https://www.nhl.com/stats)

## Section Index
- [standings/README.md](standings/README.md) - what the standings file shows and what each standings column means
- [team/README.md](team/README.md) - what the team totals show and what each team column means
- [player/README.md](player/README.md) - what the player totals show and what each player column means
- [team_players/README.md](team_players/README.md) - how the team-specific player files are organized and what each column means

## For Teachers
- Use `standings/` to compare teams within a season.
- Use `team/` to study team-level totals such as games played, goals, and goalies.
- Use `player/` to analyze skater performance across seasons.
- Use `team_players/` when you want a roster-by-team view for classroom examples or filtering exercises.
