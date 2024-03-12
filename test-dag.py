from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta


def print_hello():
    return "Hello, Airflow!"


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_airflow',
    default_args=default_args,
    description='A simple DAG that prints Hello, Airflow!',
    schedule_interval=timedelta(days=1),
)

task_hello = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

task_hello
