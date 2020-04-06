from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Full Name'}), max_length=100)
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}),)
    subject = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Subject'}), max_length=150)
    message = forms.CharField(label="",
        max_length=600, widget=forms.Textarea
    )

    def send_mail(self):
        logger.info("Sending email to customer service")
        message = "From: {0}\n{1}\n{2}\n{3}".format(
            self.cleaned_data["name"],
            self.cleaned_data["email"],
            self.cleaned_data["subject"],
            self.cleaned_data["message"],
        )
        send_mail(
        "Site message",
            message,
            "site@designscorecard.com",
            ["customerservice@designscorecard.co,"],
            fail_silently=False,
        )
