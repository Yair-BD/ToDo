from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy



def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {"form": form, "task": task}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) # הוספתי את האינסטנס כי=די שזה לא יוסיף עוד אחד אלא יעדכן .
        if form.is_valid():
            print(form)
            form.save()
            return redirect("../../")
    return render(request, 'tasks/update_tasks.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("../../")
    context = {"task": task}
    return render(request, 'tasks/delete_tasks.html', context)
