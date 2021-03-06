from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article, Category


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'category', 'created_date', 'updated_date', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', "category")
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo',  'is_published', 'views', 'created_date', 'updated_date')
    readonly_fields = ('views', 'created_date', 'updated_date', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='75'>")
        else:
            return 'Default photo'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Site Management'
admin.site.site_header = 'Site Management'