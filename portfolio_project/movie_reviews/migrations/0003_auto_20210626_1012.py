# Generated by Django 3.2.3 on 2021-06-26 07:12

from django.db import migrations, models
import django.db.models.deletion
import movie_reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0002_auto_20210626_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.TextField(verbose_name=movie_reviews.models.Movie)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='film_name',
            field=models.ForeignKey(choices=[('ГЧ', 'Гнев человеческий'), ('Л', 'Лука')], on_delete=django.db.models.deletion.PROTECT, to='movie_reviews.moviename'),
        ),
    ]