# Generated by Django 3.1.7 on 2021-03-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Astronaut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('craft', models.TextField(max_length=16)),
                ('age', models.IntegerField()),
                ('name', models.TextField(max_length=26)),
            ],
        ),
    ]
