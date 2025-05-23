from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import Truncator
from django.utils.html import strip_tags
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    is_login_required = models.BooleanField(default=False)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    date_time_published = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-date_time_created',]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"pid": self.id})
    

        # def snippets(self):
    #     return self.content[:100] + "..."

    def excerpt(self, word_count=30):
        cleaned_text = strip_tags(self.content)
        return Truncator(cleaned_text).words(word_count, truncate=' ...')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_time_created',]