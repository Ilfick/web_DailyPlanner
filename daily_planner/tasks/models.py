from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """"класс для модели задач, user обладает свзью один ко многим"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_tittle = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.task_tittle

    class Meta:
        order_with_respect_to = 'user'
