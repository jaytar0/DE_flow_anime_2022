from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import sys
import os
import subprocess

# Normalizes data columns and gets the necessary connection information
def normalized_loader(data_dir):

    # Reading dataframe
    df = pd.read_csv(data_dir)

    df.columns = ['rank', 'name', 'japanese_name', 'type', 'episodes', 'studio',
       'release_season', 'tags', 'rating', 'release_year', 'end_year',
       'description', 'content_warning', 'related_manga', 'related_anime',
       'voice_actors', 'staff']

    # Getting connection details
    env_path = '/opt/airflow/data_retrieval/.env'

    if os.path.isfile(env_path):
        load_dotenv(env_path)
    else:
        print("Problem with env paths, proper credentials !required")
        sys.exit(1)

    return df

# Utilizing sqlalchemy load pandas df into local docker postgresql
def to_postgres(df):

    # Load credentials
    database=os.getenv("PG_DB")
    user=os.getenv("PG_USER")
    password=os.getenv("PG_PASS")
    host=os.getenv("PG_HOST")
    port=os.getenv("PG_PORT")

    # Connection to database and creation of table    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    engine.execute("DROP table IF EXISTS all_anime")
    df.to_sql('all_anime', engine)


# Main Handler
def main():

    # saved csv from [extracted_anime_data] script
    csv_dir = '/opt/airflow/data/anime-dataset-2022.csv'

    # Normalizer + Credentails
    data = normalized_loader(csv_dir)

    # Loading method
    to_postgres(data)

    subprocess.call(["pip", "uninstall", "snowflake"])

if __name__ == "__main__":
    main()
