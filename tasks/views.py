from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from tasks.models import Task
from tasks.forms import TaskCreationForm, TaskUpdateForm

# Create your views here.

@login_required
def task_list_view(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_create_view(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, 'Task created successfully.')
            return redirect('tasks:task-list')

        messages.error(request, 'Invalid Task.')

    else:
        form = TaskCreationForm()

    context = {'form': form, 'title': 'Create task'}
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_update_view(request, pk: int):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task saved.')
            return redirect('tasks:task-list')

        messages.error(request, 'Invalid Task.')

    else:
        form = TaskUpdateForm(instance=task)

    context = {'form': form, 'title': 'Update task'}
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('tasks:task-list')

    context = {'task': task}
    return render(request, 'tasks/task_confirm_delete.html', context)