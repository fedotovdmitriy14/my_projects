# Generated by Django 3.2.3 on 2021-06-29 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0013_alter_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
    ]