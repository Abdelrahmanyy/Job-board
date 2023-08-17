from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<str:slug>', views.job_details, name='job_details'),

]