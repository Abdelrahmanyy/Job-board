from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import *


def job_list(request):
    job_list = Job.objects.all() 

    # filters 
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs 

    paginator = Paginator(job_list, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 


    context = {
        "jobs":page_obj ,
        "job_list":job_list ,
        "myfilter":myfilter ,
    }
    return render(request, "Job/job_list.html", context)



def job_details(request, id):
    job_details = Job.objects.get(id=id)

    if request.method== 'POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
    else:
        form = ApplyForm()    

    context = {
        'job':job_details ,
        'form':form ,
    }    
    return render(request, "Job/job_details.html", context)


@login_required
def add_job(request):

    if request.method=='POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user 
            myform.save()
            return redirect('/jobs')

    else:
        form = JobForm()    



    return render(request, 'Job/add_job.html', {'form':form})
        
    

