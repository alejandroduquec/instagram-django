"""Posts url."""

# Django
from django.urls import path

from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostFeedView.as_view(),
        name='feed'),

    path(
        route='posts/new',
        view=views.CreatePostView.as_view(),
        name='create_post'),

    path(
        route='posts/detail/<int:pk>/',
        view=views.DetailPostView.as_view(),
        name='detail_post'),
]
