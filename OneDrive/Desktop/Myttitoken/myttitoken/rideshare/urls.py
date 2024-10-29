from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RideRequestViewSet, TransactionViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'ride-requests', RideRequestViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('', include(router.urls)),
]
