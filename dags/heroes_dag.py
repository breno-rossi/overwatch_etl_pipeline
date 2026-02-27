import sys
sys.path.insert(0, '/opt/airflow')
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.extract import extract_heroes_data
from etl.transform import transform_dataset
from etl.load import load_into_db

def run_pipeline():
    df_raw = extract_heroes_data("pc", "americas", "quickplay")
    df_transformed = transform_dataset(df_raw, "pc", "americas", "quickplay")
    load_into_db(df_transformed)

with DAG(
dag_id="heroes_dag",
        start_date=datetime(2026,1,1),
        schedule_interval="@hourly",
        catchup=False
) as dag:
    
    tarefa = PythonOperator(
        task_id="run_pipeline",
        python_callable= run_pipeline,
    )
