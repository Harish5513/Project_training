from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG
from datetime import datetime
from copy_file import *

default_args = {
	'owner' : 'airflow',
	'depends_on_past' : False,
	'start_date' : datetime(2022, 2, 23),
	'retries' : 0
}
dag = DAG(dag_id='Task_!-1', default_args=default_args, start_date=datetime(2022, 2, 23), schedule_interval='*/2 * * * *',catchup=False)
start = DummyOperator(task_id='start',dag=dag)

copy = PythonOperator(task_id='copy',python_callable=task_1,dag=dag)

    #convert = PythonOperator(
     #   task_id='convert',
     #   python_callable=case_change(),
    #)

start>>copy

globals()['Task_!-1'] = dag
