from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='But what does it do?',
    schedule_interval=timedelta(days=1)
)

what_is_this_thing = BashOperator(
    task_id='what_is_this_thing',
    bash_command='python -mwebbrowser https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    dag=dag
)

what_is_this_thing
