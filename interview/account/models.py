from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя')

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

