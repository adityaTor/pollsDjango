from django.conf.urls import url

from .import views

app_name = 'addComment'
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^createComment/$',views.createComment,name='createComment'),
	url(r'^loadComments/$',views.loadComments,name='loadComments'),
	url(r'^deleteComment/$',views.deleteComment,name='deleteComment'),
	url(r'^login/$',views.login,name='login'),
]