from datasets import load_dataset
import pandas as pd


ds = load_dataset("Damir81/football-charts-results-goal-timing")

# print(ds)

# ds["train"].to_csv("football_data.csv", index=False)

# 0. to pandas dataframe
df = ds["train"].to_pandas()

# 1. remove the redundant cols
df = df.drop(
    columns=[
        "league_name",
        "kickoff_utc",
        "ht_result",
        "ft_result",
        "total_goals",
        "result",
        "first_goal_time",
        "all_goal_times"
    ]
)

# 2. clean the date format to 2 seperate columns
df["match_date"] = pd.to_datetime(df["match_date"])

df["year"] = df["match_date"].dt.year
df["month"] = df["match_date"].dt.month
df["day_of_week"] = df["match_date"].dt.day_of_week

df = df.drop(columns="match_date")

# 3. clean the time to be a float, and ensure the targets are numerical
df["time"] = pd.to_datetime(df["time"], 
                            format="%H:%M"  # % -> placeholder, H -> hour. M -> minutes
                            ).apply(
                                lambda x: x.hour + (x.minute / 60)
                            )

df["home_goals"] = df["home_goals"].astype("float32")
df["away_goals"] = df["away_goals"].astype("float32")

# 4. factorize strings into numbers -> convert categorical columns to numerical IDs
categorical_cols = [
    "league",
    "country",
    "season",
    "home_team",
    "away_team"
]

mappings = []

for col in categorical_cols:
    codes, uniques = pd.factorize(df[col])
    """
    factorize returns:
        [0]: The numerical codes assigned to each value. (what we want)
        [1]: The unique original values, in the order they were encountered.
    """
    
    df[col] = codes
    
    mapping = pd.DataFrame(
        {
            "category": col,
            "name": uniques,
            "id": range(len(uniques))
        }
    )
    
    mappings.append(mapping)

df.to_csv("cleaned_data.csv", index=False)

# save all mappings by concating them first
mapping_df = pd.concat(mappings, ignore_index=True)
mapping_df.to_csv("mappings.csv", index=False)