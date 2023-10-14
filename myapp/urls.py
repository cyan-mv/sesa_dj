from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data_dummy/', views.data_dummy, name='data_dummy'),
    # path('create_excel/', views.run_script, name='create_excel'),
    # path('create_region/', views.create_region, name='create_region'),
    path('delete_all_regions/', views.delete_all_regions_view, name='delete_all_regions'),
    path('save_data_2/', views.save_data_2, name='save_data_2'),
]
