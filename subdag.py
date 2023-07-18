from airflow import DAG 
from airflow.operators.subdag import SubDagOperator 
from datetime import datetime 
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.api.client.local_client import Client

#c = Client(None, None)
#c.trigger_dag(dag_id='hello_python_dag', run_id='test_run_id', conf={})


def create_subdag(parent_dag_name, child_dag_name, args): 
    dag_subdag = DAG( 
        dag_id=f'{hello_python_dag}.{pythonoperator_demo}', 
        default_args=args, 
        schedule_interval="@daily", 
    ) 
    
    # Define tasks within the SubDAG here 
    
    return dag_subdag 
    
# Parent DAG definition 
with DAG(dag_id='hello_python_dag', start_date=datetime(2023, 7, 14), schedule_interval="@daily") as dag: 
    start_task = DummyOperator(task_id='start_task') 
    end_task = DummyOperator(task_id='end_task') 
    
    subdag_task = SubDagOperator( 
        task_id='subdag_task', 
        subdag=create_subdag('hello_python_dag', 'pythonoperator_demo', dag.default_args), 
        dag=dag, 
    ) 
    
    start_task >> subdag_task >> end_task 