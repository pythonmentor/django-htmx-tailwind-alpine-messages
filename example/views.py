from django.shortcuts import render
from django.contrib import messages

from .forms import TaskForm
from .models import Task


def home(request):
    return render(
        request,
        "example/home.html",
        {"tasks": Task.objects.all()},
    )


def hx_task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La tâche créée avec succès")
            return render(
                request,
                "partials/hx_task_success.html",
                {"tasks": Task.objects.all()},
            )
    else:
        form = TaskForm()
    return render(request, "partials/hx_task_create_form.html", {"form": form})


def hx_task_cancel(request):
    return render(request, "partials/hx_task_create_button.html")
