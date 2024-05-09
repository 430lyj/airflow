from __future__ import annotations

import datetime

import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_conn_test", # 대시보드에 노출되는 이름
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 5, 9, tz="Asia/Seoul"),
    catchup=False, # True : DAG 가 올라오지 않아 밀린 시간동안 누적된 DAG 실행
    tags=["dags", "test"], # 대시보드에 노출되는 태그
) as dag:
    t1 = EmptyOperator(
        task_id = "t1"
    )

    t2 = EmptyOperator(
        task_id = "t2"
    )

    t3 = EmptyOperator(
        task_id = "t3"
    )

    t4 = EmptyOperator(
        task_id = "t4"
    )

    t5 = EmptyOperator(
        task_id = "t5"
    )

    t6 = EmptyOperator(
        task_id = "t6"
    )

    t7 = EmptyOperator(
        task_id = "t7"
    )

    t8 = EmptyOperator(
        task_id = "t8"
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8