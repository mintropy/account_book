from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from users.models import User
from users.serializers import UserResisterSerializer


class UserViewSet(ViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserResisterSerializer

    def resister(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        if email is None or password is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=email).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = {
            "username": email,
            "email": email,
            "password": make_password(password),
        }
        serializer = UserResisterSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data="validation error",
            status=status.HTTP_400_BAD_REQUEST,
        )
