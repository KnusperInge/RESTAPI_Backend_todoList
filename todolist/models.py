from django.db import models
from datetime import date
from django.conf import settings


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today())
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+' '+self.title

# Create your models here.
