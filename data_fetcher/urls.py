from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch, name='fetcher'),
    path('done', views.fetch_done, name='fetcher_done'),
]
