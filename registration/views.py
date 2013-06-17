# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from registration.forms import UserForm

def registration_view(request):
    send_dict = {}
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 
                " You have successfully registered. You can sign in now.")
    	    return redirect('/')
    else:
        form = UserForm()
    send_dict['form'] = form
    return render_to_response('registration/signup.html',
        send_dict,context_instance=RequestContext(request))