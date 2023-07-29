from django.contrib import admin
from data_fetcher.models import NumJobs, TitlesFrequency

# Register your models here.

admin.site.register(TitlesFrequency)
admin.site.register(NumJobs)