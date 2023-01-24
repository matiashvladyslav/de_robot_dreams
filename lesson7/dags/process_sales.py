import json
import os

from datetime import datetime

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator

DEFAULT_ARGS = {
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': 30,
}

BASE_DIR = os.environ.get("BASE_DIR")

dag = DAG(
    dag_id='process_sales',
    start_date=datetime(2022, 8, 9),
    end_date=datetime(2022, 8, 12),
    schedule_interval="0 1 * * *",
    catchup=True,
    max_active_runs=1,
    default_args=DEFAULT_ARGS
)

extract_data_from_api = SimpleHttpOperator(
    task_id='extract_data_from_api',
    method='POST',
    endpoint='http://localhost:8081/',
    http_conn_id='',
    data=json.dumps({
            "date": "{{ ds }}",
            "raw_dir": os.path.join(BASE_DIR, "raw", "sales", "{{ ds }}")
        }),
    headers={"Content-Type": "application/json"},
    response_check=lambda response: True if response.status_code == 201 else False,
    dag=dag
)

convert_to_avro = SimpleHttpOperator(
    task_id='convert_to_avro',
    method='POST',
    endpoint='http://localhost:8082/',
    http_conn_id='',
    data=json.dumps({
            "raw_dir": os.path.join(BASE_DIR, "raw", "sales", "{{ ds }}"),
            "stg_dir": os.path.join(BASE_DIR, "stg", "sales", "{{ ds }}")
        }),
    headers={"Content-Type": "application/json"},
    response_check=lambda response: True if response.status_code == 201 else False,
    dag=dag
)

extract_data_from_api >> convert_to_avro
