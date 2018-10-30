#Views for api example 
from rest_framework.generics  import ListAPIView
#Models
from posts.models import *
from .serializers import *



class PostsListAPIView(ListAPIView):
    """posts view api"""
    queryset = Post.objects.all()
    serializer_class=PostSerializer