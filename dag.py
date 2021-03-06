from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Sairanjith Thalanki',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 28),
    'email': 'sthalanki@berkeley.com',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('github', default_args=default_args, schedule_interval=timedelta(days=1))

run_script = "/Users/sthalanki/dev/Git/github.sh "
task = BashOperator(
    task_id='run_github_script',
    bash_command=run_script,
    dag=dag
)

