from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
import pandas as pd

PARAMS_FILE= pd.read_csv('dags/dynamic_dag_tutorial.conf',header=0)


with DAG("dynamic_dag_tutorial",
    start_date = days_ago(1),
    schedule_interval=None) as dag:

    start = DummyOperator(task_id='start_wf')

    end = DummyOperator(task_id='end_wf',)

    for index, row in PARAMS_FILE.iterrows():
        locals()['command_'+str(index)]=BashOperator(
            task_id="command_"+str(index),
            bash_command=PARAMS_FILE['command'][index]
            )

for index, row in PARAMS_FILE.iterrows():
    if PARAMS_FILE.shape[0]==1:
        start>>locals()['command_'+str(index)]
        locals()['command_'+str(index)]>>end
    elif index==0 and (PARAMS_FILE.shape[0])>1:
        start>>locals()['command_'+str(index)]
        locals()['command_'+str(index)]>>locals()['command_'+str(index+1)]
    elif 0<index<(PARAMS_FILE.shape[0])-1:
        locals()['command_'+str(index)]>>locals()['command_'+str(index+1)]
    else:
        locals()['command_'+str(index)]>>end