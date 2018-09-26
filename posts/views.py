""" Post views """
#Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#Utilities
from datetime import datetime 

#Forms
from posts.forms import * 

#Models
from posts.models import *

@login_required
def list_post(request):
    """view for posts"""
    posts=Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html',{'posts':posts})

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



