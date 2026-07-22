from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2026, 7, 22),
    'owner': 'matheus'
}

def second_task():
    #print('Hello from second_task')
    raise ValueError('This will turns the python task in failed state')

def third_task():
    print('3 task')

with DAG(dag_id='depends_task', schedule_interval="0 0 * * *", default_args=default_args) as dag:
    
    task_1 = BashOperator(task_id='task_1',bash_command="echo 'first task'", wait_for_downstream = True)
    
    task_2 = PythonOperator(task_id='task_2', python_callable=second_task)

    task_3 =PythonOperator(task_id='task_3', python_callable=third_task)

    task_1 >> task_2 >> task_3
    #define a ordem e dependencias das tasks no dag