from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .import views


urlpatterns = [
    #list the Asset types tables
    path('list_items', views.list_items, name='list_items'),
    path('add_items', views.add_items, name='add_items'),
    path('table_items', views.table_items, name='table_items'),
    path('COUNT', views.COUNT, name='COUNT'),
    
    #CRUD Operation for Asset types tables
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('table_items/<int:asset_type_id_id>', views.table_items, name="table_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    
    
    #List and CRUD Operation for user table
    path("auth_user", views.auth_user, name="auth_user"),
    path('add_user/', views.add_user, name='add_user'),
    path('add_user/add_user', views.add_user, name='add_user'),
    path('update_user/<str:pk>/', views.update_user, name="update_user"),
    path('delete_user/<str:pk>/', views.delete_user, name="delete_user"),
    
    
    #List and CRUD Operation for Assets table
    path("assets", views.assets, name="assets"),
    path('add_assets', views.add_assets, name='add_assets'),
    path('update_assets/<str:pk>/', views.update_assets, name="update_assets"),
    path('delete_assets/<str:pk>/', views.delete_assets, name="delete_assets"),
    
    
    #List and CRUD Operation for User Assets
    path("user_assets", views.user_asset, name="user_asset"),
    path('add_user_assets', views.add_user_assets, name='add_user_assets'),
    path('unassigned_assets', views.unassigned_assets, name='unassigned_assets'),
    path('update_user_assets/<str:pk>/', views.update_user_assets, name="update_user_assets"),
    path('delete_user_assets/<str:pk>/', views.delete_user_assets, name="delete_user_assets"),
    
    
]