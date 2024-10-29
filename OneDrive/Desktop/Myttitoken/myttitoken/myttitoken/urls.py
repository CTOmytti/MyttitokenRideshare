# myttitoken/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # Admin panel path
    path('api/', include('rideshare.urls')),   # Includes all API routes under /api/
]
