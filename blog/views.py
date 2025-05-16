from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import *


def blog_view(request, **kwargs):
    posts = Post.objects.filter(
        date_time_published__lte=timezone.now(), status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
        
        
    
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog-home.html', context)


def blog_detail_view(request, pid):
    post = get_object_or_404(
        Post, id=pid, date_time_published__lte=timezone.now(), status=True)
    posts = Post.objects.filter(
        date_time_published__lte=timezone.now(), status=True)

    post_list = list(posts)
    try:
        current_index = post_list.index(post)
    except ValueError:
        current_index = -1

    prev_post = post_list[current_index - 1] if current_index > 0 else None
    next_post = post_list[current_index +
                          1] if current_index < len(post_list) - 1 else None

    post.counted_view += 1
    post.save()

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog/blog-detail.html', context)


# def blog_category_view(request, cat_name):
#     posts = Post.objects.filter(date_time_published__lte=timezone.now(), status=True).filter(category__name=cat_name)
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/blog-home.html', context)


def blog_search_view(request):
    posts = Post.objects.filter(
        date_time_published__lte=timezone.now(), status=True)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog-home.html', context)
