from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

class Index(TemplateView):
    template_name = "core/index.html"

    