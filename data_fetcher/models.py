from django.db import models

# Create your models here.

class TitlesFrequency(models.Model):
    label = models.CharField(max_length=35)
    value = models.IntegerField()    
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return"{}-{}".format(self.label, self.value)
    
class NumJobs(models.Model):
    today = models.IntegerField(max_length=50)
    week = models.IntegerField(max_length=50)
    others = models.IntegerField(max_length=50)
    total = models.IntegerField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

