from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegistrateUserSerializer

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# это из документации
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@api_view(['POST',])
def register(request):

    if request.method == 'POST':
        serializer = RegistrateUserSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()             # это account, который возвращает функция save (из serializer)
            print(account)
            data['response'] = "Registration successful!"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key   # почему key?
            print(Token.objects.get(user=account))

            data['token'] = token

        else:
            data = serializer.errors


        return Response(data)

@api_view(['POST',])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)