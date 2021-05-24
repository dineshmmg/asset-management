from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    #path('', views.home, name="home"),
    #path('file_upload', views.file_upload, name="upload"),
    #path('',send_mail.as_view(),name='home'),
    #path('',views.send,name='home'),
    path('', views.emails, name="emails"),
]
