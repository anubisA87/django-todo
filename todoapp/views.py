from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateTask

# Create your views here.
def home(request):
    return render(request, 'index.html')

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request, project_id):
    tasks = Task.objects.all()
    project_tasks = tasks.filter(project_id=project_id)
    project = Project.objects.get(id=project_id)
    return render(request, 'tasks.html', {
        'project_tasks': project_tasks,
        'project': project
    })

def task(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task.html', {
        'task': task,
    })

def create_task(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'create_task.html', {
        'form': CreateTask(),
        'project': project,
    })
