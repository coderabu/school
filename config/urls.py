from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('groups/',include('groups.urls')),
    path('teacher/', include('teacher.urls')),
    path('attendance/', include('attendance.urls')),
]