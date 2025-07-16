from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.home,name='home'),
    path('allQuotes',views.allQuotes,name='allQuotes'),
    path('addQuotes',views.addQuotes,name='addQuotes'),
]