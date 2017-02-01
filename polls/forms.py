from django.forms import ModelForm, Textarea, CharField, BaseFormSet
from polls.models import Question, Choice


class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = ['question']


class ChoiceForm(ModelForm):
	class Meta:
		model = Choice
		fields = ['choice']

