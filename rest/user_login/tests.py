from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username": "TestUser",
            "email": "testemail@gmail.com",
            "password": "12345",
            "password2": "12345"
        }
        response = self.client.post(reverse("register"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginLogout(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testSubject", password="12345")

    def test_login(self):
        data = {
            "username": "testSubject",
            "password": "12345"
        }
        response = self.client.post(reverse("login"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="testSubject")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


