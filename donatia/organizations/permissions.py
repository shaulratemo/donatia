from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOrganizationOwnerOrAdmin(BasePermission):
    """
    Custom permission:
    - Organization owner can view/update their own organization.
    - Admins can view/update/delete any.
    - Everyone can view public (approved) orgs.
    """

    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) for everyone
        if request.method in SAFE_METHODS:
            return True
        
        # Allow if admin or organization owner
        return request.user.is_staff or obj.user == request.user

class IsOrganizationUser(BasePermission):
    """
    Allows only users with role 'organization' to create organizations.
    Other roles (donor, admin) cannot create.
    """
    def has_permission(self, request, view):
        # Read-only access for everyone (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        
        # Write access only for users with 'organization' role
        return (
            request.user.is_authenticated and 
            getattr(request.user, 'role', None) == 'organization'
        )