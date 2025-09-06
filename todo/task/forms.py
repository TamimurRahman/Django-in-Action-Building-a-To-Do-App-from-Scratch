from django import forms
from .models import models
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelsForm):
    class Meta:
        model = models.Task
        exclude = ['user']

class register(UserChangeForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']
        
