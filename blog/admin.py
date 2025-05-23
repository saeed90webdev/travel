from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from blog.models import *


admin.site.register(Category)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "date_time_created"
    list_display = ('title', 'author', 'status', 'is_login_required', 'date_time_published', 'counted_view',)
    list_filter = ('status', 'author',)
    ordering = ('-date_time_created',)
    search_fields = ('title', 'content',)
    summernote_fields = ('content',)
    list_editable = ('is_login_required', 'status',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "date_time_created"
    list_display = ('name', 'post', 'date_time_created', 'is_approved',)
    list_filter = ('is_approved',)
    list_editable = ('is_approved',)
    ordering = ('-date_time_created',)
    search_fields = ('name', 'message',)