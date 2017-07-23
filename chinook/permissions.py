from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            if request.user.is_superuser:
                return True
            else:
                return False
        else:
            return True


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method not in SAFE_METHODS:
            return obj.user == request.user
        else:
            return True
