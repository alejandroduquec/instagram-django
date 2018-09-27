""" Users view"""
#Django
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.urls import reverse
#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import *

#Forms
from users.forms import *



class UserDetailView(LoginRequiredMixin,DetailView):
    """detailview for user profile"""

    template_name = 'users/detail.html'
    #who wants to filter in query
    slug_field='username'
    slug_url_kwarg='username'
    queryset=User.objects.all()
    #how can i call the variable in form ex: {{user.username}}
    context_object_name='user'

    def get_context_data(self,**kwargs):
        """add users post to context"""
        #normal context without override it
        context=super().get_context_data(**kwargs)
        #result of query 
        user=self.get_object()
        context['posts']= Post.objects.filter(user=user).order_by('-created')
        return context

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
            url=reverse('users:detail',kwargs={'username':request.user.username})
            return redirect(url)  
    else:
        form = ProfileForm()

    return render(request,'users/update_profile.html',
        {
        'form':form,
        'profile':profile,
        'user':request.user
        }
    )

class LoginView(auth_views.LoginView):
    """Login view"""
    template_name='users/login.html'

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """logout view"""
    template_name='users/logout.html'


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


