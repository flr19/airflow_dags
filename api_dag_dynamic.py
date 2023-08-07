import json
from datetime import datetime
from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator


def read_endpoint_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()


def save_posts(ti) -> None:
    posts = ti.xcom_pull(task_ids=['get_posts'])
    with open('data/posts_2.json', 'w') as f:
        json.dump(posts[0], f)


dag_file_path = 'api_endpoint.txt'  # Update with the actual file path

with DAG(
    dag_id='api_dag_dynamic',
    schedule_interval='@daily',
    start_date=datetime(2022, 3, 1),
    catchup=False
) as dag:

    # 1. Read the API endpoint from the file
    api_endpoint = read_endpoint_from_file('dags/api_endpoint.txt')

    # 2. Check if the API is up
    task_is_api_active = HttpSensor(
        task_id='is_api_active',
        http_conn_id='api_posts',
        endpoint=api_endpoint  # Use the dynamic API endpoint here
    )

    # 3. Fetch posts from the API
    task_get_posts = SimpleHttpOperator(
        task_id='get_posts',
        http_conn_id='api_posts',
        endpoint=api_endpoint,  # Use the dynamic API endpoint here
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    # 4. Save posts to a file
    task_save = PythonOperator(
        task_id='save_posts',
        python_callable=save_posts
    )
