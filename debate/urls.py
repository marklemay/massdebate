from django.conf.urls import patterns, url

from debate import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^statement/(?P<statement_id>\d+)/$', views.statement, name='statement'),
    url(r'^statement/(?P<statement_id>\d+)/submitfor$', views.submitfor, name='submitfor'),
    url(r'^statement/(?P<statement_id>\d+)/submitagainst$', views.submitagainst, name='submitagainst'),

#     # ex: /polls/5/results/
#     url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
#     
#     
#     url(r'^t/$', views.t, name='t'),
)