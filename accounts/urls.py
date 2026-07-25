from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='account-login'),
    path('logout/', views.logout_view, name='account-logout'),
    path('register/', views.register_view, name='account-register'),
]