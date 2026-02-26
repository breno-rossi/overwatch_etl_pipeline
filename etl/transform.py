import pandas as pd
from datetime import datetime



def transform_dataset (df, platform, gamemode, region):
    df["platform"] = platform
    df["gamemode"] = gamemode
    df["region"] = region
    df["inserted_at"] = datetime.now()
    df = df.dropna(subset=["pickrate", "winrate"])

    return df