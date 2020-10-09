from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.courses.models import Course

class Index(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all()
        return context
    