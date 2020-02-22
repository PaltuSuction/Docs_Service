from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Docs_Service.settings')

app = Celery('Docs_Service')

app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task():
    print('HELLO!')