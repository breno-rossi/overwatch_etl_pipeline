import psycopg2
from transform import transform_dataset



def load_into_db (df):
    try:
        conn = psycopg2.connect(
        host = "localhost",
        port = 1818,
        dbname="weather_etl",
        user="breno",
        password="colorado63")

        cursor = conn.cursor()
        sql_command_insert = "INSERT INTO heroes_stats (hero, pickrate, winrate, platform, gamemode, region, collect_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        for row in df.itertuples():
            cursor.execute(sql_command_insert, (row.hero, row.pickrate, row.winrate, row.region, row.platform, row.gamemode, row.collect_at))
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Erro {e}")
    finally:
        cursor.close()
        conn.close()