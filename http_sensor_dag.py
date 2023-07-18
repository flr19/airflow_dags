from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.http.sensors.http import HttpSensor

with DAG(dag_id='http_sensor_example', start_date=datetime(2023, 1, 1), schedule_interval=None) as dag:
    start_task = DummyOperator(task_id='start_task')
    
    wait_for_api = HttpSensor(
        task_id='wait_for_api',
        http_conn_id='http_default',
        endpoint='https://mocki.io/v1/2ddca92b-b5f0-487d-bc01-550382035fe4',
        method='GET',
        response_check=lambda response: response.status_code == 200,
        timeout=300,
        poke_interval=60,
        dag=dag,
    )
    
    end_task = DummyOperator(task_id='end_task')
    
    start_task >> wait_for_api >> end_task
