from .models import Goal
from django.forms import ModelForm, TextInput, DateInput, Textarea


class GoalForm(ModelForm):
    class Meta:
        ''' класс мета для указания характеристик формы'''
        model = Goal
        fields = ['goal_title', 'goal_description', 'subtasks', 'date', 'deadline']

        widgets = {
            'goal_title': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название долгосрочной цели"
            }),
            'goal_description': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Описание долгосрочной цели"
            }),
            'date': DateInput(attrs={
                "class": "form-control",
                "placeholder": "Дата добавления цели"
            }),
            'deadline': DateInput(attrs={
                "class": "form-control",
                "placeholder": "Срок выполнения цели"
            }),
            'subtasks': Textarea(attrs={
                "class": "form-control",
                "placeholder": "Подзадачи"
            })
        }
