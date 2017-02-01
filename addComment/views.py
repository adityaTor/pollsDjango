from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.urls import reverse
from .models import Comments
from django.core import serializers 
from django.contrib.auth import authenticate, login, logout
from .forms import loginForm, createAccount
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
	return render (request, 'addComment/index.html')



def deleteComment(request):
	Comments.objects.filter(id=request.POST['delComment']).delete()
	comments = Comments.objects.all()

	return render(request,'addComment/comments.html',{'comments':comments})


def createComment(request):
	if request.method == "POST":
		q = Comments(comment = request.POST['comment'],pub_date = timezone.now())
		q.save()


	return HttpResponse(serializers.serialize("json",Comments.objects.filter(pk=q.pk)))


def loadComments(request):
	comments = serializers.serialize("json",Comments.objects.order_by('-pk'))
	return HttpResponse(comments)



def login(request):
	if request.method == 'POST':
		form = createAccount(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = User.objects.create_user(username,email,password)
			auth.login(request,user)
			return redirect('addComment:index')
				
	else:
		form = createAccount()

	return render(request, 'addComment/login.html',{'form':form})




