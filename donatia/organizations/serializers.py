from rest_framework import serializers
from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for listing and creating organizations."""
    
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'email', 'website', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']

