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
]