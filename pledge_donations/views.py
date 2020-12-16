from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'pledge_donations/index.html'


class TesterView(TemplateView):
    template_name = 'account/password_reset_done.html'
