from django import forms
from .models import Category


class ArticleForm(forms.Form):
	title = forms.CharField(max_length=150, label="Title of your post", widget=forms.TextInput(attrs={"class": "form-control" }))
	content = forms.CharField(label="Content", required=False, widget=forms.Textarea(attrs={
		"class": "form-control",
		"rows": 5
	}))
	is_published = forms.BooleanField(label="Publish", initial=True)
	category = forms.ModelChoiceField(empty_label="Select", queryset=Category.objects.all(), label="Select the category", widget=forms.Select(attrs={"class": "form-control"}))

