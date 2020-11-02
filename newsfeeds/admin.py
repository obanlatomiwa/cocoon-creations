from django.contrib import admin
from .models import User, Author, Article, Category, Reader


# Register your models here.

# CREATING AN ADMIN PANEL TO GET, STORE, UPDATE AND DELETE DATA

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'slug')
    list_display = ('id', 'name', 'slug')
    readonly_fields = ('id', 'slug')
    list_per_page = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'slug')
    list_display = ('id', 'name', 'slug')
    readonly_fields = ('id', 'slug')
    list_per_page = 20


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = (
        'id', 'title', 'author', 'summary', 'content', 'category', 'published_date', 'published_status', 'slug',
        'updated', 'is_bookmark')
    list_display = (
        'id', 'title', 'author', 'summary', 'content', 'category', 'published_date', 'published_status', 'slug',
        'updated', 'is_bookmark')
    readonly_fields = ('id', 'slug', 'updated',)
    list_per_page = 20


@admin.register(Reader)
class NewsAdmin(admin.ModelAdmin):
    fields = ('id', 'reader_account', 'bookmarks')
    list_display = ('id', 'reader_account', 'get_bookmarks')
    readonly_fields = ('id',)
    list_per_page = 20


