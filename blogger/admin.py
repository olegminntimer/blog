from django.contrib import admin

from blogger.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "image", "author")
    list_filter = ("created_at",)
