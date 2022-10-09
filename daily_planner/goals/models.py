from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    goal_title = models.CharField('Долгосрочная цель', max_length=50)
    goal_description = models.CharField('Описание долгосрочной цели', max_length=250)
    subtasks = models.CharField('Подзадачи', max_length=250)
    date = models.DateField('Дата добавления цели')
    deadline = models.DateField('Срок выполнения цели')
    complete = models.BooleanField(default=False)

    def __str__(self):
        """"функция для вывода название цели на странице"""
        return self.goal_title

    class Meta:
        order_with_respect_to = 'user'

    def get_absolute_url(self):
        '''функция для переадресации из шаблона для редактирования к странице с отредактированной целью'''
        return f"/goals/{self.id}"
