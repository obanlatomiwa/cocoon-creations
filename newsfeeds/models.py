from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, m2m_changed
from .utils import scramble_uploaded_image, unique_slug_generator


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20, default='Jane Doe')
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return self.name


# signal to update the Author with the slug for easily url and filtering
def author_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(author_slug_pre_save_receiver, sender=Author)


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# signal to update the Category with the slug for easily url and filtering
def category_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_slug_pre_save_receiver, sender=Category)

PUBLISHED_STATUS = (('published', 'Published'), ('submitted', 'Submitted'))


class Article(models.Model):
    title = models.CharField(max_length=40)
    summary = models.CharField(max_length=100)
    content = models.TextField()
    published_status = models.CharField(max_length=20, choices=PUBLISHED_STATUS)
    published_date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)
    is_bookmark = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='article_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title


# signal to update the News with the slug for easily url and filtering
def article_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(article_slug_pre_save_receiver, sender=Article)


class Reader(models.Model):
    reader_account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reader')
    bookmarks = models.ManyToManyField(Category, related_name='bookmarks')

    class Meta:
        verbose_name = 'reader'
        verbose_name_plural = 'readers'

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return self.reader_account

    # get all the bookmarks related to a particular Reader for the Admin Panel
    def get_bookmarks(self):
        return " ".join([bookmark.title for bookmark in self.bookmarks.all()])


# def bookmark_pre_save_receiver(sender, instance, action, *args, **kwargs):
#     if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
#         bookmarks = instance.bookmarks.all()
#         reader_bookmarks = []
#         for bookmark in bookmarks:
#             if bookmark.is_bookmark:
#                 pass
#         instance.save()
#
#
# m2m_changed.connect(bookmark_pre_save_receiver, sender=Reader.bookmarks.through)


