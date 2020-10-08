from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from apps.courses.models import Course

class CourseDetailView(DetailView):
    model = Course

