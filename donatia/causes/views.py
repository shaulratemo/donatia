from rest_framework import generics, filters
from .models import Cause
from .serializers import CauseSerializer
from .permissions import IsOrgOwnerOrAdmin, IsOrgUserForCreate

# Create your views here.
class CauseListCreateView(generics.ListCreateAPIView):
    """
    GET: List active causes (public)
    POST: Create a cause (org owner or admin)
    """
    queryset = Cause.objects.filter(is_active=True)
    serializer_class = CauseSerializer
    # allow read for everyone; creation limited via custom permission
    permission_classes = [IsOrgUserForCreate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'organization__name']

    def get_queryset(self):
        qs = super().get_queryset()
        # optional filter by organization id: ?organization_id=3
        org_id = self.request.query_params.get('organization_id')
        if org_id:
            qs = qs.filter(organization__id=org_id)
        return qs


class CauseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: view cause details (public if active)
    PUT/PATCH/DELETE: allowed for org owner or admin
    """
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer
    permission_classes = [IsOrgOwnerOrAdmin]
