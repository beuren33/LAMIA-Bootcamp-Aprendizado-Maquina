from airflow import DAG
from airflow.sensors.http_sensor import HttpSensor
from datetime import datetime, timedelta

default_args = {
            "owner": "airflow",
            "start_date": datetime(2019, 12, 4),
            "depends_on_past": False,
            "email_on_failure": False,
            "email_on_retry": False,
            "email": "youremail@host.com",
            "retries": 1,
            "retry_delay": timedelta(minutes=5)
        }
# argumentos defauts utilizados no dag
# define que na queremos nenhuma notificação sobre o airflow no email, e define tentaivas e tempo entre elas

with DAG(dag_id="forex_data_pipeline_v_2", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    # parametros de definição dag
    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        method="GET",
        http_conn_id="forex_api",
        endpoint="latest",
        response_check=lambda response: "rates" in response.text,
        # retorna True se deu certo e False se deu erro
        poke_interval=5,
        timeout=20
    )
    #teste de request