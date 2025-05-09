from django.contrib import admin
from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "date_time_created"
    list_display = ('title', 'status', 'date_time_published', 'counted_view',)
    list_filter = ('status',)
    ordering = ('-date_time_created',)
    search_fields = ('title', 'content',)