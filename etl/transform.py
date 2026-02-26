import pandas as pd
from datetime import datetime
from extract import extract_heroes_data


def transform_dataset (df, platform, gamemode, region):
    df["platform"] = platform
    df["gamemode"] = gamemode
    df["region"] = region
    df["collect_at"] = datetime.now()
    df = df.dropna(subset=["pickrate", "winrate"])

    return df

df_raw =extract_heroes_data("pc", "americas","quickplay")

df_transformed = transform_dataset(df_raw,"pc", "americas","quickplay")
print(df_transformed)
