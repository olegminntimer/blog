from rest_framework import viewsets

from blogger.models import Post, Comment
from blogger.serializers import PostSerializer, CommentSerializer
from users.permissions import IsAuthenticated, IsAuthorOrAdmin


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]  # CREATE: авторизованные пользователи, READ: все пользователи

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthorOrAdmin]
        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]  # CREATE: авторизованные пользователи, READ: все пользователи

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthorOrAdmin]
        return super().get_permissions()
