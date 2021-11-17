from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from .forms import ArticleForm


def index(request):
    posts = Article.objects.all()
    context = {
        "post_k": posts,
        'title': 'List of article',
    }
    return render(request, 'article/index.html', context)


def get_category(request, cat_id):
    posts = Article.objects.filter(category_id=cat_id)
    cur_cat = Category.objects.get(pk=cat_id)
    return render(request, 'article/category.html', {"post_k": posts, "cur_cat": cur_cat})


def view_post(request, post_id):
    post = get_object_or_404(Article, pk=post_id)
    return render(request, 'article/view_post.html', {"post": post})


def about(request):
    return render(request, 'article/about.html')

def add_post(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            post = Article.objects.create(**form.cleaned_data)
            return redirect(post)
    else:
        form = ArticleForm
    return render(request, 'article/add_post.html', {'form': form, })
