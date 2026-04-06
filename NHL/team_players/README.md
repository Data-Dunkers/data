## Goal
Provide team-specific player files that teachers can use for roster, filtering, and grouping examples.

## Source Disclosure
- League player season files from [`../player/README.md`](../player/README.md)
- The player season files themselves are built from the NHL skater summary endpoint.
- Source-limited fallback for `2004-2005` uses the legacy local NHL team-player files because the player season file does not include usable team codes for that season.

## What This Folder Contains
- One season folder per NHL season.
- One team CSV per team per season.
- One all-seasons aggregate file named `nhl_team_players_all.csv`.

## Notes
- These CSVs are cleaned and normalized for consistent classroom use.
- If a season is unavailable from the source, the gap is documented rather than filled with invented rows.

## Field Glossary
- `Name`: player name.
- `Team`: team code for the split file.
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
- `Year`: start year, used only in the all-seasons aggregate file.

## Files Included
- One season folder per NHL season
- One team CSV per team per season inside each season folder
- `nhl_team_players_all.csv` as a combined reference file across all available seasons

## Example Notebook
- [`example.ipynb`](example.ipynb)
- Loads one team-season CSV and charts the top players by points, which is useful for roster-focused classroom examples.
