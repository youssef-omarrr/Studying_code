import pandas as pd
from pathlib import Path
from tqdm import tqdm

DATA_FOLDER = Path("fpl_2025-26")

gameweek_folders = sorted(
            DATA_FOLDER.iterdir(),
            key=lambda folder: int(folder.name.replace("GW", "")))  # lambda arguments (inputs): expression (automatically returned)

# print(gameweek_folders)

selected_csvs = ["players.csv", #[player_id, team_code, position]
                "player_match_enrichment.csv", #[rating]
                "playerstats.csv", #[total_points, event_points] <-----------
                "player_gameweek_stats.csv"] #[minutes, expected_assists, expected_goals, goals_scored, assists, bonus]
                                        #[saves, defensive_contribution, expected_goals_conceded, goals_conceded, clean_sheets]

data = []

    # {"gameweeks",
    # "player_id",
    # "team_code",
    # "position",
    
    # "rating",
    
    # "total_points",
    # "event_points",
    
    # "minutes",
    # "expected_assists",
    # "expected_goals",
    # "goals_scored",
    # "assists",
    # "bonus",
    
    # "saves",
    # "defensive_contribution",
    # "expected_goals_conceded",
    # "goals_conceded",
    # "clean_sheets",
    # }

for gw in tqdm(gameweek_folders):
    
    # Read CSVs
    players = pd.read_csv(gw / "players.csv")
    
    enrichment = pd.read_csv(gw / "player_match_enrichment.csv")
    
    player_stats = pd.read_csv(gw / "playerstats.csv").rename(
        columns={"id": "player_id"}
    )
    
    gw_stats = pd.read_csv(gw / "player_gameweek_stats.csv").rename(
        columns={"id": "player_id"}
    )
    
    # Keep selected columns only
    players = players[
        ["player_id", "team_code", "position"]
        ]
    enrichment = enrichment[
        ["player_id", "rating"]
        ]
    player_stats = player_stats[
        ["player_id", "total_points", "event_points"]
        ]
    gw_stats = gw_stats[
        ["player_id", "minutes", "expected_assists", "expected_goals", "goals_scored", "assists", "bonus",
        "saves", "defensive_contribution", "expected_goals_conceded", "goals_conceded", "clean_sheets"]
        ]
    
    # combine the CSVs
    merged_csv = (
        players
        .merge(enrichment,   on="player_id", how="left") # keeps every player from the left table, even if they have no matching row in the right table
        .merge(player_stats, on="player_id", how="left")
        .merge(gw_stats,     on="player_id", how="left")
    )
    
    # add gameweek col
    merged_csv["gameweek"] = int(gw.name.replace("GW", ""))
    
    # append data to out dataframe
    data.extend(merged_csv.to_dict("records"))
    
data = pd.DataFrame(data)
data.to_csv("output.csv", index=False)