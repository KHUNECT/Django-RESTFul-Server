from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from khunect.serializers import UserSerializer
from khunect.models import User, Post
# Create your views here.

class UserList(APIView):
    """
    UserList의 반환 혹은 User 추가

    get:
    유저의 리스트를 반환 한다.

    post:
    유저의 정보를 입력, 추가 한다.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
