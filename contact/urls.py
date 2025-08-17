from django.urls import path
from .views import ContactView, NewsletterView, BookSpaceView
urlpatterns = [
    path('contact/', ContactView.as_view(), name="contact"),
    path('newsletter/', NewsletterView.as_view(), name="newsletter"),
    path('book-space/', BookSpaceView.as_view(), name="book-space"),
]
