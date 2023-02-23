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

