
from django.shortcuts import render,redirect
from .models import TodoList
from .forms import TodoForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        print(request.POST)
        return redirect('index')

    form = TodoForm()
    tasks = TodoList.objects.all()
    context = {'tasks' : tasks,'form' : form}
    return render(request, 'todo.html' , context)

# def insert(request):
    

def update(request, pk):
    task = TodoList.objects.get(id=pk)
    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST , instance=task)
        if form.is_valid:
            form.save()
            # tasks = TodoList.objects.all()
            # context = {'form' : form, 'tasks' : tasks}
            return redirect('index')

    tasks = TodoList.objects.all()
    context = {'form' : form, 'tasks' : tasks}
    return render(request , 'todo.html' , context)

def completed(request,pk):
    obj = TodoList.objects.get(id = pk)
    if obj.completed :
        obj.completed = False
    else :
        obj.completed = True
    obj.save()
    
    return redirect('index')

def delete(request, pk):
    task = TodoList.objects.get(id = pk)
    task.delete()
    return redirect('index')
    