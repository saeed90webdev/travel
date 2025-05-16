from django.contrib import admin
from core.models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "date_time_created"
    list_display = ('name', 'email', 'date_time_created',)
    ordering = ('-date_time_created',)
    search_fields = ('message', 'subject', 'name',)

    
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)