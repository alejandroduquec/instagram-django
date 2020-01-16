"""Platzigram MODULE urls"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('api/', include(('api.urls', 'api'), namespace='api')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
