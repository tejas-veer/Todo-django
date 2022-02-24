import re
from django.db import models

# Create your models here.
class TodoList(models.Model):
    taskText = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskText