from django.urls import path
from . import views
from .views import download_excel, download_naukri_excel, download_iimjobs_excel
import os
# from models import database_storage

# latest_excel = database_storage.objects().all()
app_name = 'storage'

urlpatterns = [
    # path('export-pdf', views.export_pdf, name="export-pdf")
    path('download_excel/', download_excel, name = 'database_excel_file'),
    path('download_naukri_excel/', download_naukri_excel, name = 'naukri_excel_file'),
    path('download_iimjobs_excel/', download_iimjobs_excel, name = 'iimjobs_excel_file'),
]
