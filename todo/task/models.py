from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    STATUS =[
        ('pending','pending'),
        ('compleated','complated'),
    ]
    CATEGORY = [
        ('work','work'),
        ('personal','personal'),
        ('other','other'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField()
    status = models.CharField(max_length=100,choices=STATUS,default='pending')
    category = models.CharField(max_length=100,choices=CATEGORY)
    is_compleated = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE) #one to many relationship suppose one user have multiple task so thats why i use forignkey user delete hole ter task delete hoiye jabe

    def __str__(self):
        return f'{self.title} | {self.status}'

