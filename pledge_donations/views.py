from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'pledge_donations/index.html'
