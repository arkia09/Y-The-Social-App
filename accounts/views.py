from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('post_list')
            
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('post_list')

def profile_list(request):
    return render(request, 'registration/accounts/profile_list.html')

def profile(request, pk):
    if request.user_is_authenticated:
        pass
