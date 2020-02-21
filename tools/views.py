from django.shortcuts import render
from django.views import generic

from .models import Tool
class IndexView(generic.TemplateView):
    template_name = 'tools/base.html'

class MyToolView(generic.ListView):
    template_name = 'tools/mytools.html'
    model = Tool

class UserView(generic.TemplateView):
    template_name = "tools/users.html"

class ToolListView(generic.ListView):
    template_name = 'tools/tools.html'
    model = Tool




# Create your views here.
