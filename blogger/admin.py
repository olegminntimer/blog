from django.contrib import admin

from blogger.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "image", "author")
    list_filter = ("created_at",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "text", "author")
    list_filter = ("created_at",)
