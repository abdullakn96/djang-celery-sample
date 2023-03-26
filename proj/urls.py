"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name

from django import views
from django.contrib import admin
from django.urls import path,include
# from task2.views import ReviewEmailView
from app1 import views
from bookapp.views import manager_functions, prefetch_related_view
from .views import blog_post_view, home_view, select_related_View

urlpatterns = [
    # path('app/',include('app1.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('first_task/', views.celery_test_view),
    path('first_task1/', views.celery_test_view1),
    path('send_email/', views.email_send_view),

    



    path('home_view/',home_view),
    path('blog-post/',blog_post_view),
    path('select-view/',select_related_View),
    path('prefetch-view/',prefetch_related_view),
   
    # path('reviews/',ReviewEmailView.as_view(),name='reviews'),


    path('model-manager/',manager_functions)
  
]
