from django.shortcuts import render,redirect,get_list_or_404
from .models import Task
from .import models,forms

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

def task_create(request):
    if request.method=='POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('')
        else:
            form = forms.TaskForm()
        return render(request,'',{'form':form})

def task_detail(request,task_id):
    task = get_list_or_404(Task,id = task_id,user = request.user)
    return render(request,'',{'task':task})

def task_delete(request,task_id):
    task = get_list_or_404(Task,id=task_id,user=request.user)
    task.delete()
    return redirect('')

def task_mark_completed(request,task_id):
    task = get_list_or_404(Task,id = task_id,user=request.user)
    task.is_compleated = True
    task.save()
    return redirect('')
