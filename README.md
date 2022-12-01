# Celery-Demo
Use Celery with a FastAPI application
Using Redis as message broker


## Instructions
### Docker
1. Redis
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

3. Install python packages into the environment
```
pipenv install -r requirements.txt
```

4. Run application
```
uvicorn run:app --reload
```
