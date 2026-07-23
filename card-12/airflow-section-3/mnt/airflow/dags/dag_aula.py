import airflow
from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.sensors.http_sensor import HttpSensor
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.hive_operator import HiveOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.slack_operator import SlackAPIPostOperator
from datetime import datetime, timedelta
import os
import csv
import requests
import json

FOREX_API_KEY = os.environ.get("FOREX_API_KEY")
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

default_args = {
            "owner": "Airflow",
            "start_date": datetime(2026,7,19),
            "depends_on_past": False,
            "email_on_failure": False,
            "email_on_retry": False,
            "email": "youremail@gmail.com",
            "retries": 1,
            "retry_delay": timedelta(minutes=5)
        }
# argumentos padrao usados no dag
# email de erro/retry desligado, se falhar tenta de novo 1 vez esperando 5 min

def download_rates():
    with open('/usr/local/airflow/dags/files/forex_currencies.csv') as forex_currencies:
        reader = csv.DictReader(forex_currencies, delimiter=';')
        for row in reader:
            base = row['base']
            with_pairs = row['with_pairs'].split(' ')
            indata = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={os.environ.get("FOREX_API_KEY")}').json()
            outdata = {'base': base, 'rates': {}, 'last_update': indata['date']}
            for pair in with_pairs:
                outdata['rates'][pair] = indata['rates'][pair]
            with open('/usr/local/airflow/dags/files/forex_rates.json', 'a') as outfile:
                json.dump(outdata, outfile)
                outfile.write('\n')
# funcao que le os dados da api,joga tudo em um json

with DAG(dag_id="forex_data_pipeline_final", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    # dag roda 1x por dia, catchup=False pra nao rodar as datas passadas

    is_forex_rates_available = HttpSensor(
            task_id="is_forex_rates_available",
            method="GET",
            http_conn_id="forex_api",
            endpoint="latest",
            response_check=lambda response: "rates" in response.text,
            # so passa se a palavra rates aparecer na resposta
            poke_interval=5,
            timeout=20
    )
    # testa se a api ta respondendo antes de seguir o pipeline

    is_forex_currencies_file_available = FileSensor(
            task_id="is_forex_currencies_file_available",
            fs_conn_id="forex_path",
            filepath="forex_currencies.csv",
            poke_interval=5,
            timeout=20
    )
    # espera o json com as moedas estar disponivel

    downloading_rates = PythonOperator(
            task_id="downloading_rates",
            python_callable=download_rates
    )
    # roda a funcao download_rates

    saving_rates = BashOperator(
        task_id="saving_rates",
        bash_command="""
            hdfs dfs -mkdir -p /forex && \
            hdfs dfs -put -f $AIRFLOW_HOME/dags/files/forex_rates.json /forex
            """
    )
    # sobe o json gerado pro hdfs, dentro da pasta forex
    creating_forex_rates_table = HiveOperator(
        task_id="creating_forex_rates_table",
        hive_cli_conn_id="hive_conn",
        hql="""
            CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
                base STRING,
                last_update DATE,
                eur DOUBLE,
                usd DOUBLE,
                nzd DOUBLE,
                gbp DOUBLE,
                jpy DOUBLE,
                cad DOUBLE
                )
            ROW FORMAT DELIMITED
            FIELDS TERMINATED BY ','
            STORED AS TEXTFILE
        """
    )
    # registra a tabela forex_rates no hive apontando pro arquivo que subiu
    forex_processing = SparkSubmitOperator(
        task_id="forex_processing",
        conn_id="spark_conn",
        application="/usr/local/airflow/dags/scripts/forex_processing.py",
        verbose=False
    )
    # dispara o script spark que trata os dados salvos
    sending_email_notification = EmailOperator(
            task_id="sending_email",
            to="airflow_course@yopmail.com",
            subject="forex_data_pipeline",
            html_content="""
                <h3>forex_data_pipeline succeeded</h3>
            """
            )
    # avisa por email que o pipeline terminou

    sending_slack_notification = SlackAPIPostOperator(
        task_id="sending_slack",
        token=SLACK_TOKEN,
        username="airflow",
        text="DAG forex_data_pipeline: DONE",
        channel="#airflow-exploit"
    )
    # avisa no slack tambem

    # ordem de execucao das tasks
    is_forex_rates_available >> is_forex_currencies_file_available >> downloading_rates >> saving_rates >> creating_forex_rates_table >> forex_processing >>  sending_email_notification >> sending_slack_notification