"""User forms """

#Django
from django import forms 

#model
from django.contrib.auth.models import User
from users.models import *

class SignupForms(forms.Form):
    """sign up form"""
    
    username=forms.CharField(
        min_length=4,
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))

    password=forms.CharField(
        max_length=70,
        label='',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password_confirmation=forms.CharField(
        max_length=70,
        label='',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Confirmation'}))
    
    first_name=forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    email=forms.CharField(
        min_length=6,
        max_length=70,
        label='',
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
    )
    #validation one field
    def clean_username(self):
        """username must be unique"""
        username=self.cleaned_data['username']
        username_taken=User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username
    #validations for many fields
    def clean(self):
        """veify password confirmation match """
        data= super().clean()
        password=data['password']
        password_confirmation=data['password_confirmation']
        
        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')
        return data
    #method save 
    def save(self):
        """create user and profile"""
        data=self.cleaned_data
        data.pop('password_confirmation')

        user=User.objects.create_user(**data)
        profile=Profile(user=user)
        profile.save()



class ProfileForm(forms.Form):
    """ Profile form"""

    website=forms.URLField(max_length=200,required=True)
    biography = forms.CharField(max_length=500,required=False)
    phone_number = forms.CharField(max_length=20,required=False)
    picture = forms.ImageField()