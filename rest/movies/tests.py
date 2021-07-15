from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from movies import models


class PlatformWatchlistTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testUser", password="12345")
        self.token = Token.objects.get(user__username="testUser")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.Platform.objects.create(name="Netflix", url="https://www.netflix.com")
        self.watchlist = models.Watchlist.objects.create(title="Example", description="coolMovie",
                                                         score=10, platform=self.stream)

    def test_platformCreate(self):
        data = {
            "name": "Megogo",
            "url": "https://www.megogo.com"
        }
        response = self.client.post(reverse("platform-list"), data, format="json")   # добавляем к basename роутера -list
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_platformList(self):
        response = self.client.get(reverse("platform-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_platformDetail(self):
        response = self.client.get(reverse("platform-detail", args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlistList(self):
        response = self.client.get(reverse("list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlistObj(self):
        response = self.client.get(reverse("obj", args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlistCreate(self):
        data = {
            "title": "new",
            "description": "nice movie",
            "score": 10,
            "platform": self.stream
        }
        response = self.client.post(reverse("list"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ReviewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="test", password="psw")
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.Platform.objects.create(name="Netflix", url="https://www.netflix.com")
        self.watchlist = models.Watchlist.objects.create(title="Example", description="coolMovie",
                                                         score=10, platform=self.stream)
        self.watchlist2 = models.Watchlist.objects.create(title="Example2", description="coolMovie2",
                                                         score=10, platform=self.stream)
        self.review = models.Review.objects.create(rating=9, description="great", review_user=self.user,
                                                   watchlist=self.watchlist2)

    def test_reviewCreate(self):
        data = {
            "rating": 10,
            "description": "cool",
            "review_user": self.user,
            "watchlist": self.watchlist
        }
        response = self.client.post(reverse("review_create", args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)

        response = self.client.post(reverse("review_create", args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reviewCreate_unauth(self):
        data = {
            "rating": 10,
            "description": "cool",
            "review_user": self.user,
            "watchlist": self.watchlist
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse("review_create", args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_reviewUpdate(self):
        data = {
            "rating": 8,
            "description": "cool",
            "review_user": self.user,
            "watchlist": self.watchlist2
        }
        response = self.client.put(reverse("review_detail", args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reviewList(self):
        response = self.client.get(reverse("review_list", args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reviewObj(self):
        response = self.client.get(reverse("review_detail", args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
