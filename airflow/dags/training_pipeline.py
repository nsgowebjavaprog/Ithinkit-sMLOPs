from __future__ import annotations
import json
from textwrap import dedent
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.DimondPricePredictor.pipeline.training_pipeline import TrainingPipeline

training_pipeline = TrainingPipeline()

with DAG(
    "gemstone_price_training_pipeline",
    default_args={"retries": 2},
    description="it is my training pipeline",
    schedule = "@weekly",
    start_date = pendulum.datetime(2023, 4, 11, t2="UTC"),
    catchup = False,
    tags = ["machine_learning", "classification", "gemstone"],
) as dag:
    
    dag.doc_md = __doc__
    
    def data_ingestion(**kwargs):
        