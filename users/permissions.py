from rest_framework import permissions


class IsAdminOrAuthor(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать или удалять объект только администратору или автору.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user


class IsAdmin(permissions.BasePermission):
    """
    Разрешение, позволяющее доступ только администратору.
    """

    def has_permission(self, request, view):
        return request.user.is_staff


class IsAuthenticated(permissions.BasePermission):
    """
    Разрешение, позволяющее доступ только авторизованным пользователям.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated
