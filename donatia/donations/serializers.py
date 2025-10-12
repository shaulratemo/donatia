from rest_framework import serializers
from .models import Donation
from causes.models import Cause

class DonationSerializer(serializers.ModelSerializer):
    donor = serializers.ReadOnlyField(source='donor.email')
    cause_title = serializers.ReadOnlyField(source='cause.title')

    class Meta:
        model = Donation
        fields = [
            'id',
            'donor',
            'cause',
            'cause_title',
            'amount',
            'payment_method',
            'transaction_id',
            'status',
            'donated_at'
        ]
        read_only_fields = ['id', 'donor', 'status', 'donated_at', 'cause_title']

    def validate_amount(self, value):
        """Ensure donation amount is positive."""
        if value <= 0:
            raise serializers.ValidationError("Donation amount must be greater than zero.")
        return value

    def validate_cause(self, value):
        """Ensure the cause exists and is active."""
        if not value.is_active:
            raise serializers.ValidationError("This cause is not currently active.")
        return value

    def create(self, validated_data):
        """Attach donor automatically when creating a donation."""
        request = self.context.get('request')
        donor = request.user
        validated_data['donor'] = donor
        validated_data['status'] = 'successful'  # For now, assume successful (M-PESA later)
        donation = Donation.objects.create(**validated_data)

        # Update cause raised_amount
        donation.cause.raised_amount += donation.amount
        donation.cause.save()

        return donation
