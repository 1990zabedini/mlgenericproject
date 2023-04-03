import logging
import os 
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)
# this means create new directory and append the file in the directory 

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

# if we want to overwire the functionality of this log we have to set it in the basci config 

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO   
)

if __name__=="__main__":
    logging.info("logging has staerted")