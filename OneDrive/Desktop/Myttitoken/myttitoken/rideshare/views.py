import json  # Import json to handle JSON data
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse
from django.views import View
from django import forms
from rest_framework import viewsets
from .models import RideRequest, Transaction
from .serializers import RideRequestSerializer, TransactionSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# User Registration Form
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for this view
class UserRegistrationView(View):
    def post(self, request):
        # Load JSON data from request body
        data = json.loads(request.body)
        form = UserRegistrationForm(data)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return JsonResponse({"message": "User created successfully."}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)

# Rideshare Views
class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
