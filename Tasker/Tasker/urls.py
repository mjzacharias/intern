from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('login.urls', namespace="Login")),
    url(r'^home/', include('home.urls', namespace="Home")),
    url(r'^registration/$', include('registration.urls', namespace="Registration")),
    url(r'^password/',include('passwordreset.urls', namespace= "PasswordReset")),
    url(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^tasks/', include('tasks.urls', namespace= "Task")),
    #url(r'^password/reset/$', views.password_reset, {'template_name': 'password_reset/password_reset_form.html',
    #    'email_template_name':'password_reset/password_reset_email.html',
    #    'subject_template_name':'password_reset/password_reset_subject.txt',}, name="password_reset"),
    #url(r'^password/reset/done/$', views.password_reset_done,
    #    {'template_name': 'password_reset/password_reset_done.html',}, 
    #    name="password_reset_done"),
    #url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm,
    #    {'template_name': 'password_reset/password_reset_confirm.html'},
    #    name="password_reset_confirm"),
    #url(r'^password/done/$', views.password_reset_complete,{'template_name': 'password_reset/password_reset_complete.html',}, name="password_reset_complete"),
    # Examples:
    # url(r'^$', 'Tasker.views.home', name='home'),
    # url(r'^Tasker/', include('Tasker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
