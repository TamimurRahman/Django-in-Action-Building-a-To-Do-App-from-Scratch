from django.shortcuts import render,redirect,get_list_or_404
from .models import Task
from .import models,forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def task_list(request):
    status_filter = request.GET.get('status','all')
    category_filter = request.GET.get('category','all')
    tasks = Task.objects.filter(user=request.user)

    if status_filter != 'all':
        tasks = tasks.filter(is_compleated=(status_filter == 'compleated'))
    
    if category_filter !='all':
        tasks = tasks.filter(category=category_filter)
    
    compleated_task = tasks.filter(is_compleated = True)
    pending_task = tasks.filter(is_compleated = False)

    return render(request,'task_list.html',{
        'compleated_tasks':compleated_task,
        'pending_tasks':pending_task,
        'status_filter':status_filter,
        'category_filter':category_filter,
    })

def home(request):
    task = Task.objects.all()
    return render(request,'task_list.html',{'task':task})

@login_required
def task_create(request):
    if request.method=='POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('homes')
    else:
        form = forms.TaskForm()
    return render(request,'create_task.html',{'form':form})

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

def register(request):
    if request.method == 'POST':
        form = forms.register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = forms.register()
    return render(request,'login.html',{'form':form})
    
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('homes')
            
    else:
        form = AuthenticationForm()
    
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('task')