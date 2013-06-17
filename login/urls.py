from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)