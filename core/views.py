from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "core/about.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"

class HelpView(TemplateView):
    template_name = "core/help.html"

class TermsView(TemplateView):
    template_name = "core/terms.html"