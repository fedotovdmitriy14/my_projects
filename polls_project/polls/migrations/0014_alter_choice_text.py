# Generated by Django 3.2.3 on 2021-08-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20210814_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(max_length=64),
        ),
    ]
