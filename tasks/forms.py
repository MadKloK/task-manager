from django.forms import ModelForm
from tasks.models import Task

class TaskCreationForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description']

class TaskUpdateForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
