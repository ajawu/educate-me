from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.http import JsonResponse

from .forms import ContactForm, SubscribeForm
from .models import Event, Donations

from .utils import get_book_donations_event


class LandingPageView(TemplateView):
    template_name = 'pledge_donations/index.html'


class ProblemStatementView(TemplateView):
    template_name = 'pledge_donations/problem-statement.html'


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'pledge_donations/contact.html'
    success_url = '/contact/success/'

    def form_invalid(self, form):
        return JsonResponse({'message': 'Errors occurred while saving form details',
                             'errors': form.errors.as_json()}, status=400)


class ContactSuccessView(TemplateView):
    template_name = 'account/contact_success.html'


class FaqView(TemplateView):
    template_name = 'pledge_donations/faq.html'


class EventListView(ListView):
    model = Event
    paginate_by = 9
    template_name = 'pledge_donations/event_list.html'
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.all()

        event_breakdown = []
        for event in events:
            event_breakdown.append({
                'name': event.name,
                'slug': event.slug,
                'amount_raised': event.donation_amount,
                'amount_goal': event.donation_goal,
                'donated_books_count': get_book_donations_event(event.id),
                'donated_books_goal': event.book_goal,
                'volunteers_count': event.volunteers.count(),
                'volunteer_goal': event.volunteer_goal,
                'donation_percentage': (event.donation_amount / event.donation_goal) * 100,
                'progress_position': ((event.donation_amount / event.donation_goal) * 100) - 5,
            })

        context['events'] = event_breakdown
        return context


class EventDetail(DetailView):
    model = Event
    template_name = 'pledge_donations/event_detail.html'
    context_object_name = 'event'


class BooksList(ListView):
    model = ''
    template_name = ''


class SubscribeView(CreateView):
    form_class = SubscribeForm
    success_url = '/subscription/success/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse({'message': 'Error occurred while processing input',
                             'errors': form.errors.as_json()}, status=400)


class SubscriptionSuccessView(TemplateView):
    template_name = 'account/subscription_successful.html'


class TesterView(TemplateView):
    template_name = 'account/password_reset_done.html'
