
from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # Include chat app URLs
]
