from django.db import models

from users.models import User


class Post(models.Model):

    title = models.CharField(max_length=200, verbose_name="Заголовок поста")

    text = models.TextField(verbose_name="Текст поста")

    image = models.ImageField(
        upload_to="posts/", verbose_name="Изображение", blank=True, null=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор поста",
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата редактирования"
    )

    def __str__(self):
        return f"Пост: {self.title} (автор: {self.author.username})"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]


class Comment(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария",
    )

    text = models.TextField(verbose_name="Текст комментария", max_length=1000)

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост комментария",
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    def __str__(self):
        return f"Комментарий от {self.author.username} ({self.created_at})"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]
