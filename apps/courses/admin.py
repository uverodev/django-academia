from django.contrib import admin
from .models import Category, Course, Instructor, Question

admin.site.register(Category)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Question)

