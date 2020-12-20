from django.urls import path
from . import views

app_name = 'pledge_donations'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('info/', views.ProblemStatementView.as_view(), name='problem-statement'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/success/', views.ContactSuccessView.as_view(), name='contact_success'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('event/', views.EventListView.as_view(), name='event_list'),
    path('event/<slug:slug>/', views.EventDetail.as_view(), name='event_details'),
    path('books/', views.EventListView.as_view(), name='books_list'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('subscription/success/', views.SubscriptionSuccessView.as_view(), name='subscription_success'),
    # path('test', views.TesterView.as_view(), name='tester_page'),
]
