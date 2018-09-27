""" Post views """
#Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
#Forms
from posts.forms import * 

#Models
from posts.models import *
from users.models import *


class PostFeedView(LoginRequiredMixin,ListView):
    """Return all published post"""

    template_name='posts/feed.html'
    model= Post
    ordering=('-created',)
    paginate_by=2
    context_object_name='posts'

class DetailPostView(LoginRequiredMixin,DetailView):
    """detail for each post cicked """

    template_name='posts/detail_post.html'
    pk_url_kwarg = 'pk'
    queryset=Post.objects.all()
    context_object_name='post'

class CreatePostView(LoginRequiredMixin,CreateView):
    """create new  posts"""
    template_name='posts/new.html'
    form_class=PostForm
    success_url=reverse_lazy('posts:feed')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context






