from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from tasks.models import TaskModel, CommentModel
from tasks.forms import TaskForm, CommentForm


@login_required(login_url='/')
def tasks_list(request):
    tasks = TaskModel.objects.filter(company=request.user.company).order_by('do_before')
    return render(request, 'tasks_list.html',
                  {'tasks': tasks})


@login_required(login_url='/')
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


@login_required(login_url='/')
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


@login_required(login_url='/')
def calendar(request):
    tasks = TaskModel.objects.filter(company=request.user.company).order_by('do_before')
    dates = dict()
    for task in tasks:
        if dates.get(str(task.do_before)):
            dates[str(task.do_before)].append(task)
        else:
            dates[str(task.do_before)] = [task]
    return render(request, 'calendar.html',
                  {'dates': dates})


@login_required(login_url='/')
def task_del(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    if request.user.company == task.company and request.user.job_title.add_task_permission:
        try:
            task.delete()
        except ObjectDoesNotExist:
            pass
        return redirect("/tasks")