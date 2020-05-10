from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
from random import random


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'batch_processing',
    default_args=default_args,
    description='A file processing example',
    schedule_interval=timedelta(days=1)
)

#these sensor will sucseed when the files get there.
#They both have to succeed for workflow to move forward
read_file_a = FileSensor(
    task_id='read_file_a',
    poke_interval=30,
    #filepath is dependant on how the connection fs_default is set up
    filepath='resources/fileA.txt',
    fs_conn_id='fs_default',
    dag=dag
)

read_file_b = FileSensor(
    task_id='read_file_b',
    poke_interval=30,
    filepath='resources/fileB.txt',
    fs_conn_id='fs_default',
    dag=dag
)

def file_merger():
    fileID = random()
    output_path = "resources/output{fileID}.txt".format(fileID = fileID)
    filenames = ['resources/fileA.txt', 'resources/fileB.txt']
    with open(output_path, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

merge_files = PythonOperator(
    task_id = 'merge_files',
    python_callable=file_merger,
    dag=dag
)

SLACK_CONN_ID = 'slack'
slack_msg = "Your task has finished :bowtie:"
slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password

notify = SlackWebhookOperator(
    task_id='slack_notification',
    http_conn_id='slack',
    webhook_token=slack_webhook_token,
    message=slack_msg,
    username='airflow',
    icon_emoji='frog',
    dag=dag
)

[read_file_a, read_file_b] >> merge_files >> notify
