from django.urls import path

from blogger.apps import BloggerConfig

from blogger.views import (
    PostListAPIView,
    PostCreateAPIView,
    PostRetrieveAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
    CommentCreateAPIView,
    CommentListAPIView,
    CommentRetrieveAPIView,
    CommentUpdateAPIView,
    CommentDestroyAPIView,
)

app_name = BloggerConfig.name

urlpatterns = [
    path("posts/create/", PostCreateAPIView.as_view(), name="post-create"),
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path(
        "posts/<int:pk>/", PostRetrieveAPIView.as_view(), name="post-retrieve"
    ),
    path(
        "posts/<int:pk>/update/",
        PostUpdateAPIView.as_view(),
        name="post-update",
    ),
    path(
        "posts/<int:pk>/delete/",
        PostDestroyAPIView.as_view(),
        name="post-delete",
    ),
    path(
        "comments/create/",
        CommentCreateAPIView.as_view(),
        name="comment-create",
    ),
    path("comments/", CommentListAPIView.as_view(), name="comment-list"),
    path(
        "comments/<int:pk>/",
        CommentRetrieveAPIView.as_view(),
        name="comment-retrieve",
    ),
    path(
        "comments/<int:pk>/update/",
        CommentUpdateAPIView.as_view(),
        name="comment-update",
    ),
    path(
        "comments/<int:pk>/delete/",
        CommentDestroyAPIView.as_view(),
        name="comment-delete",
    ),
]
