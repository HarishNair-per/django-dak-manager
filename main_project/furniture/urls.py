from django.contrib import admin
from django.urls import path
from . import views

app_name = 'fur'

urlpatterns = [
    path('asset_home/', views.fur_home , name='fur_home'),
    path('asset_add/', views.fur_add , name='fur_add'),
    path('asset_update/<str:pk>/', views.fur_update , name='fur_update'),
    path('asset_entry/', views.createAsset , name='asset_entry'),
    path('asset_pdf/', views.render_pdf_view , name='asset_pdf'),
    
]