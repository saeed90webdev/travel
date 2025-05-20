from django import template

register = template.Library()

from blog.models import *
from django.utils import timezone


@register.inclusion_tag("blog/latest-posts.html")
def latest_post(arg=4):
    posts = Post.objects.filter(date_time_published__lte=timezone.now(), status=True).order_by('-date_time_published')[:arg]
    return {'posts' : posts}


@register.inclusion_tag("blog/posts-categories.html")
def postcategories():
    posts = Post.objects.filter(date_time_published__lte=timezone.now(), status=True)
    categoreis = Category.objects.all()
    cat_dict={}
    for cat in categoreis:
        cat_dict[cat] = posts.filter(category=cat).count()
    return {'categories': cat_dict}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid, is_approved=True).count()
        