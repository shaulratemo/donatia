from rest_framework import generics, permissions
from .models import Donation
from .serializers import DonationSerializer
from .permissions import IsDonorUser, IsOwnerOrAdmin

# Create your views here.
class DonationListCreateView(generics.ListCreateAPIView):
    """
    Donor can view their donations and create new ones.
    Admins can view all donations.
    """
    serializer_class = DonationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return Donation.objects.all()
        return Donation.objects.filter(donor=user)

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsDonorUser()]
        return [permissions.IsAuthenticated()]

class DonationDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a specific donation.
    Only the donor or admin can view.
    """
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()
    permission_classes = [IsOwnerOrAdmin]
