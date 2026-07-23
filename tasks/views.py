from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task

# Create your views here.

@login_required
def index_view(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks-index.html', context)