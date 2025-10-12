from rest_framework import serializers
from .models import Cause
from organizations.models import Organization


class CauseSerializer(serializers.ModelSerializer):
    """
    Serializer for Cause. For create, expect `organization_id` in input.
    In responses, include nested organization id and name for convenience.
    """
    organization_id = serializers.IntegerField(write_only=True, required=True)
    organization = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cause
        fields = [
            'id', 'title', 'description',
            'target_amount', 'raised_amount', 'is_active',
            'organization_id', 'organization',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['raised_amount', 'created_at', 'updated_at']

    def get_organization(self, obj):
        # minimal organization info
        return {'id': obj.organization.id, 'name': obj.organization.name}

    def validate_organization_id(self, value):
        # Ensure organization exists and is approved
        try:
            org = Organization.objects.get(pk=value)
        except Organization.DoesNotExist:
            raise serializers.ValidationError("Organization does not exist.")
        if org.status != 'approved' and not self.context['request'].user.is_staff:
            raise serializers.ValidationError("Organization is not approved.")
        return value

    def create(self, validated_data):
        org_id = validated_data.pop('organization_id')
        organization = Organization.objects.get(pk=org_id)
        # Create cause linked to the organization
        return Cause.objects.create(organization=organization, **validated_data)
