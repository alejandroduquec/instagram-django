"""User forms."""

# Django
from django import forms

# Model
from django.contrib.auth.models import User, Group
from users.models import Profile


class SignupForms(forms.Form):
    """Sign up form."""

    username = forms.CharField(
        min_length=4,
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    password = forms.CharField(
        max_length=70,
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password_confirmation = forms.CharField(
        max_length=70,
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}))

    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    email = forms.CharField(
        min_length=6,
        max_length=70,
        label='',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        """Veirify password confirmation match"""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')
        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """ Profile form"""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()


class UserForm(forms.ModelForm):
    """User Model Form."""

    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    groups = forms.ModelMultipleChoiceField(
        label='Groups',
        queryset=Group.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'groups',
        ]
