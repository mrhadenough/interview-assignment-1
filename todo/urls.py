
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tasks/', views.TaskView.as_view(), name="tasks"),
    path('tasks/<int:pk>/', views.TaskView.as_view(), name="tasks"),
    path('tasks/<int:pk>/labels/', views.task_labels, name="task_labels"),
]
