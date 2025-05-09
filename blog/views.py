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
    post = get_object_or_404(Post, id=pid, status=True)
    posts = Post.objects.filter(date_time_published__lte=timezone.now(),status=True)
    
    post_list = list(posts)
    try:
        current_index = post_list.index(post)
    except ValueError:
        current_index = -1

    prev_post = post_list[current_index - 1] if current_index > 0 else None
    next_post = post_list[current_index + 1] if current_index < len(post_list) - 1 else None
        
    post.counted_view += 1
    post.save()
    
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog/blog-detail.html', context)
