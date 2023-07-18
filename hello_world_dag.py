
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    print ('+++++++++++ hello world +++++++++++++++++++++++') 
    

dag = DAG('hello_python_dag',description='Hello World DAG',
        schedule_interval='0 12 * * *',
        start_date=datetime(2023,7,10), catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator
