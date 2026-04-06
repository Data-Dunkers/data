## Goal
Provide season team totals that teachers can use to compare team performance across years.

## Source Disclosure
- [`https://api-web.nhle.com/v1/club-stats/{team}/{season}/{gameType}`](https://api-web.nhle.com/v1/club-stats/{team}/{season}/{gameType})
- [`https://api-web.nhle.com/v1/standings/now`](https://api-web.nhle.com/v1/standings/now)
- [`https://api-web.nhle.com/v1/standings/{date}`](https://api-web.nhle.com/v1/standings/{date})

## What This Folder Contains
- One team CSV per season.
- A current snapshot file named `nhl_team_club_stats_now.csv`.
- An all-seasons aggregate file named `nhl_team_club_stats_all.csv`.

## Notes
- These CSVs are cleaned and normalized for consistent classroom use.
- Historical team data is source-backed from the NHL data service; no legacy local team file is used for the backfill.

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

## Files Included
- `nhl_team_club_stats_now.csv` for the current season
- One season file for each backfilled season from `1993-1994` onward when range mode is used
- `nhl_team_club_stats_all.csv` as a combined reference file across seasons

## Example Notebook
- [`example.ipynb`](example.ipynb)
- Loads `nhl_team_club_stats_now.csv` and charts skater points by team, which makes it useful for comparing overall team production.
