# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from registration.forms import UserForm

def registration_view(request):
    dict = {}
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, " You have successfully registered. You can sign in now.")
    	    redirect('/')
    else:
        form = UserForm()
    dict['form'] = form
    return render_to_response('registration/signup.html',dict,context_instance=RequestContext(request))