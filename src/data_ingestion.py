import os 
import sys
import logging


from pandas.io.parsers import read_csv
from exception import CustomException
from logger import logging
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# the train data test data and raw data should be saved somewhere using 
# the below class . the inputs are raw data, traina data, test data

# the output could be file, folder, numpy array

# the reason for using the decorator dataclass is that with using this decorator 
# we do not need to use __init__ to define the variables inside our class and 
# we can define our variables directly.

@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join("artifact","train.csv")
    test_data_path : str=os.path.join("artifact","test.csv")
    raw_data_path : str=os.path.join("artifact","data.csv")

# the above are the input for data ingestion component and data ingestion component
# knows where to save all the inputs
# the data ingestion component save this train path 
# if we have only variables not methods inside the calss use dataclass decorator 
# otherwise use __init__ constructor. 
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
# this ingestion_config consists of the above values
# as soon as calling the class the variables will be saved inside the ingestion_config        # 

def initiate_data_ingestion(self):
    logging.info("entered the data ingestion method or component")
# this method is used to for instanse read the data from some data bases
    try:
        df=read_csv("notebook\data\student.csv")
        logging.info("read the dataset as a dataframe")
        os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
    # exist_ok=True mean if there is a directory name the same, there is 
    # no need to make the directory again
    # os.path.dirname() returns the directory portion of the train_data_path
        df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

        logging.info("train test split initiated")
        train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
        train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
        test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

        logging.info("ingestion of the data is complited")
    # here we read the data from database. it could be mango db and any other DB
        return(self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path)

    # we have to return the train and test data because we nned them in data transformtation process
    except Exception as e:
        raise CustomException(e,sys)
        

if __name__=="__main__":
    initiate_data_ingestion(DataIngestion())

