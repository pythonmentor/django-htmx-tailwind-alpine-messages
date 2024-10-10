from django import forms

from . import models


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ["title"]
        labels = {
            "title": "Titre de la tâche",
        }
        help_texts = {
            "title": "Définissez un titre pour votre nouvelle tâche",
        }
        error_messages = {
            "title": {
                "max_length": "Le titre que vous avez défini est trop long.",
            },
        }
