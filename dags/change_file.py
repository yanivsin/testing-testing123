import datetime
import logging
import os
import re
from datetime import timedelta

from _lib.config.parse_config import parse_dag_vars, parse_global_vars
from _lib.functions.db_utils import execute_mysql_query
from _lib.operators.monitoring_operator import MonitoringHandler
from _lib.functions.aws_utils import (
    s3_delete_prefix,
    does_s3_path_exist,
    s3_path_to_params as s3_split_path_and_bucket,
)
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.utils.dates import days_ago

dag_description = """
queries the BI_RDS in order to find the latest partitions. if there are multiple versions and the timestamp is with in
two weeks retains 2 versions, otherwise leaves only one version remaining.
"""
print('ctr')
