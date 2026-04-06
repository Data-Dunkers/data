## Goal
Provide player season statistics that teachers can use for examples, comparisons, and charting exercises.

## Source Disclosure
- [`https://api.nhle.com/stats/rest/en/skater/summary`](https://api.nhle.com/stats/rest/en/skater/summary)
- [`https://api-web.nhle.com/v1/standings/now`](https://api-web.nhle.com/v1/standings/now)
- [`https://www.nhl.com/stats`](https://www.nhl.com/stats)

## What This Folder Contains
- One player CSV per season.
- An all-seasons aggregate file named `nhl_player_stats_all.csv`.
- A current-season file that can be used directly in notebook examples.

## Notes
- These CSVs are cleaned and normalized for consistent classroom use.
- Source-limited gap: `2004-2005` does not return skater rows from the source, so that season is skipped.

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

## Files Included
- A current-season player CSV for quick classroom examples
- One season file for each historical season from 1990-1991 onward when range mode is used
- `nhl_player_stats_all.csv` as a combined reference file across seasons

## Example Notebook
- [`example.ipynb`](example.ipynb)
- Loads the current-season player CSV and charts the top 20 scorers, which is a simple way to introduce sorting and bar charts.
