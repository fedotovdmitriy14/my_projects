# Generated by Django 3.2.3 on 2021-06-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField(max_length=32)),
                ('user_psw', models.TextField(max_length=32)),
                ('token', models.TextField()),
            ],
        ),
    ]
