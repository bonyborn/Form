from django.urls import path
from . import views

urlpatterns=[
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("terms/", views.terms, name="terms"),
]