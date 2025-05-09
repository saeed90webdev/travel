from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import *


def blog_view(request):
    posts = Post.objects.filter(date_time_published__lte=timezone.now(),status=True)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog-home.html', context)


def blog_detail_view(request, pid):
    post = get_object_or_404(Post, id=pid)
    post.counted_view += 1
    post.save()
    context = {
        'post': post,
    }
    return render(request, 'blog/blog-detail.html', context)
