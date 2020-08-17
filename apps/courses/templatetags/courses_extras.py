from django import template
from apps.courses.models import Course
from random import sample
import random
from django.db.models import Q
from django.template.defaultfilters import slugify


register = template.Library()

@register.simple_tag
def get_courses():
    courses = Course.objects.filter(status = True)
    return courses



