from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
#
# Import functions
from covid_datasets import world_covid_data
from usa_covid_cases import usa_covid_data


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 10, 12),
    'retries': 2,
    'retry_delay': timedelta(seconds=20)}

dag =  DAG(dag_id = 'covid_updates',
           default_args = default_args,
           schedule_interval = "0 4 * * *")

# World datasets
t1 = PythonOperator(task_id = 'world_covid_data',
                    python_callable = world_covid_data,
                    dag = dag)

# USA datasets
t2 = PythonOperator(task_id = 'usa_covid_data',
                    python_callable = usa_covid_data,
                    dag = dag)

# Dependencies
[t1, t2]
