import re
from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Валидатор пароля
def validate_password_complexity(value):
    if len(value) < 8:
        raise ValidationError(
            _("Пароль должен содержать минимум 8 символов."),
            code="password_too_short",
        )
    if not re.search(r"\d", value):
        raise ValidationError(
            _("Пароль должен содержать хотя бы одну цифру."),
            code="password_no_digits",
        )


# Валидатор email
def validate_email_domain(value):
    allowed_domains = ["mail.ru", "yandex.ru"]
    domain = value.split("@")[-1]

    if domain not in allowed_domains:
        raise ValidationError(
            _("Допустимы только почтовые адреса с доменами: %(domains)s"),
            code="invalid_domain",
            params={"domains": ", ".join(allowed_domains)},
        )


# Валидатор возраста автора
def validate_author_age(birth_date):
    today = date.today()
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )

    if age < 18:
        raise ValidationError(
            _("Автор должен быть старше 18 лет."), code="underage_author"
        )


# Валидатор запрещённых слов в заголовке
forbidden_words = ["ерунда", "глупость", "чепуха"]


def validate_title_content(value):
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError(
                _('Заголовок содержит запрещённое слово: "%(word)s"'),
                code="forbidden_word",
                params={"word": word},
            )
