from etl.extract import extract_heroes_data
from etl.transform import transform_dataset
from etl.load import load_into_db


df_raw = extract_heroes_data("pc", "americas", "quickplay")
df_transformed = transform_dataset(df_raw, "pc", "americas", "quickplay")
load_into_db(df_transformed)

print("Pipeline executado com sucesso")