from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('boy', views.homeP, name='homeP'),
    path('pat', views.pat, name='homeP'),
]
