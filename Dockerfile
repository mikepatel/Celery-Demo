FROM python:3

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

