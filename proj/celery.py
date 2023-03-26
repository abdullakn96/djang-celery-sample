import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()




#celery beat settings
app.conf.beat_schedule={
    'send-mail-everyday-at-1':{
        'task':'app1.tasks.send_mail_func',
        'schedule': crontab(hour=17,minute=49),
        # we can pass arguments here and we can use those in
        # firemailapp/tasks.py send_mail_func function for 
        # that you need one extra argument in your function
        # currently we are not doing that
        'args': (1000,)  
    }
}