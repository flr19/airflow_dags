from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

def print_response(response):
    print(response.json())

with DAG(dag_id='http_operator_example', start_date=datetime(2023, 1, 1), schedule_interval=None) as dag:
    print_task = PythonOperator(
        task_id='print_task',
        python_callable=print_response,
        op_args=[],
        provide_context=True,
    )

    http_task = SimpleHttpOperator(
        task_id='http_task',
        http_conn_id='http_default',
        endpoint='https://jsonplaceholder.typicode.com/posts/1',
        method='GET',
        response_filter=lambda response: response.json(),
        log_response=True,
    )

    print_task << http_task
