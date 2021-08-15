from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from . import models

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class PollsTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testUser", password="12345")
        self.token = Token.objects.get(user__username="testUser")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.poll = models.Poll.objects.create(poll_title="Test", description="test")
        self.question = models.Question.objects.create(poll_id=self.poll, questions="What is your name?",
                                                         question_type='text')
        self.choice = models.Choice.objects.create(question=self.question, text='America')

    def test_pollCreate(self):
        data = {
            "poll_title": "Test Poll",
            "description": "test description",
        }
        response = self.client.post(reverse("polls-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_pollList(self):
        response = self.client.get(reverse("polls-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pollDetail(self):
        response = self.client.get(reverse("polls-detail", args=(self.poll.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_questionCreate(self):
        data = {
            "questions": "Where are you from?",
            "question_type": "text",
            'poll_id': self.poll.id
        }
        response = self.client.post(reverse("questions-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_questionList(self):
        response = self.client.get(reverse("questions-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_questionDetail(self):
        response = self.client.get(reverse("questions-detail", args=(self.question.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_choiceCreate(self):
        data = {
            "question": self.question.id,
            "text": 'USA',
        }
        response = self.client.post(reverse("choices-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_choiceList(self):
        response = self.client.get(reverse("choices-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_choiceDetail(self):
        response = self.client.get(reverse("choices-detail", args=(self.choice.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_watchlistList(self):
#         response = self.client.get(reverse("list"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_watchlistObj(self):
#         response = self.client.get(reverse("obj", args=(self.watchlist.id,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_watchlistCreate(self):
#         data = {
#             "title": "new",
#             "description": "nice movie",
#             "score": 10,
#             "platform": self.stream
#         }
#         response = self.client.post(reverse("list"), data)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
# class ReviewTest(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create(username="test", password="psw")
#         self.token = Token.objects.get(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
#
#         self.stream = models.Platform.objects.create(name="Netflix", url="https://www.netflix.com")
#         self.watchlist = models.Watchlist.objects.create(title="Example", description="coolMovie",
#                                                          score=10, platform=self.stream)
#         self.watchlist2 = models.Watchlist.objects.create(title="Example2", description="coolMovie2",
#                                                          score=10, platform=self.stream)
#         self.review = models.Review.objects.create(rating=9, description="great", review_user=self.user,
#                                                    watchlist=self.watchlist2)
#
#     def test_reviewCreate(self):
#         data = {
#             "rating": 10,
#             "description": "cool",
#             "review_user": self.user,
#             "watchlist": self.watchlist
#         }
#         response = self.client.post(reverse("review_create", args=(self.watchlist.id,)), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(models.Review.objects.count(), 2)
#
#         response = self.client.post(reverse("review_create", args=(self.watchlist.id,)), data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_reviewCreate_unauth(self):
#         data = {
#             "rating": 10,
#             "description": "cool",
#             "review_user": self.user,
#             "watchlist": self.watchlist
#         }
#         self.client.force_authenticate(user=None)
#         response = self.client.post(reverse("review_create", args=(self.watchlist.id,)), data)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def test_reviewUpdate(self):
#         data = {
#             "rating": 8,
#             "description": "cool",
#             "review_user": self.user,
#             "watchlist": self.watchlist2
#         }
#         response = self.client.put(reverse("review_detail", args=(self.review.id,)), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_reviewList(self):
#         response = self.client.get(reverse("review_list", args=(self.watchlist.id,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_reviewObj(self):
#         response = self.client.get(reverse("review_detail", args=(self.watchlist.id,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
