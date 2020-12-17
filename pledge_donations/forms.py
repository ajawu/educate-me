from django import forms
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact, Subscription


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'

    def send_email(self):
        # TODO: optimise to use celery
        send_mail(subject='Educate-Me Newsletter Subscription',
                  message='Hey, \nYourEmail was just subscribed to educate-Me\'s Newsletter.',
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[self.email])
