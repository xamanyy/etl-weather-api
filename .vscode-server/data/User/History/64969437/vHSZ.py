from airflow import DAG
from datetime import timedelta,datetime
from airflow.providers.http.sensors.http import HttpSensor


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
    catchup=False,
) as dag:
    
    is_weather_api_ready= HttpSensor(
        task_id='is_weather_api_ready',
        http_conn_id='weatherapp_api',
        endpoint='/data/2.5/weather?q=Portland&appid=e1c2b88664f3211ebc372dda792b7c58'
    )
    
    extract_weather_data= SimpleHttpOperator(
        task_id="extract_weather_data",
        http_conn_id="weatherapp_api",
        method='GET',
        endpoint='/data/2.5/weather?q=Portland&appid=e1c2b88664f3211ebc372dda792b7c58',
        data={"param1": "value1"},
        headers={"Content-Type": "application/json"},
        response_filter=lambda response: json.loads(response.text),
        log_response= bool = True,
    )