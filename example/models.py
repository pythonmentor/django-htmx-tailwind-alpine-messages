from django.db import models


class Task(models.Model):
    title = models.CharField("task title", max_length=200)
