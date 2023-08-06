from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from .forms import *



def job_list(request):
    job_list = Job.objects.all() 

    paginator = Paginator(job_list, 1) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)  

    context = {
        "jobs":page_obj ,
        "job_list":job_list ,
    }
    return render(request, "Job/job_list.html", context)



def job_details(request, slug):
    job_details = Job.objects.get(slug=slug)

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
    

