from django.shortcuts import render
from .serializers import ContactSerializer,NewsletterSerializer
from rest_framework import generics
from .models import Contact,Newsletter
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Create your views here.

class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        
        # Send email to admin
        subject = "New Contact Form Submission"
        html_message = render_to_string(
            "admin_contact_email.html",
            {"contact": contact}
        )
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],  # Send to admin email
            html_message=html_message,
        )

class NewsletterView(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
