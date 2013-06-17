from django import forms
from django.db import models

from projects.models import Project
from django.contrib.admin import widgets


class ProjectForm (forms.ModelForm):
    name = forms.CharField(max_length=50, required = True)
    description = forms.CharField(max_length=200, required = True)
    start_date = forms.DateField(widget = widgets.AdminDateWidget,required = True)
    end_date = forms.DateField(widget = widgets.AdminDateWidget,required = True)

    class Meta:
        model = Project
        fields = ('name','description','start_date','end_date','user')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget = widgets.AdminDateWidget()
        self.fields['end_date'].widget = widgets.AdminDateWidget()