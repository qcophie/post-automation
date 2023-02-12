from django.urls import path

from posts.views import PostContent


urlpatterns = [
    path('post_content/', PostContent.as_view())
]