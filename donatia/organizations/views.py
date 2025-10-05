from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Organization
from .serializers import OrganizationSerializer
from .permissions import IsOrganizationOwnerOrAdmin, IsOrganizationUser

# Create your views here.
class OrganizationListCreateView(generics.ListCreateAPIView):
    """
    GET: List all approved organizations (public).
    POST: Register a new organization (authenticated user).
    """
    serializer_class = OrganizationSerializer
    permission_classes = [IsOrganizationUser]

    def get_queryset(self):
        # Only show approved organizations
        return Organization.objects.filter(status='approved')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: View organization details (public if approved).
    PUT/PATCH: Update (owner or admin only).
    DELETE: Admin only.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsOrganizationOwnerOrAdmin]


class OrganizationApprovalView(generics.UpdateAPIView):
    """
    PATCH: Admin-only endpoint to approve or reject organizations.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, *args, **kwargs):
        org = self.get_object()
        new_status = request.data.get('status')

        if new_status not in ['approved', 'rejected']:
            return Response({'error': 'Invalid status value'}, status=status.HTTP_400_BAD_REQUEST)

        org.status = new_status
        org.save()
        return Response({'message': f'Organization {org.name} marked as {new_status}.'})
