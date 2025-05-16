from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('' , blog_view, name="blog_home"), 
    path('<int:pid>/' , blog_detail_view, name="blog_detail"), 
    path('category/<str:cat_name>/', blog_view, name="blog_category"),
    path('tag/<str:tag_name>/', blog_view, name="blog_tag"),
    path('author/<str:author_username>/', blog_view, name="blog_author"),
    path('search/', blog_search_view, name='blog_search')
]