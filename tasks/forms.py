from django.forms import ModelForm
from tasks.models import Task

class TaskCreationForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']

class TaskUpdateForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'due_date']
