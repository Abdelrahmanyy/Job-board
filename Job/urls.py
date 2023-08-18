from django.urls import path
from . import views



urlpatterns = [
    path('', views.job_list, name='job_list'), 
    path('add', views.add_job, name='add_job'),
    path('<int:id>', views.job_details, name='job_details'),

]