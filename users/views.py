""" Users view"""
#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse_lazy
#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import *

#Forms
from users.forms import *


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'users/test.html'
    form_class = UserForm
    success_url = reverse_lazy('users:me_profile')
    
    def get_object(self):
        """return user object when not came from url kwargs."""
        return self.request.user



class UserDetailView(LoginRequiredMixin, DetailView):
    """detailview for user profile"""

    template_name = 'users/detail.html'
    #who wants to filter in query
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    #how can i call the variable in form ex: {{user.username}}
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """add users post to context"""
        #normal context without override it
        context = super().get_context_data(**kwargs)
        #result of query
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class UpdateProfile(LoginRequiredMixin, UpdateView):
    """Update profile"""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'picture', 'biography']

    def get_object(self):
        """return user profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Returno to users profile"""
        username = self.object.user.username
        return reverse_lazy('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """logout view"""
    template_name = 'users/logout.html'


class SignupView(FormView):
    """users sign up view (similar to create view)"""
    template_name = 'users/signup.html'
    form_class = SignupForms

    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
