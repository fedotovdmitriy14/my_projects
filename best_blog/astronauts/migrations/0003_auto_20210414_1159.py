# Generated by Django 3.1.7 on 2021-04-14 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('astronauts', '0002_astronaut_time_in_space'),
    ]

    operations = [
        migrations.CreateModel(
            name='Craft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32)),
                ('origin', models.TextField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='astronaut',
            name='craft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astronauts.craft'),
        ),
    ]
