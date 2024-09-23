from django.urls import path
from stm_generator import views

urlpatterns = [
    path("", views.home, name='home'),
    path("data_types", views.get_list_of_data_types_supported, name='data_types'),
    path("insert_data_types", views.insert_supported_data_types, name='insert_data_types'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('insert_stm', views.insert_stm, name='insert_stm')
]