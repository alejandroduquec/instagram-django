""" users forms"""

#Django
from django import forms

#Models 
from posts.models import *

class PostForm(forms.ModelForm):
    """ post model form"""
    class Meta:
        model=Post
        fields=('user','profile','title','photo')

