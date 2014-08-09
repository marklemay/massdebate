from django.conf.urls import patterns, url

from debate import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^statement/(?P<statement_id>\d+)/$', views.statement, name='statement'),
    url(r'^statement/(?P<statement_id>\d+)/submitfor$', views.submitfor, name='submitfor'),
    url(r'^statement/(?P<statement_id>\d+)/submitagainst$', views.submitagainst, name='submitagainst'),
    #TODO should probably only have 1 argument subission url
)