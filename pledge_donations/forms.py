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
        send_mail(subject='Educate-Me Newsletter Subscription Registration',
                  message='Welcome to educate-Me\'s Newsletter. \n Your email address will never be shared with any '
                          'other organisations. You can unsubscribe anytime from your account dashboard.'
                          'We hope you don\'t though :)',
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[self.cleaned_data['email']])
