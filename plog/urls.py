from django.contrib import admin
from django.urls import path,include
from plog import views
urlpatterns = [
   
    path('',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('blogpost/<str:slug>',views.blogpost,name='blogpost'),
     path('search/',views.search,name='search'),

    path('contact/',views.contact,name='contact')

]
