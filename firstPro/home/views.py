from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeP(request):
    return HttpResponse('<h1 style="color:blue">"This is Mary Supriya...."</h1>')


def pat(request):
    return HttpResponse('<h2 style="color:blue;background-color:yellow">"This is Mary Supriya...."</h2>')            