from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('projects/', views.projects),
    path('tasks/<int:project_id>', views.tasks),
    path('task/<int:id>', views.task),
    path('create_task/<int:project_id>', views.create_task),
]