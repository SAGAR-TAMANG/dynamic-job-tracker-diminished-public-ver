from django.urls import path, include
from .views import map_of_india
from .views import viz_done

urlpatterns = [
    path('', map_of_india, name='IndianMap'),
    path('done', viz_done, name='viz_done')
]