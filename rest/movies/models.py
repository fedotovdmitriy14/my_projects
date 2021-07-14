from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    score = models.IntegerField()
    avg_rating_previous = models.FloatField(default=0)
    average_rating = models.FloatField(default=0)
    num_of_ratings = models.IntegerField(default=0)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE, related_name='watchlist')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Platform(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Платформа"
        verbose_name_plural = "Платформы"

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.CharField(max_length=200, null=True)
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title

    class Meta:
        verbose_name = "Обзор"
        verbose_name_plural = "Обзоры"