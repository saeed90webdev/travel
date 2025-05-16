from django import forms
from core.models import *


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'