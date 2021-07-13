from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    login = serializers.TextField(max_length=32)
    user_psw = serializers.TextField(max_length=32)
    token = serializers.IntegerField()
