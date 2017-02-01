from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
class loginForm(AuthenticationForm):
	pass


class createAccount(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username','email','password')