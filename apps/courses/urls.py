from django.urls import path
from apps.courses.views import CourseDetailView

urlpatterns = [
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]