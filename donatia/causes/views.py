from rest_framework import generics, filters, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Cause
from .serializers import CauseSerializer
from .permissions import IsOrgOwnerOrAdmin, IsOrgUserForCreate


class CauseListCreateView(generics.ListCreateAPIView):
    """
    GET: List active causes (public)
    POST: Create a cause (org owner or admin)
    """
    queryset = Cause.objects.filter(is_active=True)
    serializer_class = CauseSerializer
    permission_classes = [IsOrgUserForCreate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'organization__name']

    def get_queryset(self):
        qs = super().get_queryset()
        org_id = self.request.query_params.get('organization_id')
        if org_id:
            qs = qs.filter(organization__id=org_id)
        return qs

    def perform_create(self, serializer):
        organization = getattr(self.request.user, 'organization', None)
        if not organization or organization.status != 'approved':
            raise PermissionDenied("Your organization is not approved to create causes.")
        serializer.save(organization=organization)


class CauseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: View cause details (public if active)
    PUT/PATCH/DELETE: Allowed for org owner or admin
    """
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer
    permission_classes = [IsOrgOwnerOrAdmin]
