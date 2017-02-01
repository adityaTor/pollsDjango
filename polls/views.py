from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Question, Choice
from polls.forms import QuestionForm, ChoiceForm
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
	form = formset_factory(ChoiceForm, extra=2)
	return render(request, 'polls/create_poll.html', {'form': form})



class userPolls(ListView, LoginRequiredMixin):

	template_name = 'polls/userPolls.html'
	
	def get_queryset(self):
		self.user = get_object_or_404(User, username=self.request.user)
		return self.user.question_set.all()

@login_required
def createPoll(request):
	pass


	