from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOrgOwnerOrAdmin(BasePermission):
    """
    Object-level permission to only allow organization owner or admin
    to edit a cause. Read-only is allowed for any request.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only requests for everyone
        if request.method in SAFE_METHODS:
            return True

        # Admins have full access
        if request.user and request.user.is_staff:
            return True

        # obj is a Cause instance; check ownership
        return hasattr(request.user, 'id') and obj.organization.user == request.user


class IsOrgUserForCreate(BasePermission):
    """
    Permission for creating a Cause:
    - Anyone can GET.
    - To POST, the user must be authenticated AND must be the owner of the organization
      specified in the request data (or a staff user).
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        # Must be authenticated to create
        if not (request.user and request.user.is_authenticated):
            return False

        # staff allowed
        if request.user.is_staff:
            return True

        # For POST, expect organization_id in payload
        org_id = request.data.get('organization_id')
        if not org_id:
            return False

        from organizations.models import Organization
        try:
            org = Organization.objects.get(pk=org_id)
        except Organization.DoesNotExist:
            return False

        # The requesting user must be the owner of the organization
        return org.user == request.user
