from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrgOwnerOrAdmin(BasePermission):
    """
    Allows only organization owners or admins to edit a cause.
    Read-only is open to everyone.
    """

    def has_object_permission(self, request, view, obj):
        # Everyone can read
        if request.method in SAFE_METHODS:
            return True

        # Admins can edit
        if request.user and request.user.is_staff:
            return True

        # Organization owner check
        return hasattr(request.user, 'organization') and obj.organization.user == request.user


class IsOrgUserForCreate(BasePermission):
    """
    Allows organization users (with approved organizations) or admins to create causes.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if not user.is_authenticated:
            return False

        # Admins can create
        if user.is_staff:
            return True

        # Ensure user has an approved organization
        try:
            org = user.organization
            return org.status == 'approved'
        except AttributeError:
            return False
