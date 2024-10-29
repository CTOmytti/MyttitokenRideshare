from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class RideRequest(models.Model):
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ride_requests")
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    ride_status = models.CharField(max_length=50, default="pending")  # Status options can be expanded if needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rider.username} - {self.ride_status}"

class Transaction(models.Model):
    ride_request = models.ForeignKey(RideRequest, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # Ensure the amount is not negative
    payment_type = models.CharField(max_length=50, choices=[("MYTT", "MYTT"), ("fiat", "Fiat")])
    status = models.CharField(max_length=50, default="pending")  # Status options can be expanded if needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.ride_request} - Status: {self.status}"
