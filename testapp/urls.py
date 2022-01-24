from django.urls import path
from .views import *


urlpatterns = [
    path('', test, name='testapp'),
    path('rubric/<int:pk>/', get_rubric, name='rubric'),

]

