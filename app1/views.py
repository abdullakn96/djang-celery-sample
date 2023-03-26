from django.shortcuts import render

# Create your views here.
from .tasks import new_task,new_task1,send_mail_func

from django.http import HttpResponse

def celery_test_view(request):
    print("called here---------")
    new_task.delay()
    print("called here---------")
    return HttpResponse("Done")

def celery_test_view1(request):
    print("called here---------")
    new_task1.delay()
    print("called here---------")
    return HttpResponse("success")


def email_send_view(request):
    print("called here---------")
    send_mail_func.delay()
   
    return HttpResponse("successfully sended email")    




