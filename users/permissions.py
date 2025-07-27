from rest_framework import permissions


class IsAdminOrSelf(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать только себя или администратору.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user

class IsAuthenticated(permissions.BasePermission):
    """
    Разрешение для авторизованных пользователей.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать или удалять пост (комментарий) только автору или администратору.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user
