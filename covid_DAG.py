from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from covid_cases import covid_data


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 10, 4),
    'retries': 2,
    'retry_delay': timedelta(seconds=20)}

dag =  DAG(dag_id = 'covid_updates',
           default_args = default_args,
           schedule_interval = "0 4 * * *")

t1 = PythonOperator(task_id = 'covid_update',
                              python_callable = covid_data,
                              dag = dag)

t1
