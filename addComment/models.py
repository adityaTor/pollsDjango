from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.
class Comments(models.Model):
	comment = models.CharField(max_length=250)
	pub_date = models.DateTimeField('date published')


	def __str__(self):
		return self.comment










