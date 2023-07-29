from django.urls import path
from dashboard.views import IndexView  
from dashboard.views import IndiaMap
# pastreports, IndexView2

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('map_of_india', IndiaMap, name = 'map-of-india')
    # path('', IndexView2.as_view(), name = 'index2'),
    # path('past-reports', pastreports, name = "past-reports"),
]