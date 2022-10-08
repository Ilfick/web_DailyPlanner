from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """"класс для модели заметок, в котором user обладает свзью один ко многим"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    note_tittle = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.note_tittle

    class Meta:
        order_with_respect_to = 'user'
