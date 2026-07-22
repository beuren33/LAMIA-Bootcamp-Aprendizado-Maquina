import pendulum
from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy_operator import DummyOperator

from datetime import timedelta, datetime

local_tz = pendulum.timezone("Europe/Paris")

default_args = {
    'start_date': datetime(2026, 7, 22, 1),
    'owner': 'Airflow'
}

with DAG(dag_id='tz_dag', schedule_interval="0 1 * * *", default_args=default_args) as dag:
    # executa toda dia as 1 da manha
    dummy_task = DummyOperator(task_id='dummy_task')
    
    run_dates = dag.get_run_dates(start_date=dag.start_date)
    # pega do dag todas as datas de execução
    next_execution_date = run_dates[-1] if len(run_dates) != 0 else None
    # verifica se tem mais que 0 execuções retorna a ultima, caso nao tenha nenhuma retorna None
