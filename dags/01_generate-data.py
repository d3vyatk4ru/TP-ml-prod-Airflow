from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago


DEFAULT_VOLUME = '/home/d3vyatk4ru/Рабочий стол/TP-ml-prod-Airflow/data:/data'

default_args = {
    'owner': 'Devyatkin Daniil',
    'email': ['danya.devyatkin50@gmail.com'],
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    '01_generate-data',
    default_args=default_args,
    description='A DAG for synthetic data generation',
    schedule_interval='@weekly',
    start_date=days_ago(2),
) as dag:
    start = DummyOperator(task_id='Start_data_generation')

    download = DockerOperator(
        task_id='Generate_entries',
        image='airflow-generate-data',
        command='--output-path /data/raw/{{ ds }}',
        network_mode='bridge',
        do_xcom_push=False,
        volumes=[DEFAULT_VOLUME],
    )
    finish = DummyOperator(
        task_id='Finish_data_generation'
    )

    start >> download >> finish