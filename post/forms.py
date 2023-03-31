from django import forms
# from django.contrib.auth.models import User
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email','subject', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your NITK email ID'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the specific subject (e.g. Quiz 1, given by Prof. X, 6th sem, 2024 batch)'}),
            'content': forms.Textarea(attrs={'class': 'form-control md-textarea', 'placeholder': 'Write up the content or put a drive link here'}),
        }



