import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Assignment.settings')

app = Celery('Assignment')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Configuring scheduler.
app.conf.beat_schedule = {
    'update_task_status': {
        'task': 'update_task_status',  
        'schedule': 20.0,
    }
}
