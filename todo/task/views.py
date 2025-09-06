from django.shortcuts import render,redirect,get_list_or_404
from .models import Task

# Create your views here.
def task_list(request):
    status_filter = request.GET.get('status','all')
    category_filter = request.GET.get('category','all')
    tasks = Task.objects.filter(user = request.user)

    if status_filter != 'all':
        tasks = tasks.filter(is_compleated=(status_filter == 'compleated'))
    
    if category_filter !='all':
        tasks = tasks.filter(category=category_filter)
    
    compleated_task = tasks.filter(is_compleated = True)
    pending_task = tasks.filter(is_compleatd = False)

    return render(request,' ',{
        'compleated_tasks':compleated_task,
        'pending_tasks':pending_task,
        'status_filter':status_filter,
        'category_filter':category_filter,
    })