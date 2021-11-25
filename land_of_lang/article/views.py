from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Article, Category
from .forms import ArticleForm



class HomePage(ListView):
    model = Article
    template_name = 'article/article_page.html'
    context_object_name = 'post_k'
    # extra_context = {'title': 'Home Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

class ArticleByCat(ListView):
    model = Article
    template_name = 'article/category.html'
    context_object_name = 'post_k'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['cat_id'])
        return context

    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['cat_id'], is_published=True)

class ViewPost(DetailView):
    model = Article
    template_name = 'article/view_post.html'
    context_object_name = 'post'
    # pk_url_kwarg = 'post_id'


class AddPost(CreateView):
    form_class = ArticleForm
    template_name = 'article/add_post.html'
    success_url = reverse_lazy('home')



# def index(request):
#     posts = Article.objects.all()
#     context = {
#         "post_k": posts,
#         'title': 'List of article',
#     }
#     return render(request, 'article/index.html', context)


# def get_category(request, cat_id):
#     posts = Article.objects.filter(category_id=cat_id, is_published=True)
#     cur_cat = Category.objects.get(pk=cat_id)
#     return render(request, 'article/category.html', {"post_k": posts, "cur_cat": cur_cat})


# def view_post(request, post_id):
#     post = get_object_or_404(Article, pk=post_id)
#     return render(request, 'article/view_post.html', {"post": post})


def about(request):
    return render(request, 'article/about.html')

# def add_post(request):
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post)
#     else:
#         form = ArticleForm
#     return render(request, 'article/add_post.html', {'form': form, })
