from django.shortcuts import render
from . models import Project, Task

# Create your views here.
def project_list(request):
    projects = Project.objects.all().prefetch_related('tasks')
    return render(request, 'tasks/project_list.html', {'projects': projects})

def task_list(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'tasks/task_list.html', {'project': project, 'tasks': tasks})