from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG
from datetime import datetime
import pandas as pd
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 2, 23),
    'retries': 0
}

def conv():
    df = pd.read_csv (r'/home/admin-pc/csv/sample.csv')
    df.to_json (r'/home/admin-pc/json/sample.json')
    
dag = DAG(dag_id='Task_1-2', default_args=default_args, start_date=datetime(2022, 2, 23),schedule_interval='*/1 * * * *', catchup=False)
start = DummyOperator(task_id='start', dag=dag)

convert_file = PythonOperator(task_id='convert', python_callable=conv, dag=dag)

start >> convert_file

