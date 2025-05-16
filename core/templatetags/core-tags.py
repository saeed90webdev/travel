from django import template

register = template.Library()

from blog.models import *
from django.utils import timezone


@register.inclusion_tag("core/core_latest_posts.html")
def core_latest_post(arg=6):
    posts = Post.objects.filter(date_time_published__lte=timezone.now(), status=True).order_by('-date_time_published')[:arg]
    return {'posts' : posts}