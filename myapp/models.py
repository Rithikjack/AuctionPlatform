from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    description=models.CharField(max_length=300,default="")
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="note")

class UserForm(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
