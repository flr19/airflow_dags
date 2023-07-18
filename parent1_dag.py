from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime

# Define your parent DAG
parent_dag = DAG(
    'parent1_dag',
    schedule_interval='@daily',
    start_date=datetime(2023, 7, 1),
    catchup=False
)

# Define the task that triggers the child DAG
trigger_child_dag = TriggerDagRunOperator(
    task_id='trigger_child_dag',
    trigger_dag_id='child1_dag',  # Provide the ID of the child DAG to be triggered
    dag=parent_dag
)

# Define the dependencies for the task (if any)
trigger_child_dag 
