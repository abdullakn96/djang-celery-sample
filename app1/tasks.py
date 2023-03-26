from celery import shared_task


from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from proj import settings


@shared_task
def add(x,y):
    return x+y

@shared_task
def task1(x,y):
    return x+y    


@shared_task
def new_task(bind=True):
    print("task is running new")
    for i in range(10):
        print(i)
    print("task is finisheds")
    return "success"   

@shared_task
def new_task1():
    print("task is running new")
    for i in range(10):
        print(i)
    print("task is finisheds")
    return "success"      


	
@shared_task
def send_mail_func(self):
    # users=get_user_model().objects.all()
    # for user in users:
    mail_subject="This is Celery Task"
    message="subscribe TheCodeSpace Youtube channel."
    to_email="abdullakn96@gmail.com"
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
        )
    print("sended------")    
    return "Task Successfull"     


