import json
import requests
from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor

"""
Runs a DAG that invokes a webservice through mocki.io

Saves the json response to the data file

Made for testing purpose

Author:
    Farah Lubaba Rouf

"""

def save_users(ti) -> None:
    response_data = ti.xcom_pull(task_ids='invoke_web_service_task')
    
    if response_data:
        with open('data/users.json', 'w') as f:
            json.dump(response_data, f, indent=4)
        print("JSON data saved successfully.")
    else:
        print("No response data to save.")

default_args = {
    'owner': 'farah',
    'start_date': datetime(2023, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'save_users_from_webservice',
    default_args=default_args,
    description='DAG to invoke web service',
    start_date=datetime(2022, 3, 1),
    schedule_interval=timedelta(days=1),  # Runs daily
)

task_invoke_web_service = SimpleHttpOperator(
    task_id='invoke_web_service_task',
    http_conn_id = 'mocki_endpoint' ,
    endpoint = 'users/',
    method = 'GET',
    response_filter=lambda response: json.loads(response.text) ,
    log_response=True ,

   # endpoint='https://api.mocki.io/v2/11fe220e/users',  # Endpoint URL from Mocki.io
    #method='GET',  # Adjusted to GET since it's a GET request
    dag=dag,
)

task_save = PythonOperator(
        task_id='save_users',
        python_callable=save_users
)



task_invoke_web_service >> task_save

