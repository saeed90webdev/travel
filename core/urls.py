from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('' ,index_view,name='index'), 
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('newsletter',newsletter_view,name='newsletter')
]
