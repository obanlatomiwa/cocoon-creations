from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import UserViewSet, AuthorListView, AuthorDetailView, ArticleListView, ArticleDetailView, \
    CategoryListView, CategoryDetailView, ReaderListView, ReaderDetailView, ReaderBookmarkListView, \
    ReaderBookmarkDetailView

# USERS URL, INHERITED FROM DJANGO
router = DefaultRouter()
router.register('users', UserViewSet)


# CRUD URLS
urlpatterns = [
    path('', include(router.urls)),
    path('authors/', AuthorListView.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>/', ArticleDetailView.as_view()),
    path('readers/', ReaderListView.as_view()),
    path('readers/<int:pk>/', ReaderDetailView.as_view()),
    path('readers/<int:pk>/bookmarks/', ReaderBookmarkListView.as_view()),
    # path('readers/<int:pk>/bookmarks/<int:pk>', ReaderBookmarkListView.as_view()),

]

