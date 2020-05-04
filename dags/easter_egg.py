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
    'easter_egg',
    default_args=default_args,
    description='A sneaky easter egg',
    schedule_interval=timedelta(days=1)
)

show_easter_egg = BashOperator(
    task_id='show_easter_egg',
    bash_command='python -mwebbrowser https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    dag=dag
)

show_easter_egg
