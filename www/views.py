from django.views.generic import TemplateView
from www.outils.content import bio, portfolio, cv

class BioView(TemplateView):
    template_name = 'www/bio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(bio.content)

        return context


class PortfolioView(TemplateView):
    template_name = 'www/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(portfolio.content)

        return context


class CVView(TemplateView):
    template_name = 'www/cv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(cv.content)

        return context
