# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from projects.models import Project
from tasks.models import Task
from projects.forms import ProjectForm

def add_project_view(request):
    if request.user.is_authenticated():
        if request.POST:
            form = ProjectForm(request.POST)
            if form.is_valid():
                #f2 =request.POST
                data = form.cleaned_data
                try:
                    p = Project.objects.get(name = data['name'])
                    messages.add_message(request, messages.ERROR, " invalid form")
                    return (redirect(reverse('Home:Projects:add_project')))
                except:
                    pass    
                td = data['end_date'] - data['start_date']
                if td.total_seconds()>=0:
                #    form.save
                #if data['end_date'] >= data['start_date']:
                    project = Project()
                    project.name = data['name']
                    project.description = data['description']
                    project.start_date = data['start_date']
                    project.end_date = data['end_date']
                    project.user = User.objects.get(username = request.user.username)
                    project.save()
                #    messages.add_message(request, messages.INFO, " Project Added!!")
                else:
                    messages.add_message(request, messages.ERROR, " end date is less than start date!")
                    return (redirect(reverse('Home:Projects:add_project')))
                return (redirect(reverse('Home:Projects:manager')))
            else:
                messages.add_message(request, messages.ERROR, " invalid form")
                return (redirect(reverse('Home:Projects:add_project')))
        else:
            form = ProjectForm()
            dict={}
            dict['form'] = form
            return render_to_response('managers/add_project.html',dict,context_instance=RequestContext(request))
    else:
        return redirect(reverse('Login:login'))

def project_detail_view(request,slug):
    dict = {}
    project = Project.objects.get(slug = slug)
    task_list = Task.objects.filter(project= project)
    dict['task_list'] = task_list
    dict['project'] = project
    return render_to_response('managers/project_detail.html',dict,context_instance=RequestContext(request))

def project_edit_view(request,slug):
    if request.user.is_authenticated():
        if request.POST:
            form = ProjectForm(request.POST)
            if form.is_valid():
                #f2 =request.POST
                data = form.cleaned_data
                td = data['end_date'] - data['start_date']
                if td.total_seconds()>=0:
                #    form.save
                #if data['end_date'] >= data['start_date']:
                    project = Project.objects.get(slug = slug)
                    project.name = data['name']
                    project.description = data['description']
                    project.start_date = data['start_date']
                    project.end_date = data['end_date']
                    project.user = User.objects.get(username = request.user.username)
                    project.save()
                else:
                    messages.add_message(request, messages.ERROR, " end date is less than start date!")
                    dict={}
                    dict['form'] = form
                    return render_to_response('managers/edit_project.html',dict,context_instance=RequestContext(request))
                return (redirect(reverse('Home:Projects:manager')))
        else:
            
            form = ProjectForm()
            dict={}
            dict['form'] = form
            return render_to_response('managers/edit_project.html',dict,context_instance=RequestContext(request))
    else:
        return redirect(reverse('Login:login'))