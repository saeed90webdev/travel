from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('' ,blog_view, name="blog_home"), 
    path('<int:pid>' ,blog_detail_view, name="blog_detail"), 
]