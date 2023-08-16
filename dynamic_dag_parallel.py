from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
import pandas as pd

PARAMS_FILE= pd.read_csv('dags/dynamic_dag_tutorial.conf',header=0)


with DAG("dynamic_dag_parallel",
    start_date = days_ago(1),
    schedule_interval=None) as dag:

    start = DummyOperator(task_id='start_wf')

    end = DummyOperator(task_id='end_wf',)


task_list = []

for index, row in PARAMS_FILE.iterrows():
    task = BashOperator(
        task_id=f"command_task_{index}",
        bash_command=row['command']
    )
    task_list.append(task)

start >> task_list >> end