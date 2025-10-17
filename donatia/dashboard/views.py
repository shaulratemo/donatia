from rest_framework import permissions, views, response, status
from django.db.models import Sum
from donations.models import Donation
from causes.models import Cause
from organizations.models import Organization


class AdminDashboardView(views.APIView):
    """
    Dashboard for system admin:
    - Global donation stats
    - Organization stats
    - Top performing organizations
    """
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        # Aggregate global statistics
        total_donations = Donation.objects.aggregate(total=Sum('amount'))['total'] or 0
        total_donors = Donation.objects.values('donor').distinct().count()
        total_organizations = Organization.objects.count()
        total_causes = Cause.objects.count()

        # Top 2 organizations by total funds raised
        top_orgs = (
            Donation.objects
            .values('cause__organization__name')
            .annotate(total=Sum('amount'))
            .order_by('-total')[:2]
        )

        return response.Response({
            "total_donations": total_donations,
            "total_donors": total_donors,
            "total_organizations": total_organizations,
            "total_causes": total_causes,
            "top_organizations": top_orgs,
        }, status=status.HTTP_200_OK)


class OrganizationDashboardView(views.APIView):
    """
    Dashboard for organization owners:
    - Displays stats and top-performing causes
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Ensure user has an organization profile
        org = getattr(request.user, 'organization', None)
        if not org:
            return response.Response(
                {"detail": "No organization profile found for this user."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Filter related data
        causes = Cause.objects.filter(organization=org)
        donations = Donation.objects.filter(cause__in=causes)

        # Compute stats
        total_donations = donations.aggregate(total=Sum('amount'))['total'] or 0
        total_causes = causes.count()
        total_donors = donations.values('donor').distinct().count()

        # Top 3 causes by donation amount
        top_causes = (
            donations.values('cause__title')
            .annotate(total=Sum('amount'))
            .order_by('-total')[:3]
        )

        return response.Response({
            "organization": org.name,
            "total_donations": total_donations,
            "total_causes": total_causes,
            "total_donors": total_donors,
            "top_causes": top_causes,
        }, status=status.HTTP_200_OK)
