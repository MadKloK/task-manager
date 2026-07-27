from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('tasks:task-list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            next_url = request.POST.get('next') or 'tasks:task-list'
            return redirect(next_url)

        messages.error(request, 'Invalid Credentials.')

    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/account_login.html', context)

@login_required
def logout_view(request):
    if request.method != "POST":
        return redirect("tasks:task-list")

    logout(request)
    messages.success(request, "Logged out successfully.")

    return redirect("accounts:login")

def register_view(request):
    if request.user.is_authenticated:
        return redirect('tasks:task-list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Account created successfully.')

            return redirect('tasks:task-list')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'accounts/account_register.html', context)