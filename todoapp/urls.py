from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('tasks/<int:project_id>', views.tasks, name='tasks'),
    path('task/<int:id>', views.task, name='task'),
    path('create_task/<int:project_id>', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_task'),

]