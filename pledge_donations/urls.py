from django.urls import path
from . import views

app_name = 'pledge_donations'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
]
