from django.urls import path
from .apps import MypediaConfig
from . import views
from rest_framework.routers import DefaultRouter

app_name = MypediaConfig.name

router = DefaultRouter()
router.register("courses", views.CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/", views.LessonListCreateAPIView.as_view(), name="lessons"),
    path("lessons/<int:pk>/", views.LessonRetrieveUpdateDestroyAPIView.as_view(), name="lesson"),
] + router.urls
