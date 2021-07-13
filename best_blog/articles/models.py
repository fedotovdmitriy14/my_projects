from django.db import models


class Article(models.Model):
    name = models.TextField(max_length=50)
    number_of_pages = models.IntegerField()
    author = models.TextField(max_length=32)
    text = models.TextField(max_length=30000)


class Comment(models.Model):
    author = models.TextField(max_length=300)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class User(models.Model):
    login = models.TextField(max_length=32)
    user_psw = models.TextField(max_length=32)
    token = models.IntegerField()
