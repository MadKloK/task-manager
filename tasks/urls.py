from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list_view, name='task-list'),
    path('create/', views.task_create_view, name='task-create'),
    path('<int:pk>/update/', views.task_update_view, name='task-update'),
    path('<int:pk>/delete/', views.task_delete_view, name='task-delete'),
]