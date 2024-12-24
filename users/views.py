from rest_framework import generics

from .serializers import UserSerializer
from .models import User


# Create your views here.
class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    Дженерик для отображения списка и создания нового объекта User:
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Дженерик для просмотра, редактирования и удаления объекта User:
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
