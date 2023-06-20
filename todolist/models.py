from django.db import models
from datetime import date
from django.contrib.auth.models import User


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+' '+self.title

# Create your models here.
