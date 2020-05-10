##Description
This is a repository for a demo for workflow orchestration with Airflow.
It has an integration to slack to show how easy it is to add integrations to external sources
with Airflow's operators.
Airflow uses directed acyclic graphs, or DAGs to manage workflows. Where each
task in the workflow is represented by a node in the DAG and relationships between
the tasks are links in the graph.

[Link to demo video](https://youtu.be/lYMHb_muOew "Demo")

##Setup
Setup varies between platforms so it's easiest to use Airflow's guidelines to get started.

Follow Airflows installation guidelines
[installation guidelines](https://airflow.apache.org/docs/stable/start.html "Airflow Quickstart")

##Run
Note that this repository isn't exactly plug and play but rather an example.
You will have to set it up locally with correct configurations for it to run.
It's missing the config files from this repository.

Start by defining Airflow's home
`export AIRFLOW_HOME=~/airflow`

This version is using Postgres as the database
To add Postgres you have to run `pip install 'apache-airflow[postgres]'`

Set up the database according to instructions for your local environment and
operating system. Start the Postgres server as well.
Change the sql_alchemy_conn to in the airflow.cfg file
`sql_alchemy_conn = postgresql+psycopg2://username:password@localhost:5432/database_name`
And set the executor to LocalExecutor

run `airflow initdb` to start the database

- Start the Airflow server `airflow webserver -p 8080`
- Start the scheduler `airflow scheduler`

Go to localhost:8080

You should see the workflows in the UI. They are defined in dags/ folder.

To run a dag directly from the command line use
`airflow run example_bash_operator runme_0 2015-01-01`

For the tasks to run properly you will have to update the file system path in admin -> connections -> fs_default to point to the airflow how or where you store your dags, the default value for the file system path is "/"

##Slack
For everything to run smoothly with the Slack you will have to follow Slack's guide to webhooks and apps.
[Slack apps](https://api.slack.com/start/overview "Slack apps")

When you have set up and app you have go add a connection to Airflow, by going to admin -> connections -> create
Create a http connection named slack. Set the host as https://hooks.slack.com/services
and the password is the rest of the webhook url that you have generated.

##Easter Egg
Seek and you will find!
Pssst, if you can't find it check the end of the previous demo video
