import sys
import numpy as np
import pandas as pd
import datetime
import subprocess
import logging


# Utilizes Kaggle API to request the data we require
def fetch_data():
    
    # Dataset reference name
    data_id = "vishalmane10/anime-dataset-2022"

    # Creating directory where our kaggle credentials will be stored
    try:
        subprocess.call(["mkdir", "-p", "~/.kaggle"])
        subprocess.call(["cp", "./kaggle.json","~/.kaggle"])

    except Exception:
        logging.exception("Error occured while copying kaggle authetnication details")
        sys.exit(1)

    # Downloading the data
    try:
        subprocess.call(["kaggle", "datasets", "download", "-d", data_id])
        logging.info(f"Successfully Downloaded data from {data_id}")

    except Exception:
        logging.exception("Error in accessing dataset")
        sys.exit(1)
    
    # Unziping and moving dataset into data dir
    try:
        subprocess.call(["unzip", "anime-dataset-2022.zip", "-d", "data/"])
        subprocess.call(["mv","data/*.csv", "data/anime-dataset-2022.csv"])
        subprocess.call(["rm","*.zip"])
        logging.info("Successfully unziped and stored data inside /data dir")

    except Exception:
        logging.exception("Failed to unzip csv")
        sys.exit(1)
    

# Reads in the data to print metrics
def data_reader():

    df = pd.read_csv("/opt/airflow/data/anime-dataset-2022.csv")

    #logging.info("Columns obtained\n")
    #logging.info(df.columns)
    print(df.columns)

    #logging.info("Dataframe shape\n")
    #logging.info(df.shape)
    print(df.shape)


# A method that showcases simple pandas transforms to normalize some fields
def data_transformer():

    df = pd.read_csv("/opt/airflow/data/anime-dataset-2022.csv")
    

# Configurator
def main():
    
    # Setting up logging formats
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    # Fetching data from Kaggle
    #fetch_data()
    # Testing data
    data_reader()
    # Performing Simple Transformations
    data_transformer()


if __name__ == "__main__":
    main()
