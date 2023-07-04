from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def home(request):
    return HttpResponse("Home page")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, pk=id)
    return HttpResponse("Task: %s" % task.title)
