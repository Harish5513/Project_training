from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG
from datetime import datetime

default_args = {
	'owner' : 'airflow',
	'depends_on_past' : False,
	'start_date' : datetime(2022, 2, 23),
	'retries' : 0
}

def task():
    with open('/home/admin-pc/text.txt', 'r') as inp:
        y = inp.read().upper()
    with open('/home/admin-pc/copied/text.txt', 'a') as out:
        out.write(y)


dag = DAG(dag_id='Task_1-1', default_args=default_args, start_date=datetime(2022, 2, 23), schedule_interval='*/1 * * * *',catchup=False)
start = DummyOperator(task_id='start',dag=dag)

copy = PythonOperator(task_id='copy',python_callable=task,dag=dag)


start>>copy



