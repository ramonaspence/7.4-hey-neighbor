from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('users/', views.UserView.as_view(), name = "users"),
    path('mytools/', views.MyToolView.as_view(), name = "mytools"),
    path('tools/', views.ToolListView.as_view(), name='list'),
    path('', views.IndexView.as_view(), name = "home"),
]
