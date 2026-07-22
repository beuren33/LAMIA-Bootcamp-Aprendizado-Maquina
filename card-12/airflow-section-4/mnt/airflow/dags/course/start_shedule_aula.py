from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2026, 7, 22, 1),
    # quando o dag começara a ser agendado ano|mes|dia|hora
    'owner': 'Airflow'
}

with DAG(dag_id='start_and_schedule_dag', schedule_interval="0 * * * *", default_args=default_args) as dag:
                # sera programado a hora de execuçao do dag min|hora|dia|mes|semana
    
    dummy_task_1 = DummyOperator(task_id='dummy_task_1')
    
    # Task 2
    dummy_task_2 = DummyOperator(task_id='dummy_task_2')
    
    dummy_task_1 >> dummy_task_2
    # define a ordem de execução
    
