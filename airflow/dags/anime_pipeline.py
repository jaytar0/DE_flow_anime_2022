from os import remove
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta, datetime

"""
Pipeline Name: Anime Airflow DAG
Description: Extracts Anime 2022 dataset from Animeplanet from kaggle and loads onto postgres 
            + snowflake databases then transforms with DBT
"""

# Dag Arguments
output_name = datetime.now().strftime("%Y%m%d")
schedule_interval = None
start_date = days_ago(1)
default_args = {"owner": "airflow", "depends_on_past": False, "retries": 1}

# Dag Start
with DAG(
    dag_id="anime_pipeline",
    description="2022 Anime Dataset Analysis Pipeline",
    schedule_interval=schedule_interval,
    default_args=default_args,
    start_date=start_date,
    catchup=True,
    max_active_runs=1,
    tags=["Anime_Pipe"],
) as dag:

    # Operator for data extraction
    extract_anime_data = BashOperator(
        task_id="extract_anime_data",
        bash_command=f"python /opt/airflow/data_retrieval/extract_anime_data.py {output_name}",
        dag=dag,
    )

    extract_anime_data.doc_md = "Requests and recieves anime data from a Kaggle Source"

    # Operator for loading onto postgres
    put_postgres = BashOperator(
        task_id="put_postgres",
        bash_command=f"python /opt/airflow/data_retrieval/upload_postgres.py {output_name}",
        dag=dag,
    )

    put_postgres.doc_md = "Uploads and puts data to local postgres database"

    # Operator for loading onto snowflake
    put_snowflake = BashOperator(
        task_id="put_snowflake",
        bash_command=f"python /opt/airflow/data_retrieval/upload_snowflake.py {output_name}",
        dag=dag,
    )

    put_snowflake.doc_md = "Copy data csv to snowflake"

# Pipeline flow
extract_anime_data >> put_postgres >> put_snowflake
#put_postgres >> put_snowflake 