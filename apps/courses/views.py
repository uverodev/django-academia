from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from apps.courses.models import Course, Question, Instructor

class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['question_list'] = Question.objects.filter( course = self.kwargs['pk'] )
        return context
