from django.db import models


class Reviews(models.Model):
    author = models.CharField('Автор', max_length=50)
    score = models.CharField('Оценка', max_length=50)
    body = models.TextField('Отзыв', max_length=3000)

    def __str__(self):                                      #чтобы в QuerySet красиво отображался
        return self.author

    def get_absolute_url(self):
        return f'/reviews/{self.id}'

    class Meta:                                             #чтобы так прописывался в админке
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


