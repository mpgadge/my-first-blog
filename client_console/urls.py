from django.urls import path
from client_console import views

urlpatterns = [
   path('', views.home, name='home')
]
