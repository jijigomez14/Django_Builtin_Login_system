# builtapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth import logout
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Replace 'home' with the name of your home view
    else:
        form = AuthenticationForm()
    return render(request, 'builtapp/login.html', {'form': form})
def home(request):
    return render(request, 'home.html')
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout