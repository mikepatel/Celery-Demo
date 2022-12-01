################################################################################
# Imports
import os
from celery import Celery
import configparser
from fastapi import FastAPI
import time


################################################################################
# Setup
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "config.ini"))


app = FastAPI()


celery = Celery(
    main=__name__,
    broker=config["REDIS"]["broker"],
    backend=config["REDIS"]["backend"]
)


################################################################################
@app.post("/")
async def index(param: str):
    task = work.delay(param)
    return task.get()


# Simulate a long-running task
@celery.task
def work(param: str):
    time.sleep(10)
    return param
