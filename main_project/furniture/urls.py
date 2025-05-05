from django.contrib import admin
from django.urls import path
from . import views

app_name = 'fur'

urlpatterns = [
    path('fur_home', views.fur_home , name='fur_home'),
    
]