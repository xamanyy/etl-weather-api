from airflow import DAG
from datetime import timedelta,datetime

default_args ={
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':datetime(2024,1,8),
    'retries':2
}

with DAG(
    'weather-app',
    default_args=default_args,
    description='A simple Weather Api',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    catchup=False,
) as dag:
    
    is_weather_api_ready= HttpSensor(
        task_id='is_weather_api_ready',
        http_conn_id='weatherapp_api',
        endpoint=''
    )