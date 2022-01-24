from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('testapp/', testapp),
    path('', HomePage.as_view(), name='home'),
    # path('', index, name='home'),
    path('about/', about, name='about'),
    # path('category/<int:cat_id>/', get_category, name='category'),
    path('category/<int:cat_id>/', ArticleByCat.as_view(), name='category'),
    # path('post/<int:post_id>/', view_post, name='post'),
    path('post/<int:pk>/', ViewPost.as_view(), name='post'),
    # path('add_post/', add_post, name='add_post'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]
