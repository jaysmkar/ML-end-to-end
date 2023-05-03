# importing the libraries 
import os 
import logging 
from datetime import datetime 

# giving the path for the log file creation and making the log file 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) 
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# This is the logging information for the log files. 
logging.basicConfig(
    filename = LOG_FILE_PATH, 
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level = logging.INFO, 
)