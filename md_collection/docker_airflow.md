# Docker and Airflow Setup

Continuing from the data exploration phase, we are ready to get docker and all environments setup. Before this I had already setup a git repo and opened it in visual studio code.

1. We will be using airflow for pipeline orcehstration purposes. I picked airflow because it was the most common one being used but would also like to learn other methods in the future like (prefect and dagster). 
2. Our DAG(s) (directed acrylic graph), will be defined in this process helping with the automation, shceduling, and reusability of our extract and load phases.
3. Docker will be used to create containers and images that run our processes/services, we will be defining this via the docker-compose file.

Moving forward, these bits and pieces can be found within ```/airflow``` directory.


## Docker
I mainly have done everything via the ```docker-compose.yaml``` and edited it to suit my project. Like I mentioned above it will be defining our ccontainers and services.

The things I have added are:
- Additional volumes folders
- Custom Dockerfile to build from
- Custom naming on the services as you will see in the images below

```
FROM apache/airflow:2.5.1-python3.8
USER airflow
COPY requirements.txt .
RUN pip uninstall apache-airflow-providers-google -y \
    && pip install -r requirements.txt \
    && pip uninstall snowflake
```


> Note: I had trouble with setting up snowflake because there was already a python package named snowflake. Uninstalling on setup seemed to fix it.


Once I had everything setup I ran these commands and got this result.


```
docker-compose up airflow-init
docker-compose up
```

![image](/assets/docker_ui.png)


## Airflow
Now its time to create our dag for our ELT process. The example can be found in ```/airflow/dags``` under the name ```anime_pipeline.py```.

Compared to some other processes I have worked with, this is an extremely simple one. It will be sort out into three phases and utilizing ```BashOperator```, running scripts from the command line.

These separate scripts created are located in the ```/airflow/data_retrieval``` directory and do the following in order:

1. ```extract_anime_data.py```
    Utilizes the the Kaggle python API to request data, which was part written in our data acquisition phase. I left out the code pertaining to data exploration but
    left in a method that does just that so you have an idea where it can go.
2. ```upload_postgres.py```
    Takes the data from the extraction process, connects to our postgres database and funnels uploads it there.
3. ```upload_snowflake.py```
    Similar to step 2 just repeated with our cloud storage snowflake

> Steps 2 and 3 require credentials and setup, to learn more please go to their official pages to learn more.
> Learning these were rather painless as both had stellar documentation, and I had pripr experience using it already.


Once everything is setup and linked in the main dag it looked something like this.

![image](/assets/airflow_ui.png)

**Let's initiate a dag run!**

![image](/assets/airflow_dag_graph.png)


[Next Step](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/db_choice.md)



