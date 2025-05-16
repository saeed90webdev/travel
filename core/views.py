from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from core.forms import *

def index_view(request):
    return render(request, 'core/index.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "unknown"
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Your message submited successfully')
            return redirect('core:contact')
        else :
            messages.add_message(request, messages.ERROR, 'Your message did not submit.')   
    form = ContactForm()

    context = {
        'form': form
    } 
    return render(request, 'core/contact.html', context)

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


