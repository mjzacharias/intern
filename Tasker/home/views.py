# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from tasks.models import Task
from projects.models import Project

def user_profile_view(request):
    if request.user.is_authenticated():
        send_dict={}
        user = User.objects.get(username = request.user.username)
        task = Task.objects.filter(user= user)
        send_dict['task_list'] = task
        return render_to_response('users/home.html',send_dict,context_instance=RequestContext(request))
    else:
        return(redirect(reverse('Login:login')))
    #return render_to_response('users/home.html')#dict,context_instance=RequestContext(request))

def manager_profile_view(request):
    if request.user.is_authenticated():
        dict={}
        user = User.objects.get(username = request.user.username)
        projects = Project.objects.filter(user= user)
        dict['projects'] = projects
        return render_to_response('managers/home.html',dict,context_instance=RequestContext(request))
    else:
        return(redirect(reverse('Login:login')))

