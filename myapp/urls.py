from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_excel/', views.generate_excel, name='generate_excel'),
   
]

