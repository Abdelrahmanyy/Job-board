from django.shortcuts import render
from .models import *



def job_list(request):
    job_list = Job.objects.all(),
    context = {}
    return render(request, "Job/job_list.html", {})



def job_details(request, id):
    return render(request, "Job/job_details.html", {})
    

