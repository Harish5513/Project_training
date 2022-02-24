from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG
from datetime import datetime
from convert import *

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 2, 23),
    'retries': 0
}
dag = DAG(dag_id='Task_1-2', default_args=default_args, start_date=datetime(2022, 2, 23),
          schedule_interval='*/1 * * * *', catchup=False)
start = DummyOperator(task_id='start', dag=dag)

convert_file = PythonOperator(task_id='convert', python_callable=conv, dag=dag)

# convert = PythonOperator(
#   task_id='convert',
#   python_callable=case_change(),
# )

start >> convert_file

globals()['Task_1-2i'] = dag
