from django.contrib.auth.models import AbstractUser
from django.db import models

from blogger.validators import (
    validate_email_domain,
    validate_password_complexity,
)


class User(AbstractUser):

    username = None

    email = models.EmailField(
        verbose_name="Email", validators=[validate_email_domain], unique=True
    )

    # def save(self, *args, **kwargs):
    #     # Валидация перед сохранением
    #     validate_password_complexity(self.password)
    #     super().save(*args, **kwargs)

    phone = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона",
        null=True,
        blank=True,
    )

    birth_date = models.DateField(
        verbose_name="Дата рождения",
        help_text="Укажите дату рождения",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата редактирования"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
