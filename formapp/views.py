from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def login(request):
       return render(request, "formapp/login.html")

def register(request):
    if request.method == "POST":
        # accept multiple name variants used in templates
        username = request.POST.get("username") or request.POST.get("Name") or request.POST.get("email")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password") or request.POST.get("confirm-password")

        if not username or not password:
            messages.error(request, "Please provide a username and password.")
            return redirect("register")

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            # create profile record
            from .models import Profile
            Profile.objects.create(user=user, phone=phone or "")
            messages.success(request, "Registration successful.")
            return redirect("/")  # redirect to homepage
        except IntegrityError:
            messages.error(request, "Could not create account. Try again.")
            return redirect("register")

    return render(request, "formapp/register.html")

def terms(request):
       return render(request, "formapp/terms.html")
