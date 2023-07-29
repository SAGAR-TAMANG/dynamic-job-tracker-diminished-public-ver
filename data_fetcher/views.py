from django.shortcuts import render
import subprocess
from django.http import HttpResponse
from django.conf import settings
# from data_fetcher.main import main
import os
# from data_fetcher.models import TitlesFrequency

# Create your views here.

def fetch(request):
    return render(request, 'fetch.html')

def fetch_done(request):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    # run = subprocess.Popen(['python', os.path.join(cur_path, 'main.py')])
    return render(request, 'others/fetch_done.html')
