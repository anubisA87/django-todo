from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('projects/', views.projects),
    path('tasks/<int:id>', views.tasks),
]