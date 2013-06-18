from django.conf.urls import patterns, include, url

from projects import views as project_views
from home import views

urlpatterns = patterns('',
	url(r'^$', views.manager_profile_view, name='manager'),
	url(r'^projects/$', project_views.add_project_view, name='add_project'),
    url(r'^projects/details/$', project_views.project_detail_view, name='project_detail'),
    url(r'^projects/details/(?P<slug>[\w-]+)/edit/$', project_views.project_edit_view, name='edit_project'),
    url(r'^projects/details/(?P<slug>[\w-]+)/$', project_views.project_detail_view, name='project_detail'),
    
    )