"""
URL configuration for main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'vip'
urlpatterns = [
    path('', views.vip_home , name='viphome'),
    path('vip/', views.home , name='home'),
    path('add_data/', views.add_data , name='add_data'),
    path('update_data/<str:pk>', views.update_data , name='update_data'),
    path('view_ref/<str:pk>', views.view_ref, name='view_ref'),
    path('vip_entry/', views.createVIP, name='vip_entry'),
    path('hod_entry/', views.createHOD, name='hod_entry'),

]
