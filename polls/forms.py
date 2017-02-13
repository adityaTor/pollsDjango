from django.forms import ModelForm, Textarea, CharField, BaseFormSet
from polls.models import Question, Choice
from django.contrib.auth.models import User
from django import forms

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question']


class ChoiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = ['choice']


class registrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','password']