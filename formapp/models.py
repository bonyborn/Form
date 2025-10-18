from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppUser(models.Model):
  FullName = models.CharField(max_length=255)
  Email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20)
  password=models.CharField(max_length=30)
  accepted_terms=models.BooleanField(default=False)

def __str__(self):
    return self.full_name