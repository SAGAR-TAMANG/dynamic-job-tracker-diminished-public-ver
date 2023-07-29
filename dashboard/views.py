from typing import Any, Dict
from django.shortcuts import render
# from data_fetcher.main import frequency_title
from data_fetcher.models import NumJobs, TitlesFrequency
from django.views.generic import TemplateView

# Create your views here.

# def index(request):
#     bar_chart = TitlesFrequency.objects.all()
#     return render(request, 'index.html', {'titles':bar_chart})

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queryset'] = TitlesFrequency.objects.all()
        # # context['counternum'] = Num.objects.all()
        context['counternumtotal'] = NumJobs.objects.values('total')
        print('THIS IS QUERY SET: ', context['queryset'], '\n THIS IS COUNTERNUMTOTAL: ', context['counternumtotal'])
        context['counternum'] = NumJobs.objects.all()
        print('\n THIS IS COUNTERNUM: ', context['counternum'])
        
        in_between = context['queryset'][:]
        print('THIS IS IN BETWEEN', in_between)
        return context

def pastreports(request):
    return render(request, 'past_reports.html')

def IndiaMap(request):
    return render(request, 'IndianMap/india.main.html')

# from django.shortcuts import render

# def IndexView(request):
#     return render(request, 'index.html')