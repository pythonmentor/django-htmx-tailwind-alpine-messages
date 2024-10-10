from django.urls import path

from . import views

app_name = "example"

urlpatterns = [
    path("", views.home, name="home"),
    path("task/create/", views.hx_task_create, name="task-create"),
    path("task/cancel/", views.hx_task_cancel, name="task-cancel"),
]
