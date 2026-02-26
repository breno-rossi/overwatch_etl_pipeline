import requests
import pandas as pd


def extract_heroes_data(platform, region, gamemode ):

    params = {
    "platform": "pc",
    "platform": "console",
    "gamemode": "competitive",
    "gamemode": "quickplay",
    "region": "americas",
    "region": "asia",
    "region": "europe"}

    url = f"https://overfast-api.tekrop.fr/heroes/stats?platform={platform}&gamemode={gamemode}&region={region}"
    requisicao = requests.get(url, params=params)
    requisicao.raise_for_status()
    data = requisicao.json()
    data = pd.DataFrame(data)
    return data


df = extract_heroes_data("pc","americas","competitive")
print(df)