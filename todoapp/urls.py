
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('update/<str:pk>/', views.update , name="update"),
    path('completed/<str:pk>/', views.completed , name="completed"),
    path('delete/<str:pk>/', views.delete , name="delete"),
]  
