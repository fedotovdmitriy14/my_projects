# Generated by Django 3.2.3 on 2021-06-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0009_alter_moviename_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
