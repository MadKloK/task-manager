from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.

@login_required
def task_list_view(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)

@login_required
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, 'Task created successfully.')
            return redirect('tasks:task-list')

        messages.error(request, 'Invalid Task.')

    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'tasks/task_form.html', context)