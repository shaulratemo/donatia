from rest_framework import serializers
from .models import Cause


class CauseSerializer(serializers.ModelSerializer):
    """
    Serializer for Cause model.
    Organization is attached automatically from the logged-in user's organization.
    """
    organization = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cause
        fields = [
            'id', 'title', 'description',
            'target_amount', 'raised_amount',
            'is_active', 'organization',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['raised_amount', 'created_at', 'updated_at', 'organization']

    def get_organization(self, obj):
        """Return minimal organization details in responses."""
        return {'id': obj.organization.id, 'name': obj.organization.name}
