import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onemoreshop.settings')


app = Celery('onemoreshop')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
