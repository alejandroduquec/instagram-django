"""middleware to ensure bio information"""
#django
from django.shortcuts import redirect
from django.urls import reverse
class ProfileCompletionMiddleware:
    """ Profile completion middleware ensure that user have any
    bio information"""
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        """code to be executed for each request before the view is called"""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile=request.user.profile
                
                if not profile.picture or not profile.biography:
                    #except some urls
                    if request.path not in [reverse('users:update_profile'),reverse('users:logout')]:
                        return redirect('users:update_profile')
        response=self.get_response(request)
        return response
