from django.contrib import admin
from django.urls import path
from . import views

app_name = 'vig'

urlpatterns = [
    path('vig_home/', views.vig_home , name='vig_home'),
    path('get-person-details/', views.get_person_details, name='get_person_details'),
    path('comp_entry/', views.createComplainant , name='comp_entry'),
    path('vig_add/', views.vig_add_data , name='vig_add'),
    path('vig_update/<str:pk>/', views.vig_update_data , name='vig_update'),
    path('vig_view/<str:pk>/', views.vig_view_ref , name='vig_view'),
    
    
]