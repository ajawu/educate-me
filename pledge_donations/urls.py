from django.urls import path
from . import views

app_name = 'pledge_donations'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('info/', views.ProblemStatementView.as_view(), name='problem-statement'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    # path('test', views.TesterView.as_view(), name='tester_page'),
]
