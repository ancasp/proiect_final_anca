from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Trainer(models.Model):

    department_options = (
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('network', 'Network')
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40, blank=True) # blank=True face ca fieldul SA NU FIE OBLIGATORIU DE COMPLETAT
    email = models.EmailField(max_length=50)
    department = models.CharField(choices=department_options, max_length=100)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profile_trainers/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class HistoryTrainer(models.Model):
    message = models.TextField(max_length=500)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message



