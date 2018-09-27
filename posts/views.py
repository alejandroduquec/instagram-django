""" Post views """
#Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
#Forms
from posts.forms import * 

#Models
from posts.models import *
from users.models import *


class PostFeedView(ListView,LoginRequiredMixin):
    """Return all published post"""

    template_name='posts/feed.html'
    model= Post
    ordering=('-created',)
    paginate_by=2
    context_object_name='posts'

class DetailPostView(DetailView,LoginRequiredMixin):
    """detail for each post cicked """

    template_name='posts/detail_post.html'
    pk_url_kwarg = 'pk'
    queryset=Post.objects.all()
    context_object_name='post'


@login_required
def create_post(request):
    """create new view post"""
    if request.method =='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form=PostForm()
    return render(request,'posts/new.html',{
        'form':form,
        'user':request.user,
        'profile':request.user.profile

    })





