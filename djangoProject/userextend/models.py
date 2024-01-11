from django.db import models


class UserHistory(models.Model):
    message = models.TextField(max_length=600)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
