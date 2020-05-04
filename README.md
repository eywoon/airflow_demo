
## Airflow demo for the course [DD2482](https://github.com/KTH/devops-course "Devops")

## Setup
Follow Airflows installation guidelines and then the
[setup](https://airflow.apache.org/docs/stable/start.html "Airflow")

## Run
- Start the Airflow server `airflow webserver -p 8080`
- Start the scheduler `airflow scheduler`

Go to localhost:8080 in the browser

You should see the workflows in the UI. They are defined in dags/

To run an example you can trigger a task using
`airflow run dag_id task_id 2015-01-01`
