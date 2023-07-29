from django.shortcuts import render
import datetime
import subprocess
import os

# Create your views here.
def map_of_india(request):
    # return render(request, 'IndianMap/map_of_india.html')
    context = {
        'naukri': 'map_of_india_NaukriJobListing_' +  str(datetime.date.today())+ '.html',
        'iimjobs': 'map_of_india_IIMJobListing_' +  str(datetime.date.today())+ '.html',
        'timesjobs': 'map_of_india_TimesJobs_' +  str(datetime.date.today())+ '.html',
        }
    return render(request, 'map_of_india.html', context)

def viz_done(request):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    run = subprocess.Popen(['python', os.path.join(cur_path, 'main.py')])
    return render(request, 'others/viz_done.html')