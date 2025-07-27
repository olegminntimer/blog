from rest_framework_nested import routers

from blogger.apps import BloggerConfig
from rest_framework.routers import DefaultRouter

from blogger.views import PostViewSet, CommentViewSet

app_name = BloggerConfig.name

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [

] + router.urls
