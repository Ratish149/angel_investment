from django.urls import path
from .views import ContactView, NewsletterView
urlpatterns = [
    path('contact/', ContactView.as_view()),
    path('newsletter/', NewsletterView.as_view()),
]
