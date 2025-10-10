# logger.py
# code related to setting up logging for the project
# e.g., configuring log format, log level, and log file handling

import logging
import os
from datetime import datetime 

LOG_FILE = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_path = os.path.join(os.getcwd(), LOG_FILE) 
os.makedirs(os.path.dirname(log_path), exist_ok=True)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)   

