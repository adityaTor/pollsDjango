from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.utils import timezone
from .models import Question, Choice
from polls.forms import QuestionForm, ChoiceForm, registrationForm
from django.forms import formset_factory, inlineformset_factory, modelformset_factory
# Create your views here.

class PollsList(ListView):
	model = Question

class PollDetail(DetailView):
	model = Question
	template_name = 'polls/choices.html'


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	selected_choice = question.choice_set.get(id=request.POST['choice'])

	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponse(selected_choice.votes)

def test(request):
	pass


class registration(View):
	form_class = registrationForm
	template_name = 'polls/registration.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			user.set_password(password)
			user.save()

			user = authenticate(username=username,email=email,password=password)

			if user is not None:
				if user.is_active:
					auth.login(request,user)
					return redirect('polls:index')

		return render(request,self.template_name,{'form':form})



class userPolls(ListView, LoginRequiredMixin):

	template_name = 'polls/userPolls.html'
	
	def get_queryset(self):
		self.user = get_object_or_404(User, username=self.request.user)
		return self.user.question_set.all()

@login_required
def createPoll(request):

	pollFormSet = formset_factory(ChoiceForm, extra = 2, max_num = 6)
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		formset = pollFormSet(request.POST, request.FILES)
		if form.is_valid() and formset.is_valid():
			question = form.save(commit=False)
			question.poster = request.user
			question.pub_date = timezone.now()
			question.save()

			for form in formset:
				choice = Choice(choice=form.save(commit=False))
				choice.question = Question.objects.get(pk=question.id)
				choice.save()


		return redirect('polls:index')
	else:
		form = QuestionForm()
		formset = pollFormSet()

	return render(request, 'polls/create_poll.html', {'questionForm':form, 'choiceFormset':formset})




	