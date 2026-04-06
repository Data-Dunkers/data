## AHL Data Guide (Full One-Pager Draft)

### Data Dunkers

This dataset is part of the Data Dunkers project, designed to support real-world data analysis using sports data.

### Overview

This dataset provides structured American Hockey League (AHL) data for analysis using Python, with tools such as pandas and Plotly Express. The data is organized into four folders, each focusing on a different level of analysis: players, teams, standings, and team-specific rosters.

All files are in CSV format.

### Repository Location

GitHub: [https://github.com/Data-Dunkers/data/tree/main/AHL](https://github.com/Data-Dunkers/data/tree/main/AHL)

CSV link pattern:

https://raw.githubusercontent.com/Data-Dunkers/data/main/AHL/\<folder\>/\<filename\>.csv

Each folder includes a **glossary markdown file** that explains all column names.

### Folder Guide

#### Player ([`data/AHL/player/`](https://github.com/Data-Dunkers/data/tree/main/AHL/player))

Contains player-level statistics for the AHL.

Use this folder to:

* identify top scorers  
* compare players across teams  
* analyze performance trends

Includes:

* current season player stats  
* all-player historical data  
* glossary

Key columns:

* Name, Team, Age, Pos  
* GP, G, A, P  
* G/GP, A/GP, P/GP  
* PPG, SHG, GWG, SH%

#### Standings ([`data/AHL/standings/`](https://github.com/Data-Dunkers/data/tree/main/AHL/standings))

Contains team standings and rankings.

Use this folder to:

* analyze league rankings  
* compare divisions  
* track team performance over time

Includes:

* current season standings  
* multi-season standings  
* glossary

Key columns:

* Rank, DivisionRank, Team  
* GP, W, L, OTL, PTS, PCT  
* GF, GA, DIFF  
* L10, STRK

#### Team ([`data/AHL/team/`](https://github.com/Data-Dunkers/data/tree/main/AHL/team))

Contains team-level performance statistics.

Use this folder to:

* compare team offense and defense  
* analyze shooting and goaltending  
* evaluate special teams performance

Includes:

* season team stats  
* historical team stats  
* glossary

Key columns:

* Team, Rk  
* per Game\_G/GP, per Game\_P/GP  
* Shots\_SH%, Saves\_SV%  
* Power-Play\_PP%, Penalty-Kill\_PK%

#### Team Players ([`data/AHL/team_players/`](https://github.com/Data-Dunkers/data/tree/main/AHL/team_players))

Contains player data organized by **team and season**.

Use this folder to:

* analyze a specific team roster  
* compare players within a team  
* study team composition

Structure:

* folders by season (e.g., `2025-2026`)  
* one file per team (e.g., Manitoba Moose)

Key columns:

* Name, Team, Age, Pos  
* GP, G, A, P  
* P/GP, SH%

### Example: Find the Top Goal Scorers

This example loads player data and finds the top goal scorers in the league.

```python
import pandas as pd
import plotly.express as px

url = "https://raw.githubusercontent.com/Data-Dunkers/data/main/AHL/player/ahl_player_stats_2025-2026.csv"
df = pd.read_csv(url)

# Top 10 goal scorers
top_scorers = df.sort_values(by="G", ascending=False).head(10)
print(top_scorers[["Name", "Team", "G"]])

# Create a bar chart
fig = px.bar(top_scorers, x="Name", y="G", color="Team",
             title="Top 10 Goal Scorers (AHL)")
fig.show()
```

### What You Can Explore

* Who are the top players in the league?  
* Which teams are strongest offensively or defensively?  
* How do standings relate to goal differential?  
* How is scoring distributed within a team?  
* How do players and teams change across seasons?

### External Reference

Companion Google Doc (context/background):
https://docs.google.com/document/d/1sHT0bL4DQyhYKQ2Qa1ps4JFB62WXCbLHcKcMCwAo_7o/edit

### Important Notes

* All data is **CSV format** and ready for pandas  
* Files can be accessed directly using **raw GitHub URLs**  
* Each folder includes a **glossary** explaining column names
