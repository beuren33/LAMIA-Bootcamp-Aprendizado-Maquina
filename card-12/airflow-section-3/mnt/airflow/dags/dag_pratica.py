from airflow import DAG
from datetime import datetime, timedelta
from airflow.sensors.http_sensor import HttpSensor
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.hive_operator import HiveOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.slack_operator import SlackAPIPostOperator

import os
import json
import requests
import csv

FOREX_API_KEY = os.environ.get("FOREX_API_KEY")
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

default_args = {
            "owner": "airflow",
            "start_date": datetime(2026, 7, 20),
            "depends_on_past": False,
            "email_on_failure": False,
            "email_on_retry": False,
            "email": "exemplloteste@host.com",
            "retries": 2,
            "retry_delay": timedelta(minutes=1)
        }
# define argumentos default para o dag
# por enquanto nao ha notificacao por email, mas ele tentará 1 vez com um delay de 5 minutos

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
# vai fazer o download dos dados e inserir em um arquivo json como output
                
with DAG(dag_id="pipeline_project_forex", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    # define os parametros para o dag, sendo executado todo dia, usando os argumentos defaults definidos la em cima, o catchup=False garante que ele nao execute dias retroativos

    pipeline_available = HttpSensor(
        task_id="pipeline_rates_available",
        method="GET",
        http_conn_id="forex_api",
        endpoint=f"v1/latest?access_key={FOREX_API_KEY}",
        # tive que utilizar uma chave de acesso, pois o site nao esta como no video de 2020, agora precisamos de uma chave de acesso
        response_check=lambda response: "rates" in response.text,
        # o lamda vai retornar true se rates estiver no texto, indicando que deu certo
        poke_interval=5,
        timeout=50
    )
    # verifica se a requisicao vai funcionar
    
    forex_files_available = FileSensor(
        task_id="pipeline_forex_path",
        fs_conn_id="forex_path",
        filepath="forex_currencies.csv",
        poke_interval=5,
        timeout=20
    )
    # checa o arquivo para passar para a proxima task
    # le as moedas para buscar 
    
    forex_download = PythonOperator(
        task_id="pipeline_downloading_rates",
        python_callable=download_rates
    )
    # faz dowload dos dados da request
    
    saving_rates = BashOperator(
        task_id="pipeline_save_rates",
        bash_command="""
            hdfs dfs -mkdir -p /forex && \
            hdfs dfs -put -f $AIRFLOW_HOME/dags/files/forex_rates.json /forex
            """
    )
    forex_rates_table = HiveOperator(
        task_id="pipeline_rates_table",
        hive_cli_conn_id="hive_conn",
        hql="""
            CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
                base STRING,
                last_update DATE,
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
    # cria uma tabela no HUE para colocar os dados da api
    forex_processing = SparkSubmitOperator(
        task_id="pipeline_processing",
        conn_id="spark_conn",
        application="/usr/local/airflow/dags/scripts/forex_processing.py",
        verbose=False
    )
    
    forex_email =EmailOperator(
        task_id = "pipeline_email",
        to = "airflow_course@yopmail.com",
        subject = "forex_pipeline",
        html_content = "<h3>Pipeline Airflow Succes</h3>"
        
    )
    
    forex_slack = SlackAPIPostOperator(
        task_id="pipeline_slack",
        token=SLACK_TOKEN,
        username="airflow",
        text="pipeline_forex succes",
        channel="#airflow"
    )
    
    pipeline_available>>forex_files_available>>forex_download>>saving_rates>>forex_rates_table>>forex_processing>>forex_email>>forex_slack