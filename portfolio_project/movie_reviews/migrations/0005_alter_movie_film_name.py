# Generated by Django 3.2.3 on 2021-06-26 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0004_alter_moviename_film_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='film_name',
            field=models.ForeignKey(choices=[('Лука', 'Лука'), ('Гнев человеческий', 'Гнев человеческий')], on_delete=django.db.models.deletion.PROTECT, to='movie_reviews.moviename'),
        ),
    ]
