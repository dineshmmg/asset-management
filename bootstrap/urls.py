from django.urls import path

from . import views

urlpatterns = [
     path("", views.login, name="login"),
     path("login", views.login, name="login"),
     
     
     path("index", views.index, name="index"),
     
     
     path("register/", views.register, name="register"),
     path("register/register", views.register, name="register"),
     path("register/login", views.login, name="login"),
     
     
     path("user/", views.userpage, name="user-page"),
     
     
     
     
]
