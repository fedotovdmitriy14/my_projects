# Generated by Django 3.1.7 on 2021-04-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('score', models.IntegerField(verbose_name='Оценка')),
                ('body', models.TextField(verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
