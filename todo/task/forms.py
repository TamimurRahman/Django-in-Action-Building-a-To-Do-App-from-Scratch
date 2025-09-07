from django import forms
from  .import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        exclude = ['user']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'due_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

class register(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']

