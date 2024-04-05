from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages


# Create your views here.
def index(request, num=None):
    if num != None:
        tasks = Task.objects.filter(priority=int(num))  
    else:
        tasks = Task.objects.filter(title__icontains=request.GET.get('search', ''))
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', context)


def detail(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', context)


def create(request):
    if request.method == 'GET':
        form = TaskForm()
        context = {
            'form': form,
        }
        return render(request, 'tasks/create.html', context)
    if request.method == 'POST':
        validation_form = TaskForm(request.POST)
        if validation_form.is_valid():
            validation_form.save()
        messages.success(request, 'Tarea creada')
        return redirect('tasks')


def edit(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'tasks/edit.html', context)
    if request.method == 'POST':
        edited_form = TaskForm(request.POST, instance=task)
        if edited_form.is_valid():
            edited_form.save()
        context = {
            'form': edited_form,
            'id': id,
        }
        messages.success(request, 'Tarea editada')
        return render(request, 'tasks/edit.html', context)


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, 'Tarea eliminada')
    return redirect('tasks')