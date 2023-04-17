"""
This module defines the URL patterns for the 'home' app.
"""
from . import views
from django.urls import path

urlpatterns = [
    # /home/
    path('', views.home, name='home'),
    # /home/result
    path('result/', views.result, name='result'),
    # /home/1
    path('<int:sign_id>/', views.detail, name='detail')
]
