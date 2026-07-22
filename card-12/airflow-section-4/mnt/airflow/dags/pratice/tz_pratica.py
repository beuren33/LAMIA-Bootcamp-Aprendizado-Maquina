import pendulum
from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy_operator import DummyOperator
from datetime import timedelta, datetime

local_tz = pendulum.timezone("America/Sao_Paulo")
# pega o fuso horario de sao paulo

default_args = {
    'start_date': datetime(2026, 7, 22, 1),
    'owner': 'matheus'
}

with DAG(dag_id='tz_dag', schedule_interval="0 12 * * *", default_args=default_args) as dag:
    # executa toda dia as 1 da manha
    dummy_task = DummyOperator(task_id='dummy_task')
    
    run_dates = dag.get_run_dates(start_date=dag.start_date)
    # pega do dag todas as datas de execução
    next_execution = run_dates[-1] if len(run_dates) != 0 else None
    # verificação do que o airflow faz internamente
    #pega a ultima execução da lista
    