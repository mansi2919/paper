from django.urls import path
from . import views
from django.conf import settings
from .models import Router

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('ymca/', views.YmcaPageView.as_view(), name = 'ymca'),
    path('mca/', views.McaPageView.as_view(), name = 'mca'),
    path('sem1/', views.sem1PageView, name = 'sem1'),
]
