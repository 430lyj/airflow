#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Example DAG demonstrating the usage of the BashOperator."""

from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", # 대시보드에 노출되는 이름
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 5, 9, tz="Asia/Seoul"),
    catchup=False, # True : DAG 가 올라오지 않아 밀린 시간동안 누적된 DAG 실행
    # dagrun_timeout=datetime.timedelta(minutes=60), # 60분 이상이면 타임아웃
    tags=["example", "example2"], # 대시보드에 노출되는 태그
    params={"example_key": "example_value"}, # 각 테스크에 공통적으로 넘겨줘야 할 파라미터가 있다면 여기에
) as dag:
    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1", # 그래프 상 노출되는 태스크의 이름
        bash_command="echo who_am_i",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2", # 그래프 상 노출되는 태스크의 이름
        bash_command="echo $HOSTNAME",
    )
    
    bash_t1 >> bash_t2 # 태스크 간의 순서 명시
