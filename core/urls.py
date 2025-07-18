from django.urls import path
from .views import AboutView, ContactView, HelpView, TermsView

app_name = 'core'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('help/', HelpView.as_view(), name='help'),
    path('terms/', TermsView.as_view(), name='terms'),
]