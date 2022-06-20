# import the libraries

from datetime import timedelta
from hmac import new
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator

from airflow.operators.python_operator import PythonOperator


# This makes scheduling easy
from airflow.utils.dates import days_ago

# to make the HTPS requests
import requests

# To be able to manipulate the data.
import pandas as pd
import os
import random
import json

import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", joblib])


import joblib


# defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Julian Oliveros',
    'start_date': days_ago(0),
    'email': ['julian-esteban.oliveros-forero@epita.fr'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


# define the DAG
dag = DAG(
    'scheduled_predictions',
    default_args=default_args,
    description='make scheduled predictions each n mins to the API',
    schedule_interval=timedelta(minutes=1),
)


def randrange_float(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start

# define the tasks

# define the first task who ita going to take the data from the test.

def new_data(numofdata: int):

    data = []
    for i in range(1, numofdata+1):
        df2 = {
               # 'id': i,
               'battery_power': random.randint(500, 2000),
               'blue': random.randint(0, 1),
               'clock_speed': randrange_float(0.5, 3.0, 0.5),
               'dual_sim': random.randint(0, 1),
               'fc': random.randint(0, 19),
               'four_g': random.randint(0, 1),
               'int_memory': random.randint(2, 64),
               'm_dep': randrange_float(0.1, 1.0, 0.1),
               'mobile_wt': random.randint(80, 200),
               'n_cores': random.randint(0, 22),
               'pc': random.randint(0, 20),
               'px_height': random.randint(0, 2000),
               'px_width': random.randint(500, 2000),
               'ram': random.randint(263, 4000),
               'sc_h': random.randint(5, 19),
               'sc_w': random.randint(0, 18),
               'talk_time': random.randint(2, 20),
               'three_g': random.randint(0, 1),
               'touch_screen': random.randint(0, 1),
               'wifi': random.randint(0, 1)
               }
        data.append(df2)
    df = pd.DataFrame(data)
    return df


def download_data():
    #x = requests.get('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt')
    # print(x.status_code)
    # df = pd.read_csv(io.StringIO(x.text), sep='#')
    df = new_data(10)
    df.to_csv('newData.csv', index=False)
    print(df)


extract = PythonOperator(
    task_id='extract',
    provide_context=True,
    python_callable=download_data,
    dag=dag,
)


def run_this_func_to_transform():

    print("HELOOOO WE DID IT ")
    data_total = pd.read_csv("newData.csv")
    #data_total = data_total.sample(n=2)
    df_json = data_total.to_json(orient='records')
    payload = {"dataframe1": df_json}
    print(payload)

    with open('data.json', 'w') as f:
        json.dump(payload, f)


transform = PythonOperator(
    task_id='transform',
    provide_context=True,
    python_callable=run_this_func_to_transform,
    dag=dag,
)


# def run_this_func_predict(payload):
#    res = requests.post("http://fastapi:5000/predictjson", json=payload)
#    print(res)


def run_this_func_predict():

    # print("PREDICT PART")
    # with open('data.json') as f:
    #     data = json.load(f)

    df = pd.read_csv("newData.csv")

    print(df)

    model = joblib.load(os.path.join('/opt/airflow/models', "model.joblib"))
    pred = model.predict(df)
    predj = json.dumps(pred.tolist())

    print(predj)

    return predj


predictions = PythonOperator(
    task_id='predictions',
    provide_context=True,
    python_callable=run_this_func_predict,
    dag=dag,
)


# task pipeline
extract >> transform >> predictions
