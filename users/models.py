from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):

    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Логин пользователя",
        help_text="Укажите логин пользователя",
    )

    phone_number = models.CharField(
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

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
