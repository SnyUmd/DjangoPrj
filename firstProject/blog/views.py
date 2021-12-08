from django.shortcuts import render

from django.views.generic.base import TemplateView

# Create your views here.

class IndexView(TemplateView):
    '''
    Attributes:
        template_name:
    '''
    template_name = 'index.html'
    