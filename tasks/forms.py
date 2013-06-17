from django import forms
from django.db import models

from tasks.models import Task
from django.contrib.admin import widgets
from django.contrib.auth.models import User


class TaskForm (forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name','description','start_date','end_date','user')

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget = widgets.AdminDateWidget()
        self.fields['end_date'].widget = widgets.AdminDateWidget()