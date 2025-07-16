from django.shortcuts import render
from recipe_list.models import homePage
# Create your views here.
def home(request):
    context = {}
    if request.method=='POST':
        recipe=request.POST['recipe']
        ingredients=request.POST['ingredients']
        instructions=request.POST['desc']
        print(recipe)
        ins=homePage(recipe=recipe,ingredients=ingredients,instructions=instructions)
        ins.save()
        context={'success':True}


    return render(request,'home.html',context)
def task(request):
    allTasks=homePage.objects.all()
    context={'task':allTasks}
    return render(request,'task.html',context)