from rest_framework import permissions

class IsDonorUser(permissions.BasePermission):
    """
    Allow only users with donor role to create donations.
    """

    def has_permission(self, request, view):
        # Only allow POST if user is authenticated and a donor
        if request.method == "POST":
            return request.user.is_authenticated and request.user.role == "donor"
        return True  # Allow safe methods (GET, etc.)

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission: Only the owner (donor) or admin can access a donation.
    """

    def has_object_permission(self, request, view, obj):
        # Admins can view any donation
        if request.user.role == "admin":
            return True

        # Donors can only access their own donations
        return obj.donor == request.user
