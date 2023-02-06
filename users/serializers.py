from rest_framework import serializers

from users.models import User


class UserResisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
