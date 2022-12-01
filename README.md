# Celery-Demo
Use Celery with a FastAPI application
Using Redis as message broker


## Instructions
### Docker
1. Run Redis
```
docker run -d -p 6379:6379 --name my-redis redis
```

### Local virtual environment
1. Create a new virtual environment
```
pipenv --python 3
```

2. Activate the new environment (using Windows)
```
pipenv shell
```

3. Install python packages into the environment (Need Celery v4 for Windows)
```
pipenv install -r requirements.txt
```

4. Run FastAPI application (not needed)
```
uvicorn run:app --reload
```

5. Start Celery worker (Linux)
```
celery -A run.celery worker --loglevel=info
```
For Windows,
```
celery -A run.celery worker --loglevel=info -P gevent
```

6. In a new terminal, send a task to the Celery worker
```
python
>>> from run import work
>>> task = work.delay(<argument>)
>>> task = work.delay("Michael")
```

7. In Celery worker terminal, should see logs for receiving and executing task
```
[2022-11-30 20:28:51,968: INFO/MainProcess] Received task: run.work[80d9c9ef-34e5-4bc4-9374-981c73d3c2d2]
[2022-11-30 20:29:01,985: INFO/MainProcess] Task run.work[80d9c9ef-34e5-4bc4-9374-981c73d3c2d2] succeeded in 10.01600000000326s: 'Michael'
```
