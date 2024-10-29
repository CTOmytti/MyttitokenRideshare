from rest_framework import serializers
from .models import RideRequest, Transaction

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ['id', 'rider', 'pickup_location', 'dropoff_location', 'ride_status', 'created_at']  # Use ride_status

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'ride_request', 'amount', 'payment_type', 'status', 'created_at']  # Use created_at for timestamp
