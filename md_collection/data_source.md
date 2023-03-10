# Data Sources

The datasource used for this project was from kaggle [Anime DataSet 2022](https://www.kaggle.com/datasets/vishalmane10/anime-dataset-2022) uploaded by [Vishal Mane](). The author has webscraped official data from [anime-planet](https://www.anime-planet.com/) a popular anime media site. Even though this is not considered a large dataset, it includes everything we need in terms of number of media entries (rows) as well as 17 unique fields (columns) for transformations/analysis later on.


I have thought about scraping for the data myself on several occassions as that is something I'm definitely familiar with doing. However, due to the project scope, time-limit, and what I preferred to showcase, I will not be doing that here.

## Steps
We will be working with the python [Kaggle API](https://github.com/Kaggle/kaggle-api) to request our data.

1. Create an account with Kaggle.
2. Collect the correct credentials.
3. Using the docs provide the correct usage in your scripts.

More details can be found in the the ```/airflow/data_retrieval``` directory.

Before I continued to the next phase, some basic data exploration was done in a simple python script with pandas and maplotlib just so I had a good idea of what I was working with going forward, while jotting down transformation + data cleaning notes. Generally I believe this is good practice as the data might not be entirely clean and ready to use from the get go.

[Back](https://github.com/jaytar0/DE_flow_anime_2022) | [Next Step](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/docker_airflow.md)
