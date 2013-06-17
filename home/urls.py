from django.conf.urls import patterns, url

from home import views
from projects import views as project_views

urlpatterns = patterns('',
    url(r'^user/$', views.user_profile_view, name='user'),
    url(r'^manager/$', views.manager_profile_view, name='manager'),
    url(r'^manager/projects/$', project_views.add_project_view, name='add_project'),
    url(r'^manager/projects/details/$', project_views.project_detail_view, name='project_detail'),
    url(r'^manager/projects/details/(?P<slug>[\w-]+)', project_views.project_detail_view, name='project_detail'),
)