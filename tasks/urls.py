from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list_view, name='task-list'),
    path('create/', views.task_create_view, name='task-create'),
]