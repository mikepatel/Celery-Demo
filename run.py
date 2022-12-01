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
@app.get("/")
async def index():
    return {
        "message": "Returning message"
    }


# Simulate a long-running task
@celery.task
def work(arg):
    time.sleep(10)
    return arg
