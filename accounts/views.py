from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUser, CustomUserCreationForm, CustomLoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()  # Correct instantiation
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to a success page
    else:
        form = CustomLoginForm()
    return render(request, 'registration/login.html', {'form': form})