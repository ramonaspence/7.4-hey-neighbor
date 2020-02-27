from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('<int:pk>/return', views.ReturnToolView.as_view(), name='return'),
    path('<int:pk>/checkout/', views.CheckoutToolView.as_view(), name = 'checkout'),
    path('newtool/', views.CreateToolView.as_view(), name = 'new'),
    path('users/', views.UserView.as_view(), name = "users"),
    path('mytools/<str:selection>/', views.MyToolView.as_view(), name = "mytools"),
    path('', views.ToolListView.as_view(), name='list'),
    path('', views.IndexView.as_view(), name = "home"),
]
