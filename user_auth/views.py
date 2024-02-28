# user_auth/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:login')
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_auth:login')
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('user_auth:login')
# user_auth/views.py
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the polls app or any other desired URL
            return redirect('polls:index')  # Assuming 'polls:index' is the URL name for the polls index view
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})


# Create your views here.
