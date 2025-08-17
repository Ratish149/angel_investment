import os
import resend
from rest_framework import serializers
from .models import Contact, Newsletter, BookSpace
from django.template.loader import render_to_string


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


class BookSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSpace
        fields = '__all__'

    def create(self, validated_data):
        book_space = BookSpace.objects.create(**validated_data)
        email = validated_data['email']
        if email:
            resend.api_key = os.getenv('RESEND_API_KEY')
            if resend.api_key:
                html = render_to_string(
                    'email_templates/date_booking.html', validated_data)
                params = {
                    "from": "BAIN <BAIN@BAIN.com>",
                    "to": [email],
                    "subject": "Book Space Form Submission",
                    "html": html,
                }
                resend.Emails.send(params)
        return book_space
