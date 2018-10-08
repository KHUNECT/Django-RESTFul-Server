from django.shortcuts import render
from rest_framework import viewsets
from khunect.serializers import UserSerializer
from khunect.models import User
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
