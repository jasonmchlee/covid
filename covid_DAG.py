from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
#
# Import functions
from covid_datasets import covid_data, covid_pivots, mortality_data
from usa_covid_cases import usa_covid_data


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 10, 12),
    'retries': 2,
    'retry_delay': timedelta(seconds=20)}

dag =  DAG(dag_id = 'covid_updates',
           default_args = default_args,
           schedule_interval = "30 4 * * *") # 8:30 pm daily

# Download WHO dataset
t1 = PythonOperator(task_id = 'world_covid_data',
                    python_callable = world_covid_data,
                    dag = dag)

# Save pivot tables from WHO dataset
t2 = PythonOperator(task_id = 'covid_pivots',
                    python_callable = covid_pivots,
                    dag = dag)

# Mortality rate data
t3 = PythonOperator(task_id = 'mortality_data',
                    python_callable = mortality_data,
                    dag = dag)

# USA datasets
t4 = PythonOperator(task_id = 'usa_covid_data',
                    python_callable = usa_covid_data,
                    dag = dag)

# Dependecies
t1 >> [t2,t3] >> t4
