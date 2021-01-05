from django.urls import path
from .views import HomePageView, ContactPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contactUs/', ContactPageView.as_view(), name='contactUs'),

    ]
