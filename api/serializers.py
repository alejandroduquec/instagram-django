"""Serializers for api"""
#restframework
from rest_framework.serializers import ModelSerializer

#models
from posts.models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model =Post
        fields=[
            'user',
            'profile',
            'title',
            'title',
        ]


