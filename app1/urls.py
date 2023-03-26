
from django.urls import path
from app1.views import celery_test_view


urlpatterns = [
    path('first_task/', celery_test_view.view()),
 
]