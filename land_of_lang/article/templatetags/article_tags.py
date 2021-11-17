from django import template

from article.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("article/list_categories.html")
def display_categories(arg1="Hello", arh2="There"):
    categories = Category.objects.all()
    # cur_cat = Category.objects.get(pk=cat_id)
    return {"cats": categories, "arg1": arg1, "arh2":arh2}
