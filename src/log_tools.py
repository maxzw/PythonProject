from datetime import datetime
import logging

def create_logger(log_status):
    if log_status:
        dt = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
        open(f"./logs/{dt}.txt", "x")
        logging.basicConfig(
                    level=logging.DEBUG,
                    format='%(asctime)s | %(name)5s | %(levelname)8s | %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    handlers=[
                        logging.FileHandler(f"./logs/{dt}.txt"),
                        logging.StreamHandler()
                    ])
    else:
        logging.basicConfig(
                    level=logging.DEBUG,
                    format='%(asctime)s | %(name)5s | %(levelname)8s | %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S'
                    )
    return logging
