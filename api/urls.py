"""api url"""
#Django
from django.urls import path
#Views
from api import views

urlpatterns=[
    path(
        route='',
        view=views.PostsListAPIView.as_view(),
        name='api'
        ),
        path(
        route='<str:titulo_post>/',
        view=views.PostDetailAPIView.as_view(),
        name='detail'
        ),
        path(
        route='delete/<int:pk>/',
        view=views.PostDeleteAPIView.as_view(),
        name='delete'
        ),
        path(
        route='edit/<int:pk>/',
        view=views.PostUpdateAPIView.as_view(),
        name='edit'
        ),
        path(
        route='newpost',
        view=views.CreatePostAPIView.as_view(),
        name='newpost'
        ),
]