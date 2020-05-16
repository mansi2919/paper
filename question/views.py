from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Router

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class YmcaPageView(TemplateView):
    template_name = "ymca.html"

class McaPageView(TemplateView):
    template_name = "mca.html"



def sem1PageView(request):
        files = Router.objects.filter(semester = 1)
        context = {'files': files}
        return render(request, 'sem1.html', context)
