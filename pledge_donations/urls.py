from django.urls import path
from . import views

app_name = 'pledge_donations'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('contact', views.LandingPageView.as_view(), name='contact_page'),
    # path('test', views.TesterView.as_view(), name='tester_page'),
]
