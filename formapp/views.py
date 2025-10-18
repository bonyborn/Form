from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AppUser

# Create your views here.
def login(request):
       return render(request, "formapp/login.html")

def register(request):
    if request.method == 'POST':
        form = AppUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  
    else:
        form = AppUser()
    return render(request, 'formapp/register.html')

def terms(request):
       return render(request, "formapp/terms.html")
