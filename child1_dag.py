from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.python_operator import PythonOperator

# Define your child DAG
child_dag = DAG(
    'child1_dag',
    schedule_interval=None,  # Or set a suitable schedule interval for the child DAG
    start_date=datetime(2023, 7, 1),
    catchup=False
)

def print_hello():
    print ('+++++++++++ hello world +++++++++++++++++++++++') 

# Define your tasks for the child DAG
task_1 = DummyOperator(task_id='task_1', dag=child_dag)
task_2 = DummyOperator(task_id='task_2', dag=child_dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=child_dag)

# Define the dependencies between tasks (if any)
task_1 >> task_2 >> hello_operator
