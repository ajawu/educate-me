from django.urls import path
from . import views

app_name = 'pledge_donations'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('info/', views.ProblemStatementView.as_view(), name='problem-statement'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('event/', views.EventListView.as_view(), name='event_list'),
    path('books/', views.EventListView.as_view(), name='books_list'),
    path('event/<slug:event_slug>/', views.SubscribeView.as_view(), name='event_details'),
    # path('test', views.TesterView.as_view(), name='tester_page'),
]
