# DE_flow_anime_2022
This project shows an end to end Data Engineering project on Japanese animation using data collected as of 2022 from anime planet from a kaggle source. My aim is to derive interesting insights of the genreal trends surrounding anime and put some focus on analytical views within certain subcategories, all while showcasing professional skills from both data engineering and analytics.

## Inspirations
Anime was one of my favorite childhoood/early years pass times and to this day I still watch one or two from time to time from friend recommendations. It's one of those entertainment forms that will hold a timeless value to me. Thus, I thought I would give a go at applying some of what I love to my work and here is what has come to fruition.

I hope you enjoy the results!!!

## Project Flowchart
The general infrastructure of this project will be centered around what has been shown in the charts.

![flow](/assets/flow_chart.png)
*Visual diagram was self made in figma*

- Docker (for containerization and imaging)
- Airflow (pipeline orchestration tool)
- Python (language to write DAGs working with our extract + loading utilizing kaggle api)
- Postgres & Snowflake (relational database storage of choice both one for local and one for cloud)
- DBT (data build tool "cloud" used for transformation of loaded data into different models/views)
- Looker & PowerBI (visualization tools of choice)


## Output Example
Here is the final output from what I have mocked up using google looker studio. The power BI version will be available for this project later on, since I'm still experimenting with some visuals. If you would like to look at a sample of what I can do in power BI please reference the dashboard samples I have available in the main repository.


![dash](/assets/dash_update.png)

[Link to Live Dashboard](https://lookerstudio.google.com/s/mLPRgy9NtaM)


## Steps
Below are the steps for setting up this whole project and my own process/documentation.
> Notes: I have used free versions of snowflake and dbt cloud for this project. 
> Everything is done primarily on windows 11 and I use a BASH shell.


1. [Data Source](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/data_source.md)
2. [Docker & Airflow](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/docker_airflow.md)
3. [Postgres & Snowflake](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/db_choice.md)
4. [DBT](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/dbt_process.md)
5. [Dashboarding](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/dash.md)

[Next](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/data_source.md)
