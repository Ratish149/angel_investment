from .serializers import ContactSerializer, NewsletterSerializer, BookSpaceSerializer
from rest_framework import generics
from .models import Contact, Newsletter, BookSpace
from django.template.loader import render_to_string
import os
import resend
# Create your views here.

resend.api_key = os.getenv('RESEND_API_KEY')


class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        email = contact.email

        html_content = render_to_string(
            "admin_contact_email.html",
            {"contact": contact}
        )
        if resend.api_key:
            try:
                params = {
                    "from": "BAIN@BAIN.com",
                    "to": [email],
                    "subject": "New Contact Form Submission",
                    "html": html_content,
                }
                resend.Emails.send(params)
            except Exception as e:
                pass


class NewsletterView(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class BookSpaceView(generics.ListCreateAPIView):
    queryset = BookSpace.objects.all()
    serializer_class = BookSpaceSerializer
