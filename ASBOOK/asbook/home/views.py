from django.shortcuts import render
from django.http import HttpResponse
import logging

from django.views.generic import TemplateView


# Create your views here.
# def salut(request):
#     logging.debug("Userul a accesat salut")
#     return HttpResponse("Salutare domnule")

class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'



