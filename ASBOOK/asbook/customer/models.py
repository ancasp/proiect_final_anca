from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):

    gender_options =(
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=400)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(choices=gender_options, max_length=6)
    # trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    # profile = models.ImageField(upload_to='profile_students/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HistoryCustomer(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message


