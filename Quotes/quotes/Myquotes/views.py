from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def allQuotes(request):
    return render(request,"allQuotes.html")
def addQuotes(request):
    return render(request,"addQuotes.html")
