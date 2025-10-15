from django.shortcuts import render

# Create your views here.
def login(request):
       return render(request, "formapp/login.html")

def register(request):
       return render(request, "formapp/register.html")

def terms(request):
       return render(request, "formapp/terms.html")
