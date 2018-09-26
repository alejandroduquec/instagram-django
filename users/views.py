""" Users view"""
#Django
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#Models
from django.contrib.auth.models import User
from users.models import Profile
#Exeption
from django.db.utils import IntegrityError
#Forms
from users.forms import *

@login_required
def update_profile(request):
    """ update a users profile """
    profile=request.user.profile
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data=form.cleaned_data

            profile.website=data['website']
            profile.phone_number=data['phone_number']
            profile.biography=data['biography']
            profile.picture=data['picture']
            profile.save()          
            return redirect('posts:feed')  
    else:
        form = ProfileForm()

    return render(request,'users/update_profile.html',
        {
        'form':form,
        'profile':profile,
        'user':request.user
        }


    )

def login_view(request):
    """login view"""
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})

    return render(request,'users/login.html')
@login_required
def logout_view(request):
    """logout view"""
    logout(request)
    return redirect('users:login')

def signup(request):
    """sigin up view"""
    if request.method == 'POST':
        form=SignupForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignupForms()
    return render(request,'users/signup.html',{'form':form})


