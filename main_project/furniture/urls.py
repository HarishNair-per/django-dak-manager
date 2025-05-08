from django.contrib import admin
from django.urls import path
from . import views

app_name = 'fur'

urlpatterns = [
    path('fur_home/', views.fur_home , name='fur_home'),
    path('fur_add/', views.fur_add , name='fur_add'),
    path('fur_update/<str:pk>', views.fur_update , name='fur_update'),
    
]