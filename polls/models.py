from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def get_absolute_url(self):
		return reverse('Question-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.question



class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice

