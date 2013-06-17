# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,render_to_response,redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from django.contrib.auth.models import User
from projects.models import Project
from tasks.models import Task
from tasks.forms import TaskForm
        
def detail(request,slug):
    task = get_object_or_404(Task, slug=slug)
    return render(request, 'tasks/detail.html', {'task': task})


def add_project_task(request,slug):
    if request.user.is_authenticated():
        project = Project.objects.get(slug = slug)
        if request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                td = data['end_date'] - data['start_date']
                if td.total_seconds()>0:
                    task = Task()
                    task.name = data['name']
                    task.description = data['description']
                    task.start_date = data['start_date']
                    task.end_date = data['end_date']
                    task.user = data['user']
                    task.project = project
                    task.save()
                else:
                    messages.add_message(request, messages.ERROR,
                        " end date is less than start date!")
                    return (redirect(reverse('Task:add_task')))
                return (redirect(reverse('Home:manager')))
            else:
                messages.add_message(request, messages.ERROR, 
                    "invalid form")
                return (redirect(reverse('Task:add_task')))
        else:
            form = TaskForm()
            send_dict={}
            context_instance=RequestContext(request)
            send_dict['project'] = project
            send_dict['form'] = form
            return render_to_response('tasks/add_task.html',send_dict,context_instance)
    else:
        return redirect(reverse('Login:login'))