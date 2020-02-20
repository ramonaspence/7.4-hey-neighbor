from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.MyToolView.as_view(), name = "mytools"),
    path('', views.IndexView.as_view(), name = "base.html")
]
