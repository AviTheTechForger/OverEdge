import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash_operator import BashOperator

# Set the timezone to Indian Standard Time (IST)
local_tz = pendulum.timezone('Asia/Kolkata')

dag = DAG (
    'names_insertion',
    schedule_interval = '*/3 * * * *',
    start_date = pendulum.datetime(2024, 3, 10, tz = local_tz),
    catchup = False,
    tags = ["POC", "POC1"]
)

update_csv = BashOperator(
    task_id = "update_csv",
    bash_command = 'python /opt/airflow/py_scripts/namaste_world.py',
    dag = dag,
    retries = 3,
)

update_csv