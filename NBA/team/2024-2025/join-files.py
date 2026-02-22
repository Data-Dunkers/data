import pandas as pd
team_codes = ['ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GS', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NO', 'NY', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SA', 'TOR', 'UTAH', 'WSH']
dir_path = 'https://raw.githubusercontent.com/Data-Dunkers/data/refs/heads/main/NBA/team/2024-2025/'
dfs = {}

for team_code in team_codes:
    file_path = f'{dir_path}{team_code}_2024-2025_players.csv'
    tempdf = pd.read_csv(file_path)
    tempdf['Team'] = team_code
    dfs[team_code] = tempdf
df_all = pd.concat(dfs.values(), axis=0, ignore_index=True)
df.to_csv('2024-2025_players.csv')