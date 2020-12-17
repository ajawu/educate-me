from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.http import JsonResponse

from .forms import ContactForm, SubscribeForm


class LandingPageView(TemplateView):
    template_name = 'pledge_donations/index.html'


class TesterView(TemplateView):
    template_name = 'account/password_reset_done.html'


class FaqView(TemplateView):
    template_name = 'pledge_donations/faq.html'


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'pledge_donations/contact.html'

    def form_valid(self, form):
        return JsonResponse({'message': 'Message saved successfully. We will get back to you'}, status=202)

    def form_invalid(self, form):
        return JsonResponse({'message': 'Errors occurred while saving form details',
                             'errors': form.errors.as_json()}, status=400)


class ProblemStatementView(TemplateView):
    template_name = 'pledge_donations/problem-statement.html'


class EventsList(ListView):
    model = ''
    template_name = ''


class EventDetail(DetailView):
    model = ''
    template_name = ''


class BooksList(ListView):
    model = ''
    template_name = ''


class SubscribeView(CreateView):
    form_class = SubscribeForm

    def send_email(self, email_address):
        pass

    def form_valid(self, form):
        form.send_email()
        self.object = form.save()
        return JsonResponse({'message': 'Email address subscribed successfully'}, status=201)

    def form_invalid(self, form):
        return JsonResponse({'message': 'Error occurred while processing input',
                             'errors': form.errors.as_json()}, status=400)
