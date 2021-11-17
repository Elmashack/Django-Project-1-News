from django import forms
from .models import Article
from django.core.exceptions import ValidationError
import re


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



