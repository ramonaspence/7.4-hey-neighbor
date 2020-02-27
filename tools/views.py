from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Tool

User = get_user_model()

class IndexView(generic.TemplateView):
    template_name = 'tools/base.html'

class MyToolView(generic.ListView):
    template_name = 'tools/mytools.html'
    model = Tool

    def get_queryset(self):
        queryset = Tool.objects.all()

        username = self.request.user.id
        if username is not None:
            queryset = queryset.filter(owner = username)
        return queryset


class UserView(generic.ListView):
    template_name = "tools/users.html"
    model = User

class ToolListView(generic.ListView):
    template_name = 'tools/tools.html'
    model = Tool


class CreateToolView(generic.CreateView):
    template_name = 'tools/add.html'
    model = Tool
    fields = ['name', 'type', 'description']
    success_url = reverse_lazy('tools:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.borrowed = False
        form.instance.save()
        return HttpResponseRedirect(reverse_lazy('tools:list'))

class CheckoutToolView(generic.UpdateView):
    model = Tool
    template_name = 'tools/borrow.html'
    fields = ['borrowed']

    def form_valid(self, form):
        form.instance.borrowed = True
        self.object = form.save()
        form.instance.save()
        return HttpResponseRedirect(reverse_lazy('tools:list'))









# Create your views here.
