import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
from airflow.utils.dates import days_ago
import pandas as pd
from airflow.api.client.local_client import Client



def my_func():
    df = pd.read_csv(r"item_spreadsheet.csv")
    df_cleaned = df.dropna()
    print(df.head())
    df_cleaned['total price'] = df_cleaned['quantity']*df_cleaned['sales price']
    print(' ++++++++working ++++++++++ ')
    return df_cleaned

#def invoke_hello():
   # print("~~~working~~~~")
   # c = Client(None, None)
   # c.trigger_dag(dag_id='hello_python_dag', run_id='test_run_id', conf={})

default_args = {
            'owner': 'airflow',    
            #'start_date': airflow.utils.dates.days_ago(2),
            # 'end_date': datetime(),
            # 'depends_on_past': False,
            #'email': ['airflow@example.com'],
            #'email_on_failure': False,
            #'email_on_retry': False,
            # If a task fails, retry it once after waiting
            # at least 5 minutes
            #'retries': 1,
            'retry_delay': timedelta(minutes=5),
        }

dag_python = DAG(
	dag_id = "pythonoperator_demo",
	# schedule_interval='0 0 * * *',
	schedule_interval='@once',	
	dagrun_timeout=timedelta(minutes=60),
	description='use case of python operator in airflow',
	start_date = airflow.utils.dates.days_ago(1))

dummy_task = DummyOperator(task_id='dummy_task', retries=3, dag=dag_python)
python_task = PythonOperator(task_id='python_task', python_callable=my_func, dag=dag_python)
#python_task_2 = PythonOperator(task_id='python_task_2', python_callable= invoke_hello, dag=dag_python)

dummy_task >> python_task 