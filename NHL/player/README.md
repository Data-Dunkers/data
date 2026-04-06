## Goal
Build league player season stats from the NHL skater summary endpoint.

## Source Candidates
- [`https://api.nhle.com/stats/rest/en/skater/summary`](https://api.nhle.com/stats/rest/en/skater/summary)
- [`https://api-web.nhle.com/v1/standings/now`](https://api-web.nhle.com/v1/standings/now)
- [`https://www.nhl.com/stats`](https://www.nhl.com/stats)

## Expected Collection Method
- Pull all current-season skater rows from the public NHL stats REST endpoint.
- Use standings only when a team list or team code lookup is needed.
- Keep the output at the league level and avoid per-team HTML scraping.

## Legal and Operational Notes
- Keep the process within public, unauthenticated endpoints.
- Do not use login sessions, hidden tokens, or anti-bot bypasses.
- Cache responses during experimentation so repeated validation does not hammer the source.

## Field Glossary
- `Name`: player name.
- `Team`: team abbreviation from the source.
- `POS`: position.
- `GP`: games played.
- `G`: goals.
- `A`: assists.
- `PTS`: points.
- `+/-`: plus/minus.
- `PIM`: penalty minutes.
- `TOI/G`: average time on ice per game.
- `PPG`: power-play goals.
- `PPA`: power-play assists.
- `SHG`: shorthanded goals.
- `OTG`: overtime goals.
- `GWG`: game-winning goals.
- `S`: shots.
- `S%`: shooting percentage.
- `EVG`: even-strength goals.
- `EVP`: even-strength points.
- `FO%`: faceoff percentage.
- `Season`: season identifier.

## Expected Outputs
- Current-season player CSV
- Historical season CSVs from 1990-1991 onward when range mode is used
- One all-seasons aggregate for the full historical backfill
- Source-limited gap: 2004-2005 returns no skater rows from the endpoint, so that season is skipped.

## Example Notebook
- [`example.ipynb`](example.ipynb)
