from django.conf.urls import url, include
from . import views

app_name = 'polls'

urlpatterns = [
	url(r'^$', views.PollsList.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.PollDetail.as_view(), name='detail'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
	url('^', include('django.contrib.auth.urls')),
	url(r'^myPolls/$',views.userPolls.as_view(),name='userPolls'),
	url(r'myPolls/add/$', views.createPoll, name='createPoll'),
	url(r'^signUp/$',views.registration.as_view(),name='registerUser'),
	url(r'^test/$',views.test,name='test'),
]