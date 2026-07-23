from django.urls import path
from tasks.views import index_view

app_name = 'tasks'

urlpatterns = [
    path('', index_view, name='index')
]