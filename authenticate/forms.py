from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	first_name= forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	Phone_number= forms.IntegerField()
	Roll_number = forms.CharField(max_length=10)
	Branch = forms.CharField(max_length=10)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')