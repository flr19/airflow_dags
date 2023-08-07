from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'invoke_web_service_dag',
    default_args=default_args,
    description='DAG to invoke web service',
    schedule_interval=timedelta(days=1),  # Runs daily
)

task_invoke_web_service = SimpleHttpOperator(
    task_id='invoke_web_service_task',
    endpoint='https://api.mocki.io/v2/11fe220e/users',  # Endpoint URL from Mocki.io
    method='GET',  # Adjusted to GET since it's a GET request
    dag=dag,
)

task_invoke_web_service

