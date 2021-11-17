from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('category/<int:cat_id>/', get_category, name='category'),
    path('post/<int:post_id>/', view_post, name='post'),
    path('add_post/', add_post, name='add_post'),
]
