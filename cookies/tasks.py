import time
from test1.celery import app

@app.task
def sayhello():
    print('hello ...')
    time.sleep(2)
    print('world ...')