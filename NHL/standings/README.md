## Goal
Build current and historical season standings from the public NHL standings endpoint.

## Primary Source
- [`https://api-web.nhle.com/v1/standings/now`](https://api-web.nhle.com/v1/standings/now)
- [`https://api-web.nhle.com/v1/standings/{date}`](https://api-web.nhle.com/v1/standings/{date})

## Expected Collection Method
- Query standings data directly from the NHL JSON endpoint.
- Use `now` for current-season snapshots.
- Use the date-based standings endpoint for historical season backfills.
- Scan backward from the end of the regular season to find the last valid standings snapshot for each season.
- Map each row to the repo standing schema after normalization.

## Legal and Operational Notes
- This uses a public, unauthenticated endpoint exposed by NHL properties.
- Do not attempt to scrape hidden page content or circumvent access controls.
- If the endpoint shape changes, stop and document the change before altering schema.
- Source-limited gap: the current NHL standings API does not return historical rows for `2004-2005`, so that season remains unavailable in the historical backfill.

## Sort Order
- Season files keep the source standings order returned by the API.
- The all-seasons aggregate uses `seasonId` descending, then `leagueSequence` ascending, then `teamName_default` as the tiebreaker.

## Field Glossary
- `clinchIndicator`: playoff clinch status marker.
- `conferenceAbbrev`: conference abbreviation.
- `conferenceHomeSequence`: conference home ranking sequence.
- `conferenceL10Sequence`: conference last-10 ranking sequence.
- `conferenceName`: conference name.
- `conferenceRoadSequence`: conference road ranking sequence.
- `conferenceSequence`: conference overall ranking sequence.
- `date`: standings date used by the source.
- `divisionAbbrev`: division abbreviation.
- `divisionHomeSequence`: division home ranking sequence.
- `divisionL10Sequence`: division last-10 ranking sequence.
- `divisionName`: division name.
- `divisionRoadSequence`: division road ranking sequence.
- `divisionSequence`: division overall ranking sequence.
- `gameTypeId`: game type identifier.
- `gamesPlayed`: games played.
- `goalDifferential`: goals for minus goals against.
- `goalDifferentialPctg`: goal differential percentage.
- `goalAgainst`: goals against.
- `goalFor`: goals for.
- `goalsForPctg`: goals-for percentage.
- `homeGamesPlayed`: home games played.
- `homeGoalDifferential`: home goal differential.
- `homeGoalsAgainst`: home goals against.
- `homeGoalsFor`: home goals for.
- `homeLosses`: home losses.
- `homeOtLosses`: home overtime losses.
- `homePoints`: home points.
- `homeRegulationPlusOtWins`: home regulation-plus-OT wins.
- `homeRegulationWins`: home regulation wins.
- `homeTies`: home ties.
- `homeWins`: home wins.
- `l10GamesPlayed`: last-10 games played.
- `l10GoalDifferential`: last-10 goal differential.
- `l10GoalsAgainst`: last-10 goals against.
- `l10GoalsFor`: last-10 goals for.
- `l10Losses`: last-10 losses.
- `l10OtLosses`: last-10 overtime losses.
- `l10Points`: last-10 points.
- `l10RegulationPlusOtWins`: last-10 regulation-plus-OT wins.
- `l10RegulationWins`: last-10 regulation wins.
- `l10Ties`: last-10 ties.
- `l10Wins`: last-10 wins.
- `leagueHomeSequence`: league home ranking sequence.
- `leagueL10Sequence`: league last-10 ranking sequence.
- `leagueRoadSequence`: league road ranking sequence.
- `leagueSequence`: league overall ranking sequence.
- `losses`: losses.
- `otLosses`: overtime losses.
- `placeName_default`: place name in the default locale.
- `pointPctg`: point percentage.
- `points`: points.
- `regulationPlusOtWinPctg`: regulation-plus-OT win percentage.
- `regulationPlusOtWins`: regulation-plus-OT wins.
- `regulationWinPctg`: regulation win percentage.
- `regulationWins`: regulation wins.
- `roadGamesPlayed`: road games played.
- `roadGoalDifferential`: road goal differential.
- `roadGoalsAgainst`: road goals against.
- `roadGoalsFor`: road goals for.
- `roadLosses`: road losses.
- `roadOtLosses`: road overtime losses.
- `roadPoints`: road points.
- `roadRegulationPlusOtWins`: road regulation-plus-OT wins.
- `roadRegulationWins`: road regulation wins.
- `roadTies`: road ties.
- `roadWins`: road wins.
- `seasonId`: season identifier.
- `shootoutLosses`: shootout losses.
- `shootoutWins`: shootout wins.
- `streakCode`: streak direction code.
- `streakCount`: streak length.
- `teamName_default`: team name in the default locale.
- `teamName_fr`: team name in French.
- `teamCommonName_default`: common team name in the default locale.
- `teamAbbrev_default`: team abbreviation in the default locale.
- `teamLogo`: team logo URL.
- `ties`: ties.
- `waiversSequence`: waivers ranking sequence.
- `wildcardSequence`: wildcard ranking sequence.
- `winPctg`: win percentage.
- `wins`: wins.
- `sourceDate`: source timestamp.
- `wildCardIndicator`: wildcard status marker.
- `placeName_fr`: place name in French.
- `teamCommonName_fr`: common team name in French.

## Expected Outputs
- Current-season standings snapshot
- A stable `nhl_standings_now.csv` file for always-current examples
- Historical season files from `1993-1994` onward when range mode is used
- One all-seasons aggregate file for the full backfill

## Example Notebook
- [`example.ipynb`](example.ipynb)
