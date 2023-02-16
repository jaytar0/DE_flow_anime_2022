from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
#from sqlalchemy.dialects import registry
from upload_postgres import normalized_loader
import pandas as pd
import os
import sys

# Method for putting our csv file to snowflake
def to_snowflake(data_dir):
    
    # Load via pandas and use snowflake write_pandas feature
    df = normalized_loader(data_dir)

    #registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')

    #user=os.getenv("SF_USER")
    #password=os.getenv("SF_PASS")
    #account=os.getenv("SF_ACC")
    #warehouse=os.getenv("SF_WH")
    #database=os.getenv("SF_DB")
    #schema=os.getenv("SF_SM")

    #conn_string = f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}"
    # Engine credentials via sqlalchemy
    
    engine = create_engine(URL(
        user=os.getenv("SF_USER"),
        password=os.getenv("SF_PASS"),
        account=os.getenv("SF_ACC"),
        warehouse=os.getenv("SF_WH"),
        database=os.getenv("SF_DB"),
        schema=os.getenv("SF_SM")
    ))
    
    #engine = create_engine(conn_string)
    # Connect to snowflake 
    conn = engine.connect()
    conn.execute("DROP table IF EXISTS all_anime")

    # Putting table in
    # Note: Due to maximum number of expression being 16,384 for snowflake we must upload
    #       beneath the chunksize, so listed as 16000 with option append.
    df.to_sql('all_anime', engine, index=False, if_exists='append', chunksize=16000)

    
# Main Handler
def main():
    csv_location = '/opt/airflow/data/anime-dataset-2022.csv'
    to_snowflake(csv_location)


if __name__ == "__main__":
    main()