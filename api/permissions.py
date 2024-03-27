from rest_framework import permissions
from .models import UserProfile

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to assign roles.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

class IsRole(permissions.BasePermission):
    """
    Custom permission to restrict access based on user's role.
    """
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        required_roles = getattr(view, "required_roles", [])
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        user_role = user_profile.role  # Get the role associated with the user
        if user_role.name in required_roles:
            return True
        return False