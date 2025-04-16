import pandas as pd
import numpy as np
from src.logger.custom_logging import logging
from src.exception.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split # type: ignore
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started.")
        try:
            data = pd.read_csv("gemstone.csv")  # <-- make sure this path is correct
            logging.info("Successfully read the dataset.")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved raw dataset to artifact folder.")

            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Performed train-test split.")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Saved train and test datasets.")

            logging.info("Data ingestion completed successfully.")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error(f"Exception occurred during data ingestion: {e}")
            raise customexception(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
