from django.urls import path
from .apps import UsersConfig
from . import views

app_name = UsersConfig.name

urlpatterns = [
    path("users/", views.UserListCreateAPIView.as_view(), name="users"),
    path("users/<int:pk>/", views.UserRetrieveUpdateDestroyAPIView.as_view(), name="user"),
]
