"""Serializers for api"""
#restframework
from rest_framework.serializers import ModelSerializer

#models
from posts.models import *

class PostListSerializer(ModelSerializer):
    """Serializer model for posts"""
    class Meta:
        model =Post
        fields=[
            'pk',
            'user',
            'profile',
            'title',
            'created'
         
        ]
class PostDetailSerializer(ModelSerializer):
    """Serializer model detail for posts"""
    class Meta:
        model =Post
        fields=[
            'user',
            'profile',
            'title',
            'title',
            'photo'
        ]

class CreatePostSerializer(ModelSerializer):
    """Serializer model for posts"""
    class Meta:
        model =Post
        fields=[
            'id',
            'title',
            'photo',
        ]



