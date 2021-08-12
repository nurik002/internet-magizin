from django.urls import path

from posts.views import PostListView, PostDetailView, PostCommentCreateView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post-comment/<int:pk>', PostCommentCreateView.as_view(), name='post-comment'),
]
