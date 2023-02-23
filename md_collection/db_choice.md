# PostgreSQL and Snowflake
Earlier I had mentioned my creation of a snowflake account to get the credentials for our ELT process. In this project I will be using both [snowflake](https://www.snowflake.com/en/) and [postgresql](https://www.postgresql.org/) to serve as one "on-premise" and one "cloud option" approach. In the architecture diagram seen on the first page and the DAGs from the last portion in airflow you can clearly see two distinct processes. 

> Here we will not be covering many details of how it is done but you can reference any of the guides on snowflake and postgresql or reference my ```docker-compose.yml``` to see how both of these services are setup.

With that being said here are outputs for both and what the UI looks like once the data has been loaded in.

## PostgreSQL
Here is our connection to the database. I am using [pgAdmin]() via the default port on ```5432``` 


![image](/assets/pg_server_conn.png)


Below is an example query using ```*``` to see the data.


![image](/assets/pg_query_example.png)


## Snowflake
Here is an example of the results of the extract load process from the DAG we created.

![image](/assets/snowflake_ui.png)


Below is an example query on a known anime studio ```ufotable```.


![image](/assets/snowflake_query_example.png)


[Back](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/db_choice.md) | [Next Step](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/dbt_process.md)
