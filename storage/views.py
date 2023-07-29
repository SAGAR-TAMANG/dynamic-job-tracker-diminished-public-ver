
import os

from django.shortcuts import render
# from data_fetcher.scripts.data import 
from django.http import HttpResponse
from django.conf import settings
from storage.models import database_storage

# # Create your views here.
# def past_reports(request):

# def export_pdf(request):
#     response = HttpResponse(content_type = 'application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=Expensesf'

database_name = database_storage.objects.values('database')
naukri_name = database_storage.objects.values('naukri')
iimjobs_name = database_storage.objects.values('iimjob')

database_name = database_name[0]['database']
naukri_name = naukri_name[0]['naukri']
iimjobs_name = iimjobs_name[0]['iimjob']

def download_excel(request):
    file_path = os.path.join(settings.BASE_DIR, 'data_fetcher/scripts/data', database_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = f'attachment; filename={database_name}'
            return response

    return HttpResponse("File not found.")

def download_naukri_excel(request):
    file_path = os.path.join(settings.BASE_DIR, 'data_fetcher/scripts/data', naukri_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = f'attachment; filename={naukri_name}'
            return response

    return HttpResponse("File not found.")

def download_iimjobs_excel(request):
    file_path = os.path.join(settings.BASE_DIR, 'data_fetcher/scripts/data', iimjobs_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = f'attachment; filename={iimjobs_name}'
            return response

    return HttpResponse("File not found.")