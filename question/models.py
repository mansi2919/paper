from django.db import models

# Create your models here.
from django.db import models


class Router(models.Model):
    semester = models.IntegerField(default = True)
    subject = models.CharField(max_length=30, default = True)
    year = models.IntegerField(default = True)
    choice = models.CharField(max_length = 20, default = True)
    number_of_sessional = models.IntegerField(default = True)
    specifications = models.FileField(upload_to='router_specifications')
