from django.db import models


class Info(models.Model):
    place = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 50)
    email = models.EmailField(max_length=80)

    class Meta:
        verbose_name = ("info")
        verbose_name_plural = ("infos")

    def __str__(self):
        return self.email
    
    
