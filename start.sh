#!bin/sh
nohup airflow scheduler &
airflow webserver --port 8080