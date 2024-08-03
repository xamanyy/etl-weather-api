from airflow import DAG

default_args ={
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':datetime(2024,1,8)
}
dag = with DAG(
    'tutorial',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
) as dag: