from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Category


def index(request):
    posts = Article.objects.all()
    categories = Category.objects.all()
    context = {
        "post_k": posts,
        'title': 'List of article',
        'category': categories,

    }
    return render(request, 'article/index.html', context)


def get_category(request, cat_id):
    posts = Article.objects.filter(category_id=cat_id)
    categories = Category.objects.all()
    cur_cat = Category.objects.get(pk=cat_id)
    return render(request, 'article/category.html', {"post_k": posts, "cats": categories, "cur_cat": cur_cat})


def about(request):
    return render(request, 'article/about.html')
