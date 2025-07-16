from django.shortcuts import render,HttpResponse
from plog.models import Blog

# Create your views here.
def home(request):
    return render(request,'home.html')

def blog(request):
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request,'blog.html',context)

def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}

    return render(request,'blogpost.html',context)

def search(request):
    return render(request,'search.html')


def contact(request):
    return render(request,'contact.html')