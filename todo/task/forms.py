from django import forms
from .models import models

class TaskForm(forms.ModelsForm):
    class Meta:
        model = models.Task
        exclude = ['user']
