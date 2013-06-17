from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('login.urls', namespace="Login")),
    url(r'^home/', include('home.urls', namespace="Home")),
    url(r'^registration/$', include('registration.urls', namespace="Registration")),
    url(r'^password/',include('passwordreset.urls', namespace= "PasswordReset")),
    url(r'^tasks/', include('tasks.urls', namespace= "Task")),
    # Examples:
    # url(r'^$', 'Tasker.views.home', name='home'),
    # url(r'^Tasker/', include('Tasker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)