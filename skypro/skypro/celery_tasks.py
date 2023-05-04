from celery import Celery
from skypro.settings.django_environ import env
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skypro.settings.settings')

app = Celery('skypro')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {

}