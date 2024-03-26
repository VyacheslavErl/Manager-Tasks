from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from tasks.models import TaskModel, CommentModel
from users.models import UserModel
from tasks.forms import TaskForm, CommentForm

import calendar


def tasks_list(request):
    return render(request, 'tasks_list.html',
                  {'tasks': TaskModel.objects.all()})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.company = request.user.company
            form.save()
            return redirect('/tasks')
    else:
        form = TaskForm
    return render(request, 'tasks_add.html', {'form': form})


def task_info(request, task_id):
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.by_user = request.user
            form.task_id = task_id
            form.save()
            return redirect('/tasks/info/' + str(task_id))
    else:
        form = CommentForm

    task = TaskModel.objects.get(id=task_id)
    comments = CommentModel.objects.filter(task_id=task_id)
    return render(request, 'task_info.html', {'task': task, 'form': form, 'comments': comments})


def task_del(request, task_id):
    try:
        TaskModel.objects.get(id=task_id).delete()
    except ObjectDoesNotExist:
        pass
    return redirect("/tasks")


def calendar_main(request):
    cal = calendar.HTMLCalendar()
    return render(request, 'calendar.html', {'cal': cal})
