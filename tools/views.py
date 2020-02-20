from django.shortcuts import render
from django.views import generic

from .models import Tool
class IndexView(generic.TemplateView):
    template_name = 'tools/base.html'

class MyToolView(generic.ListView):
    template_name = 'tools/mytools.html'
    model = Tool



# Create your views here.
