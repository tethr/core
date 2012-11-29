from __future__ import absolute_import

from celery import Celery

celery = Celery('managr.celery',
                broker='amqp://',
                backend='amqp://')

# Optional configuration, see the application user guide.
celery.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

@celery.task
def add(x, y):
    return x + y


@celery.task
def mul(x, y):
    return x * y


@celery.task
def xsum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    celery.start()