FROM apache/airflow:2.5.1-python3.8

## adding missing python packages
USER airflow
COPY requirements.txt .
RUN pip uninstall apache-airflow-providers-google -y \
    && pip install -r requirements.txt \
    && pip uninstall snowflake