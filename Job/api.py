from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics



@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many=True).data 
    return Response({'data':data})


@api_view(['GET'])
def job_detail_api(request, id):
    job_details = Job.objects.get(id=id)
    data = JobSerializer(job_details).data 
    return Response({'data':data})   



class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class Job_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer  
    lookup_field = 'id'  