from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateTask, CreateProject, UpdateProject


# Create your views here.
def home(request):
    return render(request, "index.html")


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def tasks(request, project_id):
    tasks = Task.objects.all()
    project_tasks = tasks.filter(project_id=project_id)
    project = Project.objects.get(id=project_id)
    return render(
        request, "tasks.html", {"project_tasks": project_tasks, "project": project}
    )


def task(request, id):
    task = Task.objects.get(id=id)
    return render(request, "task.html", {"task": task})


def create_task(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "GET":
        return render(
            request,
            "create_task.html",
            {
                "form": CreateTask(),
                "project": project,
            },
        )
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=project_id,
        )
        return redirect("/tasks/" + str(project_id))


def create_project(request):
    if request.method == "GET":
        return render(
            request,
            "create_project.html",
            {
                "form": CreateProject(),
            },
        )
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect("projects")


def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("projects")


def update_project(request, id):
    if request.method == "GET":
        project = Project.objects.get(id=id)
        return render(
            request,
            "update_project.html",
            {
                "form": UpdateProject(),
                "project": project,
            },
        )
    else:
        project = Project.objects.filter(id=id)
        project.update(name=request.POST["name"])
        return redirect("projects")


def completed(request, id):
    task = Task.objects.filter(id=id)
    task.update(completed=True)
    task_object = Task.objects.get(id=id)
    fk = task_object.project
    return redirect("/tasks/" + str(fk.id))


def sign_up(request):
    if request.method == "GET":
        return render(request, "sign_up.html")
    else:
        form = RegisterForm(request.POST)
