import pandas as pd

data = pd.read_csv("output.csv")

# 1. sort by gw
data = data.sort_values(
    ["gameweek", "player_id"]
)

# 2. remove players with 0 or NaN total points in ge 38
gw38_totalpoints = data.loc[data["gameweek"] == 38].set_index("player_id")["total_points"]

players_to_keep = gw38_totalpoints[gw38_totalpoints.notna() & (gw38_totalpoints != 0)].index

data = data[ data["player_id"].isin(players_to_keep) ]

# 3. move gw to col 1
data = data[ ["gameweek"] + [col for col in data.columns if col != "gameweek"]]

# 4. map positions to numbers
pos_num = {
    "Forward":3,
    "Midfielder":2,
    "Defender":1,
    "Goalkeeper":0
}

data["position"] = data["position"].map(pos_num)

# 5. save csv
data.to_csv("players_data.csv", index = False)