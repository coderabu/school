from django.urls import path
from .views import LandingPageView

app_name = 'user'
urlpatterns = [
    path('', LandingPageView.as_view(), name='landing')
]