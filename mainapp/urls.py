from django.urls import path
from .views import *


urlpatterns = [
    path('api/teacher',TeacherAPIView.as_view(), name="teacher"),
    path('api/teacher/<int:pk>',TeacherDetailAPIView.as_view(), name="teacher-details")
]
