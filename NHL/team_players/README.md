## Goal
Build per-team player season files from the API-backed NHL player exports.

## Source
- League player season files from [`../player/README.md`](../player/README.md)
- The player season files themselves are built from the public NHL skater summary endpoint.
- Source-limited fallback for `2004-2005` uses the legacy local NHL team-player files because the player season file does not include usable team codes for that season.

## Expected Collection Method
- Read one season of NHL player data at a time.
- Split the rows into one file per team code.
- Duplicate traded-player rows into each team file when the source row contains multiple team codes.
- Keep the season folder layout aligned with the old production NHL `team_players` structure.

## Legal and Operational Notes
- This uses only public source-backed data.
- Do not scrape rendered pages or add hidden-source workarounds.
- If a player season file is missing, stop and document the gap rather than inventing rows.
- If the season is `2004-2005`, normalize the legacy local NHL team-player files into the current schema instead of leaving the season blank.

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

## Expected Outputs
- One season folder per NHL season
- One team CSV per team per season
- One all-seasons aggregate file named `nhl_team_players_all.csv`

## Example Notebook
- [`example.ipynb`](example.ipynb)
