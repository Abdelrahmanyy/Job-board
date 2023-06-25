from django.shortcuts import render
from models import *



def job_list(request):
    return render(request, template_name, {})



def job_details(request, id):
    return render(request, template_name, {})
    

