from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from .models import Profile
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

    return render(request, 'registration/register.html', {'form': form})

def profile(request, pk):
    if request.user_is_authenticated:
        pass
