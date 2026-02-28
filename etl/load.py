import psycopg2

def load_into_db (df):
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
        host="postgres",   
        port=5432,
        dbname="",            #nome do banco de dados
        user="",              #usuário do db
        password="")          #senha do db

        cursor = conn.cursor()
        sql_command_insert = "INSERT INTO heroes_stats (hero, pickrate, winrate, platform, gamemode, region, inserted_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        for row in df.itertuples():
            cursor.execute(sql_command_insert, (row.hero, row.pickrate, row.winrate, row.region, row.platform, row.gamemode, row.inserted_at))
        conn.commit()

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
