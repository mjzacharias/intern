from django.conf.urls import patterns, include, url

from home import views


urlpatterns = patterns('',
    url(r'^user/$', views.user_profile_view, name='user'),
    url(r'^manager/', include('projects.urls', namespace='Projects')),
    
    
)