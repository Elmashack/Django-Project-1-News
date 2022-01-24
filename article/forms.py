from django import forms
from .models import Article
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re


class ContactForm(forms.Form):
	subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class': 'form-control'}))
	body = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
	captcha = CaptchaField(label='')

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(UserCreationForm):

	username = forms.CharField(label='Username', help_text="150 characters or fewer.", widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'content', 'is_published', 'category']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
			'category': forms.Select(attrs={'class': 'form-control'}),
		}

	def clean_title(self):
		title = self.cleaned_data['title']
		if re.match(r'\d', title):
			raise ValidationError("Title can't start with digit")
		return title



	# title = forms.CharField(max_length=150, label="Title of your post", widget=forms.TextInput(attrs={"class": "form-control" }))
	# content = forms.CharField(label="Content", required=False, widget=forms.Textarea(attrs={
	# 	"class": "form-control",
	# 	"rows": 5
	# }))
	# is_published = forms.BooleanField(label="Publish", initial=True)
	# category = forms.ModelChoiceField(empty_label="Select", queryset=Category.objects.all(), label="Select the category", widget=forms.Select(attrs={"class": "form-control"}))



