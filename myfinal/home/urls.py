from . import views
from django.urls import path

urlpatterns = [
    # /home/
    path('', views.home, name='home'),
    # /home/result/
    path('result/', views.result, name='result')
]
