from django.shortcuts import render,HttpResponse
from .models import Task
# Create your views here.
def home(request):
    context={'success':False}
    if request.method=="POST":
        #Handle the form 
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(title=title,desc=desc)
        ins.save()
        context={'success':True}
    return render(request,'index.html',context)
def tasks(request):
    allTasks=Task.objects.all()
    # for item in allTasks:
    #     print(item.title)
    # print(allTasks)
    context={'tasksf':allTasks}

    return render(request,'tasks.html',context)
