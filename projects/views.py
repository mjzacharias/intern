from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.contrib.auth.models import User
from projects.models import Project
from tasks.models import Task
from projects.forms import ProjectForm
# Create your views here.


def add_project_view(request):
    if request.user.is_authenticated() and request.user.is_staff:
        if request.POST:
            form = ProjectForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                td = data['end_date'] - data['start_date']
                if td.total_seconds()>0:
                    project = Project()
                    project.name = data['name']
                    project.description = data['description']
                    project.start_date = data['start_date']
                    project.end_date = data['end_date']
                    project.user = User.objects.get(username = request.user.username)
                    project.save()
                else:
                    messages.add_message(request, messages.ERROR,
                        " end date is less than start date!")
                    return (redirect(reverse('Home:add_project')))
                return (redirect(reverse('Home:manager')))
            else:
                messages.add_message(request, messages.ERROR, 
                    "invalid form")
                return (redirect(reverse('Home:add_project')))
        else:
            form = ProjectForm()
            send_dict={}
            send_dict['form'] = form
            return render_to_response('managers/add_project.html',send_dict,context_instance=RequestContext(request))
    else:
        return redirect(reverse('Login:login'))


def project_detail_view(request,slug):
    if request.user.is_authenticated:
        if request.user.is_staff:
            send_dict = {}
            project = Project.objects.get(slug = slug)
            task_list = Task.objects.filter(project= project)
            send_dict['task_list'] = task_list
            send_dict['project'] = project
        else:
            return (redirect(reverse('Home:user')))
    else:
        return redirect(reverse('Login:login'))
    return render_to_response('managers/project_detail.html',send_dict,context_instance=RequestContext(request))