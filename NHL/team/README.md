## Goal
Build current and historical team summaries from the NHL club-stats endpoint.

## Primary Source
- [`https://api-web.nhle.com/v1/club-stats/{team}/{season}/{gameType}`](https://api-web.nhle.com/v1/club-stats/{team}/{season}/{gameType})

## Supporting Source
- [`https://api-web.nhle.com/v1/standings/now`](https://api-web.nhle.com/v1/standings/now)
- [`https://api-web.nhle.com/v1/standings/{date}`](https://api-web.nhle.com/v1/standings/{date})

## Expected Collection Method
- Pull the current team list from the live standings snapshot for `nhl_team_club_stats_now.csv`.
- Pull the historical team list from the season-end standings snapshot for each backfilled season.
- Fetch one club-stats payload per team.
- Aggregate skater and goalie rows into one team summary row.

## Legal and Operational Notes
- Use only public NHL JSON endpoints.
- Do not scrape rendered pages when the same data is available from JSON.
- If a field is not available or not reliable from the source, leave it out of the experiment rather than guessing.
- Historical season data is source-backed from the NHL API; no legacy local team file is used for the backfill.

## Field Glossary
- `Team`: full team name from standings.
- `TriCode`: official team abbreviation used in NHL endpoints.
- `Season`: 8-digit season identifier used by the source.
- `GameType`: NHL game type code, usually `2` for regular season.
- `Skaters`: number of skater rows returned for the team.
- `Goalies`: number of goalie rows returned for the team.
- `SkaterGP`: total skater games played.
- `SkaterG`: total skater goals.
- `SkaterA`: total skater assists.
- `SkaterPTS`: total skater points.
- `SkaterPM`: total skater plus/minus.
- `SkaterPIM`: total skater penalty minutes.
- `SkaterPPG`: total skater power-play goals.
- `SkaterSHG`: total skater shorthanded goals.
- `SkaterGWG`: total skater game-winning goals.
- `SkaterOTG`: total skater overtime goals.
- `SkaterS`: total skater shots.
- `SkaterS%`: skater shooting percentage, computed from team goals divided by team shots.
- `GoalieGP`: total goalie games played.
- `GoalieGS`: total goalie games started.
- `GoalieW`: total goalie wins.
- `GoalieL`: total goalie losses.
- `GoalieOTL`: total goalie overtime losses.
- `GoalieGAA`: goalie goals-against average, computed from goals against and time on ice.
- `GoalieSV%`: goalie save percentage, computed from saves and shots against.
- `GoalieSA`: total goalie shots against.
- `GoalieSaves`: total goalie saves.
- `GoalieGA`: total goalie goals against.
- `GoalieSO`: total goalie shutouts.
- `SourceDate`: collection timestamp in UTC.

## Expected Experimental Outputs
- Current-season team summary CSV (`nhl_team_club_stats_now.csv`)
- Historical season files from `1993-1994` onward when range mode is used
- One all-seasons aggregate file for the full backfill (`nhl_team_club_stats_all.csv`)

## Example Notebook
- [`example.ipynb`](example.ipynb)
