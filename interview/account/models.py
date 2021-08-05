from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

