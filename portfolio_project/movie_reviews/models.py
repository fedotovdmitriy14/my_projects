from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


class MovieName(models.Model):
    film_description = models.TextField(verbose_name="Описание фильма")
    film_name = models.TextField(verbose_name="Название фильма")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.film_name

    def get_absolute_url(self):
        return f'/movies/{self.slug}'
        # return reverse('movie_list', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Movie(models.Model):

    name = models.TextField(verbose_name="Заголовок")
    score = models.TextField(verbose_name="Оценка")
    text = models.TextField(verbose_name="Текст")
    film_name = models.ForeignKey(MovieName, on_delete=models.PROTECT)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):                                  # чтобы в QuerySet красиво отображался
        return self.name

    def get_absolute_url(self):
        return f'/reviews/{self.id}'


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['name']
