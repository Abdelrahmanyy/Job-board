from django.db import models

# Create your models here.




Job_type = (
    ('Full time','Full time'),
    ('Part time','Part time'),
    ('Remote','Remote'),
)
class Job(models.Model):
    title = models.CharField(max_length = 150)
    Job_type = models.CharField(max_length = 15, choices=Job_type)
    description = models.TextField(max_length = 1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
    
    

    
    

    