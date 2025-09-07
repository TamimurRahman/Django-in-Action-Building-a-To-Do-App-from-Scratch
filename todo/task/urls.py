from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.task_list,name='task'),
    path('home/',views.home,name='homes'),
    path('create/',views.task_create,name='task_create'),
    path('task/<int:task_id>/',views.task_detail,name='task_detail'),
    path('task/<int:task_id>/delete/',views.task_delete,name='task_delete'),
    path('task/<int:task_id>/mark_completed/',views.task_mark_completed,name='task_mark_completed'),
    path('register/',views.register,name='register'),
    path('logins/',views.user_login,name='logins'),
    path('logout/',views.user_logout,name='logouts'),
]
