from django.urls import path
from .views import AdminDashboardView, OrganizationDashboardView

urlpatterns = [
    path('admin/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('organization/', OrganizationDashboardView.as_view(), name='organization-dashboard'),
]
