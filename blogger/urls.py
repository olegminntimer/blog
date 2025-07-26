from blogger.apps import BloggerConfig
from rest_framework.routers import DefaultRouter

from blogger.views import PostViewSet

app_name = BloggerConfig.name

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = [

] + router.urls
