from django.db import models
from django.utils import timezone

class Todo(models.Model):
    activity = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.activity
