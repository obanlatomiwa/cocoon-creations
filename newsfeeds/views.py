from django.shortcuts import render
from rest_framework import viewsets, status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import Author, Article, Category, Reader
from django.contrib.auth.models import User
from .serializers import UserSerializer, AuthorSerializer, ArticleSerializer, CategorySerializer, ReaderSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication,)


class AuthorListView(APIView):
    """
    List all Authors, or create a new Author.
    """

    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):
    """
    Retrieve, update or delete a Author instance.
    """

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):
    """
    List all Categories, or create a new Category.
    """

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    """
    Retrieve, update or delete a Category instance.
    """

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleListView(APIView):
    """
    List all Article, or create a new Article.
    """

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    """
    Retrieve, update or delete a Article instance.
    """

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReaderListView(APIView):
    """
    List all Reader, or create a new Reader.
    """

    def get(self, request, *args, **kwargs):
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ReaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReaderDetailView(APIView):
    """
    Retrieve, update or delete a Reader instance.
    """

    def get_object(self, pk):
        try:
            return Reader.objects.get(pk=pk)
        except Reader.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        reader = self.get_object(pk)
        serializer = ReaderSerializer(reader)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        reader = self.get_object(pk)
        serializer = ReaderSerializer(reader, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        reader = self.get_object(pk)
        reader.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReaderBookmarkListView(APIView):
    """
    Views to filter bookmarks and create bookmarks for a particular reader
    """
    # filter Article Object with is_bookmark = True
    def get_object(self, pk):
        try:
            return Article.objects.filter(is_bookmark=True)
        except Article.DoesNotExist:
            raise Http404

    # get bookmarks by users
    def get(self, request, *args, **kwargs):
        if self.request.user:
            bookmarks = self.get_object(pk)
            serializer = ArticleSerializer(bookmarks)
            return Response(serializer.data)

    # create bookmarks by users
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReaderBookmarkDetailView(APIView):
    """
    Views to filter bookmarks and delete bookmarks for a particular reader
    """

    # filter Article Object with is_bookmark = True
    def get_object(self, pk):
        try:
            return Article.objects.filter(is_bookmark=True)
        except Article.DoesNotExist:
            raise Http404

    # get bookmarks by users
    def get(self, request, *args, **kwargs):
        if self.request.user:
            bookmarks = self.get_object(pk)
            serializer = ArticleSerializer(bookmarks)
            return Response(serializer.data)

    # delete bookmarks by users
    def delete(self, request, pk, *args, **kwargs):
        if self.request.user:
            bookmarks = self.get_object(pk)
            bookmarks.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
