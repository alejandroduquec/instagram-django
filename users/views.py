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

def update_profile(request):
    return render(request,'users/update_profile.html')

def login_view(request):
    """login view"""
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})

    return render(request,'users/login.html')
@login_required
def logout_view(request):
    """logout view"""
    logout(request)
    return redirect('login')

def signup(request):
    """sigin up view"""
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password_confimation=request.POST['password_confimation']
       
        if password_confimation != password:
            return render(request,'users/signup.html',{'error':'please check password try to write the same in the two fields'})
        try:
            user = User.objects.create_user(username=username,password=password)
        except IntegrityError:
            return render(request,'users/signup.html',{'error':'Username is already in use'})
        user.firstname=request.POST['firstname']
        user.lastname=request.POST['lastname']
        user.email=request.POST['email']
        user.save()
        profile=Profile(user=user)
        profile.save()
        return redirect('login')
    return render(request,'users/signup.html')

