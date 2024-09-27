from django.shortcuts import render, redirect
from .forms import UserRegisterForm
# import messages

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home (request):
    return render(request, 'index.html')

def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html', {'form': form})
    
def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You have successfully logged in as {email}')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')