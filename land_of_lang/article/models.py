from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Post content')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of publication')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Last update')
    photo = models.ImageField(upload_to="img/%Y/%m/", verbose_name='Image', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Posted')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Category")
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('post', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        ordering = ['created_date']


class Category(models.Model):
    objects = None
    title = models.CharField(max_length=150, db_index=True, verbose_name='Category')

    def get_absolute_url(self):
        return reverse('category', kwargs={"cat_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
