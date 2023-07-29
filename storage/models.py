from django.db import models

# Create your models here.

class database_storage(models.Model):
    database = models.CharField(max_length=50)
    naukri = models.CharField(max_length=50)
    iimjob = models.CharField(max_length=50)
