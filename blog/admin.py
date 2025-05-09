from django.contrib import admin
from blog.models import *


admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "date_time_created"
    list_display = ('title', 'author', 'status', 'date_time_published', 'counted_view',)
    list_filter = ('status', 'author',)
    ordering = ('-date_time_created',)
    search_fields = ('title', 'content',)
