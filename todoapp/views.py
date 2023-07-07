from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def home(request):
    return render(request, 'index.html')

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request, id):
    tasks = Task.objects.all()
    project_tasks = tasks.filter(project_id=id)
    project_name = Project.objects.get(id=id)
    return render(request, 'tasks.html', {
        'project_tasks': project_tasks,
        'project_name': project_name
    })
