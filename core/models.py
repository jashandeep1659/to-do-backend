from django.db import models
from user.models import User


class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    removed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    reminder = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
