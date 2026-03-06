from time import sleep

from celery.app import shared_task


@shared_task
def add(x, y):
    return x + y

@shared_task
def long_running_task(n: int):
    print(f"Started long-running task {n}")
    sleep(20 + n)
    print(f"Finished long-running task {n}")
