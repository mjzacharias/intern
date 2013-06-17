from django.conf.urls import patterns, url

from tasks import views

urlpatterns = patterns('',
    url(r'^details/(?P<slug>[\w-]+)', views.detail, name='detail'),
    url(r'^addTask/(?P<slug>[\w-]+)', views.add_project_task, name='add_task')
)
