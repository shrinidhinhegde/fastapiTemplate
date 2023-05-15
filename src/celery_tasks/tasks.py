from celery import shared_task


@shared_task
def test_shared_task():
    print('task executed via celery')
