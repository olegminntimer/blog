from rest_framework import viewsets

from blogger.models import Post
from blogger.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
