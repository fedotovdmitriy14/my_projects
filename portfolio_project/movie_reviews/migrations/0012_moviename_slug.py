# Generated by Django 3.2.3 on 2021-06-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0011_remove_moviename_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviename',
            name='slug',
            field=models.SlugField(default=1234, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
