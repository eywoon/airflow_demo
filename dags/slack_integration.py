from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'slack_integration',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1)
)

print_date = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

SLACK_CONN_ID = 'slack'
slack_msg = "Your task has finished :bowtie:"
slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password

slack_integration = SlackWebhookOperator(
    task_id='slack_integration',
    http_conn_id='slack',
    webhook_token=slack_webhook_token,
    message=slack_msg,
    username='airflow',
    icon_emoji='frog',
    dag=dag
)

print_date >> slack_integration
