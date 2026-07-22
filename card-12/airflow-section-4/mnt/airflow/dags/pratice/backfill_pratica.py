from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2026, 7, 22),
    'owner': 'matheus'
}

with DAG(dag_id='backfill', schedule_interval="0 0 * * *", default_args=default_args, catchup=True) as dag:
    # executa toda meia noite de cada dia, recompondo as tarfeas atrasadas ou nao executadas
    # Task 1
    task_1 = BashOperator(task_id='task_1', bash_command="echo 'first task'")
    
    # Task 2
    task_2 = BashOperator(task_id='task_2', bash_command="echo 'second task'")

    task_1 >> task_2