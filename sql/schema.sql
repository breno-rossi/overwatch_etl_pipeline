CREATE TABLE heroes_stats (
    hero VARCHAR(20),
    pickrate FLOAT,
    winrate FLOAT,
    platform VARCHAR(10),
    gamemode VARCHAR(10),
    region VARCHAR(10),
    INSERTED_AT TIMESTAMP DEFAULT NOW()

);