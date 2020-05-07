from django.db import models

class user(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    is_Admin=models.BooleanField(default=False)

    bio=models.TextField(blank=True)
    birthdate=models.DateField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

# Create your models here.
