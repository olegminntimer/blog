from rest_framework import generics

from blogger.models import Post, Comment
from blogger.serializers import PostSerializer, CommentSerializer
from users.permissions import IsAuthenticated, IsAdminOrAuthor


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

class PostRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAdminOrAuthor]

class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAdminOrAuthor]


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminOrAuthor]

class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAdminOrAuthor]
