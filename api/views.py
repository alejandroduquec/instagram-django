#Views for api example 
from rest_framework.generics  import (
    ListAPIView , RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,DestroyAPIView,
    CreateAPIView)


from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
#Models
from posts.models import *
from .serializers import *


class CreatePostAPIView(CreateAPIView):
    """Create post"""
    queryset = Post.objects.all()
    serializer_class=CreatePostSerializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self,serializer):
        """manage values before create"""
        serializer.save(user=self.request.user,profile=self.request.user.profile)

class PostsListAPIView(ListAPIView):
    """posts view api"""
    queryset = Post.objects.all()
    serializer_class=PostListSerializer

    


class PostDetailAPIView(RetrieveAPIView):
    """Detail view for each post"""
    queryset = Post.objects.all()
    serializer_class=PostDetailSerializer
    #name db column
    lookup_field='title'
    #name data receipt in url
    lookup_url_kwarg='titulo_post'

class PostDeleteAPIView(DestroyAPIView):
    """Delete view for each post"""
    queryset = Post.objects.all()
    serializer_class=PostDetailSerializer
    #name db column
    lookup_field='pk'

class PostUpdateAPIView(RetrieveUpdateAPIView):
    """Update view for each post"""
    queryset = Post.objects.all()
    serializer_class=PostDetailSerializer
    #name db column
    lookup_field='pk'



